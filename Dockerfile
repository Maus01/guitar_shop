FROM python:3.9.18-alpine3.18
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
COPY ./shop /shop
COPY ./scripts /scripts

WORKDIR /shop
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add build-base && \
    apk add linux-headers && \
    apk add python3-dev && \
    /py/bin/pip install -r /requirements.txt


RUN adduser --disabled-password --no-create-home shop && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media

COPY ./shop/static /vol/web/static    

RUN chown -R shop:shop /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER shop



CMD [ "run.sh" ]






