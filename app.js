var Hapi = require('hapi');

var server = new Hapi.Server();
server.connection({
    port: 3000,
    router: {
        stripTrailingSlash: true
    },
    routes: {
        cors: true
    }
});


server.app.base_url = process.env['VIRTUAL_HOST'] ? ('http://' + process.env['VIRTUAL_HOST'] +'/v1') : 'http://localhost:3000';
server.app.content_path = process.env['CONTENT_PATH'] || 'content';
server.app.version = "v1"

server.app.ignoreFromList = ['contents', 'mode'];
server.app.content = {};

server.start(function () {
    console.log('Server running at:', server.info.uri);
});

var start = require('./start')(server);
var methods = require('./methods')(server);
var backend = require('./backend')(server);

module.exports = server;
