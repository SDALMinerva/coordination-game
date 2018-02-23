function activeFunction(data){
	if (data.type == 'send') {	
		wall.parseAddEntry(data.content);
	} else if (data.type == 'private') {
        messenger.parseAddEntry(data.content);	    
	} else if (data.type == 'list') {
		wall.parseExistingEntries(data.content);		
	} else if (data.type == 'entry-table'){
	    console.log(data);
	    resultTable.update(data.content);
	    
	}
};

function nonActiveFunction(data){
	player_list.updateCount(data.id, data.count);
};

chat = new Chat(neighbors, activeFunction, nonActiveFunction);
chat.setActiveChannel(nodeId);

function Chat(idList, activeFunction, nonActiveFunction) {
    var channels = {};
    
	if (!(idList.indexOf(nodeId))>-1){
		channels[nodeId] = new Channel(nodeId,activeFunction, nonActiveFunction);
	}
    
	for (i = 0, len = idList.length; i < len; i++) {
		var id = idList[i];
		channels[id] = new Channel(id,activeFunction, nonActiveFunction);
	};
	this.infoChannel = new Channel('comm-'+nodeId,activeFunction,nonActiveFunction);
	this.infoChannel.active = true;
    this.privateChannel = new Channel('private-'+nodeId,activeFunction,nonActiveFunction);
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
	
	var socket;
	socket = new ReconnectingWebSocket(urlTemplate(id));
	socket.onmessage = function(message) {
		console.log('Receiving ' + this.id);
		var data = JSON.parse(message.data);		
		if(this.active){
  			this.activeFunc(data);
  		} else {
  			var data = {};
  			this.count += 1;
  			data.count = this.count;
  			data.id = this.id;
  			this.nonActiveFunction(data);
  		}
	}.bind(this);
	
	this.socket = socket;
	
	this.send = function(data){
		socket.send(data);
		console.log('Sending '+id);
	};
};

function urlTemplate(id){
	var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
	var url = ws_scheme + '://' + window.location.host + "/chat/" + id;
	return url
};