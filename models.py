from extensions import db, Base
from datetime import datetime

class RFP(Base):
    __tablename__ = 'rfp'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    submission_deadline = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    response = db.Column(db.Text)
