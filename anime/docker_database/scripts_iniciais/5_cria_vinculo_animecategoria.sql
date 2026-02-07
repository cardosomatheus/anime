-- DROP PROCEDURE public.proc_vinc_anime_categoria(int8, int4);

CREATE OR REPLACE PROCEDURE public.proc_vinc_anime_categoria(IN p_id_anime bigint, IN p_id_categoria integer)
 LANGUAGE plpgsql
AS $procedure$   
DECLARE
 IND_ANIME_EXISTE INTEGER;
 IND_CATEGORIA_EXISTE INTEGER;
 IND_CATEGORIA_ANIME INTEGER;
BEGIN
    -- 1º Valida se o anime e categoria existem e se já há esse vinculação.
    SELECT SIGN(COUNT(*)) INTO IND_ANIME_EXISTE  FROM TB_ANIME A WHERE A.ID = P_ID_ANIME;
    SELECT SIGN(COUNT(*)) INTO IND_CATEGORIA_EXISTE  FROM TB_CATEGORIA C WHERE C.ID = P_ID_CATEGORIA;
    SELECT SIGN(COUNT(*)) 
      INTO IND_CATEGORIA_ANIME 
      FROM TB_ANIME_CATEGORIA AS TAC
     WHERE TAC.ID_ANIME = P_ID_ANIME
      AND TAC.ID_CATEGORIA = P_ID_CATEGORIA;



    IF IND_CATEGORIA_EXISTE = 0 THEN
        RAISE EXCEPTION 'Categoria informada não existe.';
    END IF;

    IF IND_ANIME_EXISTE = 0 THEN
        RAISE EXCEPTION 'Anime informado não existe.';
    END IF;
    
    IF IND_CATEGORIA_ANIME > 0 THEN
        RAISE EXCEPTION 'O anime já está vinculado na categoria desejada.';
    END IF;


    -- 2º Insere o vinculo entre ambos.
    INSERT INTO TB_ANIME_CATEGORIA (ID_CATEGORIA, ID_ANIME)
        VALUES(P_ID_CATEGORIA, P_ID_ANIME);

END;
$procedure$
;
