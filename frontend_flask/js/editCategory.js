document.addEventListener("DOMContentLoaded", () => {
    const urlParams = new URLSearchParams(window.location.search);
    const category_id = urlParams.get("id");

    if (!category_id) {
        alert("Invalid category ID!");
        return;
    }

    // Load category data
    fetch(`/edit_category/${category_id}`, {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    })
        .then(res => res.json())
        .then(data => {
            document.getElementById("category_id").value = data.category_id;
            document.getElementById("category_name").value = data.category_name;
            document.getElementById("category_description").value = data.category_description;
        })
        .catch(err => console.error("Error loading category:", err));
});


// Update category using PUT
document.getElementById("updateForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const updatedData = {
        category_id: document.getElementById("category_id").value,
        category_name: document.getElementById("category_name").value,
        category_description: document.getElementById("category_description").value
    };

    fetch(`/update_category`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + getToken()
        },
        body: JSON.stringify(updatedData)
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        window.location.href = "viewCategory.html";
    })
    .catch(err => console.error("Update error:", err));
});


// Cancel
function goBack() {
    window.location.href = "viewCategory.html";
}
