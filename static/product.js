
let currentSortKey = null;
let sortAscending = true;
populateTable();
function populateTable() {
    const stockTable = document.getElementById('stockTable');
    stockTable.innerHTML = '';
    
    stock.forEach((item)=>{
        const newRow = document.createElement('tr');
        newRow.innerHTML = `<td>${item.name}</td><td>${item.pack}</td><td>${item.manufacturer}</td>`;
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
  

  
  
  