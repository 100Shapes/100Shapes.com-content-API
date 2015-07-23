var Hapi = require('hapi');

var server = new Hapi.Server();
server.connection({ port: 3000 });

server.app.content_path = './content/';
server.app.content = {};

var start = require('./start')(server);
var methods = require('./methods')(server);
var backend = require('./backend')(server);

module.exports = server;
