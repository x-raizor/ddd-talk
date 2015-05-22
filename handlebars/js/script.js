$(function() {

	$.ajax({
		//url: 'http://api.randomuser.me/?results=20',
		url: 'data/persones-20.json',
		dataType: 'json',
		success: function(d) {
			var source = $("#template").html();
			var template = Handlebars.compile(source);
			var html = template(d);
			$("body").html(html);
		}
	});

});