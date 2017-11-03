var wall = new Wall();
wall.init(playerId, entries);

function Wall() {
	
	this.init = function (id,entries) {
		
		this.Parent = document.getElementById('wall');

		this.topRow = document.createElement('div');
		this.topRow.className = 'row';
		this.Parent.appendChild(this.topRow);
		
		this.topRowImg = document.createElement('div');
		this.topRowImg.className = "col-lg-2";
		this.topRowImg.id = "wallImgContainer";
		this.topRow.appendChild(this.topRowImg);
		this.topRowHeader = document.createElement('div');
		this.topRowHeader.className = "col-lg-12";
		this.topRow.appendChild(this.topRowHeader);
		
		this.wallimg = document.createElement('img');
		this.wallimg.className = "wallimg img-responsive center-block";
		this.wallimg.alt = "not found";
		this.topRowImg.appendChild(this.wallimg);
		
		this.label = document.createElement('h2');
		this.topRowHeader.appendChild(this.label);

		this.instructions = document.createElement('h4');
		this.instructions.innerHTML = 'Post a message to ' + userNames[id] + ':';
		this.topRowHeader.appendChild(this.instructions);		
		
		// Input Form.
		this.messages = document.createElement('div');
		this.messages.className = 'input-group';
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
		this.send_button.innerHTML = "Post";
		
		this.dropdown.appendChild(this.dropdown_button);
		this.dropdown.appendChild(this.messageList);
		this.dropdown.appendChild(this.send_button);
		
		this.messages.append(this.dropdown);		
		this.topRowHeader.appendChild(this.messages);		

		this.wallLabel = document.createElement('h4');
		this.Parent.appendChild(this.wallLabel);			
		
		this.wall = document.createElement('div');
		this.wall.className = 'list-group wall well';

		this.Parent.appendChild(this.wall);
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
		this.label.innerHTML = userNames[id] + "'s Wall";
		this.instructions.innerHTML = 'Post a message to ' + userNames[id] + "'s wall:";
		this.wallLabel.innerHTML = 'Posts from ' + userNames[id] + "'s friends:";
		this.wallimg.src = '/static/avatar/' + avatars[id];
		$(this.wall).empty();	
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
  }
  $(".message-text").val('');
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
		
		listItem.className = 'list-group-item media';

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
   	
   	listP.innerHTML= 'Post by: ' + userNames[id] + '       ' 
   						+ '[' + this.timestamp + ']';
   	listP.className = 'media-body';
   	listItem.appendChild(listP);
   	
   	return listItem;
	};
};