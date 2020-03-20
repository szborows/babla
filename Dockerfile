FROM python:3.8-alpine3.11

RUN apk add --no-cache gcc musl-dev libxslt-dev
RUN pip install babla
