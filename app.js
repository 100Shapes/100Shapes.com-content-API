var Hapi = require('hapi');

var server = new Hapi.Server();
server.connection({ port: 3000 });

server.app.base_url = process.env['API_BASE_URL'] || 'http://proto.api.100shapes.com';
server.app.content_path = process.env['CONTENT_PATH'] || 'content';


server.app.ignoreFromList = ['contents', 'mode'];
server.app.content = {};

var start = require('./start')(server);
var methods = require('./methods')(server);
var backend = require('./backend')(server);

module.exports = server;
