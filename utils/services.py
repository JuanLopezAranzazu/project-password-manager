# Crear la tabla passwords en la base de datos
def create_table(db):
  query = """
  CREATE TABLE IF NOT EXISTS passwords (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      website TEXT NOT NULL,
      username TEXT NOT NULL,
      password TEXT NOT NULL
  )
  """
  db.execute_query(query)

# Obtener todas las contraseñas de la base de datos
def get_all_passwords(db):
  query = "SELECT * FROM passwords"
  return db.fetch_query(query)

# Obtener una contraseña de la base de datos
def get_password(db, id):
  query = "SELECT * FROM passwords WHERE id = ?"
  return db.fetch_query(query, (id,))

# Insertar una nueva contraseña en la base de datos
def insert_password(db, website, username, password):
  query = "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)"
  db.execute_query(query, (website, username, password))

# Actualizar una contraseña en la base de datos
def update_password(db, id, website, username, password):
  query = "UPDATE passwords SET website = ?, username = ?, password = ? WHERE id = ?"
  db.execute_query(query, (website, username, password, id))

# Eliminar una contraseña de la base de datos
def delete_password(db, id):
  query = "DELETE FROM passwords WHERE id = ?"
  db.execute_query(query, (id,))
