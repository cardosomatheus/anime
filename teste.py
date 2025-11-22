def teste (id, pconexao: ConexaoDB):
    print('entreeeeeeeeei')
    conecao = pconexao
    with conecao.session() as con:
        result = con.execute(text('SELECT now() as data'))
        for val in result:
            print(val)


teste(1, ConexaoDB())