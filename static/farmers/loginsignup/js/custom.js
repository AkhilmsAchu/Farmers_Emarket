
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
	$('.deleteproduct').click(function(e){
        // Stop acting like a button
		e.preventDefault();
		var bid = e.target.id;
	    var pid = $(this).attr('data-id');
	    var txt;
		var r = confirm("Are You Sure, You Want to Delete this Product ?");
		if (r == true) {
		  var req = new XMLHttpRequest();
		    req.onreadystatechange = function() {
		    if (this.readyState == 4 && this.status == 200) {
		      alert(req.responseText)
		      window.location.href = "/farmers/dash/";
		    }

		    };
		    req.open("GET", "/farmers/deleteproduct?id="+encodeURIComponent(pid), true);
		    req.send(); 
		} else {
		  
		}
		
    });
$('.marksold').click(function(e){
        // Stop acting like a button
		e.preventDefault();
		var bid = e.target.id;
	    var pid = $(this).attr('data-id');

		var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	location.reload();
	      alert(req.responseText)
	      if (req.responseText=='true'){
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "/farmers/markproduct?id="+encodeURIComponent(pid)+'&type='+encodeURIComponent("sold"), true);
	    req.send(); 
    });
$('.markunsold').click(function(e){
        // Stop acting like a button
		e.preventDefault();
		var bid = e.target.id;
	    var pid = $(this).attr('data-id');

		var req = new XMLHttpRequest();
	    req.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	location.reload();
	      alert(req.responseText)
	      if (req.responseText=='true'){
	      	document.getElementById(bid).disabled = true;
	      }
	    }

	    };
	    req.open("GET", "/farmers/markproduct?id="+encodeURIComponent(pid)+'&type='+encodeURIComponent("unsold"), true);
	    req.send(); 
    });
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
