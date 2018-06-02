var wall = new Wall();
wall.init(nodeId, entries, output);

var noSendMessage = 'Send no messages this round';

if (output){
    var wallMessenger = new WallMessenger();
    wallMessenger.init();
}

function disable_recipients(wall_sent_to){
    console.log('Disabling...');
    console.log(wall_sent_to);
    $('.recipient-option').each(function() {$(this).parent().removeClass('disabled')});
    console.log(wall_sent_to);
    for (var key in wall_sent_to){
        if(wall_sent_to[key] > 0){
           console.log('Disabling ' + key);
           $('#recipient-option-'+key).parent().addClass('disabled'); 
        }
    }
};

function WallMessenger() {

    this.sentMessages = {};
    
    this.init = function () {
        this.messageBlock = $('.message-tool-content')[0];
        this.instructions = document.createElement('h5');
		this.messageBlock.appendChild(this.instructions);		
		
		
        // SELECTION FORM.		
		this.sendTo = document.createElement('div');
		this.sendTo.className = 'input-group message-group';//highlight
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
		dropdown_button.className = "btn btn-default dropdown-toggle clicktrack";
		dropdown_button.setAttribute("data-toggle", "dropdown");
		var caret = document.createElement('span');
		caret.className = "caret";
		var toggle = document.createElement('span');
		toggle.className = "sr-only";
		dropdown_button.appendChild(caret);
		dropdown_button.appendChild(toggle);
		dropdown_button.id = "recipient-dropdown";
		var messageListBox = document.createElement('ul');
		messageListBox.className = "dropdown-menu";
		messageListBox.id = 'recipient-box';

		var newRow = document.createElement('li');
		var newMessage = document.createElement('a');
		newMessage.className = 'recipient-option clicktrack';
		newMessage.innerHTML = "<span class='img-recipient glyphicon glyphicon-bullhorn'></span><span class='recipient-name pull-right'>All Friends</span>" + "<span id='ID' style='visibility: hidden;'>all</span>";			
        newMessage.id = 'recipient-option-all';		
		newRow.appendChild(newMessage)			
		messageListBox.appendChild(newRow);
		
		for (i=0, len = neighbors.length; i < len; i++){
		    var tempId = neighbors[i];
			var newRow = document.createElement('li');
			var newMessage = document.createElement('a');
			newMessage.className = 'recipient-option clicktrack';

//            if (wall_sent_to[tempId] > 0){
//                newRow.classList.add('disabled');
//            }			
			
			newMessage.id = 'recipient-option-' + tempId;
			newMessage.innerHTML = "<img class='img-recipient' src='/static/avatar/" + avatars[tempId] + 
			"'><span class='recipient-name pull-right'>" + userNames[tempId] + "</span>" + "<span id='ID' style='visibility: hidden;'>"+tempId+"</span>";			
			newRow.appendChild(newMessage)			
			messageListBox.appendChild(newRow);	
		};
		
		// OWN ROW.
		var newRow = document.createElement('li');
		var newMessage = document.createElement('a');
		newMessage.className = 'recipient-option clicktrack';
		newMessage.id = 'recipient-option-' + nodeId;
		newMessage.innerHTML = "<img class='img-recipient' src='/static/avatar/" + avatars[nodeId] + 
			"'><span class='recipient-name pull-right'>" + userNames[nodeId] + " (You)</span>" + "<span id='ID' style='visibility: hidden;'>"+nodeId+"</span>";			
	
		newRow.appendChild(newMessage)			
		messageListBox.appendChild(newRow);
		
		// NO SEND.
		var newRow = document.createElement('li');
		var newMessage = document.createElement('a');
		newMessage.className = 'recipient-option clicktrack';
		newMessage.id = 'recipient-option-no-send';
		newMessage.innerHTML = "<span class='img-recipient glyphicon glyphicon-remove'></span><span class='recipient-name pull-right'>" + noSendMessage + "</span>" + "<span id='ID' style='visibility: hidden;'>all</span>";			
	
		newRow.appendChild(newMessage)			
		messageListBox.appendChild(newRow);
		
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
		this.messages.className = 'input-group message-group'; //highlight
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
		this.dropdown_button.className = "btn btn-default dropdown-toggle clicktrack";
		this.dropdown_button.id = "message-list-dropdown";
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
			newMessage.className = 'message-option clicktrack';
			newMessage.id = 'message-option-' + i;
			newMessage.innerHTML = messageList[i];			
			newRow.appendChild(newMessage)			
			this.messageList.appendChild(newRow);
			
		};
		
		this.send_button = document.createElement('button');
		this.send_button.className = "btn btn-default send-message clicktrack";
		this.send_button.type = 'button';
		this.send_button.id = "send-message-button";
		this.send_button.innerHTML = "Submit";
		
		this.dropdown.appendChild(this.dropdown_button);
		this.dropdown.appendChild(this.messageList);
		this.dropdown.appendChild(this.send_button);
		
		this.messages.append(this.dropdown);		
		this.messageBlock.appendChild(this.messages)
		
		disable_recipients(wall_sent_to);
	}
};

function Wall() {
	
	this.init = function (id,entries, output=true) {

        output = typeof output !== 'undefined' ? output : true;

        this.ownId = id;		
		
		this.Parent = document.getElementById('wall-card-body');

		this.topRow = document.createElement('div');
		this.topRow.className = 'row topRow';
		this.Parent.appendChild(this.topRow);
		
		this.topRowImg = document.createElement('div');
		this.topRowImg.className = "col-xs-2";
		this.topRowImg.id = "wallImgContainer";
		this.topRow.appendChild(this.topRowImg);
		this.topRowHeader = document.createElement('div');
		this.topRowHeader.className = "col-xs-10 titleContainer";
		this.topRow.appendChild(this.topRowHeader);
		
		this.wallimg = document.createElement('img');
		this.wallimg.className = "wallimg img-responsive center-block";
		this.wallimg.alt = "not found";
		this.topRowImg.appendChild(this.wallimg);
		
		this.label = document.createElement('h4');
		this.label.className = "card-title";
		this.labeltext = document.createElement('h6');
		this.labeltext.className = "card-subtitle mb-2 text-muted";
		if (output) {
		this.labeltext.innerHTML = 'Use the tool above to post a message on the wall. Sent posts will be received once you and everyone else is done with sending messages and proceed to the decision part by clicking "Next" below.';
        } else {
        this.labeltext.innerHTML = "View posts on your wall or your friend's wall.";        
        }
		this.topRowHeader.appendChild(this.label);
		this.topRowHeader.appendChild(this.labeltext);



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

    this.removeEntry = function(entryItem){
        $(entryItem).hide();
        entryItem.parentNode.removeChild(entryItem);
    };	
	
	this.addEntry = function(entry) {
	    var newEntry = entry.Entry();
	    var entryBackground = newEntry.backgroundColor;

	    if (!entryBackground){entryBackground = '#fff';}
		$(newEntry)
		.hide()
		.prependTo(this.wall)
		.css({
			backgroundColor: "orange",
			})
		.slideDown()
		.animate({
			backgroundColor: entryBackground,
			}, 1000);
		
	};
	
	this.parseAddEntry = function(input) {
	   this.addEntry(parseEntryData(input));		
	};
	
	this.changeId = function(id) {
		this.Id = id;
        
        var uName = ((id == this.ownId) ?  'Your' : userNames[id] + "'s");		
		
		this.label.innerHTML = "" + uName + " Wall";
		this.wallLabel.innerHTML = 'Posts on ' + uName + " wall:";
        
        var friendName = ((id == this.ownId) ? '' : uName + " friends:");
        this.friendLabel.innerHTML = friendName;
        this.friend_list = new PlayerList();
        this.friend_list.init(neighbor_net[id], 'friendWall');		
		
		this.wallimg.src = '/static/avatar/' + avatars[id];
		$(this.wall).empty();
		
	}.bind(this);
	
	this.loadFromPost = function(){
	
	};
	
	this.parseExistingEntries = function(entries){
	    if ((entries.length == 0) && (messageRound <= nMessagingRound) ){
            this.wall.innerHTML = '<p style="margin-top: 10px; font-size: 10pt; line-height: 100%;" id="wallMessage"> No messages to display.</p>';		
		} else if (entries.length == 0) {
            this.wall.innerHTML = '<p style="margin-top: 10px; font-size: 10pt; line-height: 100%;" id="wallMessage"> No messages to display.</p>';
		}

		for (i = 0, len = entries.length; i<len; i++){
			this.parseAddEntry(entries[i]);		
		}
	};
};


$("#wall").on("click", ".recipient-option", function(event){
    if(!$(this).parent().hasClass('disabled')){
        if ($(".recipient-text").val() == noSendMessage){
            $('#message-list-dropdown').attr('disabled',true);
            $('#send-message-button').addClass('btn-primary');
            $('.message-text').val('');  
        } else {
            $('#message-list-dropdown').attr('disabled',false);
        }
    
        if (($(".recipient-text").val() != noSendMessage) && ($(".message-text").val() == '')){
            $('#send-message-button').removeClass('btn-primary');
        }
    
        if (($(".recipient-text").val() != noSendMessage) && ($(".message-text").val() != '')){
            $('#send-message-button').addClass('btn-primary');
        }     
    } 
});

$("#wall").on("click", ".message-option", function(event){    
    if (($(".recipient-text").val() != '') && ($(".message-text").val() != '')){
        $('#send-message-button').addClass('btn-primary');
    }  
});


$("#wall").on("click", ".send-message", function(event){

  if ($(".recipient-text").val() == noSendMessage){
      $('#btn-discuss-next').attr('disabled', false);
      $('#send-message-button').removeClass('btn-primary');
      
      var message = {
             createdBy: nodeId,
             text: $("#wall .message-text").val(),
             messageRound: messageRound,
       }

       var toSend = JSON.stringify({
  		    'type': 'participate_flag',
  		    'content': message,
  	   });
       console.log(toSend);
       chat.infoChannel.send(toSend);
       $('#selector-alert').fadeOut();
       $('#selector-no-message').fadeIn().delay(10000).fadeOut(); 
       return;  
  }

  if ($(".message-text").val() == ''){
        $('#selector-alert').fadeIn();
  		return;
  }
  
  if ($(".recipient-text").val() == ''){
        $('#selector-alert').fadeIn();
        return;  
  }
  
  $('#selector-alert').fadeOut(); 
  
  $('#send-message-button').removeClass('btn-primary');

//$('#wallMessage').html('');
/////////////////////////////////////
///////// Messaging Portion /////////
/////////////////////////////////////

var recipient = $('#wall .recipient-text').val();
var sent = false;
if (recipient == 'All Friends'){
    for (var i=0; i < neighbors.length; i++){
        var neighbor = neighbors[i];
        
        if (!(wall_sent_to[neighbor] > 0)){
            console.log(wall_sent_to[neighbor]);
        var currentDate = new Date();
        var keyString = currentDate.toString();
        keyString += neighbor;
        keyString += nodeId;
        keyString += messageRound;
        var key = keyString.hashCode();
        
        var message = {
  	         wallId: neighbor,
             createdBy: nodeId,
             text: $("#wall .message-text").val(),
             messageRound: messageRound,
             key: key,
        }

        var toSend = JSON.stringify({
  		    'type': 'send',
  		    'content': message,
  	    });
        console.log(toSend);
        chat.channels[neighbor].send(toSend);
        $('#btn-discuss-next').attr('disabled', false);
        
        if(!(wall.Id in wall_sent_to)){wall_sent_to[wall.Id]=0;}
        wall_sent_to[wall.Id] += 1;
        disable_recipients(wall_sent_to);
        if (wall.Id == neighbor){
        sent = true;}
    }
    }
} else if (recipient != noSendMessage){
  console.log(recipient);
  var currentDate = new Date();
  var keyString = currentDate.toString();
  keyString += wall.Id;
  keyString += nodeId;
  keyString += messageRound;
  var key = keyString.hashCode();

  var message = {
  	wallId: wall.Id,
    createdBy: nodeId,
    text: $("#wall .message-text").val(),
    messageRound: messageRound,
    key: key,
  }

  var toSend = JSON.stringify({
  		'type': 'send',
  		'content': message,
  	});
  console.log(toSend);
  chat.activeChannel.send(toSend);
  $('#btn-discuss-next').attr('disabled', false);
  
          if(!(wall.Id in wall_sent_to)){wall_sent_to[wall.Id]=0;}
        wall_sent_to[wall.Id] += 1;
        disable_recipients(wall_sent_to);  
}
/////////////////////////////////////
/////////////////////////////////////

// Button Behavior After Clicking - Depends on interaction type.
if (messageRound == -1){
    
} else if((recipient == 'All Friends') && (wall.Id != nodeId) && (sent)) {
    wall.addEntry(new NewlyAddedEntry(nodeId,2018,$("#wall .message-text").val(), key));
    $('#selector-success').fadeIn().delay(5000).fadeOut(); 
} else if((recipient != 'All Friends') && (recipient != noSendMessage)) {
    wall.addEntry(new NewlyAddedEntry(nodeId,2018,$("#wall .message-text").val(), key));
    $('#selector-success').fadeIn().delay(5000).fadeOut(); 
}

    $("#wall .message-text").val('');
    $("#wall .recipient-text").val('');
    $('.user-display').empty();
	$('.user-display').html('<span class="glyphicon glyphicon-user" aria-hidden="true"></span>');  

  return;
  

});



$("#wall").on('click', '.removeEntry', function(event){
    var entry = $(this).parents(".newly-added")[0];
    var key = $(entry).children(".key").html();
    
    var message = {
  	    wallId: wall.Id,
        key: key,
    }
    var toSend = JSON.stringify({
  		'type': 'wall-delete',
  		'content': message,
  	});
    console.log(toSend);
    chat.activeChannel.send(toSend);
    wall.removeEntry(entry);
    wall_sent_to[wall.Id] -= 1;
    disable_recipients(wall_sent_to);
});

$("#wall .message-option").click(function(event){
	var text = $(this).html();
	$("#wall .message-text").val(text);
});

$("#wall .recipient-option").click(function(event){
    if(!$(this).parent().hasClass('disabled')){
        
	var text = $(this).find('.recipient-name').html();
	$("#wall .recipient-text").val(text);
	$('.user-display').empty();
	$('.user-display').html($(this).find('.img-recipient').clone());
	var id = $(this).find('#ID').html();
	if(id != 'all'){
	   chat.setActiveChannel(id);
		wall.changeId(id);
		chat.infoChannel.send(JSON.stringify({
		  'type': 'list',
		  'content': {'playerId': id, 'sentBy': nodeId},				
		}));
	}
	
    $('.linking-button').removeClass('active');
    $('#player-button'+id).addClass('active');
    
}
});







// To-do. enable clicking on text input
$('#wall input[type="text"]:disabled').click(function(e){
//	alert('hey');
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
	this.key = input.key;
	
	if (input.messageRound == messageRound) {
	   return new NewlyAddedEntry(this.sendId, this.timestamp, this.content, this.key)
	} else {
	   return new Entry(this.sendId, this.timestamp, this.content, this.key)
    }
};

function Entry(id,timestamp,content,key) {
	this.id = id;
	this.timestamp = timestamp;
	this.content = content;
	
	this.Entry = function () {
		var listItem = document.createElement('li');
		var listHeading = document.createElement('h4');
		var listP = document.createElement('p');
		
		listItem.backgroundColor = '#fff';
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
   	
   	var nameAdd = ((id == wall.ownId) ? " (You)" : '');
   	listP.style = "font-size: 9pt;";
   	listP.innerHTML= 'Post by: ' + userNames[id] + nameAdd;// + '       ' 
//   						+ '[' + this.timestamp + ']';
   	listP.className = 'media-body';
   	listItem.appendChild(listP);
   	
   	var keyDiv = document.createElement('div');
   	keyDiv.innerHTML = key;
    keyDiv.style = 'visibility: hidden; width: 0; height: 0; margin:0; padding:0;';
    keyDiv.className = 'key';
    listItem.appendChild(keyDiv);   	
   	
   	return listItem;
	};
};


function NewlyAddedEntry(id,timestamp,content, key) {
	this.id = id;
	this.timestamp = timestamp;
	this.content = content;
	
	this.Entry = function () {
		var listItem = document.createElement('li');
		var listHeading = document.createElement('h4');
		var listP = document.createElement('p');
		
		listItem.backgroundColor = '#f2f2f2';
		listItem.className = 'newly-added list-group-item media message-item ';
		
		var closebutton = document.createElement('button');
   	    closebutton.innerHTML = "<span style='font-size: 13pt; color: #000;' class='glyphicon glyphicon-trash'></span>";
   	    closebutton.className = "close pull-left removeEntry clicktrack";
   	    closebutton.style = "display: inline-block; margin-left: -10px; margin-top: 12px; padding: 0px;";
   	    closebutton.type = "button";
   	    closebutton.setAttribute('data-toggle','tooltip'); 
   	    closebutton.setAttribute('data-placement','tooltip');
   	    closebutton.title='Delete Message';
   	    closebutton.id = 'message-delete-' + key;
   	    listItem.appendChild(closebutton);

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
   	
   	var nameAdd = ((id == wall.ownId) ? " (You)" : '');
   	listP.style = "font-size: 9pt;";
   	listP.innerHTML= 'Post by: ' + userNames[id] + nameAdd; 
//   						+ '[' + this.timestamp + ']' 
   	listP.className = 'media-body';
   	listItem.appendChild(listP);
   	listItem.innerHTML += '<p class="sent-message">only you can see this message - it will be received in the decision part</p>';
   	
   	var keyDiv = document.createElement('div');
   	keyDiv.innerHTML = key;
   	keyDiv.className = 'key';
    keyDiv.style = 'visibility: hidden; width: 0; height: 0; margin:0; padding:0;';
    listItem.appendChild(keyDiv);  
    
   	return listItem;
	};
};
