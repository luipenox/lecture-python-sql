DROP TABLE IF EXISTS categories;
CREATE TABLE IF NOT EXISTS categories (
    id integer PRIMARY KEY,
    name text NOT NULL
);

DROP TABLE IF EXISTS items;
CREATE TABLE IF NOT EXISTS items (
    id integer PRIMARY KEY,
    name text NOT NULL,
    category_id integer NOT NULL,
    valid integer DEFAULT 1,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);