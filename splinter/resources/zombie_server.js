var net = require('net');
var zombie = require('zombie');
var browser = null;

/*net.createServer(function (stream) {
  stream.setEncoding('utf8');
  stream.allowHalfOpen = true;

  stream.on('data', function (data) {
    buffer += data;
  });

  stream.on('end', function () {
    if (browser == null) {
      browser = new zombie.Browser();
    }
    eval(buffer);
    buffer = "";
  });
}).listen(8042, 'localhost');*/

var net = require("net");
  
var server = net.createServer(function (stream) {
  stream.setEncoding("utf8");

  stream.on("connect", function () {
      if (browser == null) {
        browser = new zombie.Browser();
      }
  });
  
  stream.on("data", function (data) {
    console.log('executing ' + data);
    var result = eval(data);
    console.log('writing ' + data);
    stream.write(result); 
  });

  stream.execute = function(data) {
  }     
  
  stream.on("end", function () {
    stream.end();
  });
});
server.listen(8042, "localhost");


console.log('Zombie server running at http://127.0.0.1:8042/');
