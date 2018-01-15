var messenger = new Messenger();
messenger.init(playerId, entries);

function Messenger() {
	
	this.init = function (id,entries) {

        this.ownId = id;		
		
		this.Parent = document.getElementById('messenger');

		this.topRow = document.createElement('div');
		this.topRow.className = 'row topRow';
		this.Parent.appendChild(this.topRow);
		
		this.topRowImg = document.createElement('div');
		this.topRowImg.className = "col-xs-2";
		this.topRowImg.id = "wallImgContainer";
		this.topRow.appendChild(this.topRowImg);
		this.topRowHeader = document.createElement('div');
		this.topRowHeader.className = "col-xs-4 titleContainer";
		this.topRow.appendChild(this.topRowHeader);
		
		this.wallimg = document.createElement('img');
		this.wallimg.className = "wallimg img-responsive center-block";
		this.wallimg.alt = "not found";
		this.topRowImg.appendChild(this.wallimg);
		
		this.label = document.createElement('h2');
		this.topRowHeader.appendChild(this.label);

        this.postBlock = document.createElement('div');
        this.postBlock.className = "row";
        this.Parent.appendChild(this.postBlock);

        this.messageBlock = document.createElement('div');
        this.messageBlock.className = "col-xs-12";
        this.postBlock.appendChild(this.messageBlock);

		this.instructions = document.createElement('h5');
		this.instructions.innerHTML = 'Post a message to ' + userNames[id] + ':';
		this.messageBlock.appendChild(this.instructions);		
		
		// Input Form.
		this.messages = document.createElement('div');
		this.messages.className = 'input-group message-group highlight';
		this.addon = document.createElement('span');
		this.addon.className = 'input-group-addon';
		this.addon.innerHTML = '<span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>';
		this.messages.appendChild(this.addon);
		
		this.input = document.createElement('input');
		this.input.className = "form-control message-text";
		this.input.type = "text";
		this.input.disabled = true;
		this.input.placeholder = "< select message to send >";
		this.messages.appendChild(this.input);
		
		this.dropdown = document.createElement('span');
		this.dropdown.className = "input-group-btn";
		this.dropdown_button = document.createElement('button');
		this.dropdown_button.className = "btn btn-default dropdown-toggle";
		this.dropdown_button.setAttribute("data-toggle", "dropdown");
		this.caret = document.createElement('span');
		this.caret.className = "caret";
		this.toggle = document.createElement('span');
		this.toggle.className = "sr-only";
		this.dropdown_button.appendChild(this.caret);
		this.dropdown_button.appendChild(this.toggle);
		this.messageList = document.createElement('ul');
		this.messageList.className = "dropdown-menu";
		this.messageList.id = 'message-box';
		
		for (i=0, len = messageList.length; i < len; i++){
			var newRow = document.createElement('li');
			var newMessage = document.createElement('a');
			newMessage.className = 'message-option';
			newMessage.innerHTML = messageList[i];			
			newRow.appendChild(newMessage)			
			this.messageList.appendChild(newRow);
			
		};
		
		this.send_button = document.createElement('button');
		this.send_button.className = "btn btn-default send-message";
		this.send_button.innerHTML = "Post Message";
		
		this.dropdown.appendChild(this.dropdown_button);
		this.dropdown.appendChild(this.messageList);
		this.dropdown.appendChild(this.send_button);
		
		this.messages.append(this.dropdown);		
		this.messageBlock.appendChild(this.messages);		

        this.wallMain = document.createElement('div');
        this.wallMain.className = 'row';
        this.wallOne = document.createElement('div');
        this.wallOne.className = 'col-xs-8';
        this.wallTwo = document.createElement('div');
        this.wallTwo.className = 'col-xs-4 shiftleft';
        this.wallMain.appendChild(this.wallOne);
        this.wallMain.appendChild(this.wallTwo);

		this.wallLabel = document.createElement('h5');
		this.wallOne.appendChild(this.wallLabel);
		
		this.friendLabel = document.createElement('h5');
		this.wallTwo.appendChild(this.friendLabel);
		
		this.friendWall = document.createElement('div');
		this.friendWall.id = "friendWall";
		this.wallTwo.appendChild(this.friendWall);			
		
		this.wall = document.createElement('div');
		this.wall.className = 'list-group wall well';
		this.wallOne.appendChild(this.wall);

		this.Parent.appendChild(this.wallMain);
		this.changeId(id);

		this.parseExistingEntries(entries);		
		
		return
	};
	
	this.addEntry = function(entry) {
		$(entry.Entry())
		.hide()
		.prependTo(this.wall)
		.css({
			backgroundColor: "orange",
			})
		.slideDown()
		.animate({
			backgroundColor: "white",
			}, 1000);
	};
	
	this.parseAddEntry = function(input) {
		this.addEntry(parseEntryData(input));
	};
	
	this.changeId = function(id) {
		this.Id = id;
        
        var uName = ((id == this.ownId) ?  'Your' : userNames[id] + "'s");		
		
		this.label.innerHTML = uName + " Wall";
		this.instructions.innerHTML = 'Post a message to ' + uName + " wall:";
		this.wallLabel.innerHTML = 'Posts on ' + uName + " wall:";
        
        var friendName = ((id == this.ownId) ? '' : uName + " friends:");
        this.friendLabel.innerHTML = friendName;
        this.friend_list = new PlayerList();
        this.friend_list.init(neighbor_net[id], 'friendWall');		
		
		this.wallimg.src = '/static/avatar/' + avatars[id];
		$(this.wall).empty();
		
		this.wall.innerHTML = '<h5 id="wallMessage"> To display a message in the next messaging round, use the post tool above.</h5>';
	}.bind(this);
	
	this.loadFromPost = function(){
	
	};
	
	this.parseExistingEntries = function(entries){
		for (i = 0, len = entries.length; i<len; i++){
			this.parseAddEntry(entries[i]);		
		}
	};
};

$(".send-message").click(function(event){
  if ($(".message-text").val() == ''){
  		return false;
  }
  var message = {
  	 wallId: wall.Id,
    createdBy: playerId,
    text: $(".message-text").val(),
    messageRound: messageRound,
  }

// Button Behavior After Clicking - Depends on interaction type.
if (messageRound == -1){
    $(".message-text").val('');
} else {
    $(".message-text").prop("disabled", true);
    $(wall.dropdown_button).prop("disabled", true);
    wall.send_button.innerHTML = 'Posted'
    
    $("span .glyphicon").fadeOut(500, function(){
        $("span .glpyhicon").removeClass("glyphicon-pencil");
        $("span .glyphicon").addClass("glyphicon-ok");
        $("span .glyphicon").fadeIn(500);
        $(wall.send_button).prop("disabled",true);
        $(".highlight").removeClass("highlight");
    });
}  

  var toSend = JSON.stringify({
  		'type': 'send',
  		'content': message,
  	});
  console.log(toSend);
  chat.activeChannel.send(toSend);
  return false;
});


$(".message-option").click(function(event){
	var text = $(this).html();
	$(".message-text").val(text);
});

// enable clicking on text input
$('#wall input[type="text"]:disabled').click(function(e){
	alert('hey');
  // Kill click event:
//  e.stopPropagation();
  // Toggle dropdown if not already visible:
//  if ($('.dropdown').find('.dropdown-toggle').is(":hidden")){
//    $('.dropdown-toggle').dropdown('toggle');
//  }
});

function parseEntryData(input){
	this.sendId = parseInt(input.author.split(" ")[1]);
	this.timestamp = input.timestamp;
	this.content = input.content;
	
	return new Entry(this.sendId, this.timestamp, this.content)
};

function Entry(id,timestamp,content) {
	this.id = id;
	this.timestamp = timestamp;
	this.content = content;
	
	this.Entry = function () {
		var listItem = document.createElement('li');
		var listHeading = document.createElement('h4');
		var listP = document.createElement('p');
		
		listItem.className = 'list-group-item media message-item';

		var img_src = '/static/avatar/' + avatars[id];

      media_object = document.createElement('img');
		media_object.className = "media-object pull-left media-center";
		media_object.src = img_src;
		media_object.alt = "not found";
		media_object.width = 48;	
		listItem.appendChild(media_object)	
		
		listHeading.innerHTML = this.content;
   	listHeading.className = 'media-heading';
   	listItem.appendChild(listHeading);
   	
   	listP.innerHTML= 'Post by: ' + userNames[id];// + '       ' 
//   						+ '[' + this.timestamp + ']';
   	listP.className = 'media-body';
   	listItem.appendChild(listP);
   	
   	return listItem;
	};
};