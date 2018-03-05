var d = [
    {'name': 'Cow', 'icon': 'Cow-icon.png', '0': true, '1': false},
    {'name': 'Turtle', 'icon': 'Turtle-icon.png', '0': true, '1': false},
    {'name': 'Cat', 'icon': 'Cat-icon.png', '0': false, '1': true},
    {'name': 'Swan', 'icon': 'Swan-icon.png', '0': true, '1': true},
    {'name': 'Eagle', 'icon': 'Eagle-icon.png', '0': false, '1': false},
];

if (output){
    var resultTable = new ResultTable();
    resultTable.init(d);
}

function ResultTable() {

    this.getInfo = function(){
        chat.infoChannel.send(JSON.stringify({
					'type': 'entry-table',
					'content': {'sentBy': nodeId},				
				}));    
    }

    this.update = function(d){
        console.log(d);
        this.Parent.innerHTML = "";
        this.init(d);
    }    
    
    this.init = function (d) {
        
        var Parent = document.getElementById('resultTable');
        var table = document.createElement('table');
        table.className = "table table-sm";
        
        table.appendChild(this.header(this.labels));

        for (var i=0; i<d.length; i++){
            table.appendChild(this.row(d[i]));        
        }        
        
        Parent.appendChild(table);
        this.Parent = Parent;        
        };
        
        
    this.header = function (labels) { 
        var tr = document.createElement('tr');
        for (var i=0; i<labels.length; i++){
            var th = document.createElement('th');
            th.style= 'text-align: center'
            th.innerHTML = labels[i];
            tr.appendChild(th);        
        }
        return tr;
    };
    
    this.labels = ['', 'You Posted:<br/> "I will participate."', 'You Posted:<br/> "I will not participate."'];
    this.row = function (r) {
        var tr = document.createElement('tr');
        tr.innerHTML = "<td>" + this.avatarSpan(r.icon,r.name) + "</td><td style='text-align: center;'>" + this.tfspan(r['0']) + "</td><td style='text-align: center;'>" + this.tfspan(r['1']) + "</td>";
        return tr
        };
    this.avatarSpan = function(x,y){
        return "<img style = 'display: inline-block; margin-right: 20px; max-width: 20px' class = 'img img-responsive' src='/static/avatar/" + x + "' alt=''><span>" + y + "</span>"
    }    
    this.tfspan = function (x) {
        if (x){
            return "<span class='glyphicon glyphicon-ok'></span>"        
        }
        return "";
    };
};