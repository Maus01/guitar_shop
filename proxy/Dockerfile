FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./proxy/default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./proxy/uwsgi_params /etc/nginx/uwsgi_params
COPY ./proxy/run_proxy.sh /run_proxy.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN mkdir -p /vol/static

RUN chmod -R 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run_proxy.sh

VOLUME /vol/static

USER nginx

CMD [ "/run_proxy.sh" ]
