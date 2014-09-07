$(document).ready(function() {
	// All links on page make Ajax calls
	$('a').click(function() {
		$.get($(this).attr('href'));
		return false;	// don't bubble-up
	});
});
