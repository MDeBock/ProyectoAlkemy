# Proyecto Alkemy Reserva de Servicios

Este repositorio contiene un proyecto de Django que implementa un CRUD (Create, Read, Update, Delete) para la gestión de reservas de servicios. Proporciona una interfaz intuitiva y fácil de usar para que los usuarios puedan realizar y administrar sus reservas de servicios de manera eficiente.

# Características principales

* Crear reserva: Los usuarios pueden crear nuevas reservas proporcionando la información requerida, como nombre, fecha, tipo de servicio, etc.

* Ver reservas: Los usuarios pueden ver una lista de todas las reservas existentes y también pueden ver los detalles de una reserva específica.

* Actualizar reserva: Los usuarios tienen la capacidad de modificar los detalles de una reserva existente, como cambiar la fecha,el tipo de servicio, etc.

* Eliminar reserva: Los usuarios pueden eliminar una reserva existente de la base de datos.

* Gestión de clientes: Los usuarios pueden agregar, editar y eliminar clientes, lo que permite un mejor seguimiento y control de los clientes que utilizan los servicios.

* Gestión de coordinadores: Los usuarios pueden administrar coordinadores y controlar la asignación de servicios.

* Gestión de empleados: Los usuarios pueden gestionar los empleados.

* API de recuperación de registros: El proyecto también incluye una API que permite la recuperación de registros de empleados, servicios, coordinadores y clientes. Esto facilita la integración con otras aplicaciones o servicios externos que necesiten acceder a estos datos.
# Configuración y ejecución

Sigue los siguientes pasos para configurar y ejecutar el proyecto en tu entorno local:
1. Clona este repositorio en tu máquina local.

```bash
git clone https://github.com/MDeBock/ProyectoAlkemy
```
2. Accede al directorio del proyecto.
```bash
cd ProyectoAlkemy
```
3. Crea un entorno virtual para el proyecto
 ```bash
python -m venv env
  ```
4. Activa el entorno virtual
  * En windows
    ```bash
    env\Scripts\activate
    ```
  * En macOS y Linux:
    ```bash
    source env/bin/activate
    ```
5. Instala las dependencias del proyecto.
  ```bash
  pip install -r requirements.txt
  ```
6. Realiza las migraciones de la base de datos.
  ```bash
  python manage.py migrate
  ```
7. Inicia el servidor de desarrollo
  ```bash
  python manage.py runserver
  ```
8. Abre tu navegador y accede a http://localhost:8000/ para comenzar a utilizar la aplicación de reserva de servicios. 
