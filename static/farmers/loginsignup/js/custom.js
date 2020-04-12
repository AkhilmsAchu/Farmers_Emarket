
function ordercount(){
    var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	document.getElementById('ordercount').innerHTML = '['+req.responseText+']';
	      if (req.responseText=='true'){
	      	$(this).attr('disabled', true);
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "/farmers/ordercount", true);
	    req.send();
          
};

window.onload=ordercount;

$(document).ready(function(){

 $('.mark-as-delivered').click(function(e){
        // Stop acting like a button
		e.preventDefault();
		var bid = e.target.id;
	    var pid = $(this).attr('data-id');
		var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	ordercount();
	    	location.reload();
	      alert(req.responseText)
	      if (req.responseText=='Marked as Delivered'){
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "/farmers/markdelivered?id="+encodeURIComponent(pid), true);
	    req.send(); 
    });
    
});
