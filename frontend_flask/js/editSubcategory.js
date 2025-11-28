document.addEventListener("DOMContentLoaded", async () => {
    const subcategoryId = localStorage.getItem("editSubcategoryId");
    if (!subcategoryId) return;

    const res = await fetch("/subcategories", {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    });
    const subcategories = await res.json();
    const sc = subcategories.find(s => s.subcategory_id == subcategoryId);

    document.getElementById("subcategoryId").value = sc.subcategory_id;
    document.getElementById("subcategoryName").value = sc.subcategory_name;
    document.getElementById("subcategoryDescription").value = sc.subcategory_description;

    const categoryRes = await fetch("/categories", {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    });
    const categories = await categoryRes.json();
    const select = document.getElementById("categorySelect");
    select.innerHTML = categories.map(cat => `<option value="${cat.category_id}" ${cat.category_id === sc.subcategory_category_id ? 'selected' : ''}>${cat.category_name}</option>`).join('');

    document.getElementById("editSubcategoryForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = {
            subcategory_name: document.getElementById("subcategoryName").value,
            subcategory_description: document.getElementById("subcategoryDescription").value,
            subcategory_category_id: document.getElementById("categorySelect").value
        };

        const updateRes = await fetch(`/subcategories/${subcategoryId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json",
                "Authorization": "Bearer " + getToken() },
            body: JSON.stringify(data)
        });
        const result = await updateRes.json();
        alert(result.message);
        location.href = "viewSubcategory.html";
    });
});
