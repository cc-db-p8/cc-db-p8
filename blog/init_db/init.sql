PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY ASC,
  username VARCHAR(200) UNIQUE NOT NULL,
  email VARCHAR(300) UNIQUE NOT NULL,
  password VARCHAR(30) NOT NULL,
  nom VARCHAR(60),
  prenom VARCHAR(60),
  date_naiss DATE,
  date_creation REAL DEFAULT (datetime('now', 'localtime')),
  date_connection DATE

);

DROP TABLE IF EXISTS post;
CREATE TABLE IF NOT EXISTS post(
  id INTEGER PRIMARY KEY ASC,
  titre VARCHAR(500),
  text TEXT,
  date_creation REAL DEFAULT (datetime('now', 'localtime')),
  date_publication REAL DEFAULT (datetime('now', 'localtime')),
  date_modification REAL DEFAULT (datetime('now', 'localtime')),
  user_id INTEGER NOT NULL,
  FOREIGN KEY(user_id) REFERENCES user(id)
);

DROP TABLE IF EXISTS commentaire;
CREATE TABLE IF NOT EXISTS commentaire(
  id INTEGER PRIMARY KEY ASC,
  titre VARCHAR(500),
  text TEXT,
  date_creation REAL DEFAULT (datetime('now', 'localtime')),
  date_publication REAL DEFAULT (datetime('now', 'localtime')),
  date_modification REAL DEFAULT (datetime('now', 'localtime')),
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(id),
  FOREIGN KEY (post_id) REFERENCES post(id)
);

DROP TABLE IF EXISTS tag;

CREATE TABLE IF NOT EXISTS tag(
  id INTEGER PRIMARY KEY ASC,
  titre VARCHAR(500)

);

DROP TABLE IF EXISTS post_tag;
CREATE TABLE IF NOT EXISTS post_tag(
  id INTEGER PRIMARY KEY ASC,
  post_id INTEGER NOT NULL,
  tag_id INTEGER NOT NULL,
  FOREIGN KEY (post_id) REFERENCES post(id),
  FOREIGN KEY (tag_id) REFERENCES tag(id),
  UNIQUE (post_id, tag_id)
);