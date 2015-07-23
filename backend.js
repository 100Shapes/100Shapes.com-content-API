module.exports = function(server) {
  server.route({
      method: 'GET',
      path: '/',
      handler: function (request, reply) {
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
    handler: function (request, reply) {
      server.methods.getFolderItem(request.params.folder_name, request.params.item_name, function(err, item) {
        if (err) {
            console.log(err);
        } else {
            reply(item).code(200);
        }
      })
    }
  });

  server.route({
      method: 'GET',
      path: '/{folder_name}',
      handler: function (request, reply) {
        server.methods.getFolder(request.params.folder_name, function(err, folder_items) {
          if (err) {
              console.log(err);
          } else {
              reply(folder_items).code(200);
          }
        })
      }
  });
}
