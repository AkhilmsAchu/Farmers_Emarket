
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
