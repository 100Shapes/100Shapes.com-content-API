
# 100Shapes.com content-API
100 Shapes site - Content-API

## Useful URLs

### All blog posts
	/api/v1/pages/?type=blog.BlogPost&fields=title,post_category,thumbnail_url

## Deploy

1. 'docker build -t tutum.co/memolipd/ohs-api .'
2. 'docker push tutum.co/memolipd/ohs-api'
3. if you have to migrate, (added migration files) then login to tutum
4. run ohs-api terminal
5 'python manage.py migrate'

if styles are not showing:
1. login to tutum
2. run ohs-api terminal
3 'python manage.py collectstatic'

