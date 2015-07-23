var fs = require('fs');
var yaml2json = require('yaml-to-json');

module.exports = function(server) {
  server.start(function () {
      content_folders = fs.readdirSync(server.app.content_path);
      content_folders.forEach(function(folder_name) {
        var folder = {};
        folder.path = server.app.content_path + folder_name;
        server.app.content[folder_name] = folder;
        content_files = fs.readdirSync(server.app.content_path + folder_name);
        server.app.content[folder_name].items = [];
        console.log('loaded --' + folder_name);
        content_files.forEach(function(item_name) {
          var path = server.app.content_path + folder_name + '/' + item_name
          var item = {};
          item = yaml2json(fs.readFileSync(path + '/index.html', "utf8"), {prose: true});
          item.slug = item_name;
          item.path = path;
          server.app.content[folder_name].items.push(item)
          console.log('loaded ----' + item.title);
        });
      });
      console.log('Server running at:', server.info.uri);
  });
};
