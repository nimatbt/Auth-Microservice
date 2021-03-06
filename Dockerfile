FROM python:slim

ENV AMIMA_AUTHZ_DATABASE_URI=NULL AMIMA_AUTHZ_SECRET_KEY=SECRET-KEY AMIMA_AUTHZ_TIMEZONE=Asia/Tehran

EXPOSE 8080

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ARG GIT_COMMIT="nocommit"
ARG GIT_TAG="notag"
LABEL gitCommit=$GIT_COMMIT gitTag=$GIT_TAG

ENTRYPOINT ./start

