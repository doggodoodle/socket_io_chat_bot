var util = require("util");

var spawn = require("child_process").spawn;
var process;

util.log('readingin')

process = spawn('python',["processCommand.py","BUY"]);

var s = "/riskex j17 165/150 ps x187 .02/.025";
if(s.startsWith("/riskex ")){
    util.log("starts with /riskex ");
    var arg = s.substring(8,s.length);
    util.log("arg="+arg);
}


process.stdout.on('data',function(chunk){



    var textChunk = chunk.toString('utf8');// buffer to string

    util.log(textChunk);
});