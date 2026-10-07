# MongoDB Atlas — Configuración del entorno local

Este documento describe la configuración necesaria para acceder a MongoDB Atlas desde el entorno local de Windows utilizando:

- MongoDB Shell (`mongosh`)
- MongoDB Atlas CLI (`atlas`)
- Surfshark VPN con WireGuard
- Surfshark Bypasser
- Python mediante el entorno virtual del proyecto
- Una IP Access List temporal de MongoDB Atlas

## 1. Arquitectura

El entorno utiliza la siguiente estructura:

```text
Windows
│
├── Surfshark / WireGuard
│       │
│       └── tráfico general → VPN
│
└── Surfshark Bypasser
        │
        ├── atlas.exe
        ├── mongosh.exe
        └── <proyecto>\.venv\Scripts\python.exe
                │
                ▼
          Internet directo
                │
                ▼
          MongoDB Atlas
```

El tráfico general del sistema continúa utilizando Surfshark.

Las herramientas necesarias para trabajar con MongoDB Atlas se excluyen de la VPN mediante Bypasser.

---

## 2. Herramientas necesarias

En Windows deben estar instaladas las siguientes herramientas:

### MongoDB Shell

Comprobar la instalación:

```powershell
mongosh --version
```

`mongosh` permite conectarse directamente al clúster y ejecutar consultas MongoDB.

### MongoDB Atlas CLI

Comprobar la instalación:

```powershell
atlas --version
```

Atlas CLI permite administrar recursos de MongoDB Atlas, incluida la IP Access List.

---

## 3. Autenticación de Atlas CLI

La primera vez que se utilice Atlas CLI:

```powershell
atlas auth login
```

Completar la autenticación mediante el navegador.

Para comprobar que la autenticación funciona:

```powershell
atlas projects list
```

Localizar el Project ID correspondiente al proyecto que contiene el clúster MongoDB.

---

## 4. Configuración de Surfshark Bypasser

Con Surfshark conectado mediante WireGuard, configurar Bypasser para excluir de la VPN los ejecutables que necesitan acceder directamente a MongoDB Atlas.

Añadir:

```text
atlas.exe
mongosh.exe
<proyecto>\.venv\Scripts\python.exe
```

Es recomendable seleccionar específicamente el `python.exe` perteneciente al entorno virtual del proyecto:

```text
<proyecto>\.venv\Scripts\python.exe
```

De esta forma otros intérpretes Python y otras aplicaciones continúan utilizando normalmente la VPN.

Es importante excluir también `atlas.exe`.

Esto permite que:

```text
atlas.exe
mongosh.exe
python.exe
     │
     └── utilicen la misma IP pública directa
```

Por tanto, la IP detectada mediante `atlas --currentIp` coincide con la utilizada posteriormente por `mongosh` y por la aplicación Python.

---

## 5. Script de autorización temporal

El proyecto contiene:

```text
scripts/
└── mongodb-atlas-access.ps1
```

Este script:

1. Comprueba que Atlas CLI está instalado.
2. Obtiene mediante Atlas la IP pública actual.
3. Añade dicha IP a la IP Access List.
4. Autoriza exclusivamente esa dirección.
5. Configura una expiración automática.
6. Muestra la IP Access List resultante.

La duración predeterminada es:

```text
8 horas
```

Esto evita mantener indefinidamente direcciones IP antiguas autorizadas.

---

## 6. Ejecutar el script

El script debe ejecutarse **antes de iniciar la aplicación**.

Desde la raíz del proyecto:

```powershell
.\scripts\mongodb-atlas-access.ps1 `
    -ProjectId "PROJECT_ID"
```

No es necesario activar previamente el entorno virtual Python, ya que `atlas` es una herramienta instalada globalmente en Windows.

También puede ejecutarse desde cualquier ubicación indicando la ruta completa al script.

El resultado esperado es una entrada similar a:

```text
XXX.XXX.XXX.XXX/32
```

con una expiración de aproximadamente 8 horas.

Para comprobar manualmente la Access List:

```powershell
atlas accessLists list --projectId "PROJECT_ID"
```

---

## 7. Verificación mediante mongosh

Antes de iniciar la aplicación puede comprobarse opcionalmente la conectividad con MongoDB Atlas:

```powershell
mongosh "mongodb+srv://<CLUSTER>.mongodb.net/" `
    --apiVersion 1 `
    --username <USERNAME>
```

Introducir la contraseña cuando `mongosh` la solicite.

Una conexión correcta confirma:

```text
DNS              OK
Red              OK
Bypasser         OK
IP Access List   OK
TLS              OK
Credenciales     OK
MongoDB Atlas    OK
```

Esta comprobación es especialmente útil cuando cambia la configuración de red, VPN o Bypasser.

---

## 8. Arranque de la aplicación

Una vez autorizada la IP, activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

o desde Git Bash:

```bash
source .venv/Scripts/activate
```

A continuación, iniciar normalmente la aplicación.

Por ejemplo:

```powershell
flask run
```

La aplicación utilizará:

```text
.venv\Scripts\python.exe
```

que está incluido en Surfshark Bypasser.

Por tanto:

```text
Aplicación Flask
      ↓
.venv\Scripts\python.exe
      ↓
Surfshark Bypasser
      ↓
IP pública autorizada
      ↓
MongoDB Atlas
```

---

## 9. Orden recomendado de trabajo

Al comenzar una sesión de desarrollo:

```text
1. Iniciar Surfshark
2. Conectar WireGuard
3. Comprobar que Bypasser está activo
4. Ejecutar mongodb-atlas-access.ps1
5. Comprobar mongosh (opcional)
6. Activar .venv
7. Iniciar la aplicación
8. Trabajar normalmente
```

Ejemplo:

```powershell
.\scripts\mongodb-atlas-access.ps1 `
    -ProjectId "PROJECT_ID"

mongosh "mongodb+srv://<CLUSTER>.mongodb.net/" `
    --apiVersion 1 `
    --username <USERNAME>

.\.venv\Scripts\Activate.ps1

flask run
```

La comprobación con `mongosh` puede omitirse durante el uso diario una vez validada la configuración.

---

## 10. Expiración de la IP

La entrada creada por el script tiene una duración predeterminada de:

```text
8 horas
```

Al finalizar ese período, MongoDB Atlas elimina automáticamente la autorización temporal.

No es necesario eliminar manualmente la IP.

En la siguiente sesión de desarrollo simplemente debe volver a ejecutarse:

```powershell
.\scripts\mongodb-atlas-access.ps1 `
    -ProjectId "PROJECT_ID"
```

De esta forma se autoriza la IP pública utilizada en ese momento.

---

## 11. Consideraciones de seguridad

No utilizar una regla global como:

```text
0.0.0.0/0
```

para el desarrollo habitual.

Debe autorizarse únicamente la IP pública actual mediante una entrada `/32`.

No almacenar contraseñas de MongoDB directamente en:

```text
mongodb-atlas-access.ps1
```

El script únicamente debe gestionar la autorización temporal de red.

Las credenciales de la aplicación deben gestionarse independientemente, por ejemplo mediante variables de entorno o un fichero `.env` excluido del repositorio.

Ejemplo de `.gitignore`:

```gitignore
.env
.venv/
```

El Project ID puede proporcionarse como argumento al script y no requiere almacenar las credenciales de MongoDB.

---

## 12. Diagnóstico de conectividad

Para comprobar los registros SRV del clúster:

```powershell
Resolve-DnsName `
    -Name "_mongodb._tcp.<CLUSTER>.mongodb.net" `
    -Type SRV
```

Para comprobar la conectividad con un nodo:

```powershell
Test-NetConnection `
    -ComputerName "<HOST_MONGODB>" `
    -Port 27017
```

Una conexión correcta mostrará:

```text
TcpTestSucceeded : True
```

Si `mongosh` funciona sin VPN pero falla al pasar directamente por Surfshark, comprobar que `mongosh.exe`, `atlas.exe` y el `python.exe` del entorno virtual siguen configurados correctamente en Bypasser.

---

## Resumen

El script de acceso a Atlas debe considerarse una tarea de preparación del entorno y no una parte de la aplicación.

El flujo recomendado es:

```text
Surfshark
   ↓
WireGuard + Bypasser
   ↓
mongodb-atlas-access.ps1
   ↓
IP /32 autorizada durante 8 horas
   ↓
mongosh (comprobación opcional)
   ↓
entorno virtual Python
   ↓
aplicación
   ↓
MongoDB Atlas
```

De esta forma se mantiene la VPN activa para el resto del sistema, mientras las herramientas específicas del proyecto acceden directamente y de forma temporal a MongoDB Atlas.