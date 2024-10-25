import tkinter as tk
from tkinter import ttk, messagebox
from db.database import Database
from utils.services import (
  create_table,
  get_all_passwords,
  insert_password,
  update_password,
  delete_password
)
import sqlite3

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Proyecto Administrador de Contraseñas")
    self.root.geometry("800x500")

    # Crear la instancia de la clase Database
    self.db = Database("database.db")
    create_table(self.db)

    self.selected_id = None

    self.create_widgets()

  def create_widgets(self):
    # Marco para el formulario
    frame_form = ttk.Frame(self.root)
    frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Etiqueta para el nombre del sitio
    label_site = ttk.Label(frame_form, text="Sitio:")
    label_site.grid(row=0, column=0, pady=5, sticky="ew")

    # Campo de texto para el nombre del sitio
    self.site = ttk.Entry(frame_form)
    self.site.grid(row=1, column=0, pady=5, sticky="ew")

    # Etiqueta para el nombre de usuario
    label_username = ttk.Label(frame_form, text="Usuario:")
    label_username.grid(row=2, column=0, pady=5, sticky="ew")

    # Campo de texto para el nombre de usuario
    self.username = ttk.Entry(frame_form)
    self.username.grid(row=3, column=0, pady=5, sticky="ew")

    # Etiqueta para la contraseña
    label_password = ttk.Label(frame_form, text="Contraseña:")
    label_password.grid(row=4, column=0, pady=5, sticky="ew")

    # Campo de texto para la contraseña
    self.password = ttk.Entry(frame_form)
    self.password.grid(row=5, column=0, pady=5, sticky="ew")

    # Botón para seleccionar la contraseña
    button_select = ttk.Button(frame_form, text="Seleccionar", command=self.on_select_password)
    button_select.grid(row=6, column=0, pady=5, sticky="ew")

    # Botón para guardar la contraseña
    button_save = ttk.Button(frame_form, text="Guardar", command=self.on_insert_password)
    button_save.grid(row=7, column=0, pady=5, sticky="ew")

    # Botón para actualizar la contraseña
    button_update = ttk.Button(frame_form, text="Actualizar", command=self.on_update_password)
    button_update.grid(row=8, column=0, pady=5, sticky="ew")

    # Botón para eliminar la contraseña
    button_delete = ttk.Button(frame_form, text="Eliminar", command=self.on_delete_password)
    button_delete.grid(row=9, column=0, pady=5, sticky="ew")

    # Marco para la tabla
    frame_table = ttk.Frame(self.root)
    frame_table.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Crear la tabla
    columns = ("#1", "#2", "#3", "#4")
    self.table = ttk.Treeview(frame_table, columns=columns, show="headings")
    self.table.heading("#1", text="ID")
    self.table.heading("#2", text="Sitio")
    self.table.heading("#3", text="Usuario")
    self.table.heading("#4", text="Contraseña")
    self.table.grid(row=0, column=0, sticky="nsew")

    # Ajustar el ancho de las columnas para que no ocupen tanto espacio
    self.table.column("#1", width=50, anchor="center")  # ID - 50px de ancho
    self.table.column("#2", width=150, anchor="center")  # Sitio - 150px de ancho
    self.table.column("#3", width=150, anchor="center")  # Usuario - 150px de ancho
    self.table.column("#4", width=200, anchor="center")  # Contraseña - 200px de ancho

    self.table.grid(row=0, column=0, sticky="nsew")

    # Agregar Scrollbars
    scrollbar_x = ttk.Scrollbar(frame_table, orient="horizontal", command=self.table.xview)
    scrollbar_x.grid(row=1, column=0, sticky="ew")
    self.table.configure(xscrollcommand=scrollbar_x.set)

    scrollbar_y = ttk.Scrollbar(frame_table, orient="vertical", command=self.table.yview)
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    self.table.configure(yscrollcommand=scrollbar_y.set)

    # Configurar el frame_form para expandirse en ambas direcciones
    frame_form.grid_columnconfigure(0, weight=1)  # Permitir crecimiento horizontal

    # Configurar el frame_table para expandirse en ambas direcciones
    frame_table.grid_rowconfigure(0, weight=1)  # Permitir crecimiento vertical
    frame_table.grid_columnconfigure(0, weight=1)  # Permitir crecimiento horizontal

    # Ajustar el peso de las columnas
    self.root.grid_columnconfigure(0, weight=1)  # Columna del formulario
    self.root.grid_columnconfigure(1, weight=2)  # Columna de resultados

    # Ajustar el peso de las filas
    self.root.grid_rowconfigure(0, weight=1)  # Fila principal

    # Llenar la tabla con los datos de la base de datos
    self.fill_table()

  def clear_form(self):
    self.site.delete(0, tk.END)
    self.username.delete(0, tk.END)
    self.password.delete(0, tk.END)

  def fill_table(self):
    try:
      # Limpiar la tabla
      records = self.table.get_children()
      for record in records:
        self.table.delete(record)

      # Obtener los datos de la base de datos
      passwords = get_all_passwords(self.db)

      # Llenar la tabla con los datos
      for password in passwords:
        self.table.insert("", "end", values=(password[0], password[1], password[2], password[3]))
    except sqlite3.Error as e:
      messagebox.showerror("Error", f"Error al obtener las contraseñas: {e}")

  def on_insert_password(self):
    site = self.site.get()
    username = self.username.get()
    password = self.password.get()

    # Validar los campos
    if not site or not username or not password:
      messagebox.showwarning("Advertencia", "Todos los campos son requeridos")
      return

    try:
      # Insertar la contraseña en la base de datos
      insert_password(self.db, site, username, password)
      self.clear_form()
      self.fill_table()
    except sqlite3.Error as e:
      messagebox.showerror("Error", f"Eror al guardar la contraseña: {e}")

  def on_select_password(self):
    # Obtener el índice seleccionado
    selected = self.table.selection()

    if not selected:
      messagebox.showwarning("Advertencia", "Seleccione una contraseña")
      return
    
    # Obtener los valores de la fila seleccionada
    values = self.table.item(selected, "values")
    self.selected_id = values[0]
    site = values[1]
    username = values[2]
    password = values[3]

    # Llenar los campos del formulario
    self.site.delete(0, tk.END)
    self.site.insert(0, site)
    self.username.delete(0, tk.END)
    self.username.insert(0, username)
    self.password.delete(0, tk.END)
    self.password.insert(0, password)

  def on_update_password(self):
    site = self.site.get()
    username = self.username.get()
    password = self.password.get()

    # Validar si se ha seleccionado una contraseña
    if not self.selected_id:
      messagebox.showwarning("Advertencia", "Seleccione una contraseña")
      return

    # Validar los campos
    if not site or not username or not password:
      messagebox.showwarning("Advertencia", "Todos los campos son requeridos")
      return

    try:
      # Actualizar la contraseña en la base de datos
      update_password(self.db, self.selected_id, site, username, password)
      self.clear_form()
      self.selected_id = None
      self.fill_table()
    except sqlite3.Error as e:
      messagebox.showerror("Error", f"Error al actualizar la contraseña: {e}")

  def on_delete_password(self):
    # Validar si se ha seleccionado una contraseña
    if not self.selected_id:
      messagebox.showwarning("Advertencia", "Seleccione una contraseña")
      return
    
    try:
      # Eliminar la contraseña de la base de datos
      delete_password(self.db, self.selected_id)
      self.clear_form()
      self.selected_id = None
      self.fill_table()
    except sqlite3.Error as e:
      messagebox.showerror("Error", f"Error al eliminar la contraseña: {e}")

if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()
