# Challenge_sessions
Genera una clave tomando como entrada los usuarios registrados en el sistema. Por lo tanto, detecta cuándo se conecta un nuevo usuario.

Ejemplo de configuracion json
```json
{
	"FileName": "sesiones_challenge.dll",
	"Description": "Challenge that generates a key by taking as input the logged in users in the system. Therefore it detects when a new user is logged in.",
	"Props": {
		"validity_time": 3600,
		"refresh_time": 3000
	},
	"Requirements": "none"
}
```

## Funcionamiento

Toda la funcionalidad de challenge se encuentra en el fichero sessions_challenge.py. En concreto, la funcionalidad se desarrolla dentro de la función executeChallenge(). 

Se hace uso del comando query users del sistema, lanzado desde Python. Para ello, se ejecuta la línea de código: os.popen('query user').read(), la cual abre un proceso query users. El challenge lanza el comando, espera a recibir la respuesta y la parsea eliminando la información innecesaria, para lo cual primero de todo elimina la parte de la salida que no tiene nada que ver con las sesiones de usuario. Posteriormente se separan los usuarios conectados mediante un salto (‘\n’), de forma que cada uno de esos usuarios representa una sesión. Finalmente, esta información es almacenada en un array de sesiones. Con el este array se genera una clave, la cual será la clave del challenge.

Es aplicable fundamentalmente al contenido de equipos en los que pueden existir muchas sesiones simultáneas (p.ej. servidores).
El contexto de seguridad requiere de la concurrencia de varios usuarios logeados para que se revele el contenido a cualquiera de ellos. Si uno de los usuarios no está “presente” el resto no podrá acceder al contenido
