USE hp_mysql;

CREATE TABLE performance_campanhas (
  canal TEXT,
  campanha TEXT,
  grupo_anuncio TEXT,
  data TEXT,
  impressoes INTEGER,
  cliques INTEGER,
  leads INTEGER,
  valor_gasto DECIMAL(16,4)
);