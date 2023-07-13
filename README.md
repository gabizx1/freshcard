# freshcard
Atividade PABD

colocar seu banco de dados PostgreSQL no services/database.py

    CREATE TABLE usuario (
        id_cardu SERIAL PRIMARY KEY,
        matricula VARCHAR(50),
        serie VARCHAR(50),
        nome VARCHAR(50)
    )

    CREATE TABLE freshcard (
        id_card SERIAL PRIMARY KEY,
        materia VARCHAR(50),
        frente VARCHAR(50),
        verso VARCHAR(50),
        assunto VARCHAR(50),
        id_cardu INTEGER REFERENCES usuario (id_cardu)
    )
