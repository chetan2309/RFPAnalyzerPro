from flask import Blueprint, render_template, request, jsonify
from extensions import db
from models import RFP
from utils.document_processor import process_rfp
from utils.notification import send_teams_notification

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_rfp():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        rfp_data = process_rfp(file)
        new_rfp = RFP(
            title=rfp_data['title'],
            summary=rfp_data['summary'],
            submission_deadline=rfp_data['submission_deadline']
        )
        db.session.add(new_rfp)
        db.session.commit()

        # Send notification to Teams
        send_teams_notification(f"New RFP uploaded: {new_rfp.title}")

        return jsonify({"message": "RFP processed successfully", "id": new_rfp.id}), 200

@bp.route('/results/<int:rfp_id>')
def results(rfp_id):
    rfp = RFP.query.get_or_404(rfp_id)
    return render_template('results.html', rfp=rfp)

@bp.route('/rfps')
def list_rfps():
    rfps = RFP.query.all()
    return jsonify([{
        "id": rfp.id,
        "title": rfp.title,
        "submission_deadline": rfp.submission_deadline.isoformat()
    } for rfp in rfps])
