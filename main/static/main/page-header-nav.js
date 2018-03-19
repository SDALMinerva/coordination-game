$('.page-header').append(
  '<ul id="help-nav" class="nav pull-right">' +
    '<li class="no-hover nav-item pull-right">' + 
    	'<a id="quiz-nav" class="nav-link clicktrack" href="" data-toggle="modal" data-target="#QuizModal">Quiz</a>'+
  	'</li>' +
    '<li class="no-hover nav-item pull-right">' + 
    	'<a id="instructions-nav" class="nav-link clicktrack" href="" data-toggle="modal" data-target="#InstructionsModal">Instructions</a>' +
  	'</li>' +
  	'<li class="no-hover nav-item pull-right">' +
    	'<a id="tour-nav" class="nav-link clicktrack" href="javascript:void(0);" onclick="startIntro();">Tour</a>' +
  	'</li>'+
  	'</ul>'
);
