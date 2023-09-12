const tr = document.getElementById('invoice');

        tr.addEventListener('blur', function(){
            val = tr.value;
            if (val!=''){
                if (json_inv.includes(val)==true) {
                    tr.value = null;
                    alert('Invoice Number already exists !');
                }
            };
        });

        document.addEventListener("DOMContentLoaded", function() {
            const form = document.getElementById("myform");
            
          
            form.addEventListener("submit", function(event) {
                event.preventDefault(); // Prevent the default form submission behavior
                
                const invtype = document.getElementsByName('invType')[0];
                const gstrate = document.getElementsByName('gstrate')[0];
                const party = document.getElementById('party');
                
                if (invtype.value!='none' && gstrate.value!='none' && tr.value!='' && party.value!='none'){
                   
                    form.submit();
                    
                } else {
                    alert('Please Fill All the Required Details!');
                    location.reload(true);
                }


                 // Then, submit the form programmatically
            });
          });