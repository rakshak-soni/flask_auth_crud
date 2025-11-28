document.getElementById("loginBtn").addEventListener("click", loginUser);

async function loginUser() {
    const email = document.getElementById("user_email").value.trim();
    const pass = document.getElementById("user_password").value;
    const messageBox = document.getElementById("message");

    const payload = {
        user_email: email,
        user_password: pass
    };

    try {
        const response = await fetch("/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.status !== 200) {
            messageBox.style.color = "red";
            messageBox.textContent = data.message;
            return;
        }

        localStorage.setItem("token", data.token);
        localStorage.setItem("roles", JSON.stringify(data.roles));
        localStorage.setItem("user", JSON.stringify(data.user));

        messageBox.style.color = "green";
        messageBox.textContent = "Login successful";

        // Redirect based on role
        if (data.roles.includes("admin")) {
            window.location.href = "home.html";
        } else {
            window.location.href = "user_dashboard.html";
        }

    } catch (error) {
        console.error(error);
        messageBox.style.color = "red";
        messageBox.textContent = "Server error";
    }
}
