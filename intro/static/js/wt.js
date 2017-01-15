var $logo = $('#logo-scr');
var $brandname = $('#brand-name');
$(document).ready(function() {
 	$(document).scroll(function() {
 	$brandname.css({display: $(this).scrollTop()>100 ? "block":"none"});
 	$logo.css({display: $(this).scrollTop()<100 ? "block":"none"});
	});
});
 

