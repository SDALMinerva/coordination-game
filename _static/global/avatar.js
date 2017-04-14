var Avatar_grid = function () {
	
	this.grid = document.createElement("div");
	this.grid.className = 'row';

	this.create = function (parent) {
		$(this.grid).appendTo(parent);
	};

	this.addAvatar = function(src) {
		var div = document.createElement("div");
		div.className = "col-xs-6 col-sm-4 col-md-2 avatar_container";
		div.id = src.split('/').pop();
		
		var a = document.createElement("a");
		a.className = 'thumbnail';
		a.href = '#';
		
		var img = document.createElement('img');
		img.src = src;
		img.alt = 'No Avatar Found!';
		
		a.appendChild(img);
		div.appendChild(a);
		this.grid.appendChild(div);
		
		return div;
	};
};


var Avatar_form = function () {
	this.create = function (form) {	
		
		var avatar_img = document.createElement('img');
		avatar_img.src = root + 'Default-icon.png';
		avatar_img.id = 'avatar-selected';
		$(avatar_img).addClass("img-responsive");

		$(form).find(".image-form-selection").append(avatar_img);		
		this.input = document.createElement("input");
		this.input.type = "hidden";
		this.input.name = "avatar";
		this.input.id = "id_avatar";
		this.input.value = "none";		
		$(this.input).appendTo(form);
		
		avatar_grid = new Avatar_grid();
		grid_div = $(form).find(".image-form-choose");
		avatar_grid.create(grid_div);
		for (var i = 0, len = avatar_list.length; i < len; i++){
			avatar_grid.addAvatar(root + avatar_list[i]);
		}
		
		$('.avatar_container').click(function () {
			var img_name = $(this).attr('id');
			$('#id_avatar').attr('value', img_name);
			$('#avatar-selected').attr('src', root + img_name);	
		});
	};
};

var root = '/static/avatar/';
new_form = new Avatar_form();
new_form.create($("#image-form"));