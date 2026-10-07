::page{title="Crear Servicio para Obtener Imágenes con Flask"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/IDSN-logo.png" width="200/">

##

**Tiempo estimado necesario**: 90 minutos

##

Bienvenido al laboratorio práctico **Crear Servicio para Obtener Imágenes con Flask**. En este laboratorio, comenzarás a construir el servicio que eventualmente desplegarás en IBM Code Engine. El laboratorio proporciona un repositorio de plantilla en GitHub para ayudarte a comenzar. El repositorio también contiene pruebas unitarias en Python. Se te pedirá que completes el código para que pueda pasar todas las pruebas.

## Objetivos
En este laboratorio, tú:

- Crearás un servidor Flask
- Escribirás APIs RESTful sobre el recurso de URL de imágenes
- Verificarás que las APIs deben pasar las pruebas dadas de **pytest**

::page{title="Nota: Información de Seguridad Importante"}

Bienvenido al Cloud IDE. Aquí es donde se llevará a cabo todo tu desarrollo. Tiene todas las herramientas que necesitarás, incluyendo **Python** y **Flask**.

Es importante entender que el entorno del laboratorio es efímero. Solo vive por un corto tiempo antes de ser destruido. Es imperativo que empujes todos los cambios realizados a tu propio repositorio de GitHub para que pueda ser recreado en un nuevo entorno de laboratorio cada vez que sea necesario.

Además, ten en cuenta que este entorno es compartido y, por lo tanto, no es seguro. No debes almacenar ninguna información personal, nombres de usuario, contraseñas o tokens de acceso en este entorno para ningún propósito.

## Tu Tarea
Si no has generado un Token de Acceso Personal de GitHub, deberías hacerlo ahora. Lo necesitarás para empujar código de vuelta a tu repositorio. Debe tener permisos de `repo` y `write`, y estar configurado para expirar en `60` días. Cuando Git te pida una contraseña en el entorno de Cloud IDE, utiliza tu Token de Acceso Personal en su lugar. Sigue los pasos en el [Laboratorio de Generación de Token de Git](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/labs/deployment/git_token.md.html "Laboratorio de Generación de Token de Git") para obtener instrucciones detalladas.

## Nota sobre Capturas de Pantalla
A lo largo de este laboratorio, se te pedirá que tomes capturas de pantalla y las guardes en tu dispositivo. Estas capturas de pantalla son necesarias para la evaluación calificada por IA y la revisión calificada por pares al final del curso.

Tus capturas de pantalla deben tener una extensión .jpg o .png.

Para tomar capturas de pantalla, puedes usar varias herramientas gratuitas de captura de pantalla o las teclas de acceso directo de tu sistema operativo. Por ejemplo:

- Mac: Puedes usar `Shift + Command + 3 (⇧ + ⌘ + 3)` en tu teclado para capturar toda tu pantalla o `Shift + Command + 4 (⇧ + ⌘ + 4)` para capturar una ventana o área. Las capturas de pantalla se guardarán como archivos .jpg o .png en tu Escritorio.

- Windows: Puedes capturar tu ventana activa presionando `Alt + Print Screen` en tu teclado. Este comando copia una imagen de tu ventana activa al portapapeles. Luego, abre un editor de imágenes, pega la imagen de tu portapapeles en el editor de imágenes y guarda la imagen como un archivo .jpg o .png.

::page{title="Inicializar el Entorno de Desarrollo"}

Debido a que el entorno de Cloud IDE es efímero, puede ser eliminado en cualquier momento. La próxima vez que ingreses al laboratorio, se puede crear un nuevo entorno. Desafortunadamente, esto significa que necesitarás inicializar tu entorno de desarrollo cada vez que se recree. Esto no debería ocurrir con frecuencia, ya que el entorno puede durar varios días, pero cuando se elimine, el procedimiento para recrearlo es el siguiente.

## Descripción General

### Crear un nuevo repositorio a partir de una plantilla
1. Haz clic en esta URL para abrir el proyecto de código inicial: https://github.com/ibm-developer-skills-network/luggb-Back-End-Development-Pictures
2. Usa el botón verde **Usar esta plantilla** para clonar este repositorio a tu cuenta privada de GitHub.

   **No uses Fork; usa el botón de Plantilla.**

   ![El botón de usar esta plantilla está resaltado como recordatorio](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/ce-deploy-fork-template.png "Usar plantilla")
3. Dale a tu repositorio el nombre `Back-End-Development-Pictures`. Este es el nombre que los evaluadores buscarán para calificar tu trabajo.
4. Asegúrate de seleccionar la opción Pública para tu repositorio y luego créalo.

### Inicializar el Entorno de Desarrollo

Cada vez que necesites configurar tu entorno de desarrollo en el laboratorio, deberás ejecutar tres comandos.

Cada comando se explicará con más detalle, uno a la vez, en la siguiente sección.

`{your_github_account}` representa el nombre de usuario de tu cuenta de GitHub.

Los comandos incluyen:
- clonar el repositorio de GitHub desde tu cuenta
- cambiar al directorio `Back-End-Development-Pictures`
- ejecutar el script de configuración bash
- salir de la terminal

Ahora, discutamos cada uno de estos comandos y expliquemos qué se necesita hacer.

## Detalles de la Tarea
Inicializa tu entorno utilizando los siguientes pasos:

1. Abre una terminal con `Terminal` -> `Nueva Terminal` si no hay una abierta ya.

2. A continuación, utiliza el comando export GITHUB_ACCOUNT para exportar una variable de entorno que contenga el nombre de tu cuenta de GitHub.

   > **Nota:** Sustituye tu verdadera cuenta de GitHub por el marcador de posición {your_github_account} a continuación:

```bash
export GITHUB_ACCOUNT={your_github_account}
```


3. Luego utiliza los siguientes comandos para clonar tu repositorio.

```bash
git clone https://github.com/$GITHUB_ACCOUNT/Back-End-Development-Pictures.git
```


4. Cambia al directorio devops-capstone-project y ejecuta el `./bin/setup.sh` comando.

```bash
cd /home/project/Back-End-Development-Pictures
bash ./bin/setup.sh
```


5. Deberías ver lo siguiente al final de la ejecución de la configuración:

	![setup script done](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/get_pics_setup_done.png "setup script done")

6. Finalmente, usa el comando `exit` para cerrar la terminal actual. El entorno no estará completamente activo hasta que abras una nueva terminal en el siguiente paso.

```bash
exit
```


## Validar
Para validar que tu entorno está funcionando correctamente, debes abrir una nueva terminal porque el entorno virtual de Python solo se activará cuando se cree una nueva terminal. Asegúrate de haber utilizado el comando `exit` para salir de la terminal en tu tarea anterior.

1. Abre una terminal usando el comando `Terminal` -> `New Terminal`. Deberías ver el entorno virtual de Python `(backend-pics-venv)` precedido en el aviso de la terminal. Verifica que todo esté funcionando correctamente utilizando el comando `which python`:

	Verifica qué Python estás usando:

	```bash
	which python
	````

	Deberías obtener:

	![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/image39.png)

	Verifica la versión de Python:

	```bash
	python --version
	```

	Deberías obtener algún nivel de parche de Python 3.9.18:

	![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/image%20\(38\).png)
	

## Actualizar README.md del Proyecto
Después de configurar el entorno, actualiza el archivo README.md en tu repositorio.

Reemplaza o agrega el siguiente contenido:

```md
# Back-End-Development-Pictures

## Environment Setup

- Repository created from the provided template.
- Environment initialized using `bin/setup.sh`.
- Python version: 3.9.x
- Virtual environment: backend-pics-venv
```


> Esta actualización del README es **obligatoria**. Las presentaciones sin ella pueden fallar en la evaluación automatizada.

---

### Evaluación

**Opción 1: Presentación y Evaluación Calificada por IA**: Copia y guarda la **URL pública de GitHub del archivo README.md** del repositorio llamado Back-End-Development-Pictures en un archivo de texto.

**Opción 2: Presentación y Evaluación Calificada por Pares**: Copia y guarda la **URL pública del repositorio de GitHub** del repositorio llamado Back-End-Development-Pictures en un archivo de texto.

Esto completa la configuración del entorno de desarrollo. Cada vez que se recree tu entorno, necesitarás seguir el procedimiento anterior.

Ahora estás listo para comenzar a trabajar.

::page{title="Descripción del Proyecto"}

Tu cliente te ha pedido que construyas un sitio web para una banda famosa. El desarrollador backend del proyecto ha dejado recientemente, y necesitas terminar el código para que el sitio web pueda estar en línea. La aplicación consiste en varios microservicios que trabajan juntos.

En este laboratorio se te pide que termines el microservicio **Obtener Imágenes**. Este microservicio almacena URLs de imágenes de eventos pasados. El desarrollador anterior comenzó una API REST basada en Python Flask y escribió algunas pruebas siguiendo el proceso de desarrollo guiado por pruebas (TDD). Necesitarás obtener el código de GitHub y completar las partes faltantes para que el código pueda pasar todas las pruebas.

::page{title="Revisión de Directrices de API REST"}

El arquitecto te ha proporcionado el siguiente esquema para los endpoints:

## Endpoints de API RESTful

| Acción  | Método  | Código de retorno | Cuerpo | Endpoint URL  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Listar  | GET  | 200 OK  | Array de URLs de imágenes `[{...}]`  | `GET /picture`  |
| Crear  | POST  | 201 CREADO  | Un recurso de imagen en json `{...}`  | POST `/picture`  |
| Leer  | GET  | 200 OK  | Una imagen en json `{...}`  | GET `/picture/{id}`  |
| Actualizar  | PUT | 200 OK  | Una imagen en json `{...}`  | PUT `/picture/{id}`  |
| Eliminar  | DELETE  | 204 SIN CONTENIDO  | `""`  | DELETE `/picture/{id}`  |

Los siguientes endpoints fueron completados por el desarrollador anterior y se pueden usar como referencia:

| Acción  | Método  | Código de retorno | Cuerpo | Endpoint URL  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Salud  | GET  | 200 OK  | `""`  | GET `/health`  |
| Contar  | GET  |  200 OK | `""`  |  GET `/count` |

::page{title="Ejercicio 1: Probar los endpoints de salud y conteo"}

Antes de implementar la API `Get Pictures`, primero probemos los dos endpoints que implementó el desarrollador anterior.
- `/health`
- `/count`

Una forma de probar el endpoint es iniciar el servidor y luego usar el comando `curl` para enviar una solicitud a los endpoints. Abre la terminal si no la tienes abierta ya y cambia al directorio ``.

```bash
cd /home/project/Back-End-Development-Pictures
```


A continuación, ejecuta el siguiente comando para iniciar el servidor de Flask en modo de desarrollo:

```bash
flask --app app run --debugger --reload
```


Dado que tu aplicación principal está en un archivo llamado `app.py`, no es necesario especificarlo. El siguiente comando tiene el mismo resultado:

```bash
flask run --debugger --reload
```


Deberías ver el servidor Flask en ejecución con la siguiente salida en la terminal:

```
$ flask --app app run --debugger --reload
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 132-341-814
```


Ahora puedes ejecutar el siguiente comando `curl` para ver la salida de los endpoints `health` y `count`. **Usa el botón de dividir en la terminal para crear otra terminal al lado de la que está ejecutando el servidor.** Necesitarás cambiar de nuevo al directorio correcto antes de ejecutar el comando:

```
cd /home/project/Back-End-Development-Pictures
```


Ejecuta los siguientes comandos:

```bash
curl --request GET --url http://localhost:5000/health
```


y

```bash
curl --request GET --url http://localhost:5000/count
```


Deberías ver los siguientes resultados:
`/health`

```
$ curl --request GET --url http://localhost:5000/health
{"status":"OK"}
```


`/count`

```
$ curl --request GET --url http://localhost:5000/count
{"length":10}
```


Una segunda y preferida forma de probar el código durante el desarrollo es siguiendo el método TDD. Como se mencionó anteriormente, el desarrollador anterior ha escrito las pruebas para el código. Puedes usar el comando `pytest` y ver si el código pasa las pruebas. Debería pasar para los endpoints `/count` y `/health`.

## Tu Tarea
1. Ejecuta el comando pytest para realizar dos pruebas para los endpoints `health` y `count`. Puedes usar el siguiente comando:

```bash
pytest -k 'test_health or test_count'
```


Deberías ver la siguiente salida:

![pytest command output](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/get_pics_pytest-new.png "pytest command output")

Si ejecutas el comando `pytest` sin la bandera `-k`, se ejecutarán todas las pruebas y verás que las otras pruebas fallan. Usas la bandera `-k` para limitar la salida a solo las dos pruebas de punto final.

## Evaluación:

**Opción 1: Envío y Evaluación Calificada por IA**: Copia y guarda la **salida exacta del terminal** mostrando tanto `test_health` como `test_count` como **APROBADOS** en un **archivo de texto** llamado `exercise1-count-health-passing` para la entrega y evaluación del proyecto final.

**Opción 2: Envío y Evaluación Calificada por Pares**: Ejecuta el comando pytest mencionado anteriormente y toma una captura de pantalla del terminal. Guarda la captura de pantalla como `exercise1-count-health-passing.jpg` (o `.png`). La captura de pantalla debe mostrar tanto `test_health` como `test_count` como **APROBADOS**.

¡Felicidades! Acabas de completar tu primera historia.

::page{title="Ejercicio 2: Implementar el endpoint GET /picture"}

Es hora de implementar el resto de los endpoints. Si ejecutas el comando `pytest` ahora, verás 9 pruebas como fallidas. Tu salida puede verse un poco diferente a la captura de pantalla ya que hemos eliminado todos los registros de las pruebas fallidas por brevedad.

![pytest picture](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/get_pics_pytest_2-new.png "pytest picture")

Tu tarea para el resto del laboratorio es completar el código restante para pasar las pruebas fallidas. Comencemos con el endpoint `GET /picture` primero.

## Tu Tarea
Antes de escribir el código para el endpoint, creemos una rama para que puedas enviar tu código de vuelta a GitHub.

### Tarea 1 : Crear una Rama
Dado que estás trabajando en ramas, debes obtener los últimos cambios de la rama principal para mantenerte actualizado. Luego, puedes crear una nueva rama.

Cambia al directorio `Back-End-Development-Pictures` y ejecuta los siguientes pasos:

```bash
cd /home/project/Back-End-Development-Pictures
git checkout main
git pull
git checkout -b backend-rest
```


> Esto cambiará a la rama principal, obtendrá los últimos cambios y creará una nueva rama. Se te pedirá que envíes todos tus cambios a tu repositorio de GitHub y que fusiones todo el código de nuevo en tu rama principal con una solicitud de extracción.

### Tarea 2 : Completa el código para el endpoint

Escribirás todo el código en el archivo `Back-End-Development-Pictures/backend/routes.py`.

::openFile{path="Back-End-Development-Pictures/backend/routes.py"}

**Nota:** Para abrir en el Explorador de Archivos, ve a esta ubicación:
`Back-End-Development-Pictures/backend/routes.py`

1. Crea una ruta de Flask que responda al método GET para el endpoint `/picture`.
2. Crea una función llamada `get_pictures()` para contener la implementación.
3. Las URLs se cargan en una lista llamada `data`. Necesitas devolverla en este método.
4. Ejecuta pytest hasta que las siguientes funciones pasen:
	```
	tests/test_api.py::test_health PASSED
	tests/test_api.py::test_count PASSED
	tests/test_api.py::test_data_contains_10_pictures PASSED
	tests/test_api.py::test_get_picture PASSED
	tests/test_api.py::test_get_pictures_check_content_type_equals_json PASSED
	```

## Evaluación:

**Opción 1: Envío y Evaluación Calificados por IA**: **Copia y guarda la salida exacta del terminal** mostrando todas las pruebas del servicio Get Pictures como pasadas en un **archivo de texto llamado `exercise2-get-pictures-passing`** para la entrega y evaluación del proyecto final.

**Opción 2: Envío y Evaluación Calificados por Pares**: Una vez que las funciones pasen, toma una captura de pantalla de las pruebas aprobadas y guárdala como `exercise2-get-pictures-passing.jpg` (o `.png`). La captura de pantalla debe mostrar todas las pruebas del servicio Get Pictures como pasadas.

¡Felicidades! Acabas de agregar el primer endpoint REST a tu backend.

::page{title="Ejercicio 3: Implementar el endpoint GET /picture/id"}

Como antes, escribirás el código para el endpoint en el `./backend/routes.py`.

::openFile{path="Back-End-Development-Pictures/backend/routes.py"}

**Nota:** Para abrir en el Explorador de Archivos, ve a esta ubicación:
`Back-End-Development-Pictures/backend/routes.py`

1. Crea una ruta de Flask que responda al método GET para el endpoint `/picture/<id>`.
2. Crea una función llamada `get_picture_by_id(id)` para contener la implementación.
3. Las URLs se cargan en una lista llamada `data`. Necesitarás recorrer la lista, encontrar la URL con el id dado y devolverla al llamador.
4. Ejecuta pytest hasta que las siguientes funciones pasen:
	```
	tests/test_api.py::test_health PASSED
	tests/test_api.py::test_count PASSED
	tests/test_api.py::test_data_contains_10_pictures PASSED
	tests/test_api.py::test_get_picture PASSED
	tests/test_api.py::test_get_pictures_check_content_type_equals_json PASSED
	tests/test_api.py::test_get_picture_by_id PASSED
	tests/test_api.py::test_pictures_json_is_not_empty PASSED
	```

¡Felicidades! Acabas de agregar el segundo endpoint REST a tu backend.

::page{title="Ejercicio 4: Implementar el endpoint POST /picture"}

Como antes, escribirás el código para el endpoint en el `./backend/routes.py`.

::openFile{path="Back-End-Development-Pictures/backend/routes.py"}

**Nota:** Para abrir en el Explorador de Archivos, ve a esta ubicación:
`Back-End-Development-Pictures/backend/routes.py`

1. Crea una ruta de Flask que responda al método POST para el endpoint `/picture/<id>`. Usa `methods=["POST"]` en tu decorador de app.
2. Crea una función llamada `create_picture()` para contener la implementación.
3. Primero necesitarás extraer los datos de la imagen del cuerpo de la solicitud y luego añadirlos a la lista `data`.
4. Si ya existe una imagen con el id, envía un código HTTP `302` de vuelta al usuario con un mensaje de `{"Message": "imagen con id {picture['id']} ya presente"}`.
4. Ejecuta pytest hasta que las siguientes funciones pasen:
	```
	tests/test_api.py::test_health PASSED
	tests/test_api.py::test_count PASSED
	tests/test_api.py::test_data_contains_10_pictures PASSED
	tests/test_api.py::test_get_picture PASSED
	tests/test_api.py::test_get_pictures_check_content_type_equals_json PASSED
	tests/test_api.py::test_get_picture_by_id PASSED
	tests/test_api.py::test_pictures_json_is_not_empty PASSED
	tests/test_api.py::test_post_picture {'id': 200, 'pic_url': 'http://dummyimage.com/230x100.png/dddddd/000000', 'event_country': 'United States', 'event_state': 'California', 'event_city': 'Fremont', 'event_date': '11/2/2030'}
	PASSED
	tests/test_api.py::test_post_picture_duplicate {'id': 200, 'pic_url': 'http://dummyimage.com/230x100.png/dddddd/000000', 'event_country': 'United States', 'event_state': 'California', 'event_city': 'Fremont', 'event_date': '11/2/2030'}
	PASSED
	```

## Evaluación:

**Opción 1: Envío y Evaluación Calificada por IA**: **Copia y guarda la salida exacta del terminal** mostrando todas las pruebas de POST de imagen como aprobadas en un **archivo de texto llamado `exercise4-post-picture-passing`** para la presentación y evaluación del proyecto final.

**Opción 2: Envío y Evaluación Calificada por Pares**: Una vez que las funciones pasen, toma una captura de pantalla de las pruebas aprobadas y guárdala como `exercise4-post-picture-passing.jpg` (o `.png`). La captura de pantalla debe mostrar todas las pruebas de POST de imagen como aprobadas.

::page{title="Ejercicio 5: Implementar el endpoint PUT /picture"}

El endpoint PUT se utilizará para actualizar un recurso de imagen existente. Como antes, escribirás el código para el endpoint en el `./backend/routes.py`.

::openFile{path="Back-End-Development-Pictures/backend/routes.py"}

**Nota:** Para abrir en el Explorador de Archivos, ve a esta ubicación:
`Back-End-Development-Pictures/backend/routes.py`

1. Crea una ruta de Flask que responda al método POST para el endpoint `/picture/<int:id>`. Usa `methods=["PUT"]` en tu decorador de aplicación.
2. Crea una función llamada `update_picture(id)` para contener la implementación.
3. Primero necesitarás extraer los datos de la imagen del cuerpo de la solicitud.
4. Luego encontrarás la imagen en la lista `data`. Si la imagen existe, la actualizarás con la solicitud entrante.
4. Si la imagen no existe, devolverás un estado de `404` con un mensaje `{"message": "imagen no encontrada"}`.
4. Ejecuta pytest hasta que las siguientes funciones pasen:
	```
	tests/test_api.py::test_health PASSED
	tests/test_api.py::test_count PASSED
	tests/test_api.py::test_data_contains_10_pictures PASSED
	tests/test_api.py::test_get_picture PASSED
	tests/test_api.py::test_get_pictures_check_content_type_equals_json PASSED
	tests/test_api.py::test_get_picture_by_id PASSED
	tests/test_api.py::test_pictures_json_is_not_empty PASSED
	tests/test_api.py::test_post_picture {'id': 200, 'pic_url': 'http://dummyimage.com/230x100.png/dddddd/000000', 'event_country': 'Estados Unidos', 'event_state': 'California', 'event_city': 'Fremont', 'event_date': '11/2/2030'}
	PASSED
	tests/test_api.py::test_post_picture_duplicate {'id': 200, 'pic_url': 'http://dummyimage.com/230x100.png/dddddd/000000', 'event_country': 'Estados Unidos', 'event_state': 'California', 'event_city': 'Fremont', 'event_date': '11/2/2030'}
	PASSED
	tests/test_api.py::test_update_picture_by_id PASSED
	```

::page{title="Ejercicio 6: Implementar el endpoint DELETE /picture"}

### Tarea 1 : Implementar el endpoint Delete

El endpoint DELETE se utiliza para eliminar un recurso de imagen existente. Como antes, escribirás el código para el endpoint en el archivo `./backend/routes.py`.

::openFile{path="Back-End-Development-Pictures/backend/routes.py"}

**Nota:** Para abrir en el Explorador de Archivos, ve a esta ubicación:
`Back-End-Development-Pictures/backend/routes.py`

1. Crea una ruta de Flask que responda al método POST para el endpoint `/picture/<int:id>`. Usa `methods=["DELETE"]` en tu decorador de aplicación.
2. Crea una función llamada `delete_picture(id)` para contener la implementación.
3. Primero extraerás el id de la URL.
4. A continuación, recorrerás la lista `data` para encontrar la imagen por id. Si la imagen existe, eliminarás el elemento de la lista y devolverás un cuerpo vacío con un estado de HTTP_204_NO_CONTENT.
4. Si la imagen no existe, devolverás un estado de `404` con un mensaje `{"message": "imagen no encontrada"}`.
4. Ejecuta pytest hasta que las siguientes funciones pasen:
	```
	tests/test_api.py::test_health PASSED
	tests/test_api.py::test_count PASSED
	tests/test_api.py::test_data_contains_10_pictures PASSED
	tests/test_api.py::test_get_picture PASSED
	tests/test_api.py::test_get_pictures_check_content_type_equals_json PASSED
	tests/test_api.py::test_get_picture_by_id PASSED
	tests/test_api.py::test_pictures_json_is_not_empty PASSED
	tests/test_api.py::test_post_picture {'id': 200, 'pic_url': 'http://dummyimage.com/230x100.png/dddddd/000000', 'event_country': 'Estados Unidos', 'event_state': 'California', 'event_city': 'Fremont', 'event_date': '11/2/2030'}
	PASSED
	tests/test_api.py::test_post_picture_duplicate {'id': 200, 'pic_url': 'http://dummyimage.com/230x100.png/dddddd/000000', 'event_country': 'Estados Unidos', 'event_state': 'California', 'event_city': 'Fremont', 'event_date': '11/2/2030'}
	PASSED
	tests/test_api.py::test_update_picture_by_id PASSED
	tests/test_api.py::test_delete_picture_by_id PASSED
	```

## Evaluación:

**Opción 1: Envío y evaluación calificados por IA**: **Copia y guarda la salida exacta del terminal** mostrando todas las pruebas de actualización y eliminación de imágenes como aprobadas en un **archivo de texto llamado `exercise6-delete-picture-passing`** para la entrega y evaluación del proyecto final.

**Opción 2: Envío y evaluación calificados por pares**: Una vez que las funciones pasen, toma una captura de pantalla de las pruebas aprobadas y guárdala como `exercise6-delete-picture-passing.jpg` (o `.png`). La captura de pantalla debe mostrar todas las pruebas de actualización y eliminación de imágenes como aprobadas.

Ahora deberías tener todas las pruebas aprobadas como se muestra en la captura de pantalla aquí:
![Lista de todas las pruebas aprobadas con pruebas aprobadas](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/all-tests-passing.png "Lista de todas las pruebas aprobadas")

### Tarea 2 : Empujar la rama a GitHub y crear un PR
Ahora que has terminado el código para el microservicio, puedes empujar la rama `backend-rest` de regreso a tu fork de GitHub. Dado que eres el único trabajando en este proyecto, adelante y fusiona el PR y elimina la rama. Asegúrate de que todos tus cambios de código estén empujados de vuelta a la rama principal antes de proceder al siguiente laboratorio.

1. Se te pedirá que configures tu usuario y correo electrónico de git la primera vez que empujes:
	```
	git config --local user.name "{tu nombre de GitHub aquí}"
	git config --local user.email {tu correo electrónico de GitHub aquí}
	```
1. Usa el comando `g&#8203;it commit -am` para confirmar tus cambios con el mensaje "implementado servicio de imágenes", y el comando `g&#8203;it push` para empujar esos cambios a tu repositorio.

	<details>
		<summary>Haz clic aquí para una pista.</summary>

	```bash
	git commit -am "{mensaje aquí}"
	git push --set-upstream origin {nombre de la rama aquí}
	```
	</details>

	<details>
	<summary>Haz clic aquí para una pista.</summary>

	```bash
	git commit -am "implementado servicio de imágenes"
	git push --set-upstream origin backend-rest
	```
	</details>

1. Deberías ver un diálogo en la parte inferior de la pantalla pidiendo permiso para abrir el flujo de inicio de sesión de GitHub. Haz clic en `Permitir`.
	![Permiso para empujar a Github](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/github-push-permission.png "Permiso para empujar a Github")

1. El IDE te pedirá tu nombre de usuario y contraseña de GitHub. Usa el token que creaste al principio del laboratorio como tu contraseña.
	![Nombre de usuario de Github](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/github-push-username.png "Nombre de usuario de Github")

1. Puedes ver los registros de empuje en el terminal si la autenticación es exitosa.
	![Registros de terminal de Github](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/github-push-done.png "Registros de terminal de Github")

1. Crea una solicitud de extracción en GitHub para fusionar tus cambios en la rama principal. 
	![Crear solicitud de extracción en Github](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/github-push-pr.png "Crear solicitud de extracción en Github")

1. Dado que no hay nadie más en tu equipo, acepta la solicitud de extracción, fusiónala y elimina la rama.
	![Eliminar rama de empuje en Github](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/github-push-branch-delete.png "Eliminar rama de empuje en Github")

La rama principal, en este punto, debería tener tu código completo.

::page{title="Referencia: Servicio RESTful"}

Aquí hay algunas pistas sobre el comportamiento RESTful de cada uno de los endpoints.

## Listar
- Listar simplemente debe devolver la lista de diccionarios de imágenes y retornar el código de retorno HTTP_200_OK. Simplemente devuelve la estructura `data`.
- Nunca debe devolver un 404_NOT_FOUND.

## Leer
- Leer debe aceptar un id de imagen y recorrer la `data` para encontrar el id.
- Debe devolver un HTTP_404_NOT_FOUND si la imagen no puede ser encontrada con un mensaje `{"message": "imagen no encontrada"}`.
- Si se encuentra la imagen, debe devolver la imagen como un diccionario de Python con un código de retorno de HTTP_200_OK.

## Crear
- Crear solo debe aceptar solicitudes con el método POST.
- Buscará la imagen en la solicitud entrante.
- Debe devolver un HTTP_302_FOUND si la imagen ya existe en la lista `data`.
- De lo contrario, debe agregar la imagen entrante a la lista `data` y devolver un HTTP_201_CREATED con un mensaje `{"Message": f"imagen con id {picture_in['id']} ya presente"}`.

## Actualizar
- Actualizar debe aceptar un account_id y el método HTTP PUT.
- Debe devolver un HTTP_404_NOT_FOUND si la imagen no puede ser encontrada.
- Si se encuentra la imagen, debe reemplazar el contenido de la imagen con el de la solicitud. Debe devolver un código de HTTP_201_CREATED y la imagen actualizada.
- Si la imagen no se encuentra, debe devolver un código de HTTP_404_NOT_FOUND y un mensaje `{"message": "imagen no encontrada"}`.

## Eliminar
- Eliminar debe aceptar un id de imagen y buscar la imagen en la lista `data`.
- Si la imagen no se encuentra, debe devolver un código de HTTP_404_NOT_FOUND y un mensaje `{"message": "imagen no encontrada"}`.
- Si se encuentra la imagen, debe eliminar la imagen de la lista `data`.
- Debe devolver una cadena vacía "" con un código de retorno de HTTP_204_NO_CONTENT.

::page{title="Sugerencias y Soluciones"}

Esta página contiene las sugerencias y soluciones restantes para las API REST de Listar, Crear, Actualizar y Eliminar.

## Sugerencias
### Listar
<details>
	<summary>Haz clic aquí para una sugerencia.</summary>

```bash
@app.route("{insert URL here}", methods="{insert HTTP method name here}")
def {insert method name here}():
	return jsonify({insert data list here})
```


</details>

### Leer

<details>
	<summary>Haz clic aquí para una pista.</summary>

```bash
@app.route("{insert URL here}", methods=["GET"])
def {insert method name here}(id):
    {enumerate the data list}:
        if picture["id"] == id:
            return picture
    return {"message": "{insert error message here}"}, {insert HTTP_NOT_FOUND_STATUS}
```


</details>

### Crear
<details>
	<summary>Haz clic aquí para una pista.</summary>

```bash
@app.route("{insert URL here}", methods="insert list of correct method here")
def {insert method name here}():

    # get data from the json body
    picture_in = {insert code to get json from the request here}

    # if the id is already there, return 303 with the URL for the resource
    {enumerate the picture in data list}:
        if picture_in["id"] == picture["id"]:
            return {
                "Message": f"{insert message here}"
            }, {insert HTTP code here}

    data.append(picture_in)
    return picture_in, {insert HTTP content created code here}

```


</details>

### Actualización
<details>
	<summary>Haz clic aquí para una pista.</summary>

```bash
@app.route("{insert URL here}", methods={insert List of HTTP method here})
def {insert method name here}(id):

    # get data from the json body
    picture_in = {insert code to get json from request here}

    {insert code to enumerate picture in data list with index}:
        if picture["id"] == id:
            data[index] = picture_in
            return picture, {insert HTTP code here}

    return {"message": "insert error message here"}, {insert HTTP NOT FOUND code here}
```


</details>

### Eliminar
<details>
	<summary>Haz clic aquí para una pista.</summary>

```bash
@app.route("{insert URL here}", methods={insert List of HTTP method here})
def {insert method name here}(id):

    {insert code to enumerate pictures in data}:
        if picture["id"] == id:
            {insert code to delete picture from data}
            return "", {insert code to return HTTP code}

    return {"message": "{insert error message here}"}, {insert code to return HTTP code}

```


</details>

## Soluciones

### Lista
<details>
	<summary>Haz clic aquí para verificar tu solución.</summary>

```
@app.route("/picture", methods=["GET"])
def get_pictures():
	return jsonify(data)
```


</details>

### Leer
<details>
	<summary>Haz clic aquí para verificar tu solución.</summary>

```
@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    for picture in data:
        if picture["id"] == id:
            return picture
    return {"message": "picture not found"}, 404
```


</details>

### Crear
<details>
	<summary>Haz clic aquí para verificar tu solución.</summary>

```
@app.route("/picture", methods=["POST"])
def create_picture():

    # get data from the json body
    picture_in = request.json
    print(picture_in)

    # if the id is already there, return 303 with the URL for the resource
    for picture in data:
        if picture_in["id"] == picture["id"]:
            return {
                "Message": f"picture with id {picture_in['id']} already present"
            }, 302

    data.append(picture_in)
    return picture_in, 201
```


</details>

### Actualización
<details>
	<summary>Haz clic aquí para verificar tu solución.</summary>

```
@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):

    # get data from the json body
    picture_in = request.json

    for index, picture in enumerate(data):
        if picture["id"] == id:
            data[index] = picture_in
            return picture, 201

    return {"message": "picture not found"}, 404
```


</details>

### Eliminar
<details>
	<summary>Haz clic aquí para verificar tu solución.</summary>

```
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):

    for picture in data:
        if picture["id"] == id:
            data.remove(picture)
            return "", 204

    return {"message": "picture not found"}, 404
```


</details>

::page{title="Conclusión"}

¡Felicidades! Has terminado de implementar el primer microservicio para obtener imágenes. Este microservicio será utilizado por el sitio principal en el laboratorio final del proyecto.

## Próximos Pasos
Puedes reanudar el curso en este punto. Se te pedirá que crees otro microservicio en el próximo módulo.

## Author(s)
CF

::align{type="center"}

### © IBM Corporation. Todos los derechos reservados.
::/align

<!--
## Changelog
| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2023-02-04 | 0.1 | CF | Initial version created |
| 2023-02-09 | 0.2 | SH | QA pass with edits |
| 2024-01-30 | 0.3| Manvi Gupta | updated Python version and routes.py |
| 2026-01-19 | 0.4 | Nikesh Kumar | Update as per PR and MARK |
|   |   |   |   |
-->