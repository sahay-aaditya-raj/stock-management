function deleteInvoice(locat){
  const conf = confirm('Are you sure you want to delete this entry!');
  if (conf){
    window.location.href = locat
  }  
}

const stock = document.getElementById('stock');

const product = document.getElementById('product');
product.addEventListener('change', function() {
    const selectedValue = this.value;

    let filtered = [];
    for (var i=0; i<jsonData.length; i+=1){
      if (selectedValue == jsonData[i].name){
      filtered.push(jsonData[i]);
      }
    }
    /* stock select options */
    
    for (let i = stock.options.length - 1; i > 0; i--) {
      stock.remove(i);
    }
    for (let i=0; i<filtered.length; i++){
      const newOption = document.createElement('option');
      let fil = filtered[i];
      newOption.value = fil.id;
      newOption.textContent = `Batch-${fil.batch}, Expiry-${fil.expiry}`;
      stock.appendChild(newOption);
    }
});

var x = 0;

const stockDetails = document.getElementById('stockDetails')
stock.addEventListener('change',function(){
   while (stockDetails.firstChild){
    stockDetails.removeChild(stockDetails.firstChild);
   }
   
   for (let i=0; i<jsonData.length; i++){
    if(jsonData[i].id == stock.value ){
      const stockInfo1 = document.createElement('div');
      stockInfo1.textContent = `Name: ${jsonData[i].name}`;
      const stockInfo2 = document.createElement('div');
      stockInfo2.textContent = `Batch: ${jsonData[i].batch}`;
      const stockInfo3 = document.createElement('div');
      stockInfo3.textContent = `Expiry: ${jsonData[i].expiry}`;
      const stockInfo4 = document.createElement('div');
      stockInfo4.textContent = `Quantity: ${jsonData[i].quantity}`;
      stockDetails.appendChild(stockInfo1);
      stockDetails.appendChild(stockInfo2);
      stockDetails.appendChild(stockInfo3);
      stockDetails.appendChild(stockInfo4);
      x = i
    }
   }
});

/* hint text */
const mrp = document.getElementById('mrp');
const ptr = document.getElementById('ptr');
const qty = document.getElementById('qty');

function eventMSG(event, msg){
    let chck = Number(event.value);
    if (isNaN(chck) == true){
        alert(`${msg} must be a number!`)
        event.value='';
    }
}


mrp.addEventListener('change', function(){
    eventMSG(mrp, 'MRP')
});
ptr.addEventListener('change', function(){
    eventMSG(ptr, 'PTR')
});


document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("myform");
  
  form.addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent the default form submission behavior
      
      const product = document.getElementById("product");
      const stock = document.getElementById("stock");
      const mrp = document.getElementById("mrp");
      const ptr = document.getElementById("ptr");
      const qty = document.getElementById("qty");
      const bonus = document.getElementById("bonus");
      
      

      if (product.value != 'none' && stock.value != 'none' && mrp.value !='' && ptr.value!='' && qty.value != '' && bonus.value !='') {
        
        if (jsonData[x].quantity<Number(qty.value)+ Number(bonus.value)){
          alert('Sum of Quantity and Bonus must be less than or equal to the displayed quantity!');
          qty.value = 0;
          bonus.value= 0;
        } else{
        form.submit();
        }
      } else{
        alert('Please Fill All the Required Fields !');
        location.reload(true);
      }
      
      
  });
});