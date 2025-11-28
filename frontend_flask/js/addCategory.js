document.getElementById("categoryForm").addEventListener("submit", function (e) {
    e.preventDefault();

    let name = document.getElementById("category_name").value.trim();
    let desc = document.getElementById("category_description").value.trim();

    if (!name || !desc) {
        alert("All fields are required");
        return;
    }

    let data = {
        category_name: name,
        category_description: desc
    };

    fetch("/insert_category", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + getToken()
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        alert(result.message);
        window.location.href = "viewCategory.html";
    })
    .catch(err => console.error("Error:", err));
});
