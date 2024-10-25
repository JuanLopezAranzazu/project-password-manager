import sqlite3

class Database:
  def __init__(self, db_name):
    self.db_name = db_name
  
  def connect(self):
    # Conectar a la base de datos
    self.conn = sqlite3.connect(self.db_name)
    self.cursor = self.conn.cursor()
  
  def close(self):
    # Guardar los cambios y cerrar la conexión
    self.conn.close()
  
  def execute_query(self, query, params=None):
    # Ejecutar una consulta SQL
    if params is None:
      params = []
    self.connect()
    self.cursor.execute(query, params)
    self.conn.commit()
    self.close()

  def fetch_query(self, query, params=None):
    # Ejecutar una consulta SQL y devolver los resultados
    if params is None:
      params = []
    self.connect()
    self.cursor.execute(query, params)
    results = self.cursor.fetchall()
    self.close()
    return results
