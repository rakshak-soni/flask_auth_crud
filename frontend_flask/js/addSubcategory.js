document.addEventListener("DOMContentLoaded", async () => {
    await loadCategories();

    document.getElementById("addSubcategoryForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = {
            subcategory_name: document.getElementById("subcategoryName").value,
            subcategory_description: document.getElementById("subcategoryDescription").value,
            subcategory_category_id: document.getElementById("categorySelect").value
        };

        const res = await fetch("/subcategories", {
            method: "POST",
            headers: { "Content-Type": "application/json", 
                "Authorization": "Bearer " + getToken() },
            body: JSON.stringify(data)
        });

        const result = await res.json();
        alert(result.message);
        document.getElementById("addSubcategoryForm").reset();
    });
});

async function loadCategories() {
    const res = await fetch("/categories", {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    });
    const categories = await res.json();
    const select = document.getElementById("categorySelect");
    select.innerHTML = categories.map(cat => `<option value="${cat.category_id}">${cat.category_name}</option>`).join('');
}
