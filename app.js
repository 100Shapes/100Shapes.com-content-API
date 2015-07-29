var Hapi = require('hapi');
var url = require('url')
var sm = require('sitemap')
var RSS = require('rss');

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

server.app.content_path = process.env['CONTENT_PATH'] || 'content';
server.app.base_url = process.env['VIRTUAL_HOST'] ? ('http://' + process.env['VIRTUAL_HOST']) : 'http://localhost:3000';

server.app.frontend_url = process.env['FRONTEND_URL'] || 'http://frontend.100shapes.com';


server.app.ignoreFromList = ['contents', 'mode', 'stats'];
server.app.content = {};

server.start(function () {
    console.log('Server running at:', server.info.uri);
});

server.app.sitemap = sm.createSitemap ({
    hostname: server.app.base_url,
    cacheTime: 600000
});

server.app.feed = new RSS({
    title: "100 Shapes - Blog",
    feed_url: url.resolve(server.app.base_url, '/blog/feed/'),
    site_url: server.app.frontend_url
});

var start = require('./start')(server);
var methods = require('./methods')(server);
var backend = require('./backend')(server);

module.exports = server;
