FROM phusion/passenger-customizable:0.9.15
MAINTAINER 100 Shapes <paolo@100shapes.com>
# Set correct environment variables.

# ENV HOME /app

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]

#   Build system and git.
RUN /pd_build/utilities.sh
RUN /pd_build/python.sh
RUN /pd_build/nodejs.sh

WORKDIR /tmp

RUN git clone https://github.com/100Shapes/100Shapes.com-content-API.git app

RUN mkdir -p /home/app

RUN cp app/package.json /home/app/

WORKDIR /home/app/

RUN npm install -g npm

RUN npm install

RUN cp -r /tmp/app/* /home/app/

RUN chown -R app /home/app/

ENV VIRTUAL_HOST proto.api.100shapes.com

# Enable nginx
RUN rm -f /etc/service/nginx/down
RUN rm /etc/nginx/sites-enabled/default
ADD nginx.conf /etc/nginx/sites-enabled/nginx.conf
ADD env.conf /etc/nginx/main.d/node-env.conf

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80
