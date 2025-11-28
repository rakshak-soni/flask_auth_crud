document.addEventListener("DOMContentLoaded", loadSubcategories);

async function loadSubcategories() {
    const res = await fetch("/subcategories", {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    });
    const subcategories = await res.json();
    const tbody = document.getElementById("subcategoryTable");
    tbody.innerHTML = subcategories.map(sc => `
        <tr>
            <td>${sc.subcategory_id}</td>
            <td>${sc.category_name}</td>
            <td>${sc.subcategory_name}</td>
            <td>${sc.subcategory_description}</td>
            <td>
                <button onclick="editSubcategory(${sc.subcategory_id})">Edit</button>
                <button onclick="deleteSubcategory(${sc.subcategory_id})">Delete</button>
            </td>
        </tr>
    `).join('');
}

function editSubcategory(id) {
    localStorage.setItem("editSubcategoryId", id);
    location.href = "editSubcategory.html";
}

async function deleteSubcategory(id) {
    if(confirm("Are you sure?")) {
        const res = await fetch(`/subcategories/${id}`, { method: "DELETE", headers: {
            "Authorization": "Bearer " + getToken()
        } });
        const result = await res.json();
        alert(result.message);
        loadSubcategories();
    }
}
