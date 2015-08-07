var _ = require('lodash');

module.exports = function(server) {
    server.method('getFolders', function(next) {
        return next(null, _.keys(server.app.content));
    });

    server.method('getFolder', function(folder_name, query, next) {
        if (!_.has(server.app.content, [folder_name])) {
            return next('No folder found');
        }
        var folder = {};
        folder.meta = {};
        folder.meta = _.omit(server.app.content[folder_name].meta, server.app.ignoreFromList)

        if (query.meta != true) {
            var items_name = 'items';
            folder[items_name] = [];

            // Pull out reserved queries
            var limit = parseInt(query.limit);
            var random = false;
            if (_.has(query, 'random')) {
                random = (query['random'].toLowerCase() != 'false');
            }
            var draft = false;
            if (_.has(query, 'draft')) {
                draft = (query['draft'].toLowerCase() != 'false');
            }

            query = _.omit(query, ['limit', 'random', 'draft']);

            // Convert queries
            _.forEach(query, function(n, key) {
              if (_.indexOf(server.app.content[folder_name].meta.types.boolean, key) > -1) {
                    query[key] = (n.toLowerCase() != 'false');
                } else if (_.indexOf(server.app.content[folder_name].meta.types.number, key)> -1) {
                    query[key] = Number(n);
                }
            });

            // Filter items by coverted query
            folder[items_name] = _.filter(server.app.content[folder_name].items, query)

            // Sane Defaults
            if (draft) {
              folder[items_name] = _.filter(folder[items_name], 'draft', true)
            } else {
              folder[items_name] = _.reject(folder[items_name], 'draft', true)
            }

            // Sort returned items
            if (random != true) {
                folder[items_name] = _.sortBy(folder[items_name], '-date');
            } else {
                folder[items_name] = _.shuffle(folder[items_name]);
            }

            // Slice array down to size
            if (!isNaN(limit)){
              folder[items_name] = folder[items_name].slice(0, limit);
            }
        }

        return next(null, folder);
    });

    server.method('getFolderItem', function(folder_name, item_name, next) {
        if (!_.has(server.app.content, [folder_name])) {
            return next('No item found');
        }
        var item = _.find(server.app.content[folder_name].items, 'slug', item_name);
        return next(null, item);
    });
};
