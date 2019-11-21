$( document ).ready(function() {
	$('#mail').on("change keyup paste click", function(){
		if ($('#mail').val().length > 3)
		{
			$('#btn_envoyer').removeAttr('disabled');
		}
		else
		{
			$('#btn_envoyer').attr('disabled', 'disabled');
		}
	});
});