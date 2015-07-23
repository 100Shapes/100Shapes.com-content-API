var _ = require('lodash');

module.exports = function(server) {
  server.method('getFolders', function (next) {
    folders = [];
    return next(null, _.keys(server.app.content));
  });

  server.method('getFolder', function (folder_name, next) {
    folder = {};
    folder[folder_name] = [];
    server.app.content[folder_name].items.forEach(function(item) {
      item_meta = _.omit(item, ['html','noop'])
      folder[folder_name].push(item_meta);
    });
    return next(null, folder);
  });

  server.method('getFolderItem', function (folder_name, item_name,  next) {
    item = server.app.content[folder_name].items.filter(function(filtered_item) {
      return filtered_item.slug == item_name;
    });
    return next(null, item);
  });
};
