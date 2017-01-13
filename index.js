var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var util = require("util");
var spawn = require("child_process").spawn;
var process;


app.get('/', function(req, res){
  res.sendfile('index.html');
});

users = [];

io.on('connection', function(socket){
  console.log('a user connected'+socket);

    socket.on('setUsername', function(data){
        console.log(data);
        users.push(data);
        socket.emit('userSet', {username: data});
    });

    socket.on('msg', function(datam){

        //Send message to everyone
        if (datam.message.toString().startsWith("/bot ")) {
            var s = datam.message.toString();
            console.log('keyword found'+datam.message);
            var arg = s.substring(8,s.length);

            var textChunk = "";

            util.log('readingin')

            process = spawn('python',["processCommand.py",arg]);

            process.stdout.on('data',function(chunk){
                textChunk = chunk.toString();// buffer to string

                io.sockets.emit('newmsg', datam);
                datam.message = "Riskex Output: "+textChunk;
                console.log("Python returned 1: " +textChunk);
                datam.user = "RiskexBOT";
                io.sockets.emit('newmsg', datam);
            });
            //console.log("Python returned 2: " +textChunk);
            //console.log("Data message being published:"+datam.message);

            //console.log("Now the data message is:"+datam.message);
        }
        else{
            console.log('keyword not found'+datam.message);
            io.sockets.emit('newmsg', datam);
        }

    })

  socket.on('chat message', function(msg){
      console.log(socket.toString()+": "+msg);
      io.sockets.emit('chat message', io+": "+msg);

      if (msg === "/riskex buy") {
          io.sockets.emit('chat message', "............."+socket.toString()+", You wanna buy?");
      }
      if (msg === "/riskex sell") {
          io.sockets.emit('chat message', "............."+socket.toString()+", You wanna buy?");
      }
  });


  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
