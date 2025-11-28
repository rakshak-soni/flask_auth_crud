function loadProducts() {
    fetch('/product', {
        headers: {
            "Authorization": "Bearer " + getToken()
        }
    })
      .then(r => r.json())
      .then(data => renderTable(data))
      .catch(err => console.error('Load products error', err));
  }
  
  function renderTable(items) {
    const c = document.getElementById('productContainer');
    if (!items || !items.length) {
      c.innerHTML = '<p>No products found.</p>';
      return;
    }
  
    let html = '<table><thead><tr><th>Category</th><th>Subcategory</th><th>Name</th><th>Price</th><th>Qty</th><th>Image</th><th>Action</th></tr></thead><tbody>';
    items.forEach(it => {
      const imgUrl = it.product_image_name ? `/product_image/${it.product_image_name}` : '';
      html += `<tr>
        <td>${it.category_name || ''}</td>
        <td>${it.subcategory_name || ''}</td>
        <td>${it.product_name || ''}</td>
        <td>${it.product_price || ''}</td>
        <td>${it.product_quantity || ''}</td>
        <td>${imgUrl ? `<img src="${imgUrl}" onclick="showPreview('${imgUrl}')" />` : ''}</td>
        <td class="actions-row">
          <button onclick="gotoEdit(${it.product_id})">Edit</button>
          <button onclick="deleteProduct(${it.product_id})">Delete</button>
        </td>
      </tr>`;
    });
    html += '</tbody></table>';
    c.innerHTML = html;
  }
  
  function gotoEdit(id) { location.href = `editProduct.html?id=${id}`; }
  
  function deleteProduct(id) {
    if (!confirm('Delete product?')) return;
    fetch(`/product/${id}`, { method: 'DELETE', headers: {
        "Authorization": "Bearer " + getToken()
    } })
      .then(r => r.json())
      .then(resp => {
        if (resp && resp.message) loadProducts();
        else alert('Delete failed');
      })
      .catch(err => console.error('Delete error', err));
  }
  
  function showPreview(src) {
    const modal = document.getElementById('previewModal');
    document.getElementById('previewImg').src = src;
    modal.classList.remove('hidden');
  }
  
  function hidePreview() {
    document.getElementById('previewModal').classList.add('hidden');
  }
  
  document.addEventListener('DOMContentLoaded', loadProducts);
  