var _ = require('lodash');

module.exports = function(server) {
    server.method('getFolders', function(next) {
            return next(null, _.keys(server.app.content));
        }
        // , {
        //     cache: {
        //         expiresIn: 60 * 60 * 1000
        //     },
        //     generateKey: function(opts) {
        //         return JSON.stringify(opts);
        //     }
        // }
    );

    server.method('getFolder', function(requested, next) {
        if (!_.has(server.app.content, [requested.folder])) {
            return next('No folder found');
        }
        var folder = {};
        folder.meta = {};

        folder.meta = _.omit(server.app.content[requested.folder].meta, server.app.ignoreFromList)
        if (requested.meta != true) {
            var items_name = 'items'
            folder[items_name] = [];
            server.app.content[requested.folder].items.forEach(function(item) {
                item_meta = _.omit(item, server.app.ignoreFromList)
                if (requested.featured == item_meta.featured) {
                    folder[items_name].push(item_meta);
                }
            });
            if (requested.random == true) {
                console.log('random')
                folder[items_name] = _.shuffle(folder[items_name]);
            } else {
                folder[items_name] = _.sortBy(folder[items_name], 'date');
                folder[items_name] = folder[items_name].reverse()
            }
            folder[items_name] = folder[items_name].slice(0, requested.limit);
        }
        return next(null, folder);
    }
    // , {
    //     cache: {
    //         expiresIn: 60 * 60 * 1000
    //     },
    //     generateKey: function(opts) {
    //         return JSON.stringify(opts);
    //     }
    // }
    );

    server.method('getFolderItem', function(folder_name, item_name, next) {
        if (!_.has(server.app.content, [folder_name])) {
            return next('No item found');
        }
        var item = _.find(server.app.content[folder_name].items, 'slug', item_name);
        return next(null, item);
    }, {
        cache: {
            expiresIn: 60 * 60 * 1000
        },
        generateKey: function(opts) {
            return JSON.stringify(opts);
        }
    });
};
