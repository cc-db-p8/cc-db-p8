PRAGMA foreign_keys = ON;

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
  cod_pos TEXT,
  cod_com TEXT,
  FOREIGN KEY (personne_id) REFERENCES personne(id),
  FOREIGN KEY (type_id) REFERENCES type_adresse(id),
  FOREIGN KEY (cod_pos, cod_com) REFERENCES commune(cod_pos, cod_com)
);

CREATE TABLE type_adresse(
  id INTEGER PRIMARY KEY ASC,
  label TEXT
);

CREATE TABLE IF NOT EXISTS commune(
  cod_com TEXT,
  cod_pos TEXT,
  label TEXT,
  PRIMARY KEY(cod_com, cod_pos)
);


