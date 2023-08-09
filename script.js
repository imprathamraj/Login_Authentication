document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Simulate a delay for demonstration purposes
    setTimeout(function() {
        // Simulate a random login result (success or failure)
        const randomSuccess = Math.random() < 0.5; // Adjust the threshold for success rate
        if (randomSuccess) {
            redirectToThankYouPage();
        } else {
            showLoginMessage("Invalid credentials. Please try again.", "red");
        }
    }, 1000); // Simulate a 1-second delay
});

function showLoginMessage(message, color) {
    const messageElement = document.getElementById("message");
    messageElement.textContent = message;
    messageElement.style.color = color;
}

function redirectToThankYouPage() {
    // Redirect to the thank you page after successful login
    window.location.href = "thankyou.html";
}
