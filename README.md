# roomie-bot
[![Build Status](https://travis-ci.com/dipzza/roomie-bot.svg?branch=master)](https://travis-ci.com/dipzza/roomie-bot)
[![codecov](https://codecov.io/gh/dipzza/roomie-bot/branch/master/graph/badge.svg?token=DR8OVMCUBX)](undefined)

Bot de telegram en desarrollo para el [curso de programación para QA](https://github.com/JJ/curso-tdd)

Al compartir piso hay muchos gastos en común que suele pagar una persona temporalmente, recordar cuanto dinero se debe entre todos los compañeros puede ser complicado.

Como solución a este problema se plantea un cliente de API de telegram, un bot, que permita de forma transparente y común tener apuntadas la deudas en grupo. Este módulo de deudas sería una parte del bot con utilidades para compañeros de piso, al que posteriormente tras el curso se le pueden añadir recordatorios, reparto de tareas de limpieza u otras funciones.

## Instrucciones

[Poetry](https://python-poetry.org/) se usa para gestionar el proyecto.

Instalar solo las dependencias necesarias para ejecutar el bot
    
    poetry install --no-dev

Instalar todas las dependencias incluidas las de desarrollo (necesario para usar poetry run task ...)
    
    poetry install

Ejecutar el bot

1. Exporta una variable de entorno llamada TOKEN con el token de tu bot. Ejemplo en linux.
        
        export TOKEN="your_api_token"

2. Inicia el bot
        
        poetry run task bot
        
    ó
        
        poetry run roomie_bot/bot.py

Ejecutar los tests unitarios

    poetry run task test

Ejecutar los tests de cobertura

    poetry run task coverage

## Herramientas utilizadas

+ Lenguaje: Python con [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).
+ Servicio de Logging: modulo logging de Python.
+ Configuración remota: etcd.
+ Almacenamiento de datos: SQLite

Discutido en Issue [#3](https://github.com/dipzza/roomie-bot/issues/3)

## Estructura del proyecto

+ Todo el código se encuentra en la carpeta 'roomie-bot'.
	- El módulo principal [bot.py](roomie-bot/bot.py) se encarga de recibir y responder a los mensajes de telegram llamando a los siguientes submodulos
	- El módulo [database](roomie-bot/database/) se encarga de hacer operaciones en la base de datos sqlite.
	- El módulo [expenses](roomie-bot/expenses/) se encarga de procesar todo lo necesario relativo a las deudas.

## Contribuidores
+ [Francisco Javier Bolívar Expósito](https://github.com/dipzza)
+ [Aburo](https://github.com/AburoSenpai) Icono.

### Icono (provisional)

 ![Icono del bot](/img/robotito.png)
