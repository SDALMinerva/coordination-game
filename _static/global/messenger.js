var messenger = new Messenger();
messenger.init(playerId, privateEntries);

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
		
		this.wallimg = document.createElement('span');
		this.wallimg.className = "wallimg glyphicon glyphicon-envelope center-block";
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
//		this.instructions.innerHTML = 'Send a message to ' + userNames[id] + ':';
		this.messageBlock.appendChild(this.instructions);		
		
		
        // SELECTION FORM.		
		this.sendTo = document.createElement('div');
		this.sendTo.className = 'input-group message-group highlight';
		var addon = document.createElement('span');
		addon.className = 'input-group-addon user-display';
		addon.innerHTML = '<span class="glyphicon glyphicon-user" aria-hidden="true"></span>';
		this.sendTo.appendChild(addon);
		
		var input = document.createElement('input');
		input.className = "form-control recipient-text";
		input.type = "text";
		input.disabled = true;
		input.placeholder = "< select recipient >";
		this.sendTo.appendChild(input);
		
		var dropdown = document.createElement('span');
		dropdown.className = "input-group-btn";
		dropdown_button = document.createElement('button');
		dropdown_button.className = "btn btn-default dropdown-toggle";
		dropdown_button.setAttribute("data-toggle", "dropdown");
		var caret = document.createElement('span');
		caret.className = "caret";
		var toggle = document.createElement('span');
		toggle.className = "sr-only";
		dropdown_button.appendChild(caret);
		dropdown_button.appendChild(toggle);
		var messageListBox = document.createElement('ul');
		messageListBox.className = "dropdown-menu";
		messageListBox.id = 'recipient-box';

		var tempId = neighbors[i];
		var newRow = document.createElement('li');
		var newMessage = document.createElement('a');
		newMessage.className = 'recipient-option';
		newMessage.innerHTML = "<span class='img-recipient glyphicon glyphicon-bullhorn'></span><span class='recipient-name pull-right'>Everyone</span>" + "<span id='ID' style='visibility: hidden;'>all</span>";			
		newRow.appendChild(newMessage)			
		messageListBox.appendChild(newRow);
		
		for (i=0, len = neighbors.length; i < len; i++){
		    var tempId = neighbors[i];
			var newRow = document.createElement('li');
			var newMessage = document.createElement('a');
			newMessage.className = 'recipient-option';
			newMessage.innerHTML = "<img class='img-recipient' src='/static/avatar/" + avatars[tempId] + 
			"'><span class='recipient-name pull-right'>" + userNames[tempId] + "</span>" + "<span id='ID' style='visibility: hidden;'>"+tempId+"</span>";			
			newRow.appendChild(newMessage)			
			messageListBox.appendChild(newRow);	
		};
		
//		var send_button = document.createElement('button');
//		send_button.className = "btn btn-default send-message";
//		send_button.innerHTML = "Post Message";
		
		dropdown.appendChild(dropdown_button);
		dropdown.appendChild(messageListBox);
//		dropdown.appendChild(send_button);
		
		this.sendTo.append(dropdown);		
		this.messageBlock.appendChild(this.sendTo);		
		
		
		// INPUT FORM.
		this.messages = document.createElement('div');
		this.messages.className = 'input-group message-group highlight';
		this.addon = document.createElement('span');
		this.addon.className = 'input-group-addon';
		this.addon.innerHTML = '<span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>';
		this.messages.appendChild(this.addon);
		
		this.input = document.createElement('input');
		this.input.className = "form-control private-message-text";
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
			newMessage.className = 'private-message-option';
			newMessage.innerHTML = messageList[i];			
			newRow.appendChild(newMessage)			
			this.messageList.appendChild(newRow);
			
		};
		
		this.send_button = document.createElement('button');
		this.send_button.className = "btn btn-default send-message";
		this.send_button.innerHTML = "Send Message";
		
		this.dropdown.appendChild(this.dropdown_button);
		this.dropdown.appendChild(this.messageList);
		this.dropdown.appendChild(this.send_button);
		
		this.messages.append(this.dropdown);		
		this.messageBlock.appendChild(this.messages);		

        this.wallMain = document.createElement('div');
        this.wallMain.className = 'row';
        this.wallOne = document.createElement('div');
        this.wallOne.className = 'col-xs-12';
        this.wallTwo = document.createElement('div');
        this.wallTwo.className = 'col-xs-4 shiftleft';
        this.wallMain.appendChild(this.wallOne);
//        this.wallMain.appendChild(this.wallTwo);

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
		
		this.label.innerHTML = "Private Messages";
		this.instructions.innerHTML = "Choose a recipient and private message:";
		this.wallLabel.innerHTML = "Private messages sent to you:";
        
//        var friendName = ((id == this.ownId) ? '' : uName + " friends:");
//        this.friendLabel.innerHTML = friendName;
//        this.friend_list = new PlayerList();
//        this.friend_list.init(neighbor_net[id], 'friendWall');		
		
		this.wallimg.src = '/static/avatar/' + avatars[id];

//		$(this.wall).empty();	
//		this.wall.innerHTML = '<h5 id="wallMessage"> You do not have any private messages, yet.</h5>';

	}.bind(this);
	
	this.loadFromPost = function(){
	
	};
	
	this.parseExistingEntries = function(entries){
		for (i = 0, len = entries.length; i<len; i++){
			this.parseAddEntry(entries[i]);		
		}
	};
};

$("#messenger .send-message").click(function(event){
  if ($("#messenger .private-message-text").val() == ''){
  		return false;
  }
  if ($("#messenger .recipient-text").val() == ''){
  		return false;
  }
  
  var message = {
  	recipientId: messenger.Id,
    createdBy: playerId,
    text: $("#messenger .private-message-text").val(),
    messageRound: messageRound,
  }

// Button Behavior After Clicking - Depends on interaction type.
if (messageRound == -1){
    $("#messenger .private-message-text").val('');
} else {
//    $("#messenger .private-message-text").prop("disabled", true);
//    $(messenger.dropdown_button).prop("disabled", true);
//    messenger.send_button.innerHTML = 'Posted'
    
//    $("#messenger span .glyphicon").fadeOut(500, function(){
//        $("#messenger span .glpyhicon").removeClass("glyphicon-pencil");
//        $("#messenger span .glyphicon").addClass("glyphicon-ok");
//        $("#messenger span .glyphicon").fadeIn(500);
//        $(messenger.send_button).prop("disabled",true);
//        $("#messenger .highlight").removeClass("highlight");
//    });
    $("#messenger .private-message-text").val('');
}  

  var toSend = JSON.stringify({
  		'type': 'private',
  		'content': message,
  	});

  console.log(toSend);
  chat.privateChannel.send(toSend);
  
  return false;
});


$("#messenger .recipient-option").click(function(event){
	var text = $(this).find('.recipient-name').html();
	$("#messenger .recipient-text").val(text);
	messenger.changeId($(this).find('#ID').html());
	$('.user-display').empty();
	$('.user-display').html($(this).find('.img-recipient').clone());
});


$("#messenger .private-message-option").click(function(event){
	var text = $(this).html();
	$("#messenger .private-message-text").val(text);
});


// enable clicking on text input
$('#messenger input[type="text"]:disabled').click(function(e){
	//alert('hey');
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
   	
   	listP.innerHTML= 'Sent by: ' + userNames[id];// + '       ' 
//   						+ '[' + this.timestamp + ']';
   	listP.className = 'media-body';
   	listItem.appendChild(listP);
   	
   	return listItem;
	};
};