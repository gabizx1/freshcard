#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, matricula, frente,verso,assunto,serie,materia):
    # Primeiro, insira um usuário
    db.cur.execute("""
    INSERT INTO usuario (matricula, serie, nome)
    VALUES (%s, %s, %s)
    RETURNING id_cardu
""", (matricula, serie, nome))
    usuario_id = db.cur.fetchone()[0]
    db.cur.execute("""
    INSERT INTO freshcard (materia, frente, verso, assunto, id_cardu)
    VALUES (%s, %s, %s, %s, %s)
""", (materia, frente, verso, assunto, usuario_id))
    # Em seguida, insira um endereço associado ao usuário
    
   
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT *
FROM usuario

                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def excluir(id):
    db.cur.execute("DELETE FROM freshcard WHERE id_cardu = %s", (id,))

    # Em seguida, excluir o registro da tabela "usuario"
    db.cur.execute("DELETE FROM usuario WHERE id_cardu = %s", (id,))
    db.con.commit()

def editar(id, pergunta, resposta, assunto, materia):
    

    db.cur.execute("UPDATE freshcard SET frente = %s, verso = %s, assunto = %s, materia = %s WHERE id_card = %s",
                (pergunta, resposta, assunto, materia, id))

    db.con.commit()
    