// webcam access
navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        const video = document.getElementById('videoFeed');
        video.srcObject = stream;
    })
    .catch((error) => {
        console.error("Error accessing the webcam:", error);
    });

document.getElementById('coachBtn').addEventListener('click', function() {
    const moveInput = document.getElementById('moveInput').value;

    const feedback = getMoveFeedback(moveInput);

    // display feedback
    document.getElementById('feedbackOutput').textContent = feedback;
});

// feedback func
function getMoveFeedback(move) {
    if (!move || !move.includes('to')) {
        return 'Please enter a valid move (e.g., e2 to e4).';
    }
    return `Move "${move}" looks solid! Consider controlling the center.`; // Example feedback
}
