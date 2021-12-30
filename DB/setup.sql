CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title TEXT,
    genres TEXT
);

COPY movies(movie_id, title, genres)
FROM '/app/movies.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE ratings (
    user_id INT,
    movie_id INT,
    rating REAL,
    timestamp INT,
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

COPY ratings(user_id, movie_id, rating, timestamp)
FROM '/app/ratings.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE links (
  movie_id INT,
  imdb_id INT,
  tmdb_id INT,
  FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

COPY links(movie_id, imdb_id, tmdb_id)
FROM '/app/links.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE tags (
    user_id INT,
    movie_id INT,
    tag TEXT,
    timestamp INT,
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

COPY tags(user_id, movie_id, tag, timestamp)
FROM '/app/tags.csv'
DELIMITER ','
CSV HEADER;
