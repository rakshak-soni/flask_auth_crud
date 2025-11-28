// load categories then wire change handler for subcategories
function loadCategories() {
    return fetch('/view_category', {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    })
      .then(r => r.json())
      .then(data => {
        const sel = document.getElementById('product_category_id');
        sel.innerHTML = '<option value="">Select Category</option>';
        data.forEach(c => sel.innerHTML += `<option value="${c.category_id}">${c.category_name}</option>`);
      })
      .catch(err => console.error('Load categories error', err));
  }
  
  function loadSubcategoriesByCategory(categoryId) {
    const sel = document.getElementById('product_subcategory_id');
    if (!categoryId) {
      sel.innerHTML = '<option value="">Select Subcategory</option>';
      return Promise.resolve();
    }
    return fetch(`/view_subcategory_by_category/${categoryId}`, {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    })
      .then(r => r.json())
      .then(data => {
        sel.innerHTML = '<option value="">Select Subcategory</option>';
        data.forEach(s => sel.innerHTML += `<option value="${s.subcategory_id}">${s.subcategory_name}</option>`);
      })
      .catch(err => console.error('Load subcategories error', err));
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    loadCategories();
    document.getElementById('product_category_id').addEventListener('change', function () {
      loadSubcategoriesByCategory(this.value);
    });
  
    document.getElementById('productForm').addEventListener('submit', function (e) {
      e.preventDefault();
      const form = new FormData(this);
      fetch('/product', { method: 'POST', body: form, headers: {
        "Authorization": "Bearer " + getToken()
    } })
        .then(r => r.json())
        .then(resp => {
          if (resp && resp.message) {
            alert('Product added successfully');
            this.reset();
          } else {
            alert('Unexpected response');
          }
        })
        .catch(err => {
          console.error('Insert error', err);
          alert('Insert failed');
        });
    });
  });
  