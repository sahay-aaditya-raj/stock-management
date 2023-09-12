
let currentSortKey = null;
let sortAscending = true;
populateTable();
function populateTable() {
    const stockTable = document.getElementById('stockTable');
    stockTable.innerHTML = '';
    
    stock.forEach((item)=>{
        const newRow = document.createElement('tr');
        newRow.addEventListener('click', function(){
            const conf = confirm('Are you Sure want to Delete this Stock?');
            if (conf){
                window.location.href = `${item.id}`;
            }
        });
        newRow.innerHTML = `<td>${item.name}</td><td>${item.batch}</td><td>${item.manufacturer}</td><td>${item.pack}</td><td>${item.expiry}</td><td>${item.quantity}</td>`;
        stockTable.append(newRow)
  })
}


function sortTable(key) {
    if (currentSortKey === key) {
      sortAscending = !sortAscending;
    } else {
      currentSortKey = key;
      sortAscending = true;
    }
  
    stock.sort((a, b) => {
      const aValue = a[key];
      const bValue = b[key];
      if (aValue < bValue) return sortAscending ? -1 : 1;
      if (aValue > bValue) return sortAscending ? 1 : -1;
      return 0;
    });
  
    populateTable();
  };