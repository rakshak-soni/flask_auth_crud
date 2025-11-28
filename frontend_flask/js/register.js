document.getElementById("registerBtn").addEventListener("click", registerUser);

async function registerUser() {
    const first_name = document.getElementById("first_name").value.trim();
    const last_name = document.getElementById("last_name").value.trim();
    const email = document.getElementById("user_email").value.trim();
    const pass = document.getElementById("user_password").value;
    const confirm = document.getElementById("user_confirm_password").value;
    const phone = document.getElementById("user_phone").value.trim();

    if (pass !== confirm) {
        alert("Passwords do not match");
        return;
    }

    const payload = {
        first_name,
        last_name,
        user_email: email,
        user_password: pass,
        user_phone: phone
    };

    try {
        const response = await fetch("/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        alert(data.message);

        if (response.status === 201) {
            window.location.href = "login.html";
        }

    } catch (error) {
        console.error(error);
        alert("Server error");
    }
}
