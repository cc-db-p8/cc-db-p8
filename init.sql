CREATE TABLE IF NOT EXISTS personne (
  id INTEGER PRIMARY KEY ASC,
  nom TEXT,
  prenom TEXT,
  date_naissance TEXT
);

CREATE TABLE IF NOT EXISTS adresse (
  id INTEGER PRIMARY KEY ASC,
  personne_id INTEGER,
  label TEXT,
  ville TEXT,
  code_postal INT
);


INSERT INTO personne (id, nom, prenom, date_naissance) VALUES (NULL , 'Guichon', 'Paul', NULL );
INSERT INTO adresse (id, personne_id, label, ville, code_postal) VALUES
  (NULL, 1, '2 rue de la liberté', 'st denie', '93500');

INSERT INTO adresse (id, personne_id, label, ville, code_postal) VALUES
  (NULL, 1, '5 rue de la contrainte', 'Paris', '75016');

SELECT * FROM adresse;