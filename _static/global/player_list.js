var player_list = new PlayerList();
player_list.init(neighbors);

function PlayerList() {
	
	this.init = function (idList) {
			
		this.Parent = document.getElementById('playerList');

		this.playerList = document.createElement('div');
		this.playerList.className = 'list-group';
		
		//var listTitle = document.createElement('li');
		//listTitle.className = 'list-group-item';
		//listTitle.innerHTML = 'Your Friends';
		
		//this.playerList.appendChild(listTitle);		

		this.Parent.appendChild(this.playerList);
		
		this.counts = {}
		for (var i=0, len = idList.length; i<len; i++){
			var newButton = new PlayerButton(idList[i]);			
			this.addButton(newButton);
			this.counts[idList[i]] = newButton.count;	
		}
		
		this.updateCount = function(id,count) {
			//Change when decide what to do with player counts...
			if (id != playerId){			
				if (count > 0){
					this.counts[id].innerHTML = count;
				} else {
					this.counts[id].innerHTML = '';
				}
			}
		};
		return
	};
	
	this.addButton = function(playerButton) {
		this.playerList.appendChild(playerButton.Link())
	};
	
	
};

function createMediaObject(img_src, heading, content){
	var media = document.createElement('div');
	media.className = "media";
	
	var media_object = document.createElement('img');
	media_object.className = "media-object pull-left media-center";
	media_object.src = img_src;
	media_object.alt = "not found";
	media_object.width = 48;
	
	var media_body = document.createElement('div');
	media_body.className = "media-body";
	
	var media_heading = document.createElement('h4');
	media_heading.className = "media-heading";
	media_heading.innerHTML = heading;	

	var media_content = document.createElement('p');
	media_content.innerHTML = content;	
	
	media_body.appendChild(media_heading);
	media_body.appendChild(media_content);
	
	media.appendChild(media_object);
	media.appendChild(media_body);
	
	return media;
};

function PlayerButton(id) {
	this.id = id;
	
	var display_name = userNames[id];
	var display_threshold = 'Threshold: ' + thresholds[id];
	
	var count = document.createElement('span');
	count.className = 'badge';
	
	var img_src = '/static/avatar/' + avatars[id];
	
	this.Link = function(){

		var media = createMediaObject(img_src, display_name, display_threshold);		
		
		var element = document.createElement('a');
		element.href = "#" + id;
		element.className = "list-group-item";
		element.onclick = function () {
				chat.setActiveChannel(id);
				wall.changeId(id);
				chat.infoChannel.send(JSON.stringify({
					'type': 'list',
					'content': {'playerId': id},				
				}));
			};
		element.appendChild(media);
		element.appendChild(count);
		return element
	};
	
	this.count = count;
};