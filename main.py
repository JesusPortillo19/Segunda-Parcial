import flet as ft
import sqlite3

# Conexión a la base de datos
def crear_conexion():
    conexion = sqlite3.connect('usuarios.db')
    return conexion

# Crear la tabla si no existe
def crear_tabla():
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

def guardar_datos(nombre, edad):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conexion.commit()
    conexion.close()

def main(page: ft.Page):
    page.title = "Gestión de Usuarios"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Crear la tabla si no existe
    crear_tabla()

    # Crear el título con fondo blanco translúcido
    title_text = ft.Container(
        content=ft.Text("Gestión de Usuarios", size=30, color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        opacity=0.7,
        padding=ft.padding.all(10),
        border_radius=ft.border_radius.all(5)
    )

    # Crear los componentes de la interfaz con fondos transparentes
    nombre_input = ft.TextField(
        label="Nombre",
        width=300,
        bgcolor="#FFFFFFA0",
        border_color="#FFFFFFA0"
    )
    edad_input = ft.TextField(
        label="Edad",
        width=300,
        bgcolor="#FFFFFFA0",
        border_color="#FFFFFFA0"
    )

    mensaje_container = ft.Column()

    def guardar_click(e):
        mensaje_container.controls.clear()
        nombre = nombre_input.value
        edad = edad_input.value
        
        if nombre and edad.isdigit():
            edad = int(edad)
            guardar_datos(nombre, edad)
            # Mensaje de resultado con estilo
            mensaje_text = ft.Container(
                content=ft.Text(
                    f"{nombre} es {'mayor' if edad >= 18 else 'menor'} de edad.",
                    size=20,  # Tamaño de texto más grande
                    color=ft.colors.BLACK
                ),
                bgcolor=ft.colors.WHITE,
                opacity=0.7,
                padding=ft.padding.all(10),
                border_radius=ft.border_radius.all(5)
            )
            mensaje_container.controls.append(mensaje_text)
            nombre_input.value = ""
            edad_input.value = ""
        else:
            mensaje_container.controls.append(ft.Text("Por favor, ingrese un nombre válido y una edad.", color=ft.colors.RED))
        
        page.update()
    
    guardar_button = ft.ElevatedButton("Guardar", on_click=guardar_click, bgcolor=ft.colors.BLUE_500, color=ft.colors.WHITE)
    
    def limpiar_click(e):
        nombre_input.value = ""
        edad_input.value = ""
        mensaje_container.controls.clear()
        page.update()

    limpiar_button = ft.ElevatedButton("Limpiar", on_click=limpiar_click, bgcolor=ft.colors.RED_500, color=ft.colors.WHITE)

    # Contenedor principal de contenido
    content_container = ft.Column(
        controls=[
            title_text,
            nombre_input,
            edad_input,
            guardar_button,
            limpiar_button,
            mensaje_container
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Estructura de la página con la imagen de fondo y el contenido centrado más abajo
    page.add(
        ft.Stack(
            [
                ft.Image(
                    src="C:\\Users\\Owner\\OneDrive\\Documents\\SegundaParcial\\fondo.jpg",
                    fit=ft.ImageFit.COVER,
                    opacity=0.8
                ),
                ft.Container(
                    content=content_container,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=100)
                )
            ]
        )
    )

# Inicializar la aplicación
ft.app(target=main)


































