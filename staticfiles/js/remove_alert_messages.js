setTimeout(function() {
    const alertMessage = document.getElementById("alert-message");
    if (alertMessage) {
        let opacity = 1;
        const intervalId = setInterval(function() {
            opacity -= 0.03;
            alertMessage.style.opacity = opacity;
            if (opacity <= 0) {
                clearInterval(intervalId); // Stop the interval when opacity reaches 0
                alertMessage.style.display = "none"; // Hide the alert message
            }
        }, 30); // 30 milliseconds interval
    }
}, 3000); // 3000 milliseconds = 3 seconds
