var net = require('net');
var zombie = require('zombie');
var browser = null;
var buffer = '';

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

  
var server = net.createServer(function (stream) {
  stream.allowHalfOpen = true;
  //stream.setEncoding("utf8");

  stream.on("data", function (data) {
    //browser = new zombie.Browser();
    //console.log('executing ' + data);
    //var result = eval(data);
    //console.log('writing ' + result);
    //stream.write(result);
    buffer += data;
    console.log('data', buffer);
  });

  stream.on("end", function () {
    console.log('end');
    
    if (browser === null) {
      browser = new zombie.Browser();
    }
    eval(buffer);
    buffer = "";
    //stream.end();
  });
});
server.listen(8042, "localhost");


console.log('Zombie server running at http://127.0.0.1:8042/');
