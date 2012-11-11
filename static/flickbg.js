
function generateBgUrl(){

	var urlPrefix = "";

    urlPrefix = "full";

	var photourl = $("#photopage").val();
	var m = photourl.match(/photos\/[^\/]+\/([0-9]+)/i);


	$("#finalurl").val("http://" + domain +"/" + urlPrefix + "/" + m[1]);

}


function showPreview(){
	window.open($("#finalurl").val());
	return false;
}



$(document).ready(function() {

	//Events in which to generate the new URL
	$("#photopage").bind("change", generateBgUrl);
	$("#photopage").keyup(function(event) {generateBgUrl();});


	//Handles the preview link click
	$("#preview").click(function() { showPreview(); })


	//Selects all the text in a textbox
	$('#photopage, #finalurl, #colorpicker').live('focus mouseup', function(e) {
					if (e.type == 'focusin') {
					this.select();
					}

		if (e.type == 'mouseup') {
		return false;
		}
		});


	$('body').addClass('has-js');
	$('.label_check, .label_radio').click(function() {
		setupLabel();
	});
	setupLabel();
});