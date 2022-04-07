FROM postgres:alpine

ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=user
ENV POSTGRES_DB=test-db

COPY init-table.sql /docker-entrypoint-initdb.d/

