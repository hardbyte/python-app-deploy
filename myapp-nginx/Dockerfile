FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

# Copy any static site assets:
COPY static /usr/share/nginx/html
RUN ls /usr/share/nginx/html

# Copy the nginx configuration
COPY nginx /etc/nginx/conf.d

EXPOSE 80