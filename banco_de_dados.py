import psycopg2

# Dados de acesso ao banco
hostname = 'dpg-cs3u05o8fa8c73dhme30-a'
port = 5432
database = 'test_database_62yd'
username = 'root'
password = 'a4D65IiLJicqrNtxFn5SJkMc4TLI6zqj'

# Conexão com o banco de dados PostgreSQL
try:
    conn = psycopg2.connect(
        host=hostname,
        port=port,
        database=database,
        user=username,
        password=password
    )
    cursor = conn.cursor()
    print("Conexão estabelecida com sucesso!")

    # Criação da tabela tb_cliente
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_cliente (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100),
            telefone VARCHAR(15),
            salario FLOAT
        );
    ''')
    print("Tabela 'tb_cliente' criada com sucesso!")

    # Inserir 10 registros na tabela tb_cliente
    clientes = [
        ('João Silva', '555-1234', 2000.00),
        ('Maria Oliveira', '555-2345', 3000.50),
        ('Pedro Souza', '555-3456', 4000.75),
        ('Ana Pereira', '555-4567', 2500.80),
        ('Carlos Alberto', '555-5678', 3200.00),
        ('Paula Lima', '555-6789', 2900.90),
        ('Fernanda Gomes', '555-7890', 4100.10),
        ('Rodrigo Silva', '555-8901', 3800.20),
        ('Lucas Andrade', '555-9012', 2750.30),
        ('Juliana Santos', '555-0123', 3150.40)
    ]

    insert_query = '''
        INSERT INTO tb_cliente (nome, telefone, salario)
        VALUES (%s, %s, %s)
    '''
    
    cursor.executemany(insert_query, clientes)
    conn.commit()
    print("Registros inseridos com sucesso!")

except Exception as e:
    print(f"Erro ao acessar o banco de dados: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexão fechada.")
