
let currentSortKey = null;
let sortAscending = true;
populateTable();
function populateTable() {
    const stockTable = document.getElementById('invlist');
    stockTable.innerHTML = '';
    
    sv_inv_list.forEach((item)=>{
        const newRow = document.createElement('tr');
        newRow.addEventListener('click', function(){
            window.location.href = `${item.id}`;
        })
        if (item.paid){
            newRow.innerHTML = `<td>${item.inv}</td><td>${item.name}</td><td>${item.date}</td><td>${item.gstid}</td><td>${item.dlno}</td><td>${item.city}</td><td style='padding-right:20px;text-align:right;'>₹ ${item.amount}</td><td>Yes</td>`;
        }
        else{
            newRow.innerHTML = `<td>${item.inv}</td><td>${item.name}</td><td>${item.date}</td><td>${item.gstid}</td><td>${item.dlno}</td><td>${item.city}</td><td style='padding-right:20px;text-align:right;'>₹ ${item.amount}</td><td>No</td>`;
        }
        
        
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
  
    sv_inv_list.sort((a, b) => {
      const aValue = a[key];
      const bValue = b[key];
      if (aValue < bValue) return sortAscending ? -1 : 1;
      if (aValue > bValue) return sortAscending ? 1 : -1;
      return 0;
    });
  
    populateTable();
  };