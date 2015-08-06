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
            var requested = {
                folder: request.params.folder_name,
                limit: request.query.limit,
                featured: request.query.featured,
                meta: request.query.meta,
                draft: request.query.draft,
                random: request.query.random
            };
            server.methods.getFolder(requested, function(err, folder_items) {
                if (err) {
                    console.log(err, requested.folder);
                    reply(err).code(404);
                } else {
                    reply(folder_items).code(200);
                }
            })
        },
        config: {
            validate: {
                query: {
                    limit: Joi.number().integer(),
                    featured: Joi.boolean(),
                    meta: Joi.boolean(),
                    draft: Joi.boolean().default(false),
                    random: Joi.boolean()
                }
            }
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
