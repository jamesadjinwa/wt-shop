 var $logo = $('#logo-scr');
 var $brandname = $('#brand-name');
 $(document).onload(function() {
 	$brandname.css({display: none);
 	$logo.css({display: $(this)});
 });
 $(document).scroll(function() {
 	$brandname.css({display: $(this).scrollTop()>100 ? "block":"none"});
 	$logo.css({display: $(this).scrollTop()<100 ? "block":"none"});
 });

