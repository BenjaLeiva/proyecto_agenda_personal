Agenda Personal (proyecto backend)

Requisitos Previos
- Antes de comenzar, asegúrate de tener instalado:Python (personalmente use la version 3.13.7)
- pip (Administrador de paquetes de Python)
- Base de Datos MySQL/MariaDB (o SQLite para desarrollo rápido)
- phpMyAdmin (si utilizas MySQL para una gestión visual de la DB)
para la base de datos recomiendo usar appserv para instalar los 2 ultimos servicios mencionados previamente

1. Configuración e Instalación Inicial
1.1 Clonar el Repositorio e Instalar Dependencias
Navega a la carpeta principal del proyecto "cd proyecto_agenda_personal-main/agenda_personal"

# Instala todas las dependencias de Python
pip install django
pip install mssql-django
1.2 Configurar la Base de DatosAbre el archivo settings.py de tu proyecto y asegúrate de que la configuración de DATABASES apunte correctamente a tu base de datos (MySQL o MariaDB)
1.3 Ejecutar MigracionesUna vez configurada la conexión a la DB, aplica los cambios del modelo a la base de datos:# Crea los archivos de migración (si hay cambios pendientes)
python manage.py makemigrations 

# Aplica todas las migraciones (incluyendo tablas de Django Auth y tu tabla Task)
python manage.py migrate

2. Configuración de Usuarios
2.1 Crear el Superusuario (Administrador)Necesitas un superusuario para acceder al panel de administración de Django:python manage.py createsuperuser
Sigue las instrucciones en pantalla para ingresar un nombre de usuario, email (opcional) y contraseña (si la contraseña es muy debil pedira confirmar pulsando "y" o "N" de si esta seguro
de que quiere que esa sea su contraseña, "y" para si y "N" para no
2.2 Poblar la Base de Datos (Opcional)Si deseas tener datos de ejemplo en la tabla agenda_task, utiliza los comandos SQL proporcionados anteriormente, asegurándote de usar 
user_id = 1 (o el ID de tu superusuario) y la función de fecha correcta (NOW() para MySQL)

3. Ejecución del Servidor
Inicia el servidor de desarrollo local de Django:python manage.py runserver
La aplicación estará disponible en tu navegador en http://127.0.0.1:8000/

4. Manual de Uso de la Aplicación
4.1. Acceso y RegistroURL Principal: Al abrir la aplicación, serás redirigido automáticamente a la página de Inicio de Sesión (/accounts/login/)
Registro: Si no tienes cuenta, haz clic en el enlace "Regístrate aquí" para crear un nuevo usuario
Inicio de Sesión: Ingresa tu usuario y contraseña. Serás llevado a la Agenda Personal (/agenda/)
4.2. Gestión de Tareas
La interfaz principal muestra todas tus tareas pendientes y un formulario en la parte superior
Instrucciones
Crear Tarea: Utiliza el formulario superior. Rellena el título y opcionalmente la descripción y fecha límite. Clic en "Agregar Tarea"
Marcar Completada: Haz clic en el checkbox o botón de "Completar" junto a la tarea. La tarea se moverá al final de la lista
Editar Tarea: Haz clic en el ícono de lápiz (Editar) para abrir el formulario de edición, modificar los campos y hacer clic en "Guardar Cambios"
Eliminar Tarea: Haz clic en el ícono de papelera (Eliminar) para borrar la tarea de forma permanente
4.3. Cerrar Sesión
Haz clic en el botón de "Cerrar Sesión" disponible en la interfaz para finalizar tu sesión de forma segura. Serás redirigido con un boton para iniciar sesion nuevamente con un mensaje de
cerraste sesion
