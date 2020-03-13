
$(document).ready(function(){

var quantitiy=1;
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
	    	
	      alert(req.responseText)
	      if (req.responseText=='true'){
	      	$(this).attr('disabled', true);
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
