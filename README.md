# Gestión de Proyectos - IW G6

Aplicación web desarrollada como parte de la asignatura Ingeniería Web, enfocada en la gestión de proyectos y tareas en el entorno industrial. Forma parte del reto 3 propuesto en el proyecto web colaborativo. Permite registrar y administrar proyectos, tareas, empleados y clientes; además de algunas funcionalidades extra añadidas en la última entrega y que se citaran en 'Funcionalidades'.

## Requisitos de instalación

1. Clona el repositorio:
   git clone https://github.com/juancebellan/E2_IW_G6.git

2. Instala dependencias:
   pip install -r requirements.txt

3. Ejecuta el servidor de desarrollo:
   python manage.py runserver

> Nota: No se incluye el entorno virtual según las normas de entrega.

## Autores

- [Juan Cebellán](https://www.github.com/juancebellan)
- [Unai Pinilla](https://www.github.com/unaipini)
- [Xabier Lopez](https://www.github.com/Xabierlb)

## Funcionalidades

- Gestión de proyectos con cliente, fechas y presupuesto
- Gestión de tareas vinculadas a proyectos
- Gestión de empleados y asignación de tareas
- Gestión de clientes con datos de contacto
- Asignación de múltiples responsables a un mismo proyecto (relación many-to-many)
- Notas editables en tareas
- Interfaz responsive y validaciones en formularios
- Envio de email de bienvenida a nuevos empleados
- Registro de usuarios para entrar en la página
- Funcion para marcar proyectos como favoritos y filtrarlos
- Ampliación de información de clientes, empleados y proyectos desde la lista, sin entrar a detalle

## Uso

Desde el navegador, navega por el menú principal para acceder a la gestión de clientes, proyectos, tareas y empleados. Cada módulo permite operaciones CRUD y navegación intuitiva entre relaciones.
