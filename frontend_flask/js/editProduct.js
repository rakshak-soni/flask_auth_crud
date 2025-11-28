function qs(key) {
    return new URLSearchParams(window.location.search).get(key);
  }
  
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
      });
  }
  
  function loadSubByCategory(categoryId, selectedSubId = null) {
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
        if (selectedSubId) sel.value = selectedSubId;
      });
  }
  
  function loadProduct() {
    const id = qs('id');
    if (!id) return;
    fetch(`/product/${id}`, {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    })
      .then(r => r.json())
      .then(p => {
        document.getElementById('product_id').value = p.product_id;
        document.getElementById('product_name').value = p.product_name || '';
        document.getElementById('product_description').value = p.product_description || '';
        document.getElementById('product_price').value = p.product_price || 0;
        document.getElementById('product_quantity').value = p.product_quantity || 0;
        document.getElementById('current_img').src = p.product_image_name ? `http://127.0.0.1:5000/product_image/${p.product_image_name}` : '';
        document.getElementById('product_category_id').value = p.product_category_id || '';
        return loadSubByCategory(p.product_category_id, p.product_subcategory_id);
      })
      .catch(err => console.error('Load product error', err));
  }
  
  function updateProduct() {
    const id = qs('id');
    if (!id) return alert('Missing product id');
  
    const formEl = document.getElementById('editForm');
    const fd = new FormData(formEl);
  
    fetch(`/product/${id}`, { method: 'PUT', body: fd, headers: {
        "Authorization": "Bearer " + getToken()
    } })
      .then(r => r.json())
      .then(resp => {
        if (resp && resp.message) {
          alert('Product updated');
          location.href = 'viewProduct.html';
        } else {
          alert('Update failed');
        }
      })
      .catch(err => {
        console.error('Update error', err);
        alert('Update failed');
      });
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    Promise.all([loadCategories()]).then(loadProduct);
    document.getElementById('product_category_id').addEventListener('change', function () {
      loadSubByCategory(this.value);
    });
    document.getElementById('saveBtn').addEventListener('click', updateProduct);
  });
  