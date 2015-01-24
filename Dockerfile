FROM phusion/passenger-customizable:0.9.15

# Set correct environment variables.
ENV HOME /root

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]

#   Build system and git.
RUN /pd_build/utilities.sh
RUN apt-get install -y build-essential python python-dev python-setuptools libpq-dev libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev python-opencv python-numpy
RUN easy_install -U pip

ENV PYTHONUNBUFFERED 1
WORKDIR /home/app/

# Shortcuts
RUN pip install wagtail==0.8.4

ADD requirements.txt /home/app/
RUN pip install -r requirements.txt
ADD . /home/app/

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*