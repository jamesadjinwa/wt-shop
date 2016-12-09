$( document ).ready(function() {
    console.log( "ready!" );
   $('.messages').fadeOut(5000);
   
   /*$('#fbutton').click(function() {
	var name = $("input#name").val();
	if (name == "") {
		console.log( "Error" );
		$("{{ form.contact_name.errors }}").show();
		$("input#name").focus();
		return false;
	}
	var email = $("input#email").val();
	if (email == "") {
		$("{{ form.contact_email.errors }}").show();
		$("input#email").focus();
		return false;
	}
});*/

});


/*{% if messages %}
function fadeMessages(element) {
    var op = 0.9;  // initial opacity
    var timer = setInterval(function () {
        if (op <= 0.1){
            clearInterval(timer);
            element.style.display = 'none';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
    }, 50);
}


{% endif %}*/

