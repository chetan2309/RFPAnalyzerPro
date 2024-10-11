document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const rfpList = document.getElementById('rfpList');
    const errorMessage = document.createElement('div');
    errorMessage.className = 'alert alert-danger mt-3 d-none';
    if (uploadForm) {
        uploadForm.after(errorMessage);
    }

    if (uploadForm) {
        uploadForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            errorMessage.classList.add('d-none');

            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.id) {
                    alert('RFP processed successfully!');
                    window.location.href = `/results/${data.id}`;
                } else if (data.error) {
                    errorMessage.textContent = data.error;
                    errorMessage.classList.remove('d-none');
                } else {
                    errorMessage.textContent = 'An unexpected error occurred.';
                    errorMessage.classList.remove('d-none');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                errorMessage.textContent = 'An error occurred while uploading the file. Please try again.';
                errorMessage.classList.remove('d-none');
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
            .catch(error => {
                console.error('Error loading RFPs:', error);
                errorMessage.textContent = 'Failed to load RFPs. Please refresh the page.';
                errorMessage.classList.remove('d-none');
            });
    }

    if (rfpList) {
        loadRFPs();
    }

    // New code for handling the Generate Response button
    const generateResponseBtn = document.getElementById('generateResponseBtn');
    const responseSection = document.getElementById('responseSection');
    const generatedResponse = document.getElementById('generatedResponse');

    if (generateResponseBtn) {
        generateResponseBtn.addEventListener('click', function() {
            const rfpId = this.getAttribute('data-rfp-id');
            this.disabled = true;
            this.textContent = 'Generating...';

            fetch(`/generate_response/${rfpId}`, {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                if (data.response) {
                    // Update this line to use innerHTML instead of textContent
                    generatedResponse.innerHTML = data.response;
                    responseSection.classList.remove('d-none');
                } else if (data.error) {
                    alert(`Error: ${data.error}`);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while generating the response. Please try again.');
            })
            .finally(() => {
                this.disabled = false;
                this.textContent = 'Generate Response';
            });
        });
    }
});
