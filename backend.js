var Joi = require('joi');

module.exports = function(server) {
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
                    console.log(err);
                } else {
                    reply(item).code(200);
                }
            })
        },
        config: {
            validate: {
                query: {
                    limit: Joi.number().integer(),
                    featured: Joi.boolean()
                }
            }
        }
    });

    server.route({
        method: 'GET',
        path: '/{folder_name}',
        handler: function(request, reply) {
            var requested = {
                folder: request.params.folder_name,
                limit: request.query.limit,
                featured: request.query.featured
            };
            server.methods.getFolder(requested, function(err, folder_items) {
                if (err) {
                    console.log(err);
                } else {
                    reply(folder_items).code(200);
                }
            })
        },
        config: {
            validate: {
                query: {
                    limit: Joi.number().integer(),
                    featured: Joi.boolean()
                }
            }
        }
    });
}
