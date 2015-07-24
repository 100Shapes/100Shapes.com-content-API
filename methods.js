var _ = require('lodash');

module.exports = function(server) {
  server.method('getFolders', function (next) {
    return next(null, _.keys(server.app.content));
  });

  server.method('getFolder', function (folder_name, next) {
    folder = {};
    folder[folder_name] = [];
    if(_.has(server.app.content, [folder_name])){
      server.app.content[folder_name].items.forEach(function(item) {
        item_meta = _.omit(item, server.app.ignoreFromList)
        folder[folder_name].push(item_meta);
      });
    }
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
