var Joi = require('joi');

module.exports = function(server, feed) {
    server.route({
        method: 'GET',
        path: '/',
        handler: function(request, reply) {
            server.methods.getFolders(function(err, folders) {
                if (err) {
                    console.log(err);
                } else {
                    reply(folders).code(200);
                }
            })
        }
    });

    server.route({
        method: 'GET',
        path: '/{folder_name}/{item_name}',
        handler: function(request, reply) {
            server.methods.getFolderItem(request.params.folder_name, request.params.item_name, function(err, item) {
                if (err) {
                    console.log(err, request.params.folder_name, request.params.item_name);
                    reply(err).code(404);
                } else {
                    reply(item).code(200);
                }
            })
        }
    });

    server.route({
        method: 'GET',
        path: '/{folder_name}',
        handler: function(request, reply) {
            server.methods.getFolder(request.params.folder_name, request.query, function(err, folder_items) {
                if (err) {
                    reply(err).code(404);
                } else {
                    reply(folder_items).code(200);
                }
            })
        }
    });
    server.route({
        method: 'GET',
        path: '/sitemap.xml',
        handler: function(request, reply) {
            reply(server.app.sitemap.toString()).code(200);
        }
    });
    server.route({
        method: 'GET',
        path: '/rss.xml',
        handler: function(request, reply) {
            reply(server.app.feed.xml()).code(200);
        }
    });
}
