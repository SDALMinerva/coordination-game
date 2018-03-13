// Simulated Messaging

var someEntries = {
    1:  [
        {'id': 1, 'content': 'I will not participate', 'author': 'Player 2'},
        {'id': 1, 'content': 'I will participate', 'author': 'Player 4'},
        {'id': 1, 'content': 'I will not participate', 'author': 'Player 3'},
        ],
    2:  [
        {'id': 1, 'content': 'I will participate', 'author': 'Player 1'},
        {'id': 1, 'content': 'I will not participate', 'author': 'Player 2'},
        ],
    3:  [
        {'id': 1, 'content': 'I will not participate', 'author': 'Player 1'},
        ],
    4:  [
        {'id': 1, 'content': 'I will participate', 'author': 'Player 4'},
        ],
    5:  [
        {'id': 1, 'content': 'I will not participate', 'author': 'Player 1'},
        {'id': 1, 'content': 'I will not participate', 'author': 'Player 5'},
        ],};

function activeFunction(data){
	if (data.type == 'send') {	
		wall.parseAddEntry(data.content);
	} else if (data.type == 'private') {
        messenger.parseAddEntry(data.content);	    
	} else if (data.type == 'list') {
		wall.parseExistingEntries(data.content);		
	}
};

function nonActiveFunction(data){
	player_list.updateCount(data.id, data.count);
};

chat = new Chat(neighbors, activeFunction, nonActiveFunction);
chat.setActiveChannel(nodeId);

function Chat(idList, activeFunction, nonActiveFunction) {

	if (!(idList.indexOf(nodeId))>-1){
		idList.push(nodeId);
	}

	var channels = {};
	for (i = 0, len = idList.length; i < len; i++) {
		var id = idList[i];
		channels[id] = new Channel(id,activeFunction, nonActiveFunction);
	};
	this.infoChannel = new Channel('pseudo-comm-'+nodeId,activeFunction,nonActiveFunction);
	this.infoChannel.active = true;
    this.privateChannel = new Channel('pseudo-private-'+nodeId,activeFunction,nonActiveFunction);
	this.privateChannel.active = true;
	this.channels = channels;

	this.setActiveChannel = function (id) {
		for (var i in this.channels) {
			channels[i].active = false;		
		}
		
		this.channels[id].active = true;
		this.channels[id].count = 0;
		nonActiveFunction({'type': 'send', 'id': id, 'count': this.count});
		this.activeChannel = this.channels[id];
	}.bind(this);
};

function Channel(id, activeFunc, nonActiveFunction){
	this.id = id;
	this.activeFunc = activeFunc;
	this.nonActiveFunction = nonActiveFunction;
	this.active = false;
	this.count = 0;
	
	this.send = function(data){
		console.log('PseudoSending '+id);
		wall.parseExistingEntries(someEntries[chat.activeChannel.id]);
	};
};