
CREATE SEQUENCE IF NOT EXISTS SQ_ANIME START WITH 1 INCREMENT BY 1;


CREATE TABLE IF NOT EXISTS TB_ANIME(
    ID BIGINT NOT NULL DEFAULT NEXTVAL('SQ_ANIME'),
    NOME VARCHAR(50) NOT NULL,
    DATA_LANCAMENTO DATE,
    DESCRICAO VARCHAR(2000),
    CONSTRAINT PK_ANIME PRIMARY KEY(ID)
);


CREATE UNIQUE INDEX IF NOT EXISTS UNQ_ANIME_NOME ON TB_ANIME(NOME);

INSERT INTO PUBLIC.TB_ANIME (NOME, DATA_LANCAMENTO, DESCRICAO)
VALUES 
('Fullmetal Alchemist: Brotherhood', TO_DATE('05/04/2009', 'DD/MM/YYYY'), 'Dois irmãos alquimistas buscam restaurar seus corpos após uma tentativa de transmutação proibida.'),
('Steins;Gate', TO_DATE('06/04/2011', 'DD/MM/YYYY'), 'Um grupo de amigos descobre um modo de enviar mensagens para o passado e acaba alterando linhas temporais.'),
('Made in Abyss', TO_DATE('07/07/2017', 'DD/MM/YYYY'), 'Uma garota e um robô exploram um abismo misterioso cheio de criaturas perigosas e segredos antigos.'),
('Mob Psycho 100', TO_DATE('11/07/2016', 'DD/MM/YYYY'), 'Um garoto com poderes psíquicos tenta levar uma vida normal enquanto controla suas emoções.'),
('Attack on Titan', TO_DATE('07/04/2013', 'DD/MM/YYYY'), 'A humanidade luta pela sobrevivência em um mundo cercado por gigantes que devoram humanos.')
ON CONFLICT (NOME) DO NOTHING;