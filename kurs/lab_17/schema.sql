CREATE TABLE IF NOT EXISTS users (
    id_user INTEGER NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(30) NOT NULL UNIQUE CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    password_hash VARCHAR(72),
    registration_date TIMESTAMP,
    last_login TIMESTAMP,
    path_to_photo VARCHAR(80)
    );

CREATE TABLE IF NOT EXISTS typePermission (
    id_type_permission INTEGER NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    description VARCHAR(30) UNIQUE CHECK (description IN ('basic', 'writer', 'admin'))
    );

INSERT INTO typePermission
       (description)
VALUES ('basic' ),
       ('writer'),
       ('admin') ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS userPermission (
    id_user_permission INTEGER NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    user_id INTEGER REFERENCES users (id_user),
    type_permission_id INTEGER REFERENCES typePermission (id_type_permission),
        CONSTRAINT unq
            UNIQUE (user_id, type_permission_id)
    );

CREATE TABLE IF NOT EXISTS categories (
    id_category INTEGER NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    description VARCHAR(40) NOT NULL UNIQUE
    );

INSERT INTO categories
       (description)
VALUES ('Topic 1'),
       ('Topic 2'),
       ('Topic 3'),
       ('Topic 4'),
       ('Topic 5') ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS posts (
    id_post INTEGER NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    user_id INTEGER REFERENCES users (id_user),
    category_id INTEGER REFERENCES categories (id_category),
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    creation_date TIMESTAMP,
    validity_date TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS userComments (
    id_comment INTEGER NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    user_id INTEGER REFERENCES users (id_user),
    post_id INTEGER REFERENCES posts (id_post),
    body TEXT NOT NULL,
    creation_date TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS photos (
    id_photo INTEGER NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    post_id INTEGER REFERENCES posts (id_post),
    path_to_photo VARCHAR(80) NOT NULL
    );

CREATE INDEX IF NOT EXISTS index_post_category_with_creation_date ON posts (category_id, creation_date);

CREATE OR REPLACE VIEW main_information_by_users AS SELECT
    users.id_user,
    users.first_name,
    users.last_name,
    users.password_hash,
    COUNT(DISTINCT posts.id_post) n_posts,
    COUNT(DISTINCT userComments.id_comment) n_comments
    FROM users LEFT JOIN posts
    ON posts.user_id = users.id_user
    LEFT JOIN userComments
    ON userComments.user_id = users.id_user
    GROUP BY users.id_user;

CREATE EXTENSION IF NOT EXISTS pgcrypto;