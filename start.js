var path = require('path')
var _ = require('lodash');
var url = require('url')
var cheerio = require('cheerio');
var fs = require('fs');
var md5 = require('md5');
var typeset = require('typeset');

var Metalsmith = require('metalsmith');

var htmlMinifier = require("metalsmith-html-minifier");
var ignore = require('metalsmith-ignore');

function getFolderAtLevel(file_path, level) {
    return file_path.split(path.sep)[level];
}

module.exports = function(server) {
    server.start(function() {
        console.log('Using base url: ' + server.app.base_url)
        console.log('Using content From: ' + server.app.content_path)
        var metalsmith = Metalsmith(__dirname)

        .source(server.app.content_path)
            .destination("public")

        .use(htmlMinifier()) // Use the default options

        //.use(typeset_content)

        .use(load)

        .use(ignore('**/index.html'))

        .build(function(err) {
            if (err) throw err;
        });

        console.log('Server running at:', server.info.uri);
    });

    function make_links_absolute(contents, relative_path) {
        $ = cheerio.load(contents.toString());
        $('img').each(function(i, elem) {
            var src = url.parse(elem.attribs.src);
            if (src.protocol == null) {
                var absolute_url = url.resolve(server.app.base_url, path.join(relative_path, src.href));
                elem.attribs.src = absolute_url;
            }
        });
        return $.html();
    };


    function load(files, metalsmith, done) {

        var folders = [];
        // Find all root folders
        _.forOwn(files, function(file, file_path) {
            folders.push(getFolderAtLevel(file_path, 0));
        });
        folders = _.uniq(folders, true)

        _.forEach(folders, function(folder_name) { // loop over folders

            // Add a 'folder' to server's 'content' object
            server.app.content[folder_name] = {};
            server.app.content[folder_name].items = [];
            server.app.content[folder_name].meta = [];
            console.log('loaded --' + folder_name);

            _.forOwn(files, function(item, file_path) { // Loop over all metalsmith 'files'

                if (getFolderAtLevel(file_path, 0) == folder_name) { // Loop over all metalsmith 'files'
                    if ('title' in item) { // Check to see if the current metalsmith 'file' has a title
                        item.slug = getFolderAtLevel(file_path, 1);
                        item.absolute_url = url.resolve(server.app.base_url, path.join(folder_name, item.slug))
                        item.contents = make_links_absolute(item.contents, path.join(folder_name, item.slug));
                        item.frontend_url = url.resolve(server.app.frontend_url, path.join(folder_name, item.slug))
                        item.guid = md5(item.slug);

                        // Add items sitemap and RSS feeds
                        server.app.sitemap.add({
                            url: item.frontend_url
                        });

                        if (folder_name == "blog") {
                            server.app.feed.item({
                                title: item.title,
                                description: item.contents,
                                url: item.frontend_url,
                                date: item.date,
                                author: item.author || "100 Shapes",
                                guid: item.guid
                            });
                        }

                        // Find any image properties and make them absolute
                        _.forOwn(item, function(value, key) {
                            if (key.indexOf('_image') >= 0) {

                                item[key] = url.resolve(server.app.base_url, path.join(folder_name, item.slug, value));
                            }
                        });

                        server.app.content[folder_name].items.push(item) // Add metalsmith 'file' to server's 'content' object
                        console.log('loaded  ----' + item.title);
                    } else if (getFolderAtLevel(file_path, 1) == 'meta.html') { // is therefore static
                        server.app.content[folder_name].meta = item // add metalsmith 'file' to folder's meta
                        console.log('loaded  ----' + folder_name + '-META');
                    } else {
                        console.log('loaded  ------(static)-' + file_path);
                    }
                    server.app.content[folder_name].meta.count = _.size(server.app.content[folder_name].items)
                }
            });
        });
        done();
    };

    function typeset_content(files, metalsmith, done) {
        _.each(files, function (file, key) {
           if (path.extname(key) === '.html') {
               file.contents = typeset(file.contents.toString());
           }
        });
        done();
    };
};
