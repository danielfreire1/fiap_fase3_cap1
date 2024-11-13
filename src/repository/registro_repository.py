from repository.oracle import get_connection

def criar(registro):
    query = """
    INSERT INTO registry (k, p, ldr, humidity, temperature, relay, data)
    VALUES (:k, :p, :ldr, :humidity, :temperature, :relay, SYSDATE)
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, registro)
            connection.commit()
    except Exception as e: 
        print(e)

def listar():
    query = """
    SELECT id, k, p, ldr, humidity, temperature, relay, data
    FROM registry
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        print(e)





