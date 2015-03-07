FROM nginx

RUN apt-get update && apt-get install -y curl

RUN curl -o /etc/nginx/conf.d/default.conf https://raw.githubusercontent.com/AndreaGini/3sca/master/default.conf
RUN curl -o /etc/nginx/nginx.conf https://raw.githubusercontent.com/AndreaGini/3sca/master/nginx.conf 
RUN curl -o /etc/nginx/htpasswd https://raw.githubusercontent.com/AndreaGini/3sca/master/htpasswd

RUN service nginx restart

EXPOSE 80
