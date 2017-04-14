var wall = new Wall();
wall.init(playerId, entries);

function Wall() {
	
	this.init = function (id,entries) {
		
		this.Parent = document.getElementById('wall');
		
		this.label = document.createElement('h2');
		this.label.innerHTML = 'Player ' + id + ' Wall';
		this.Parent.appendChild(this.label);

		this.instructions = document.createElement('h4');
		this.instructions.innerHTML = 'Send a message to Player ' + id + ':';
		this.Parent.appendChild(this.instructions);		
		
		this.messages = document.createElement('div');
		this.messages.className = 'list-group';
		for (i=0, len = messageList.length; i < len; i++){
			var newMessage = document.createElement('a');
			newMessage.className = 'list-group-item message';
			newMessage.innerHTML = messageList[i];			
			this.messages.appendChild(newMessage);
		};
		this.Parent.appendChild(this.messages);		
		
		this.wall = document.createElement('div');
		this.wall.className = 'list-group';

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
		this.label.innerHTML = 'Player ' + id + ' Wall';
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

$(".message").click(function(event){
  var message = {
  	 wallId: wall.Id,
    createdBy: playerId,
    text: $(this).text(),
  }
  var toSend = JSON.stringify({
  		'type': 'send',
  		'content': message,
  	});
  console.log(toSend);
  chat.activeChannel.send(toSend);
  return false;
});

function parseEntryData(input){
	this.author = input.author;
	this.timestamp = input.timestamp;
	this.content = input.content;
	
	return new Entry(this.author, this.timestamp, this.content)
};

function Entry(author,timestamp,content) {
	this.author = author;
	this.timestamp = timestamp;
	this.content = content;
	
	this.Entry = function () {
		var listItem = document.createElement('li');
		var listHeading = document.createElement('h4');
		var listP = document.createElement('p');
		
		listItem.className = 'list-group-item';
		
		listHeading.innerHTML = '[' + this.timestamp 
										 + '][' + this.author + ']';
   	listHeading.className = 'list-group-item-heading';
   	listItem.appendChild(listHeading);
   	
   	listP.innerHTML= this.content;
   	listP.className = 'list-group-item-text';
   	listItem.appendChild(listP);
   	
   	return listItem;
	};
};