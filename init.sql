CREATE TABLE IF NOT EXISTS personne (
  id INTEGER PRIMARY KEY ASC,
  nom TEXT,
  prenom TEXT,
  sexe TEXT,
  email TEXT UNIQUE,
  date_naissance TEXT
);

CREATE TABLE IF NOT EXISTS adresse (
  id INTEGER PRIMARY KEY ASC,
  type_id INTEGER,
  personne_id INTEGER,
  label TEXT,
  ville TEXT,
  cod_pos TEXT,
  cod_com TEXT
);

CREATE TABLE type_adresse(
  id INTEGER PRIMARY KEY ASC,
  label TEXT
);

CREATE TABLE IF NOT EXISTS cod_com(
  cod_com TEXT,
  cod_pos TEXT,
  label TEXT,
  PRIMARY KEY(cod_com, cod_pos)
);


