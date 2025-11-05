
document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const torrentFile = document.getElementById('torrentFile');
    const uploadMessage = document.getElementById('uploadMessage');
    const torrentsTableBody = document.querySelector('#torrentsTable tbody');
    const processDataForm = document.getElementById('processDataForm');
    const dataPayload = document.getElementById('dataPayload');
    const processDataMessage = document.getElementById('processDataMessage');

    const fetchTorrents = async () => {
        try {
            const response = await fetch('/torrents/');
            const torrents = await response.json();
            torrentsTableBody.innerHTML = ''; // Clear existing rows
            torrents.forEach(torrent => {
                const row = torrentsTableBody.insertRow();
                row.insertCell(0).textContent = torrent.id;
                row.insertCell(1).textContent = torrent.name;
                row.insertCell(2).textContent = torrent.status;
                row.insertCell(3).textContent = `${torrent.progress.toFixed(2)}%`;
                const actionsCell = row.insertCell(4);
                actionsCell.classList.add('action-buttons');

                const startButton = document.createElement('button');
                startButton.textContent = 'Start';
                startButton.onclick = () => startTorrent(torrent.id);
                actionsCell.appendChild(startButton);

                const stopButton = document.createElement('button');
                stopButton.textContent = 'Stop';
                stopButton.onclick = () => stopTorrent(torrent.id);
                actionsCell.appendChild(stopButton);

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = () => deleteTorrent(torrent.id);
                actionsCell.appendChild(deleteButton);
            });
        } catch (error) {
            console.error('Error fetching torrents:', error);
        }
    };

    const startTorrent = async (id) => {
        try {
            const response = await fetch(`/torrent/${id}/start`, {
                method: 'POST',
            });
            const data = await response.json();
            alert(data.message);
            fetchTorrents();
        } catch (error) {
            console.error('Error starting torrent:', error);
            alert('Failed to start torrent.');
        }
    };

    const stopTorrent = async (id) => {
        try {
            const response = await fetch(`/torrent/${id}/stop`, {
                method: 'POST',
            });
            const data = await response.json();
            alert(data.message);
            fetchTorrents();
        } catch (error) {
            console.error('Error stopping torrent:', error);
            alert('Failed to stop torrent.');
        }
    };

    const deleteTorrent = async (id) => {
        if (!confirm('Are you sure you want to delete this torrent?')) {
            return;
        }
        try {
            const response = await fetch(`/torrent/${id}`, {
                method: 'DELETE',
            });
            const data = await response.json();
            alert(data.message);
            fetchTorrents();
        } catch (error) {
            console.error('Error deleting torrent:', error);
            alert('Failed to delete torrent.');
        }
    };

    uploadForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', torrentFile.files[0]);

        try {
            const response = await fetch('/upload-torrent/', {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();
            uploadMessage.textContent = data.message;
            uploadMessage.style.color = 'green';
            fetchTorrents();
        } catch (error) {
            console.error('Error uploading torrent:', error);
            uploadMessage.textContent = 'Failed to upload torrent.';
            uploadMessage.style.color = 'red';
        }
    });

    processDataForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const payload = { data: dataPayload.value };

        try {
            const response = await fetch('/process-data/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            });
            const data = await response.json();
            processDataMessage.textContent = data.message + (data.result ? `: ${data.result}` : '');
            processDataMessage.style.color = 'green';
        } catch (error) {
            console.error('Error processing data:', error);
            processDataMessage.textContent = 'Failed to process data.';
            processDataMessage.style.color = 'red';
        }
    });

    // Initial fetch of torrents when the page loads
    fetchTorrents();
    // Refresh torrents every 10 seconds (example of a subtle bug: potential for race conditions if updates are frequent)
    setInterval(fetchTorrents, 10000);
});
