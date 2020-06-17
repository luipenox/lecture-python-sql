DROP TABLE IF EXISTS categories;
CREATE TABLE IF NOT EXISTS categories (
    id integer PRIMARY KEY,
    name text NOT NULL
);

DROP TABLE IF EXISTS departments;
CREATE TABLE IF NOT EXISTS departments (
    id integer PRIMARY KEY,
    name text NOT NULL
);

DROP TABLE IF EXISTS positions;
CREATE TABLE IF NOT EXISTS positions (
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

DROP TABLE IF EXISTS persons;
CREATE TABLE IF NOT EXISTS persons (
    id integer PRIMARY KEY,
    name text NOT NULL,
    surname text NOT NULL,
    title_before text NULL,
    title_after text NULL,
    department_id integer NOT NULL,
    position_id integer NOT NULL,
    active integer DEFAULT 1,
    FOREIGN KEY (department_id) REFERENCES departments (id),
    FOREIGN KEY (position_id) REFERENCES positions (id)
);
