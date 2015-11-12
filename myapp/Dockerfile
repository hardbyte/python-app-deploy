FROM python:3.5

# If you have a src folder add that instead
ADD . /var/www

COPY requirements.txt /var/www/requirements.txt

WORKDIR /var/www

RUN pip install -r requirements.txt

EXPOSE 5001

# Useful for debugging
#CMD python3 server.py

# Serve using gunicorn
# Note this should additionally be behind nginx
CMD gunicorn warfarin:app -w 4 -b 0.0.0.0:5001