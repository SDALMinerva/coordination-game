for (var i = 0; i < network_nodes.length; i++) {
      var x = 100*Math.cos(i*2*Math.PI/network_nodes.length) + 100;
      var y = 100*Math.sin(i*2*Math.PI/network_nodes.length) + 100;
      network_nodes[i]['x'] = x;
      network_nodes[i]['y'] = y;
  }

  // create an array with nodes
  var nodes = new vis.DataSet(network_nodes);

  // create an array with edges
  var edges = new vis.DataSet(network_edges);

  // create a network
  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {
        physics: {
            enabled: false,
        },
  		interaction:{
    	dragNodes:false,
    	dragView: false,
    	hideEdgesOnDrag: false,
    	hideNodesOnDrag: false,
    	hover: true,
    	hoverConnectedEdges: true,
    	keyboard: {
      	enabled: false,
      	speed: {x: 10, y: 10, zoom: 0.02},
      	bindToWindow: true
    	},
    	multiselect: false,
    	navigationButtons: false,
    	selectable: true,
    	selectConnectedEdges: true,
    	tooltipDelay: 300,
    	zoomView: false,
  		},
  		nodes:{
  		    mass: 1,
  		    borderWidth: 2,
            color: '#ffffff',
            fixed: false,
            font: '16px arial black',
            font: {
                multi: 'html',
                size: 18,
                align: 'left',
                vadjust: -15,
            },
            scaling: {
                label: true
            },
            shadow: true,
            size: 40,
        },
        edges:{
            width: 6,
            length: 150,
            smooth: {'enabled': false},
        },

	}

  var network = new vis.Network(container, data, options);
  $('a[data-toggle="tab"][href="#network"]').on('shown.bs.tab', function (e) {
    network.fit();  		
  });
  
  network.on("afterDrawing", function (event) {
  	network.fit();
  	network.off("afterDrawing");
  });
  window.onresize = function() {network.fit();}