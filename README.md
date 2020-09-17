# roomie-bot
Bot de telegram en desarrollo para el [curso de programación para QA](https://github.com/JJ/curso-tdd)

Al compartir piso hay muchos gastos en común que suele pagar una persona temporalmente, recordar cuanto dinero se debe entre todos los compañeros puede ser complicado.

Como solución a este problema se plantea un cliente de API de telegram, un bot, que permita de forma transparente y común tener apuntadas la deudas en grupo. Este módulo de deudas sería una parte del bot con utilidades para compañeros de piso, al que posteriormente tras el curso se le pueden añadir recordatorios, reparto de tareas de limpieza u otras funciones.

## Herramientas utilizadas

+ Lenguaje: Python con [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).
+ Servicio de Logging: modulo logging de Python.
+ Configuración remota: etcd.
+ Almacenamiento de datos: SQLite

Discutido en Issue [#3](https://github.com/dipzza/roomie-bot/issues/3)

## Estructura del proyecto

+ Todo el código se encuentra en la carpeta 'roomie-bot'.
	- [bot.py](roomie-bot/bot.py) contiene el módulo principal, que se encarga de recibir y responder a los mensajes de telegram llamando a los siguientes submodulos
	- El modulo [database](roomie-bot/database/) se encarga de hacer operaciones en la base de datos sqlite.
	- El modulo [expenses](roomie-bot/expenses/) se encarga de procesar todo lo necesario relativo a las deudas.

+ Se han añadido a la raíz del repositorio los archivos [requirements.txt](requirements.txt) y [setup.py](setup.py) para facilitar la instalación de la aplicación y sus dependencias.

## Contribuidores
+ [Francisco Javier Bolívar Expósito](https://github.com/dipzza)
