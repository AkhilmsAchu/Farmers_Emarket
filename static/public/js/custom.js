
function cartcount(){
    var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	document.getElementById('cartcount').innerHTML = '['+req.responseText+']';
	      if (req.responseText=='true'){
	      	$(this).attr('disabled', true);
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "cartcount", true);
	    req.send();
          
};



window.onload=cartcount;
$(document).ready(function(){

var quantitiy=1;

$('.remove-from-wish').click(function(e){
        // Stop acting like a button
		e.preventDefault();
		var bid = e.target.id;
	    var pid = $(this).attr('data-id');

		var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	cartcount();
	    	location.reload();
	      alert(req.responseText)
	      if (req.responseText=='true'){
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "removefromwish?id="+encodeURIComponent(pid), true);
	    req.send(); 
    });

 $('.add-to-wish').click(function(e){
        // Stop acting like a button
		e.preventDefault();
		var bid = e.target.id;
	    var pid = $(this).attr('data-id');

	    var qty =  $("#quantity").val()
	    if (qty == null){
	    	qty=1;
	    }
		var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	cartcount();
	      alert(req.responseText)
	      if (req.responseText=='true'){
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "addtowish?id="+encodeURIComponent(pid)+'&qty='+encodeURIComponent(qty), true);
	    req.send(); 
    });


$('.remove-from-cart').click(function(e){
        // Stop acting like a button
		e.preventDefault();
		var bid = e.target.id;
	    var pid = $(this).attr('data-id');

		var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	cartcount();
	    	location.reload();
	      alert(req.responseText)
	      if (req.responseText=='true'){
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "removefromcart?id="+encodeURIComponent(pid), true);
	    req.send(); 
    });

 $('.add-to-cart').click(function(e){
        // Stop acting like a button
		e.preventDefault();
		var bid = e.target.id;
	    var pid = $(this).attr('data-id');

	    var qty =  $("#quantity").val()
	    if (qty == null){
	    	qty=1;
	    }
		var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	cartcount();
	      alert(req.responseText)
	      if (req.responseText=='true'){
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "addtocart?id="+encodeURIComponent(pid)+'&qty='+encodeURIComponent(qty), true);
	    req.send(); 
    });


   $('.quantity-right-plus').click(function(e){
        
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#quantity').val());
        
        // If is not undefined
            
            $('#quantity').val(quantity + 1);

          
            // Increment
        
    });

     $('.quantity-left-minus').click(function(e){
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#quantity').val());
        
        // If is not undefined
      
            // Increment
            if(quantity>1){
            $('#quantity').val(quantity - 1);
            }
    });
    
});
