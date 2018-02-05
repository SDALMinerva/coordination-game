var wall = new Wall();
wall.init(nodeId, entries, output);

function Wall() {
	
	this.init = function (id,entries, output=true) {

        this.ownId = id;		
		
		this.Parent = document.getElementById('wall');

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
        
        if (output){
            this.postBlock.appendChild(this.messageBlock);
        }

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
		
		this.label.innerHTML = uName + " Wall";
		this.instructions.innerHTML = 'Post a message to ' + uName + " wall:";
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
            this.wall.innerHTML = '<p style="font-size: 10pt; line-height: 100%;" id="wallMessage"> Use the tool above to post a message on the wall. The posts will appear once you and everyone else is done with sending messages and proceed to the decision part by clicking "Next" below.</p>';		
		}

		for (i = 0, len = entries.length; i<len; i++){
			this.parseAddEntry(entries[i]);		
		}
	};
};

$("#wall .send-message").click(function(event){
  if ($(".message-text").val() == ''){
  		return false;
  }  
  
  var currentDate = new Date();
  var key = currentDate.toString();
  key += wall.Id;
  key += nodeId;
  key += messageRound;
  key = key.hashCode();

  $('#wallMessage').html('');
  var message = {
  	 wallId: wall.Id,
    createdBy: nodeId,
    text: $("#wall .message-text").val(),
    messageRound: messageRound,
    key: key,
  }

// Button Behavior After Clicking - Depends on interaction type.
if (messageRound == -1){
    $("#wall .message-text").val('');
} else {
//    $("#wall .message-text").prop("disabled", true);
//    $(wall.dropdown_button).prop("disabled", true);
//    wall.send_button.innerHTML = 'Posted'
    
//    $("#wall span .glyphicon").fadeOut(500, function(){
//        $("#wall span .glpyhicon").removeClass("glyphicon-pencil");
//        $("#wall span .glyphicon").addClass("glyphicon-ok");
//        $("#wall span .glyphicon").fadeIn(500);
//        $(wall.send_button).prop("disabled",true);
//        $("#wall .highlight").removeClass("highlight");
//    });
    wall.addEntry(new NewlyAddedEntry(nodeId,2018,$("#wall .message-text").val(), key));
    $("#wall .message-text").val('');
}  

  var toSend = JSON.stringify({
  		'type': 'send',
  		'content': message,
  	});
  console.log(toSend);
  chat.activeChannel.send(toSend);
  return false;
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
});

$("#wall .message-option").click(function(event){
	var text = $(this).html();
	$("#wall .message-text").val(text);
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
		
		listItem.backgroundColor = '#ddd';
		listItem.className = 'newly-added list-group-item media message-item';
		
		var closebutton = document.createElement('button');
   	    closebutton.innerHTML = "<span style='font-size: 25pt;'>&times;</span>";
   	    closebutton.className = "close pull-left removeEntry";
   	    closebutton.style = "margin-left: -10px; margin-top: 0; padding: 0;";
   	    closebutton.type = "button";
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
//   						+ '[' + this.timestamp + ']';
   	listP.className = 'media-body';
   	listItem.appendChild(listP);
   	
   	var keyDiv = document.createElement('div');
   	keyDiv.innerHTML = key;
   	keyDiv.className = 'key';
    keyDiv.style = 'visibility: hidden; width: 0; height: 0; margin:0; padding:0;';
    listItem.appendChild(keyDiv);  
    
   	return listItem;
	};
};
