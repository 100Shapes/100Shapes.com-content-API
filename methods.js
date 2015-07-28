var _ = require('lodash');

module.exports = function(server) {
  server.method('getFolders', function (next) {
    return next(null, _.keys(server.app.content));
  });

  server.method('getFolder', function (requested, next) {
    folder_name = requested.folder
    folder = {};
    folder[folder_name] = [];
    if(_.has(server.app.content, [folder_name])){
      server.app.content[folder_name].items.forEach(function(item) {
        item_meta = _.omit(item, server.app.ignoreFromList)
        if (requested.featured==item_meta.featured) {
            folder[folder_name].push(item_meta);
        }
      });
    }
    folder[folder_name] = folder[folder_name].reverse()
    folder[folder_name] = folder[folder_name].slice(0,requested.limit);
    _.sortBy(folder[folder_name],'date');
    return next(null, folder);
  });

  server.method('getFolderItem', function (folder_name, item_name,  next) {
    item = {};
    if(_.has(server.app.content, [folder_name])){
      item = _.find(server.app.content[folder_name].items, 'slug', item_name);
    }
    return next(null, item);
  });
};
