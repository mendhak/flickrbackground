function setupLabel() {
	if ($('.label_check input').length) {
		$('.label_check').each(function() {
			$(this).removeClass('c_on');
		});
		$('.label_check input:checked').each(function() {
			$(this).parent('label').addClass('c_on');
		});
	};

	if ($('.label_radio input').length) {
		$('.label_radio').each(function() {
			$(this).removeClass('r_on');
		});
		$('.label_radio input:checked').each(function() {
			$(this).parent('label').addClass('r_on');
		});
	};
};

function generateBgUrl(){
	 var selectedBgType = $("input[name='bgtype']:checked").val();

	var urlPrefix = "";

	switch(selectedBgType){
		case "1":
		urlPrefix = "magic";
		break;

		case "2":
		urlPrefix = "full";
		break;

		case "3":
		urlPrefix = $("#colorpicker").val();
		default:
		break;
	}


	var photourl = $("#photopage").val();
	var m = photourl.match(/photos\/[^\/]+\/([0-9]+)/i);


	$("#finalurl").val("http://flkr.me/" + urlPrefix + "/" + m[1]);

}


function showPreview(){
	window.open($("#finalurl").val());
	return false;
}

function colorPickerChanged(){
	generateBgUrl();
	document.getElementsByTagName('BODY')[0].style.backgroundColor = '#'+this.color;
}


$(document).ready(function() {

	$("#photopage").bind("change", generateBgUrl);
	$("#photopage").keyup(function(event) {generateBgUrl();});
	$("#colorpicker").bind("change", colorPickerChanged);
	$("#previewlink").click(function() { showPreview(); })
	$("input[name='bgtype']").change(function(){ generateBgUrl(); })

	$('textarea, input').live('focus mouseup', function(e) {
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