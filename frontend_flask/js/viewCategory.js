function loadCategories() {
    fetch("/view_category", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + getToken()
        }
    })
    .then(res => res.json())
    .then(data => {
        console.log("Loaded categories:", data);

        let table = document.getElementById("categoryTable");
        table.innerHTML = "";

        data.forEach(cat => {
            let row = `
                <tr>
                    <td>${cat.category_name}</td>
                    <td>${cat.category_description}</td>
                    <td>
                        <button onclick="editCategory(${cat.category_id})">Edit</button>
                        <button onclick="deleteCategory(${cat.category_id})">Delete</button>
                    </td>
                </tr>
            `;
            table.innerHTML += row;
        });
    })
    .catch(err => console.error("Error loading categories:", err));
}

function editCategory(id) {
    window.location.href = `editCategory.html?id=${id}`;
}

function deleteCategory(id) {
    console.log("Deleting category with id:", id);
    if (!confirm("Are you sure you want to delete this category?")) return;

    fetch(`/delete_category/${id}`, {
        method: "DELETE",
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadCategories();
    })
    .catch(err => console.error("Error deleting:", err));
}


