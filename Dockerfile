FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    apache2 libapache2-mod-wsgi-py3 python3 python3-pip python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install mod_wsgi
RUN a2enmod wsgi

# Copy the application code
COPY . /var/www/app
WORKDIR /var/www/app

# Install Python dependencies
RUN pip3 install .
RUN pip3 install -r requirements.txt

# Copy Apache Config File
COPY flask-app-80.conf /etc/apache2/sites-available
RUN a2ensite flask-app-80.conf
RUN a2dissite 000-default.conf

# Expose Port 80

# Run Apache in the foreground
CMD ["apache2ctl", "-D", "FOREGROUND"]
