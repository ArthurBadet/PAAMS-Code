var continuousVisualization = function(width, height, context) {
	var height = height;
	var width = width;
	var context = context;

	this.draw = function(objects) {
        // Draw the lines then the object
		for (var i in objects) {
			var p = objects[i];
            for (var j = parseInt(i) + 1 ; j < objects.length ; j++) {
                var q = objects[j];
                if (((p.x - q.x) * width) ** 2 + ((p.y - q.y) * height) ** 2 <= p.Range ** 2) {
                    this.drawLine(p.x, p.y, q.x, q.y, "black");
                }
            }
        }
        // Draw the objects with their name
		for (var i in objects) {
			var a = objects[i];
            var x = a.x * width;
            var y = a.y * height;
            this.drawCircle(x, y, a.Radius, a.Color, true);
            context.fillStyle = "white";
            context.font = "bold 11px mono";
            context.textAlign = "center";
            var text_metrics = context.measureText(a.Id);
            context.fillText(a.Id, x, y + text_metrics.actualBoundingBoxAscent/2);
        }
	};

	this.drawCircle = function(x, y, radius, color, fill) {
		var r = radius;
        context.lineWidth = 1;
		context.beginPath();
		context.arc(x, y, r, 0, Math.PI * 2, false);
		context.closePath();
		context.strokeStyle = color;
		context.stroke();
		if (fill) {
			context.fillStyle = color;
			context.fill();
		}
	};

    this.drawLine = function(x1, y1, x2, y2, color) {
        context.lineWidth = .3;
        context.beginPath();
        context.moveTo(x1 * width, y1 * height);
        context.lineTo(x2 * width, y2 * height);
		context.closePath();
        context.strokeStyle = color;
        context.stroke();
    };

	this.resetCanvas = function() {
		context.clearRect(0, 0, width, height);
		context.beginPath();
	};
};

var continuousSpace = function(canvas_width, canvas_height) {
	// Create the canvas and add it to the body
	var canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
	canvas_tag += "style='border:1px solid'></canvas>";
    //var canvas = document.getElementById(canvas_tag)[0];
    var canvas = $(canvas_tag)[0];
    //document.getElementById("#elements").appendChild(canvas);
	$("#elements").append(canvas);

	// Create the context and the drawing controller:
	var context = canvas.getContext("2d");
	var canvasDraw = new continuousVisualization(canvas_width, canvas_height, context);

	this.render = function(data) {
		canvasDraw.resetCanvas();
		canvasDraw.draw(data);
	};

	this.reset = function() {
		canvasDraw.resetCanvas();
	};

};
