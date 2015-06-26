FROM phusion/passenger-customizable:0.9.15
MAINTAINER 100 Shapes <paolo@100shapes.com>
# Set correct environment variables.

# ENV HOME /app
ENV VIRTUAL_HOST api.100shapes.com
ENV PRODUCTION True

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]

#   Build system and git.
RUN /pd_build/utilities.sh
RUN /pd_build/python.sh

RUN apt-get update && apt-get install -y -o Dpkg::Options::="--force-confold" passenger nginx-extras

RUN apt-get -y install libpq-dev python-dev python-pip postgresql-server-dev-all libxml2-dev libxslt1-dev \
    && apt-get -y build-dep pillow \
    && apt-get -y autoremove

ADD requirements.txt /home/app/


WORKDIR /home/app/

RUN pip install psycopg2
RUN pip install -r requirements.txt

ADD . /home/app/

WORKDIR /home/app/

RUN mkdir -p /home/app/public/
RUN chmod -R 777 /home/app/public/

ENV SECRET "TEMP"

RUN python manage.py collectstatic --noinput

VOLUME /home/app/public





# Enable nginx
RUN rm -f /etc/service/nginx/down
RUN rm /etc/nginx/sites-enabled/default
ADD env.conf /etc/nginx/main.d/env.conf
ADD nginx.conf /etc/nginx/sites-enabled/nginx.conf


# Clean up APT when done.

# RUN python manage.py migrate

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80
