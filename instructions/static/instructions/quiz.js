var highlightQuizMessage = function () {
    $(this).closest('li').siblings('li').find('.question-message').css('visibility', 'hidden');
	$(this).find('.question-message').css('visibility', 'visible'); 
}

$("#quiz .tf label").click(highlightQuizMessage);

$("#quiz select").change(function () {
    $(this).siblings('.oi').css('visibility','visible');
    
	if ($(this).find(':selected').hasClass('ok')){
	   $(this).siblings('.oi').removeClass('oi-x').addClass('ioi-check');
	   var qName = $(this).attr('name');
	   $('#quiz .question-message.'+qName).css('visibility','visible');
	} else {
	   $(this).siblings('.oi').removeClass('oi-check').addClass('oi-x');
	   var qName = $(this).attr('name');
	   $('#quiz .question-message.'+qName).css('visibility','visible');
	}
});

var complete = function () {
    $("#quiz select").find('.ok').prop('selected',true).trigger('change');
    $("#quiz input.ok").prop('checked', true).trigger('click');	
}

var disable = function () {
    $("#quiz input").prop('disabled', true);
    $("#quiz select").prop('disabled', true);
    $("#quiz .tf label").off('click', highlightQuizMessage);
}
