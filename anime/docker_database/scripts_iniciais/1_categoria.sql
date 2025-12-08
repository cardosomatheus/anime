
CREATE SEQUENCE IF NOT EXISTS SQ_CATEGORIA START WITH 1 INCREMENT BY 1;

CREATE TABLE IF NOT EXISTS TB_CATEGORIA(
    ID BIGINT NOT NULL DEFAULT NEXTVAL('SQ_CATEGORIA'),
    NOME VARCHAR(50) NOT NULL,
    DESCRICAO VARCHAR(200),
    CONSTRAINT PK_CATEGORIA PRIMARY KEY(ID)
);

CREATE UNIQUE INDEX IF NOT EXISTS UNQ_CATEGORIA_NOME ON TB_CATEGORIA(NOME);

INSERT INTO PUBLIC.TB_CATEGORIA (NOME, DESCRICAO)
VALUES ('FANTASIA', 'Histórias com elementos mágicos e sobrenaturais.'),
('FICÇÃO CIENTÍFICA', 'Narrativas envolvendo tecnologia avançada ou futuro distante.'),
('AVENTURA', 'Tramas focadas em exploração, jornadas e descobertas.'),
('TERROR', 'Histórias criadas para assustar e gerar tensão psicológica.'),
('DRAMA', 'Foco em emoções intensas, conflitos pessoais e evolução dos personagens.'),
('COMÉDIA', 'Obras que têm como objetivo provocar humor e leveza.'),
('AÇÃO', 'Tramas marcadas por lutas, perseguições e cenas rápidas.'),
('MISTÉRIO', 'Histórias envolvendo enigmas, investigações e revelações.'),
('SOBRENATURAL', 'Temas com espíritos, demônios, poderes ocultos e fenômenos inexplicáveis.'),
('ROMANCE', 'Histórias centradas em relacionamentos amorosos e desenvolvimento emocional.')
ON CONFLICT (NOME) DO NOTHING;
