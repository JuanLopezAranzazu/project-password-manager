## Proyecto administrador de contraseñas

### Descripción:

Proyecto para administrar contraseñas con SQLite y Python

### Estructura de archivos

```
app/
│
├── main.py                   # Archivo principal para ejecutar la aplicación
├── db/
│   ├── __init__.py           # Hace que la carpeta sea un módulo de Python
│   └── database.py           # Lógica de conexión y manejo de la base de datos
│
└── utils/
    ├── __init__.py           # Hace que la carpeta sea un módulo de Python
    └── services.py           # Funciones para manejar operaciones relacionadas con contraseñas
```

### Crear entorno virtual

Para crear un entorno virtual se debe ejecutar los siguientes comandos:

```bash
python -m venv venv
.\venv\Scripts\activate
```

### Instalar dependencias

Para instalar las dependencias especificadas en `requirements.txt`, abre una terminal y navega hasta el directorio del proyecto. Luego, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

### Ejecución del programa

Para ejecutar el programa, ejecuta el siguiente comando:

```bash
python main.py
```

### Generar ejecutable

Para generar el ejecutable del programa, ejecuta el siguiente comando:

```bash
pyinstaller --onefile --windowed main.py
```