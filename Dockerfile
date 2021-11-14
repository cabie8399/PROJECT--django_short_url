
FROM python:3.7-alpine
RUN mkdir /django


# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8
RUN apk add libxml2-dev libxslt-dev
RUN apk add --no-cache libressl-dev musl-dev libffi-dev python3-dev jpeg-dev zlib-dev

    
ADD requirements.txt /django/requirements.txt
COPY . /django
RUN pip install -r /django/requirements.txt



WORKDIR /django
EXPOSE 8000