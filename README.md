# CAPSTONE_BICING_2025

## Introducción y desarrollo del proyecto:

Como usuarios de Bicing y residentes de Barcelona, debatimos sobre qué variables incluir en el modelo para mejorarlo e incorporar la mayoría de los casos y situaciones que pueden favorecer o dificultar el uso del servicio de Bicing en la ciudad.
Escojimos 3 variables que respresentavan la mayoria de casuisticas significativas. Son la siguientes:

Variables climáticas:
Para ello, consideramos datos meteorológicos provenientes de la Xarxa d'Estacions Meteorològiques Automàtiques (XEMA) de la estación del Raval:
Temperatura
- Precipitación máxima en 1 minuto
- Dirección de la racha máxima del viento a 10 m
- Velocidad del viento a 10 m (esc.)
- Irradiancia solar global
- Racha máxima del viento a 10 m
- Precipitación
- Humedad relativa

Eventos
Partidos del F.C. Barcelona: Utilizamos los datos de la web Livefutbol.com.

Festividades: Recurriendo a la web de Betevé del Ajuntament de Barcelona.

Para verificar la relevancia de estas variables, analizamos su impacto mediante la creación de gráficos y mapas, ajustando las fechas y comparando los resultados con los datos reales y la predicción. También identificamos fechas clave para evaluar si permitían predecir escenarios específicos, lo que ayudó a validar el modelo.
Para relizar el trabajo anterior de forma más fluida usamos mtflow para comparar los efectos de las variaciones incorporadas.

Finalmente, consideramos que sería una buena idea aplicar el modelo en una aplicación, permitiendo sintetizar el trabajo en un sistema tangible.

## Explicación de las varibles extra incluidas en el modelo:

### Variables climáticas

En los siguientes gráficos se puede observar cómo el uso de variables climáticas, como la lluvia (cuando se registran precipitaciones) y la radiación solar, tiene un impacto positivo en la predicción del modelo.

Asimismo, en los dos gráficos siguientes, correspondientes a fechas diferentes, se aprecia cómo el porcentaje de docks disponibles dismminuye en el momento en que hay precipitaciones. Cuando comienza a llover, se evidencia que los usuarios depositan sus bicicletas en las estaciones.

![Image](https://github.com/user-attachments/assets/565609d4-e185-422f-976e-22128347d6ec) 

En los dos gráficos siguientes se observa cómo funciona la disponibilidad de sitios cuando no hay lluvia.

![Image](https://github.com/user-attachments/assets/7692986e-08d9-4a03-b33f-1ab86c11f8b8) 

En el siguiente gráfico se puede observar cómo evoluciona la intensidad de los rayos solares durnate un día de julio. La radiación aumenta hasta el mediodía y luego comienza a descender hasta la puesta de sol.

![Image](https://github.com/user-attachments/assets/5e0ab0f3-19c3-450f-aa4a-64b73a3ff567)

En el siguiente gráfico se puede observar el porcentaje de docks disponibles en un día de julio de 2020 sin sol.

![Image](https://github.com/user-attachments/assets/7d679508-db92-4a16-8dcb-66340f57f9e2) 

En el siguiente gráfico se puede observar un día de julio de 2020 con sol y cómo el porcentaje de docks disponibles disminuye especialmente en la zona costera.

![Image](https://github.com/user-attachments/assets/11284f97-ea93-4b39-9f4f-98f3fa9e4de8) 

En el siguiente gráfico coparamos prediciones del modelo con y sin sol para un mismo escenario. La diferencia en el porcentaje de docks disponibles entre días ese día soleado y si no lo fuera, evidenciando así su impacto.

![Image](https://github.com/user-attachments/assets/608de8d6-ad04-4580-a862-b87aa8f2e955) 



### Variable "Eventos: Partidos del FC Barcelona"

Al incluir la variable "partido en casa", se observa cómo disminuye el porcentaje de docks disponibles alrededor del estadio donde se juega el partido.

En el siguiente gráfico se puede ver cómo, en la zona del Camp Nou, se produce una disminución en el porcentaje de docks disponibles en enero del 2020 a la hora del partido (20:00).

![Image](https://github.com/user-attachments/assets/7ee606d8-67a6-4ce6-905f-3ae417df3d28) 

Por otro lado, esta dinámica no se observa en días sin partido. Por ejemplo, en un día de enero de 2020, no se registra una disminución significativa en el porcentaje de docks disponibles alrededor del estadio.

![Image](https://github.com/user-attachments/assets/73123f8a-04dc-42d4-be1b-caa58bfad1e8) 

A continuacion mostramos dos mapas de calor que muestran como el hecho de que haya o no partido afecta a las prediciones del modelo.

El siguiente mapa muestra la diferencia disponibilidad de docks predicha por el modelo en un día con partido versus si no lo hubiera (en enero de 2020 a las 20:00 horas). Se puede observar cómo el modelo predice una disminución en la disponibilidad de docks en la zona del Camp Nou.
![Image](https://github.com/user-attachments/assets/f02225bd-8004-454e-9c40-c62ad77a653a) 


Por otro lado,  si comoaramos predicciones para un mismo escenario con o sin partido, pero en 2024, se observa una reducción predicha por el modelo en la disponibilidad de docks en la zona de Plaça Espanya durante (en marzo de 2024 a las 20:00 horas). Actualmente, esta área concentra conexiones de bus, metro y tren con el servicio de Bicing, facilitando el acceso al Estadio Lluís Companys, donde el FC Barcelona juega mientras el Camp Nou se encuentra en obras.

![Image](https://github.com/user-attachments/assets/1e8afcd0-bec7-452b-8205-4cb974ddadfd) 

El modelo captura estos comportamiento de los usuarios y tiene la capacidad de anticipar (en parte) los comportamientos habituales de los usuarios del Bicing.
 
# Explicacion de codigo:

Hemos procesado por separado los datos crudos y los datos de test para unirlos solamente en el último archivo para crear la entrega de Kaggle. El diagrama de flujo de datos y procesado sería el siguiente:

![data_flow_diagram](https://github.com/user-attachments/assets/9b2f0b06-5fda-4c72-ba7e-4556d6d7cfae)
