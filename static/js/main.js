document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const rfpList = document.getElementById('rfpList');

    if (uploadForm) {
        uploadForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.id) {
                    alert('RFP processed successfully!');
                    window.location.href = `/results/${data.id}`;
                } else {
                    alert('Error processing RFP');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error uploading file');
            });
        });
    }

    function loadRFPs() {
        fetch('/rfps')
            .then(response => response.json())
            .then(rfps => {
                rfpList.innerHTML = '';
                rfps.forEach(rfp => {
                    const li = document.createElement('li');
                    li.className = 'list-group-item d-flex justify-content-between align-items-center';
                    li.innerHTML = `
                        <span>${rfp.title}</span>
                        <span class="badge bg-primary rounded-pill">${new Date(rfp.submission_deadline).toLocaleDateString()}</span>
                    `;
                    li.addEventListener('click', () => {
                        window.location.href = `/results/${rfp.id}`;
                    });
                    rfpList.appendChild(li);
                });
            })
            .catch(error => console.error('Error loading RFPs:', error));
    }

    if (rfpList) {
        loadRFPs();
    }
});
