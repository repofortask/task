FROM postgres:alpine
WORKDIR /app
COPY . /app/
ADD links.csv /app/
ADD movies.csv /app/
ADD ratings.csv /app/
ADD tags.csv /app/
COPY *.sql /docker-entrypoint-initdb.d/
ADD setup.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*
