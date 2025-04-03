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

[Uploading <!DOCTYPE html>
<html>
<head>
    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_1c26a2450131341257ad30f4f0561955 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>
        
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
</head>
<body>
    
    
    <style>
        .legend {
            font-size: 16px !important;
            padding: 10px;
            line-height: 20px;
        }
    </style>
    
    
            <div class="folium-map" id="map_1c26a2450131341257ad30f4f0561955" ></div>
        
</body>
<script>
    
    
            var map_1c26a2450131341257ad30f4f0561955 = L.map(
                "map_1c26a2450131341257ad30f4f0561955",
                {
                    center: [41.403278, 2.174055],
                    crs: L.CRS.EPSG3857,
                    zoom: 13,
                    zoomControl: true,
                    preferCanvas: false,
                    rotate: 30,
                }
            );

            

        
    
            var tile_layer_fbc8e54bbdb88464949cf530db4a26f4 = L.tileLayer(
                "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors", "detectRetina": false, "maxNativeZoom": 19, "maxZoom": 19, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            );
        
    
            tile_layer_fbc8e54bbdb88464949cf530db4a26f4.addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
    var color_map_d44ee3e6147b285a468bf2f2d9f4c92d = {};

    
    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.color = d3.scale.threshold()
              .domain([-5.0, -4.979959919839679, -4.959919839679359, -4.939879759519038, -4.919839679358717, -4.8997995991983965, -4.8797595190380765, -4.859719438877756, -4.839679358717435, -4.819639278557114, -4.799599198396794, -4.779559118236473, -4.759519038076152, -4.739478957915832, -4.719438877755511, -4.69939879759519, -4.679358717434869, -4.659318637274549, -4.6392785571142285, -4.619238476953908, -4.599198396793587, -4.579158316633267, -4.559118236472946, -4.539078156312625, -4.519038076152305, -4.498997995991984, -4.478957915831663, -4.458917835671342, -4.438877755511022, -4.4188376753507015, -4.398797595190381, -4.37875751503006, -4.35871743486974, -4.338677354709419, -4.318637274549098, -4.298597194388778, -4.278557114228457, -4.258517034068136, -4.238476953907815, -4.218436873747495, -4.198396793587174, -4.1783567134268536, -4.158316633266534, -4.138276553106213, -4.118236472945892, -4.098196392785571, -4.07815631262525, -4.05811623246493, -4.038076152304609, -4.018036072144288, -3.9979959919839683, -3.9779559118236474, -3.9579158316633265, -3.937875751503006, -3.9178356713426856, -3.8977955911823647, -3.877755511022044, -3.8577154308617234, -3.837675350701403, -3.817635270541082, -3.797595190380761, -3.777555110220441, -3.7575150300601203, -3.7374749498997994, -3.717434869739479, -3.6973947895791586, -3.6773547094188377, -3.657314629258517, -3.6372745490981964, -3.617234468937876, -3.597194388777555, -3.577154308617234, -3.5571142284569137, -3.5370741482965933, -3.5170340681362724, -3.496993987975952, -3.4769539078156315, -3.4569138276553106, -3.4368737474949898, -3.4168336673346693, -3.396793587174349, -3.376753507014028, -3.356713426853707, -3.3366733466933867, -3.3166332665330662, -3.2965931863727453, -3.276553106212425, -3.2565130260521045, -3.2364729458917836, -3.2164328657314627, -3.1963927855711423, -3.176352705410822, -3.156312625250501, -3.13627254509018, -3.1162324649298596, -3.096192384769539, -3.0761523046092183, -3.056112224448898, -3.0360721442885774, -3.0160320641282565, -2.995991983967936, -2.975951903807615, -2.9559118236472948, -2.935871743486974, -2.9158316633266534, -2.8957915831663326, -2.875751503006012, -2.8557114228456912, -2.835671342685371, -2.81563126252505, -2.7955911823647295, -2.775551102204409, -2.755511022044088, -2.7354709418837677, -2.715430861723447, -2.6953907815631264, -2.6753507014028055, -2.655310621242485, -2.635270541082164, -2.6152304609218437, -2.595190380761523, -2.5751503006012024, -2.555110220440882, -2.535070140280561, -2.5150300601202407, -2.49498997995992, -2.4749498997995993, -2.4549098196392785, -2.434869739478958, -2.414829659318637, -2.3947895791583167, -2.374749498997996, -2.3547094188376754, -2.3346693386773545, -2.314629258517034, -2.2945891783567136, -2.2745490981963927, -2.2545090180360723, -2.2344689378757514, -2.214428857715431, -2.19438877755511, -2.1743486973947896, -2.1543086172344688, -2.1342685370741483, -2.1142284569138274, -2.094188376753507, -2.0741482965931866, -2.0541082164328657, -2.0340681362725452, -2.0140280561122244, -1.993987975951904, -1.973947895791583, -1.9539078156312626, -1.9338677354709417, -1.9138276553106213, -1.8937875751503004, -1.87374749498998, -1.8537074148296595, -1.8336673346693386, -1.8136272545090182, -1.7935871743486973, -1.7735470941883769, -1.753507014028056, -1.7334669338677355, -1.7134268537074147, -1.6933867735470942, -1.6733466933867733, -1.653306613226453, -1.6332665330661325, -1.6132264529058116, -1.5931863727454911, -1.5731462925851702, -1.5531062124248498, -1.533066132264529, -1.5130260521042085, -1.4929859719438876, -1.4729458917835672, -1.4529058116232463, -1.4328657314629258, -1.4128256513026054, -1.3927855711422845, -1.372745490981964, -1.3527054108216432, -1.3326653306613228, -1.3126252505010019, -1.2925851703406814, -1.2725450901803605, -1.25250501002004, -1.2324649298597192, -1.2124248496993988, -1.1923847695390783, -1.1723446893787575, -1.152304609218437, -1.1322645290581161, -1.1122244488977957, -1.0921843687374748, -1.0721442885771544, -1.0521042084168335, -1.032064128256513, -1.0120240480961922, -0.9919839679358722, -0.9719438877755513, -0.9519038076152304, -0.9318637274549095, -0.9118236472945895, -0.8917835671342687, -0.8717434869739478, -0.8517034068136269, -0.8316633266533069, -0.811623246492986, -0.7915831663326651, -0.7715430861723451, -0.7515030060120242, -0.7314629258517034, -0.7114228456913825, -0.6913827655310625, -0.6713426853707416, -0.6513026052104207, -0.6312625250500998, -0.6112224448897798, -0.591182364729459, -0.5711422845691381, -0.5511022044088181, -0.5310621242484972, -0.5110220440881763, -0.4909819639278554, -0.47094188376753543, -0.45090180360721455, -0.43086172344689366, -0.4108216432865728, -0.3907815631262528, -0.3707414829659319, -0.350701402805611, -0.330661322645291, -0.31062124248497014, -0.29058116232464926, -0.2705410821643284, -0.2505010020040084, -0.2304609218436875, -0.2104208416833666, -0.19038076152304573, -0.17034068136272573, -0.15030060120240485, -0.13026052104208397, -0.11022044088176397, -0.09018036072144309, -0.0701402805611222, -0.05010020040080132, -0.030060120240481325, -0.010020040080160442, 0.010020040080160442, 0.030060120240481325, 0.05010020040080132, 0.0701402805611222, 0.09018036072144309, 0.11022044088176397, 0.13026052104208397, 0.15030060120240485, 0.17034068136272573, 0.19038076152304573, 0.2104208416833666, 0.2304609218436875, 0.2505010020040084, 0.2705410821643284, 0.29058116232464926, 0.31062124248497014, 0.330661322645291, 0.350701402805611, 0.3707414829659319, 0.3907815631262528, 0.4108216432865728, 0.43086172344689366, 0.45090180360721455, 0.47094188376753543, 0.4909819639278554, 0.5110220440881763, 0.5310621242484972, 0.5511022044088181, 0.5711422845691381, 0.591182364729459, 0.6112224448897798, 0.6312625250500998, 0.6513026052104207, 0.6713426853707416, 0.6913827655310625, 0.7114228456913825, 0.7314629258517034, 0.7515030060120242, 0.7715430861723451, 0.7915831663326651, 0.811623246492986, 0.8316633266533069, 0.8517034068136269, 0.8717434869739478, 0.8917835671342687, 0.9118236472945895, 0.9318637274549095, 0.9519038076152304, 0.9719438877755513, 0.9919839679358722, 1.0120240480961922, 1.032064128256513, 1.052104208416834, 1.072144288577154, 1.0921843687374748, 1.1122244488977957, 1.1322645290581166, 1.1523046092184366, 1.1723446893787575, 1.1923847695390783, 1.2124248496993992, 1.2324649298597192, 1.25250501002004, 1.272545090180361, 1.292585170340681, 1.3126252505010019, 1.3326653306613228, 1.3527054108216436, 1.3727454909819636, 1.3927855711422845, 1.4128256513026054, 1.4328657314629263, 1.4529058116232463, 1.4729458917835672, 1.492985971943888, 1.513026052104208, 1.533066132264529, 1.5531062124248498, 1.5731462925851707, 1.5931863727454907, 1.6132264529058116, 1.6332665330661325, 1.6533066132264533, 1.6733466933867733, 1.6933867735470942, 1.713426853707415, 1.733466933867735, 1.753507014028056, 1.7735470941883769, 1.7935871743486977, 1.8136272545090177, 1.8336673346693386, 1.8537074148296595, 1.8737474949899804, 1.8937875751503004, 1.9138276553106213, 1.9338677354709422, 1.9539078156312621, 1.973947895791583, 1.993987975951904, 2.014028056112225, 2.034068136272545, 2.0541082164328657, 2.0741482965931866, 2.0941883767535074, 2.1142284569138274, 2.1342685370741483, 2.154308617234469, 2.174348697394789, 2.19438877755511, 2.214428857715431, 2.234468937875752, 2.254509018036072, 2.2745490981963927, 2.2945891783567136, 2.3146292585170345, 2.3346693386773545, 2.3547094188376754, 2.3747494989979963, 2.3947895791583163, 2.414829659318637, 2.434869739478958, 2.454909819639279, 2.474949899799599, 2.49498997995992, 2.5150300601202407, 2.5350701402805615, 2.5551102204408815, 2.5751503006012024, 2.5951903807615233, 2.6152304609218433, 2.635270541082164, 2.655310621242485, 2.675350701402806, 2.695390781563126, 2.715430861723447, 2.7354709418837677, 2.7555110220440886, 2.7755511022044086, 2.7955911823647295, 2.8156312625250504, 2.8356713426853704, 2.8557114228456912, 2.875751503006012, 2.895791583166333, 2.915831663326653, 2.935871743486974, 2.9559118236472948, 2.9759519038076157, 2.9959919839679356, 3.0160320641282556, 3.0360721442885765, 3.0561122244488974, 3.0761523046092183, 3.096192384769539, 3.11623246492986, 3.136272545090181, 3.156312625250502, 3.176352705410821, 3.196392785571142, 3.2164328657314627, 3.2364729458917836, 3.2565130260521045, 3.2765531062124253, 3.2965931863727462, 3.3166332665330653, 3.336673346693386, 3.356713426853707, 3.376753507014028, 3.396793587174349, 3.4168336673346698, 3.4368737474949906, 3.4569138276553097, 3.4769539078156306, 3.4969939879759515, 3.5170340681362724, 3.5370741482965933, 3.557114228456914, 3.577154308617235, 3.597194388777556, 3.617234468937875, 3.637274549098196, 3.657314629258517, 3.6773547094188377, 3.6973947895791586, 3.7174348697394795, 3.7374749498998003, 3.7575150300601194, 3.7775551102204403, 3.797595190380761, 3.817635270541082, 3.837675350701403, 3.857715430861724, 3.8777555110220447, 3.897795591182364, 3.9178356713426847, 3.9378757515030056, 3.9579158316633265, 3.9779559118236474, 3.9979959919839683, 4.018036072144289, 4.03807615230461, 4.058116232464929, 4.07815631262525, 4.098196392785571, 4.118236472945892, 4.138276553106213, 4.158316633266534, 4.178356713426854, 4.1983967935871735, 4.218436873747494, 4.238476953907815, 4.258517034068136, 4.278557114228457, 4.298597194388778, 4.318637274549099, 4.338677354709418, 4.358717434869739, 4.37875751503006, 4.398797595190381, 4.4188376753507015, 4.438877755511022, 4.458917835671343, 4.478957915831664, 4.498997995991983, 4.519038076152304, 4.539078156312625, 4.559118236472946, 4.579158316633267, 4.599198396793588, 4.6192384769539085, 4.639278557114228, 4.6593186372745485, 4.679358717434869, 4.69939879759519, 4.719438877755511, 4.739478957915832, 4.759519038076153, 4.779559118236472, 4.799599198396793, 4.819639278557114, 4.839679358717435, 4.859719438877756, 4.8797595190380765, 4.899799599198397, 4.919839679358718, 4.939879759519037, 4.959919839679358, 4.979959919839679, 5.0])
              .range(['#ff0000ff', '#ff0000ff', '#ff0101ff', '#ff0202ff', '#ff0303ff', '#ff0404ff', '#fe0505ff', '#fe0505ff', '#fe0606ff', '#fe0707ff', '#fe0808ff', '#fe0909ff', '#fd0a0aff', '#fd0b0bff', '#fd0b0bff', '#fd0c0cff', '#fd0d0dff', '#fc0e0eff', '#fc0f0fff', '#fc1010ff', '#fc1010ff', '#fc1111ff', '#fc1212ff', '#fb1313ff', '#fb1414ff', '#fb1515ff', '#fb1616ff', '#fb1616ff', '#fb1717ff', '#fa1818ff', '#fa1919ff', '#fa1a1aff', '#fa1b1bff', '#fa1c1cff', '#f91c1cff', '#f91d1dff', '#f91e1eff', '#f91f1fff', '#f92020ff', '#f92121ff', '#f82121ff', '#f82222ff', '#f82323ff', '#f82424ff', '#f82525ff', '#f82626ff', '#f72727ff', '#f72727ff', '#f72828ff', '#f72929ff', '#f72a2aff', '#f62b2bff', '#f62c2cff', '#f62c2cff', '#f62d2dff', '#f62e2eff', '#f62f2fff', '#f53030ff', '#f53131ff', '#f53232ff', '#f53232ff', '#f53333ff', '#f53434ff', '#f43535ff', '#f43636ff', '#f43737ff', '#f43838ff', '#f43838ff', '#f33939ff', '#f33a3aff', '#f33b3bff', '#f33c3cff', '#f33d3dff', '#f33d3dff', '#f23e3eff', '#f23f3fff', '#f24040ff', '#f24141ff', '#f24242ff', '#f24343ff', '#f14343ff', '#f14444ff', '#f14545ff', '#f14646ff', '#f14747ff', '#f04848ff', '#f04949ff', '#f04949ff', '#f04a4aff', '#f04b4bff', '#f04c4cff', '#ef4d4dff', '#ef4e4eff', '#ef4e4eff', '#ef4f4fff', '#ef5050ff', '#ef5151ff', '#ee5252ff', '#ee5353ff', '#ee5454ff', '#ee5454ff', '#ee5555ff', '#ed5656ff', '#ed5757ff', '#ed5858ff', '#ed5959ff', '#ed5959ff', '#ed5a5aff', '#ec5b5bff', '#ec5c5cff', '#ec5d5dff', '#ec5e5eff', '#ec5f5fff', '#eb5f5fff', '#eb6060ff', '#eb6161ff', '#eb6262ff', '#eb6363ff', '#eb6464ff', '#ea6565ff', '#ea6565ff', '#ea6666ff', '#ea6767ff', '#ea6868ff', '#ea6969ff', '#e96a6aff', '#e96a6aff', '#e96b6bff', '#e96c6cff', '#e96d6dff', '#e86e6eff', '#e86f6fff', '#e87070ff', '#e87070ff', '#e87171ff', '#e87272ff', '#e77373ff', '#e77474ff', '#e77575ff', '#e77676ff', '#e77676ff', '#e77777ff', '#e67878ff', '#e67979ff', '#e67a7aff', '#e67b7bff', '#e67b7bff', '#e57c7cff', '#e57d7dff', '#e57e7eff', '#e57f7fff', '#e58080ff', '#e58181ff', '#e48181ff', '#e48282ff', '#e48383ff', '#e48484ff', '#e48585ff', '#e48686ff', '#e38686ff', '#e38787ff', '#e38888ff', '#e38989ff', '#e38a8aff', '#e28b8bff', '#e28c8cff', '#e28c8cff', '#e28d8dff', '#e28e8eff', '#e28f8fff', '#e19090ff', '#e19191ff', '#e19292ff', '#e19292ff', '#e19393ff', '#e19494ff', '#e09595ff', '#e09696ff', '#e09797ff', '#e09797ff', '#e09898ff', '#df9999ff', '#df9a9aff', '#df9b9bff', '#df9c9cff', '#df9d9dff', '#df9d9dff', '#de9e9eff', '#de9f9fff', '#dea0a0ff', '#dea1a1ff', '#dea2a2ff', '#dea3a3ff', '#dda3a3ff', '#dda4a4ff', '#dda5a5ff', '#dda6a6ff', '#dda7a7ff', '#dca8a8ff', '#dca8a8ff', '#dca9a9ff', '#dcaaaaff', '#dcababff', '#dcacacff', '#dbadadff', '#dbaeaeff', '#dbaeaeff', '#dbafafff', '#dbb0b0ff', '#dab1b1ff', '#dab2b2ff', '#dab3b3ff', '#dab3b3ff', '#dab4b4ff', '#dab5b5ff', '#d9b6b6ff', '#d9b7b7ff', '#d9b8b8ff', '#d9b9b9ff', '#d9b9b9ff', '#d9babaff', '#d8bbbbff', '#d8bcbcff', '#d8bdbdff', '#d8bebeff', '#d8bfbfff', '#d7bfbfff', '#d7c0c0ff', '#d7c1c1ff', '#d7c2c2ff', '#d7c3c3ff', '#d7c4c4ff', '#d6c4c4ff', '#d6c5c5ff', '#d6c6c6ff', '#d6c7c7ff', '#d6c8c8ff', '#d6c9c9ff', '#d5cacaff', '#d5cacaff', '#d5cbcbff', '#d5ccccff', '#d5cdcdff', '#d4ceceff', '#d4cfcfff', '#d4d0d0ff', '#d4d0d0ff', '#d4d1d1ff', '#d4d2d2ff', '#d3d3d3ff', '#d3d3d3ff', '#d2d2d4ff', '#d1d1d4ff', '#d0d0d4ff', '#d0d0d4ff', '#cfcfd4ff', '#ceced4ff', '#cdcdd5ff', '#ccccd5ff', '#cbcbd5ff', '#cacad5ff', '#cacad5ff', '#c9c9d6ff', '#c8c8d6ff', '#c7c7d6ff', '#c6c6d6ff', '#c5c5d6ff', '#c4c4d6ff', '#c4c4d7ff', '#c3c3d7ff', '#c2c2d7ff', '#c1c1d7ff', '#c0c0d7ff', '#bfbfd7ff', '#bfbfd8ff', '#bebed8ff', '#bdbdd8ff', '#bcbcd8ff', '#bbbbd8ff', '#babad9ff', '#b9b9d9ff', '#b9b9d9ff', '#b8b8d9ff', '#b7b7d9ff', '#b6b6d9ff', '#b5b5daff', '#b4b4daff', '#b3b3daff', '#b3b3daff', '#b2b2daff', '#b1b1daff', '#b0b0dbff', '#afafdbff', '#aeaedbff', '#aeaedbff', '#adaddbff', '#acacdcff', '#ababdcff', '#aaaadcff', '#a9a9dcff', '#a8a8dcff', '#a8a8dcff', '#a7a7ddff', '#a6a6ddff', '#a5a5ddff', '#a4a4ddff', '#a3a3ddff', '#a3a3deff', '#a2a2deff', '#a1a1deff', '#a0a0deff', '#9f9fdeff', '#9e9edeff', '#9d9ddfff', '#9d9ddfff', '#9c9cdfff', '#9b9bdfff', '#9a9adfff', '#9999dfff', '#9898e0ff', '#9797e0ff', '#9797e0ff', '#9696e0ff', '#9595e0ff', '#9494e1ff', '#9393e1ff', '#9292e1ff', '#9292e1ff', '#9191e1ff', '#9090e1ff', '#8f8fe2ff', '#8e8ee2ff', '#8d8de2ff', '#8c8ce2ff', '#8c8ce2ff', '#8b8be2ff', '#8a8ae3ff', '#8989e3ff', '#8888e3ff', '#8787e3ff', '#8686e3ff', '#8686e4ff', '#8585e4ff', '#8484e4ff', '#8383e4ff', '#8282e4ff', '#8181e4ff', '#8181e5ff', '#8080e5ff', '#7f7fe5ff', '#7e7ee5ff', '#7d7de5ff', '#7c7ce5ff', '#7b7be6ff', '#7b7be6ff', '#7a7ae6ff', '#7979e6ff', '#7878e6ff', '#7777e7ff', '#7676e7ff', '#7676e7ff', '#7575e7ff', '#7474e7ff', '#7373e7ff', '#7272e8ff', '#7171e8ff', '#7070e8ff', '#7070e8ff', '#6f6fe8ff', '#6e6ee8ff', '#6d6de9ff', '#6c6ce9ff', '#6b6be9ff', '#6a6ae9ff', '#6a6ae9ff', '#6969eaff', '#6868eaff', '#6767eaff', '#6666eaff', '#6565eaff', '#6565eaff', '#6464ebff', '#6363ebff', '#6262ebff', '#6161ebff', '#6060ebff', '#5f5febff', '#5f5fecff', '#5e5eecff', '#5d5decff', '#5c5cecff', '#5b5becff', '#5a5aedff', '#5959edff', '#5959edff', '#5858edff', '#5757edff', '#5656edff', '#5555eeff', '#5454eeff', '#5454eeff', '#5353eeff', '#5252eeff', '#5151efff', '#5050efff', '#4f4fefff', '#4e4eefff', '#4e4eefff', '#4d4defff', '#4c4cf0ff', '#4b4bf0ff', '#4a4af0ff', '#4949f0ff', '#4949f0ff', '#4848f0ff', '#4747f1ff', '#4646f1ff', '#4545f1ff', '#4444f1ff', '#4343f1ff', '#4343f2ff', '#4242f2ff', '#4141f2ff', '#4040f2ff', '#3f3ff2ff', '#3e3ef2ff', '#3d3df3ff', '#3d3df3ff', '#3c3cf3ff', '#3b3bf3ff', '#3a3af3ff', '#3939f3ff', '#3838f4ff', '#3838f4ff', '#3737f4ff', '#3636f4ff', '#3535f4ff', '#3434f5ff', '#3333f5ff', '#3232f5ff', '#3232f5ff', '#3131f5ff', '#3030f5ff', '#2f2ff6ff', '#2e2ef6ff', '#2d2df6ff', '#2c2cf6ff', '#2c2cf6ff', '#2b2bf6ff', '#2a2af7ff', '#2929f7ff', '#2828f7ff', '#2727f7ff', '#2727f7ff', '#2626f8ff', '#2525f8ff', '#2424f8ff', '#2323f8ff', '#2222f8ff', '#2121f8ff', '#2121f9ff', '#2020f9ff', '#1f1ff9ff', '#1e1ef9ff', '#1d1df9ff', '#1c1cf9ff', '#1c1cfaff', '#1b1bfaff', '#1a1afaff', '#1919faff', '#1818faff', '#1717fbff', '#1616fbff', '#1616fbff', '#1515fbff', '#1414fbff', '#1313fbff', '#1212fcff', '#1111fcff', '#1010fcff', '#1010fcff', '#0f0ffcff', '#0e0efcff', '#0d0dfdff', '#0c0cfdff', '#0b0bfdff', '#0b0bfdff', '#0a0afdff', '#0909feff', '#0808feff', '#0707feff', '#0606feff', '#0505feff', '#0505feff', '#0404ffff', '#0303ffff', '#0202ffff', '#0101ffff', '#0000ffff', '#0000ffff']);
    

    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.x = d3.scale.linear()
              .domain([-5.0, 5.0])
              .range([0, 450 - 50]);

    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.legend = L.control({position: 'topright'});
    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.legend.onAdd = function (map) {var div = L.DomUtil.create('div', 'legend'); return div};
    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.legend.addTo(map_1c26a2450131341257ad30f4f0561955);

    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.xAxis = d3.svg.axis()
        .scale(color_map_d44ee3e6147b285a468bf2f2d9f4c92d.x)
        .orient("top")
        .tickSize(1)
        .tickValues([-5.0, 0.0, 5.0]);

    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.svg = d3.select(".legend.leaflet-control").append("svg")
        .attr("id", 'legend')
        .attr("width", 450)
        .attr("height", 40);

    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.g = color_map_d44ee3e6147b285a468bf2f2d9f4c92d.svg.append("g")
        .attr("class", "key")
        .attr("fill", "black")
        .attr("transform", "translate(25,16)");

    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.g.selectAll("rect")
        .data(color_map_d44ee3e6147b285a468bf2f2d9f4c92d.color.range().map(function(d, i) {
          return {
            x0: i ? color_map_d44ee3e6147b285a468bf2f2d9f4c92d.x(color_map_d44ee3e6147b285a468bf2f2d9f4c92d.color.domain()[i - 1]) : color_map_d44ee3e6147b285a468bf2f2d9f4c92d.x.range()[0],
            x1: i < color_map_d44ee3e6147b285a468bf2f2d9f4c92d.color.domain().length ? color_map_d44ee3e6147b285a468bf2f2d9f4c92d.x(color_map_d44ee3e6147b285a468bf2f2d9f4c92d.color.domain()[i]) : color_map_d44ee3e6147b285a468bf2f2d9f4c92d.x.range()[1],
            z: d
          };
        }))
      .enter().append("rect")
        .attr("height", 40 - 30)
        .attr("x", function(d) { return d.x0; })
        .attr("width", function(d) { return d.x1 - d.x0; })
        .style("fill", function(d) { return d.z; });

    color_map_d44ee3e6147b285a468bf2f2d9f4c92d.g.call(color_map_d44ee3e6147b285a468bf2f2d9f4c92d.xAxis).append("text")
        .attr("class", "caption")
        .attr("y", 21)
        .attr("fill", "black")
        .text("sun Impact 2020-07-02_15_pred_diff_sun_day");
    
            var circle_marker_b679dd975e240ae560c13a4d112d869d = L.circleMarker(
                [41.3979779, 2.1801069],
                {"bubblingMouseEvents": true, "color": "#6b6be9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6b6be9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b28850cc0ec0b164b4df42c7d4507a66 = L.popup({"maxWidth": "100%"});

        
            
                var html_619951370a9c065563d275bc05566e39 = $(`<div id="html_619951370a9c065563d275bc05566e39" style="width: 100.0%; height: 100.0%;">Station 1<br>Result: 2.5%<br></div>`)[0];
                popup_b28850cc0ec0b164b4df42c7d4507a66.setContent(html_619951370a9c065563d275bc05566e39);
            
        

        circle_marker_b679dd975e240ae560c13a4d112d869d.bindPopup(popup_b28850cc0ec0b164b4df42c7d4507a66)
        ;

        
    
    
            var circle_marker_29ea23c8306559b5c30cd13b1fd3b0fa = L.circleMarker(
                [41.3954877, 2.1771985],
                {"bubblingMouseEvents": true, "color": "#0000ffff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#0000ffff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e2ea1c3ea374880a97aabb6db1318593 = L.popup({"maxWidth": "100%"});

        
            
                var html_889a67f0454292ffd25bb9a4da89a1b5 = $(`<div id="html_889a67f0454292ffd25bb9a4da89a1b5" style="width: 100.0%; height: 100.0%;">Station 2<br>Result: 5.1%<br></div>`)[0];
                popup_e2ea1c3ea374880a97aabb6db1318593.setContent(html_889a67f0454292ffd25bb9a4da89a1b5);
            
        

        circle_marker_29ea23c8306559b5c30cd13b1fd3b0fa.bindPopup(popup_e2ea1c3ea374880a97aabb6db1318593)
        ;

        
    
    
            var circle_marker_ea120202dfd5a9eb23cd848670d15cb0 = L.circleMarker(
                [41.3941557, 2.1813305],
                {"bubblingMouseEvents": true, "color": "#7777e7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7777e7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_37fff2eb8059428f2c6b29636894647d = L.popup({"maxWidth": "100%"});

        
            
                var html_e116e0a6bbe5fb0281399effda8d6e80 = $(`<div id="html_e116e0a6bbe5fb0281399effda8d6e80" style="width: 100.0%; height: 100.0%;">Station 3<br>Result: 2.2%<br></div>`)[0];
                popup_37fff2eb8059428f2c6b29636894647d.setContent(html_e116e0a6bbe5fb0281399effda8d6e80);
            
        

        circle_marker_ea120202dfd5a9eb23cd848670d15cb0.bindPopup(popup_37fff2eb8059428f2c6b29636894647d)
        ;

        
    
    
            var circle_marker_f4bd1c9edb9b6ed420457ea75f801aef = L.circleMarker(
                [41.3933173, 2.1812483],
                {"bubblingMouseEvents": true, "color": "#7272e8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7272e8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_39de40a0abfdf80c387149e1740f8407 = L.popup({"maxWidth": "100%"});

        
            
                var html_0c069600b793f2246beb1c4a5c23e817 = $(`<div id="html_0c069600b793f2246beb1c4a5c23e817" style="width: 100.0%; height: 100.0%;">Station 4<br>Result: 2.3%<br></div>`)[0];
                popup_39de40a0abfdf80c387149e1740f8407.setContent(html_0c069600b793f2246beb1c4a5c23e817);
            
        

        circle_marker_f4bd1c9edb9b6ed420457ea75f801aef.bindPopup(popup_39de40a0abfdf80c387149e1740f8407)
        ;

        
    
    
            var circle_marker_f91cdcc622ae0654a72eb00a9960976f = L.circleMarker(
                [41.3911035, 2.1801763],
                {"bubblingMouseEvents": true, "color": "#d8bfbfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d8bfbfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_058deda4edd05147692e8c9c99a99dd6 = L.popup({"maxWidth": "100%"});

        
            
                var html_413b87e3d87dd1d188a9f03201bc0d5b = $(`<div id="html_413b87e3d87dd1d188a9f03201bc0d5b" style="width: 100.0%; height: 100.0%;">Station 5<br>Result: -0.5%<br></div>`)[0];
                popup_058deda4edd05147692e8c9c99a99dd6.setContent(html_413b87e3d87dd1d188a9f03201bc0d5b);
            
        

        circle_marker_f91cdcc622ae0654a72eb00a9960976f.bindPopup(popup_058deda4edd05147692e8c9c99a99dd6)
        ;

        
    
    
            var circle_marker_b81a824cf611f71c9ef08b76fef8d9ba = L.circleMarker(
                [41.3914292, 2.1805685],
                {"bubblingMouseEvents": true, "color": "#b7b7d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b7b7d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_678959bee62f27773620e3b5b7579e11 = L.popup({"maxWidth": "100%"});

        
            
                var html_685b2cc33e5f43d5971683652a9ca331 = $(`<div id="html_685b2cc33e5f43d5971683652a9ca331" style="width: 100.0%; height: 100.0%;">Station 6<br>Result: 0.7%<br></div>`)[0];
                popup_678959bee62f27773620e3b5b7579e11.setContent(html_685b2cc33e5f43d5971683652a9ca331);
            
        

        circle_marker_b81a824cf611f71c9ef08b76fef8d9ba.bindPopup(popup_678959bee62f27773620e3b5b7579e11)
        ;

        
    
    
            var circle_marker_1398e2083ae1aef0c9279012f9e71347 = L.circleMarker(
                [41.388885, 2.18329],
                {"bubblingMouseEvents": true, "color": "#e57d7dff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e57d7dff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_941d8466fa4e540113ffa2be7441ba27 = L.popup({"maxWidth": "100%"});

        
            
                var html_2591dafaf455627ac45e6b9090ac659c = $(`<div id="html_2591dafaf455627ac45e6b9090ac659c" style="width: 100.0%; height: 100.0%;">Station 7<br>Result: -2.0%<br></div>`)[0];
                popup_941d8466fa4e540113ffa2be7441ba27.setContent(html_2591dafaf455627ac45e6b9090ac659c);
            
        

        circle_marker_1398e2083ae1aef0c9279012f9e71347.bindPopup(popup_941d8466fa4e540113ffa2be7441ba27)
        ;

        
    
    
            var circle_marker_af1548f9b567f49957077a1e4896cdcc = L.circleMarker(
                [41.389135, 2.183489],
                {"bubblingMouseEvents": true, "color": "#e28d8dff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e28d8dff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8594ccca2ab3cf9c98a492b823347018 = L.popup({"maxWidth": "100%"});

        
            
                var html_73783d714ad47cfecf7cb8e0ac9c2327 = $(`<div id="html_73783d714ad47cfecf7cb8e0ac9c2327" style="width: 100.0%; height: 100.0%;">Station 8<br>Result: -1.7%<br></div>`)[0];
                popup_8594ccca2ab3cf9c98a492b823347018.setContent(html_73783d714ad47cfecf7cb8e0ac9c2327);
            
        

        circle_marker_af1548f9b567f49957077a1e4896cdcc.bindPopup(popup_8594ccca2ab3cf9c98a492b823347018)
        ;

        
    
    
            var circle_marker_8954c917ca64ae82a68baf3c7a447f19 = L.circleMarker(
                [41.384546, 2.184922],
                {"bubblingMouseEvents": true, "color": "#ccccd5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ccccd5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_bca578fd186e7d20b0793c4450335c9c = L.popup({"maxWidth": "100%"});

        
            
                var html_2128d2282b40c9d0faf1fc398ee1fe65 = $(`<div id="html_2128d2282b40c9d0faf1fc398ee1fe65" style="width: 100.0%; height: 100.0%;">Station 9<br>Result: 0.2%<br></div>`)[0];
                popup_bca578fd186e7d20b0793c4450335c9c.setContent(html_2128d2282b40c9d0faf1fc398ee1fe65);
            
        

        circle_marker_8954c917ca64ae82a68baf3c7a447f19.bindPopup(popup_bca578fd186e7d20b0793c4450335c9c)
        ;

        
    
    
            var circle_marker_79dd9400ca68d7f60e8454fa338fe960 = L.circleMarker(
                [41.382398, 2.194294],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_051dcef71cfd3a7c6aaf3e9d31ff53a5 = L.popup({"maxWidth": "100%"});

        
            
                var html_35ff92bdc8e442a8f12a283cadc94098 = $(`<div id="html_35ff92bdc8e442a8f12a283cadc94098" style="width: 100.0%; height: 100.0%;">Station 11<br>Result: -6.3%<br></div>`)[0];
                popup_051dcef71cfd3a7c6aaf3e9d31ff53a5.setContent(html_35ff92bdc8e442a8f12a283cadc94098);
            
        

        circle_marker_79dd9400ca68d7f60e8454fa338fe960.bindPopup(popup_051dcef71cfd3a7c6aaf3e9d31ff53a5)
        ;

        
    
    
            var circle_marker_52535c27f61501bc5f7008568cdfa616 = L.circleMarker(
                [41.3833653, 2.1946255],
                {"bubblingMouseEvents": true, "color": "#fe0606ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#fe0606ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f99fd8e182d1febeb363df711d0e9e27 = L.popup({"maxWidth": "100%"});

        
            
                var html_a67857ef51130c08cce6b542c8a561fb = $(`<div id="html_a67857ef51130c08cce6b542c8a561fb" style="width: 100.0%; height: 100.0%;">Station 12<br>Result: -4.8%<br></div>`)[0];
                popup_f99fd8e182d1febeb363df711d0e9e27.setContent(html_a67857ef51130c08cce6b542c8a561fb);
            
        

        circle_marker_52535c27f61501bc5f7008568cdfa616.bindPopup(popup_f99fd8e182d1febeb363df711d0e9e27)
        ;

        
    
    
            var circle_marker_b095e9d654fb57e5c37abfe63b375628 = L.circleMarker(
                [41.388143, 2.195551],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6667b2762273543b720b85d0a8ad3872 = L.popup({"maxWidth": "100%"});

        
            
                var html_38e302f53f66cff903a0e4a56d659fd9 = $(`<div id="html_38e302f53f66cff903a0e4a56d659fd9" style="width: 100.0%; height: 100.0%;">Station 13<br>Result: -5.6%<br></div>`)[0];
                popup_6667b2762273543b720b85d0a8ad3872.setContent(html_38e302f53f66cff903a0e4a56d659fd9);
            
        

        circle_marker_b095e9d654fb57e5c37abfe63b375628.bindPopup(popup_6667b2762273543b720b85d0a8ad3872)
        ;

        
    
    
            var circle_marker_18b6b022cee9e0c7e24fbf6062d0c2c7 = L.circleMarker(
                [41.384844, 2.185085],
                {"bubblingMouseEvents": true, "color": "#e09595ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e09595ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_747fdd7da4743e272b822734175178a7 = L.popup({"maxWidth": "100%"});

        
            
                var html_64bc08a37492af08519556b9547dc323 = $(`<div id="html_64bc08a37492af08519556b9547dc323" style="width: 100.0%; height: 100.0%;">Station 14<br>Result: -1.5%<br></div>`)[0];
                popup_747fdd7da4743e272b822734175178a7.setContent(html_64bc08a37492af08519556b9547dc323);
            
        

        circle_marker_18b6b022cee9e0c7e24fbf6062d0c2c7.bindPopup(popup_747fdd7da4743e272b822734175178a7)
        ;

        
    
    
            var circle_marker_eea41d30b7f7703d36b894212313565f = L.circleMarker(
                [41.39161170092347, 2.1689031978751205],
                {"bubblingMouseEvents": true, "color": "#9e9edeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9e9edeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d3c5018136a6eb80529ba71aee216f9a = L.popup({"maxWidth": "100%"});

        
            
                var html_119293025a92d96703e1a7d2605c50ad = $(`<div id="html_119293025a92d96703e1a7d2605c50ad" style="width: 100.0%; height: 100.0%;">Station 15<br>Result: 1.3%<br></div>`)[0];
                popup_d3c5018136a6eb80529ba71aee216f9a.setContent(html_119293025a92d96703e1a7d2605c50ad);
            
        

        circle_marker_eea41d30b7f7703d36b894212313565f.bindPopup(popup_d3c5018136a6eb80529ba71aee216f9a)
        ;

        
    
    
            var circle_marker_f422270a6357d22989badedb44a193a5 = L.circleMarker(
                [41.3982615, 2.1866517],
                {"bubblingMouseEvents": true, "color": "#7373e8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7373e8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4e0d165641d5e74f36047f363eaf1939 = L.popup({"maxWidth": "100%"});

        
            
                var html_1edb012ea6ac812414434d328908fa47 = $(`<div id="html_1edb012ea6ac812414434d328908fa47" style="width: 100.0%; height: 100.0%;">Station 17<br>Result: 2.3%<br></div>`)[0];
                popup_4e0d165641d5e74f36047f363eaf1939.setContent(html_1edb012ea6ac812414434d328908fa47);
            
        

        circle_marker_f422270a6357d22989badedb44a193a5.bindPopup(popup_4e0d165641d5e74f36047f363eaf1939)
        ;

        
    
    
            var circle_marker_276a33e1a06fb9414749750dcebc915e = L.circleMarker(
                [41.4060589, 2.1740472],
                {"bubblingMouseEvents": true, "color": "#a6a6ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a6a6ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7c074a7a531873fd53994a137369ec13 = L.popup({"maxWidth": "100%"});

        
            
                var html_df7fb261bd9b92e09de7e23d64caf651 = $(`<div id="html_df7fb261bd9b92e09de7e23d64caf651" style="width: 100.0%; height: 100.0%;">Station 18<br>Result: 1.1%<br></div>`)[0];
                popup_7c074a7a531873fd53994a137369ec13.setContent(html_df7fb261bd9b92e09de7e23d64caf651);
            
        

        circle_marker_276a33e1a06fb9414749750dcebc915e.bindPopup(popup_7c074a7a531873fd53994a137369ec13)
        ;

        
    
    
            var circle_marker_1bd2b0689d670b4d762ede06b035ff47 = L.circleMarker(
                [41.4031491, 2.1707947],
                {"bubblingMouseEvents": true, "color": "#b4b4daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b4b4daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_36cb81cfc0dace6efdbbe3dc7f89e70a = L.popup({"maxWidth": "100%"});

        
            
                var html_90d2e47fb5e709f251cd8cc41f36a604 = $(`<div id="html_90d2e47fb5e709f251cd8cc41f36a604" style="width: 100.0%; height: 100.0%;">Station 19<br>Result: 0.7%<br></div>`)[0];
                popup_36cb81cfc0dace6efdbbe3dc7f89e70a.setContent(html_90d2e47fb5e709f251cd8cc41f36a604);
            
        

        circle_marker_1bd2b0689d670b4d762ede06b035ff47.bindPopup(popup_36cb81cfc0dace6efdbbe3dc7f89e70a)
        ;

        
    
    
            var circle_marker_2aa291a8b453c11727005e955236a4a0 = L.circleMarker(
                [41.410314, 2.1757334],
                {"bubblingMouseEvents": true, "color": "#7979e6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7979e6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0e8e75f9d6e71472a1a4b8638563b9bb = L.popup({"maxWidth": "100%"});

        
            
                var html_ce04879efdb9e311a470647aeec32b3f = $(`<div id="html_ce04879efdb9e311a470647aeec32b3f" style="width: 100.0%; height: 100.0%;">Station 20<br>Result: 2.1%<br></div>`)[0];
                popup_0e8e75f9d6e71472a1a4b8638563b9bb.setContent(html_ce04879efdb9e311a470647aeec32b3f);
            
        

        circle_marker_2aa291a8b453c11727005e955236a4a0.bindPopup(popup_0e8e75f9d6e71472a1a4b8638563b9bb)
        ;

        
    
    
            var circle_marker_a187bc5a04089d5e9132587e4cb7495d = L.circleMarker(
                [41.4108439, 2.1740575],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7193119683d2665e46234e1564fcdd36 = L.popup({"maxWidth": "100%"});

        
            
                var html_fe36a07e0fd8bd54fc51f0ad8ef05df3 = $(`<div id="html_fe36a07e0fd8bd54fc51f0ad8ef05df3" style="width: 100.0%; height: 100.0%;">Station 21<br>Result: 0.9%<br></div>`)[0];
                popup_7193119683d2665e46234e1564fcdd36.setContent(html_fe36a07e0fd8bd54fc51f0ad8ef05df3);
            
        

        circle_marker_a187bc5a04089d5e9132587e4cb7495d.bindPopup(popup_7193119683d2665e46234e1564fcdd36)
        ;

        
    
    
            var circle_marker_19e9bbdbe6d47bc71dbdd94693774266 = L.circleMarker(
                [41.4016969, 2.175767],
                {"bubblingMouseEvents": true, "color": "#5b5becff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5b5becff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_78d0161f09b27e5929f3de195dd78718 = L.popup({"maxWidth": "100%"});

        
            
                var html_130a8c6ac8e1568cd1e510037a9fb404 = $(`<div id="html_130a8c6ac8e1568cd1e510037a9fb404" style="width: 100.0%; height: 100.0%;">Station 22<br>Result: 2.8%<br></div>`)[0];
                popup_78d0161f09b27e5929f3de195dd78718.setContent(html_130a8c6ac8e1568cd1e510037a9fb404);
            
        

        circle_marker_19e9bbdbe6d47bc71dbdd94693774266.bindPopup(popup_78d0161f09b27e5929f3de195dd78718)
        ;

        
    
    
            var circle_marker_336f7116524b61eab504534cb4437998 = L.circleMarker(
                [41.3924661, 2.1717397],
                {"bubblingMouseEvents": true, "color": "#d8bfbfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d8bfbfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d9d2ba2de0dd58189c2bf5ea7cafdbc0 = L.popup({"maxWidth": "100%"});

        
            
                var html_9fa723b75c4da2a9a7acef856b4e462b = $(`<div id="html_9fa723b75c4da2a9a7acef856b4e462b" style="width: 100.0%; height: 100.0%;">Station 23<br>Result: -0.5%<br></div>`)[0];
                popup_d9d2ba2de0dd58189c2bf5ea7cafdbc0.setContent(html_9fa723b75c4da2a9a7acef856b4e462b);
            
        

        circle_marker_336f7116524b61eab504534cb4437998.bindPopup(popup_d9d2ba2de0dd58189c2bf5ea7cafdbc0)
        ;

        
    
    
            var circle_marker_9b3801e33999a2be1ce90f05dc7c87f5 = L.circleMarker(
                [41.4005784, 2.1788855],
                {"bubblingMouseEvents": true, "color": "#9797e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9797e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b435148c63e5cd90cff7a7f2f8b927bd = L.popup({"maxWidth": "100%"});

        
            
                var html_35944baa119e07ae3e649d999e2e388e = $(`<div id="html_35944baa119e07ae3e649d999e2e388e" style="width: 100.0%; height: 100.0%;">Station 24<br>Result: 1.4%<br></div>`)[0];
                popup_b435148c63e5cd90cff7a7f2f8b927bd.setContent(html_35944baa119e07ae3e649d999e2e388e);
            
        

        circle_marker_9b3801e33999a2be1ce90f05dc7c87f5.bindPopup(popup_b435148c63e5cd90cff7a7f2f8b927bd)
        ;

        
    
    
            var circle_marker_6e447871e9ebbf6c6ff3086de4d282c2 = L.circleMarker(
                [41.3954041, 2.1681961],
                {"bubblingMouseEvents": true, "color": "#b9b9d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b9b9d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f350db074b5834bd60c919467ed1ddd4 = L.popup({"maxWidth": "100%"});

        
            
                var html_724cf9a7a439837533354561d8b83bfe = $(`<div id="html_724cf9a7a439837533354561d8b83bfe" style="width: 100.0%; height: 100.0%;">Station 25<br>Result: 0.6%<br></div>`)[0];
                popup_f350db074b5834bd60c919467ed1ddd4.setContent(html_724cf9a7a439837533354561d8b83bfe);
            
        

        circle_marker_6e447871e9ebbf6c6ff3086de4d282c2.bindPopup(popup_f350db074b5834bd60c919467ed1ddd4)
        ;

        
    
    
            var circle_marker_470fbf06e2117892593246bee4ee31ca = L.circleMarker(
                [41.4071692, 2.1820722],
                {"bubblingMouseEvents": true, "color": "#0000ffff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#0000ffff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_63cc83ad61dfd0667c17bd5a2ec1197f = L.popup({"maxWidth": "100%"});

        
            
                var html_62478e8602cafbae3b8f896f49dd63be = $(`<div id="html_62478e8602cafbae3b8f896f49dd63be" style="width: 100.0%; height: 100.0%;">Station 26<br>Result: 5.5%<br></div>`)[0];
                popup_63cc83ad61dfd0667c17bd5a2ec1197f.setContent(html_62478e8602cafbae3b8f896f49dd63be);
            
        

        circle_marker_470fbf06e2117892593246bee4ee31ca.bindPopup(popup_63cc83ad61dfd0667c17bd5a2ec1197f)
        ;

        
    
    
            var circle_marker_c3a70fd89d1e05a699d4f6ccf240584f = L.circleMarker(
                [41.3967524, 2.1646338],
                {"bubblingMouseEvents": true, "color": "#9191e1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9191e1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_91988c594ea7629a803df69402664222 = L.popup({"maxWidth": "100%"});

        
            
                var html_ab7bc8877ca85e39f3b93c53384975c6 = $(`<div id="html_ab7bc8877ca85e39f3b93c53384975c6" style="width: 100.0%; height: 100.0%;">Station 27<br>Result: 1.6%<br></div>`)[0];
                popup_91988c594ea7629a803df69402664222.setContent(html_ab7bc8877ca85e39f3b93c53384975c6);
            
        

        circle_marker_c3a70fd89d1e05a699d4f6ccf240584f.bindPopup(popup_91988c594ea7629a803df69402664222)
        ;

        
    
    
            var circle_marker_accee4f1a3a5c969563fff805e535cd5 = L.circleMarker(
                [41.4055143, 2.1706498],
                {"bubblingMouseEvents": true, "color": "#adaddbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#adaddbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8faaaf0cfbedea0c09843d320f95f425 = L.popup({"maxWidth": "100%"});

        
            
                var html_090c393d8189b4a24fc01527460f9baf = $(`<div id="html_090c393d8189b4a24fc01527460f9baf" style="width: 100.0%; height: 100.0%;">Station 28<br>Result: 0.9%<br></div>`)[0];
                popup_8faaaf0cfbedea0c09843d320f95f425.setContent(html_090c393d8189b4a24fc01527460f9baf);
            
        

        circle_marker_accee4f1a3a5c969563fff805e535cd5.bindPopup(popup_8faaaf0cfbedea0c09843d320f95f425)
        ;

        
    
    
            var circle_marker_f02c695e8da4eccc22d67d72d619ea58 = L.circleMarker(
                [41.401061, 2.169941],
                {"bubblingMouseEvents": true, "color": "#7b7be6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7b7be6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_fce3db6fece20f3c8a7ddbe1ca825107 = L.popup({"maxWidth": "100%"});

        
            
                var html_d10c68fd34429a2a5034fe6a3f083d27 = $(`<div id="html_d10c68fd34429a2a5034fe6a3f083d27" style="width: 100.0%; height: 100.0%;">Station 29<br>Result: 2.1%<br></div>`)[0];
                popup_fce3db6fece20f3c8a7ddbe1ca825107.setContent(html_d10c68fd34429a2a5034fe6a3f083d27);
            
        

        circle_marker_f02c695e8da4eccc22d67d72d619ea58.bindPopup(popup_fce3db6fece20f3c8a7ddbe1ca825107)
        ;

        
    
    
            var circle_marker_4a70ad7558551575590b2d3099d2cc35 = L.circleMarker(
                [41.4021805, 2.1829894],
                {"bubblingMouseEvents": true, "color": "#6565eaff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6565eaff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_af3af0bc3f96318333cb8d63a2da7ac7 = L.popup({"maxWidth": "100%"});

        
            
                var html_fd5441f5c2f5e323cf744e350585b2ae = $(`<div id="html_fd5441f5c2f5e323cf744e350585b2ae" style="width: 100.0%; height: 100.0%;">Station 30<br>Result: 2.6%<br></div>`)[0];
                popup_af3af0bc3f96318333cb8d63a2da7ac7.setContent(html_fd5441f5c2f5e323cf744e350585b2ae);
            
        

        circle_marker_4a70ad7558551575590b2d3099d2cc35.bindPopup(popup_af3af0bc3f96318333cb8d63a2da7ac7)
        ;

        
    
    
            var circle_marker_dd7ceef2188452b94d2cbedf166f27ef = L.circleMarker(
                [41.3748001, 2.1889045],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d179a1561815a70ddb11dcf8c5bfe904 = L.popup({"maxWidth": "100%"});

        
            
                var html_a9beae192a87409e4b87250b8a65f5d7 = $(`<div id="html_a9beae192a87409e4b87250b8a65f5d7" style="width: 100.0%; height: 100.0%;">Station 31<br>Result: -6.3%<br></div>`)[0];
                popup_d179a1561815a70ddb11dcf8c5bfe904.setContent(html_a9beae192a87409e4b87250b8a65f5d7);
            
        

        circle_marker_dd7ceef2188452b94d2cbedf166f27ef.bindPopup(popup_d179a1561815a70ddb11dcf8c5bfe904)
        ;

        
    
    
            var circle_marker_132e3c85ea433e0ef9f77aa1d4ec83ef = L.circleMarker(
                [41.3871079, 2.1753364],
                {"bubblingMouseEvents": true, "color": "#dab3b3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dab3b3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6ef762fd1065ad89cd3bf77d833e2200 = L.popup({"maxWidth": "100%"});

        
            
                var html_795d8e7ef8200a69efeced67554567db = $(`<div id="html_795d8e7ef8200a69efeced67554567db" style="width: 100.0%; height: 100.0%;">Station 34<br>Result: -0.8%<br></div>`)[0];
                popup_6ef762fd1065ad89cd3bf77d833e2200.setContent(html_795d8e7ef8200a69efeced67554567db);
            
        

        circle_marker_132e3c85ea433e0ef9f77aa1d4ec83ef.bindPopup(popup_6ef762fd1065ad89cd3bf77d833e2200)
        ;

        
    
    
            var circle_marker_b7baa0e2292246ecde28c1596eb18734 = L.circleMarker(
                [41.4134833, 2.2206913],
                {"bubblingMouseEvents": true, "color": "#df9b9bff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#df9b9bff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_49819ae99262fb4fd0d13b8b735a0084 = L.popup({"maxWidth": "100%"});

        
            
                var html_89f3479222912cb0134c667de4a95e8d = $(`<div id="html_89f3479222912cb0134c667de4a95e8d" style="width: 100.0%; height: 100.0%;">Station 35<br>Result: -1.3%<br></div>`)[0];
                popup_49819ae99262fb4fd0d13b8b735a0084.setContent(html_89f3479222912cb0134c667de4a95e8d);
            
        

        circle_marker_b7baa0e2292246ecde28c1596eb18734.bindPopup(popup_49819ae99262fb4fd0d13b8b735a0084)
        ;

        
    
    
            var circle_marker_304e6a1d2ef5fadcfe9540332b93eb05 = L.circleMarker(
                [41.3850616, 2.1766834],
                {"bubblingMouseEvents": true, "color": "#6363ebff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6363ebff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_3d255140ac671ae16d7fc4c1d8c94d12 = L.popup({"maxWidth": "100%"});

        
            
                var html_b753be38ecae4138a2b6283d229a9f77 = $(`<div id="html_b753be38ecae4138a2b6283d229a9f77" style="width: 100.0%; height: 100.0%;">Station 36<br>Result: 2.7%<br></div>`)[0];
                popup_3d255140ac671ae16d7fc4c1d8c94d12.setContent(html_b753be38ecae4138a2b6283d229a9f77);
            
        

        circle_marker_304e6a1d2ef5fadcfe9540332b93eb05.bindPopup(popup_3d255140ac671ae16d7fc4c1d8c94d12)
        ;

        
    
    
            var circle_marker_1458908d0d1ef8699549d7e2a4c0b172 = L.circleMarker(
                [41.381046, 2.186576],
                {"bubblingMouseEvents": true, "color": "#fd0c0cff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#fd0c0cff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6235f76b986d48089debd9da4959787a = L.popup({"maxWidth": "100%"});

        
            
                var html_cea7d8cecd8ab9a65ac61b37db43ba10 = $(`<div id="html_cea7d8cecd8ab9a65ac61b37db43ba10" style="width: 100.0%; height: 100.0%;">Station 39<br>Result: -4.7%<br></div>`)[0];
                popup_6235f76b986d48089debd9da4959787a.setContent(html_cea7d8cecd8ab9a65ac61b37db43ba10);
            
        

        circle_marker_1458908d0d1ef8699549d7e2a4c0b172.bindPopup(popup_6235f76b986d48089debd9da4959787a)
        ;

        
    
    
            var circle_marker_cda82aae68563271a1ae14d5401c580f = L.circleMarker(
                [41.382335, 2.187093],
                {"bubblingMouseEvents": true, "color": "#eb6060ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#eb6060ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_511ce9e2d4b4f6937e0fedff9f2f0534 = L.popup({"maxWidth": "100%"});

        
            
                var html_e1e7fdcecffb08f8ad463934deb614f8 = $(`<div id="html_e1e7fdcecffb08f8ad463934deb614f8" style="width: 100.0%; height: 100.0%;">Station 40<br>Result: -2.7%<br></div>`)[0];
                popup_511ce9e2d4b4f6937e0fedff9f2f0534.setContent(html_e1e7fdcecffb08f8ad463934deb614f8);
            
        

        circle_marker_cda82aae68563271a1ae14d5401c580f.bindPopup(popup_511ce9e2d4b4f6937e0fedff9f2f0534)
        ;

        
    
    
            var circle_marker_4071745ece24d8d131eb79052b2d9000 = L.circleMarker(
                [41.379326, 2.189906],
                {"bubblingMouseEvents": true, "color": "#f23f3fff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#f23f3fff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8a5c4be07818b54482aa8922fc726754 = L.popup({"maxWidth": "100%"});

        
            
                var html_98ef58f7410d72f308ad209368802587 = $(`<div id="html_98ef58f7410d72f308ad209368802587" style="width: 100.0%; height: 100.0%;">Station 41<br>Result: -3.5%<br></div>`)[0];
                popup_8a5c4be07818b54482aa8922fc726754.setContent(html_98ef58f7410d72f308ad209368802587);
            
        

        circle_marker_4071745ece24d8d131eb79052b2d9000.bindPopup(popup_8a5c4be07818b54482aa8922fc726754)
        ;

        
    
    
            var circle_marker_f4036b4aff7c9f702970af9923c110be = L.circleMarker(
                [41.404511, 2.189881],
                {"bubblingMouseEvents": true, "color": "#bebed8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bebed8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_43c6a704418f7226348012a010485438 = L.popup({"maxWidth": "100%"});

        
            
                var html_e66e94ee8bc82ca6036ac260f4355991 = $(`<div id="html_e66e94ee8bc82ca6036ac260f4355991" style="width: 100.0%; height: 100.0%;">Station 42<br>Result: 0.5%<br></div>`)[0];
                popup_43c6a704418f7226348012a010485438.setContent(html_e66e94ee8bc82ca6036ac260f4355991);
            
        

        circle_marker_f4036b4aff7c9f702970af9923c110be.bindPopup(popup_43c6a704418f7226348012a010485438)
        ;

        
    
    
            var circle_marker_e51ba1f71c7d2dc94f0ec54339711fdf = L.circleMarker(
                [41.391466, 2.189371],
                {"bubblingMouseEvents": true, "color": "#dbaeaeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dbaeaeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0d7dab513108e20e0f24cb443f0ee4e6 = L.popup({"maxWidth": "100%"});

        
            
                var html_e27f5e5671cd426d24822788908def2c = $(`<div id="html_e27f5e5671cd426d24822788908def2c" style="width: 100.0%; height: 100.0%;">Station 45<br>Result: -0.9%<br></div>`)[0];
                popup_0d7dab513108e20e0f24cb443f0ee4e6.setContent(html_e27f5e5671cd426d24822788908def2c);
            
        

        circle_marker_e51ba1f71c7d2dc94f0ec54339711fdf.bindPopup(popup_0d7dab513108e20e0f24cb443f0ee4e6)
        ;

        
    
    
            var circle_marker_472778de8d42c7d2cab5770608aa4a40 = L.circleMarker(
                [41.38860659692564, 2.1921945084594707],
                {"bubblingMouseEvents": true, "color": "#ef5050ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ef5050ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a11d5f34e6595e236bd30a00754027d8 = L.popup({"maxWidth": "100%"});

        
            
                var html_097d51cfeceea19724f75e7010733a67 = $(`<div id="html_097d51cfeceea19724f75e7010733a67" style="width: 100.0%; height: 100.0%;">Station 46<br>Result: -3.1%<br></div>`)[0];
                popup_a11d5f34e6595e236bd30a00754027d8.setContent(html_097d51cfeceea19724f75e7010733a67);
            
        

        circle_marker_472778de8d42c7d2cab5770608aa4a40.bindPopup(popup_a11d5f34e6595e236bd30a00754027d8)
        ;

        
    
    
            var circle_marker_b3b0c5f48c6c38bdec51820ec8cf8eec = L.circleMarker(
                [41.3902194, 2.1904003],
                {"bubblingMouseEvents": true, "color": "#f53030ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#f53030ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6aa102397f178cefee2d90d9aa2b2251 = L.popup({"maxWidth": "100%"});

        
            
                var html_be026410cff9c2c6d7ddb95b86f9eef0 = $(`<div id="html_be026410cff9c2c6d7ddb95b86f9eef0" style="width: 100.0%; height: 100.0%;">Station 47<br>Result: -3.9%<br></div>`)[0];
                popup_6aa102397f178cefee2d90d9aa2b2251.setContent(html_be026410cff9c2c6d7ddb95b86f9eef0);
            
        

        circle_marker_b3b0c5f48c6c38bdec51820ec8cf8eec.bindPopup(popup_6aa102397f178cefee2d90d9aa2b2251)
        ;

        
    
    
            var circle_marker_566bc8a9bccfb53c983405f62d18a2cf = L.circleMarker(
                [41.3960652, 2.1871959],
                {"bubblingMouseEvents": true, "color": "#b0b0dbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b0b0dbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f42f2165f6d22940bba50597f7440ea3 = L.popup({"maxWidth": "100%"});

        
            
                var html_1ad68458cdd62bb66be5441811bfe4c1 = $(`<div id="html_1ad68458cdd62bb66be5441811bfe4c1" style="width: 100.0%; height: 100.0%;">Station 48<br>Result: 0.8%<br></div>`)[0];
                popup_f42f2165f6d22940bba50597f7440ea3.setContent(html_1ad68458cdd62bb66be5441811bfe4c1);
            
        

        circle_marker_566bc8a9bccfb53c983405f62d18a2cf.bindPopup(popup_f42f2165f6d22940bba50597f7440ea3)
        ;

        
    
    
            var circle_marker_cb66e11c174c0afe21549716f2762778 = L.circleMarker(
                [41.3910756, 2.1965766],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_77c7935f6842cea884caae004a6cd792 = L.popup({"maxWidth": "100%"});

        
            
                var html_d54e0de1d9ce0df2635af10015496e1b = $(`<div id="html_d54e0de1d9ce0df2635af10015496e1b" style="width: 100.0%; height: 100.0%;">Station 49<br>Result: -6.7%<br></div>`)[0];
                popup_77c7935f6842cea884caae004a6cd792.setContent(html_d54e0de1d9ce0df2635af10015496e1b);
            
        

        circle_marker_cb66e11c174c0afe21549716f2762778.bindPopup(popup_77c7935f6842cea884caae004a6cd792)
        ;

        
    
    
            var circle_marker_f44e87a03b1ef883c53d720f0e662089 = L.circleMarker(
                [41.3751145, 2.1709386],
                {"bubblingMouseEvents": true, "color": "#ea6565ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ea6565ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_3d5c4af56d3923ef99cf22b714b4331d = L.popup({"maxWidth": "100%"});

        
            
                var html_82e4809431cce44c474a1190f824ed57 = $(`<div id="html_82e4809431cce44c474a1190f824ed57" style="width: 100.0%; height: 100.0%;">Station 50<br>Result: -2.6%<br></div>`)[0];
                popup_3d5c4af56d3923ef99cf22b714b4331d.setContent(html_82e4809431cce44c474a1190f824ed57);
            
        

        circle_marker_f44e87a03b1ef883c53d720f0e662089.bindPopup(popup_3d5c4af56d3923ef99cf22b714b4331d)
        ;

        
    
    
            var circle_marker_04ce7d6b43ebdf4f17e26b396e480e41 = L.circleMarker(
                [41.3842634, 2.1692556],
                {"bubblingMouseEvents": true, "color": "#df9c9cff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#df9c9cff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_670358d1d88f113bf11dcabeddf566c8 = L.popup({"maxWidth": "100%"});

        
            
                var html_c31b236fc6477dabc88f933fd5fc7a13 = $(`<div id="html_c31b236fc6477dabc88f933fd5fc7a13" style="width: 100.0%; height: 100.0%;">Station 51<br>Result: -1.3%<br></div>`)[0];
                popup_670358d1d88f113bf11dcabeddf566c8.setContent(html_c31b236fc6477dabc88f933fd5fc7a13);
            
        

        circle_marker_04ce7d6b43ebdf4f17e26b396e480e41.bindPopup(popup_670358d1d88f113bf11dcabeddf566c8)
        ;

        
    
    
            var circle_marker_fe71962b95770d58c6264ec4563c1ff8 = L.circleMarker(
                [41.385086, 2.174016],
                {"bubblingMouseEvents": true, "color": "#d6c6c6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c6c6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e17505d14d7e6a72b70f51a2c7f2eb8e = L.popup({"maxWidth": "100%"});

        
            
                var html_3d45aa7b7e62bae9519ae5255b1b2d50 = $(`<div id="html_3d45aa7b7e62bae9519ae5255b1b2d50" style="width: 100.0%; height: 100.0%;">Station 53<br>Result: -0.3%<br></div>`)[0];
                popup_e17505d14d7e6a72b70f51a2c7f2eb8e.setContent(html_3d45aa7b7e62bae9519ae5255b1b2d50);
            
        

        circle_marker_fe71962b95770d58c6264ec4563c1ff8.bindPopup(popup_e17505d14d7e6a72b70f51a2c7f2eb8e)
        ;

        
    
    
            var circle_marker_107609854a61e82f499a89edcc60e33e = L.circleMarker(
                [41.3775319, 2.1707321],
                {"bubblingMouseEvents": true, "color": "#0b0bfdff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#0b0bfdff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ba5d1fa3fa101bae2f3dca1f81371960 = L.popup({"maxWidth": "100%"});

        
            
                var html_cb2dd78a87ea56b2eb72f721ac489017 = $(`<div id="html_cb2dd78a87ea56b2eb72f721ac489017" style="width: 100.0%; height: 100.0%;">Station 54<br>Result: 4.7%<br></div>`)[0];
                popup_ba5d1fa3fa101bae2f3dca1f81371960.setContent(html_cb2dd78a87ea56b2eb72f721ac489017);
            
        

        circle_marker_107609854a61e82f499a89edcc60e33e.bindPopup(popup_ba5d1fa3fa101bae2f3dca1f81371960)
        ;

        
    
    
            var circle_marker_8426f5b0c158e11d5a14ffd7eba95c30 = L.circleMarker(
                [41.3770715, 2.1758261],
                {"bubblingMouseEvents": true, "color": "#9c9cdfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9c9cdfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8abe8dbd75aac007210e3ea4d9cdf41b = L.popup({"maxWidth": "100%"});

        
            
                var html_c3331a577f2269ddf6e5eaf5ff17003e = $(`<div id="html_c3331a577f2269ddf6e5eaf5ff17003e" style="width: 100.0%; height: 100.0%;">Station 56<br>Result: 1.3%<br></div>`)[0];
                popup_8abe8dbd75aac007210e3ea4d9cdf41b.setContent(html_c3331a577f2269ddf6e5eaf5ff17003e);
            
        

        circle_marker_8426f5b0c158e11d5a14ffd7eba95c30.bindPopup(popup_8abe8dbd75aac007210e3ea4d9cdf41b)
        ;

        
    
    
            var circle_marker_6f0e635048bea89ef05c700c58c60c12 = L.circleMarker(
                [41.376326, 2.176971],
                {"bubblingMouseEvents": true, "color": "#ed5a5aff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ed5a5aff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_590faa55c48a42ccad2a41b265195b84 = L.popup({"maxWidth": "100%"});

        
            
                var html_3a2549507ae2d307a8a71c12cacc3c75 = $(`<div id="html_3a2549507ae2d307a8a71c12cacc3c75" style="width: 100.0%; height: 100.0%;">Station 57<br>Result: -2.9%<br></div>`)[0];
                popup_590faa55c48a42ccad2a41b265195b84.setContent(html_3a2549507ae2d307a8a71c12cacc3c75);
            
        

        circle_marker_6f0e635048bea89ef05c700c58c60c12.bindPopup(popup_590faa55c48a42ccad2a41b265195b84)
        ;

        
    
    
            var circle_marker_9f366a122d74fbdbf0791204c323a8c8 = L.circleMarker(
                [41.38268, 2.16712],
                {"bubblingMouseEvents": true, "color": "#e28d8dff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e28d8dff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_004542756592ca167251e8c60610e2e7 = L.popup({"maxWidth": "100%"});

        
            
                var html_5624076783fd50217a6be35646d0029f = $(`<div id="html_5624076783fd50217a6be35646d0029f" style="width: 100.0%; height: 100.0%;">Station 58<br>Result: -1.7%<br></div>`)[0];
                popup_004542756592ca167251e8c60610e2e7.setContent(html_5624076783fd50217a6be35646d0029f);
            
        

        circle_marker_9f366a122d74fbdbf0791204c323a8c8.bindPopup(popup_004542756592ca167251e8c60610e2e7)
        ;

        
    
    
            var circle_marker_33d040728b28def5722d3082d6e525be = L.circleMarker(
                [41.3902625, 2.164035],
                {"bubblingMouseEvents": true, "color": "#3c3cf3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#3c3cf3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_efd5130575ae0cf9c42a7aaf59846a9f = L.popup({"maxWidth": "100%"});

        
            
                var html_86f19739646711a3e0fc1f411b0f7a1f = $(`<div id="html_86f19739646711a3e0fc1f411b0f7a1f" style="width: 100.0%; height: 100.0%;">Station 60<br>Result: 3.6%<br></div>`)[0];
                popup_efd5130575ae0cf9c42a7aaf59846a9f.setContent(html_86f19739646711a3e0fc1f411b0f7a1f);
            
        

        circle_marker_33d040728b28def5722d3082d6e525be.bindPopup(popup_efd5130575ae0cf9c42a7aaf59846a9f)
        ;

        
    
    
            var circle_marker_85565a5aad252f149a642363570f7370 = L.circleMarker(
                [41.39352, 2.166797],
                {"bubblingMouseEvents": true, "color": "#6565eaff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6565eaff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_dc0c94daf369a1cae321a6ecf2b11ff8 = L.popup({"maxWidth": "100%"});

        
            
                var html_30c215cea3747a222ced949cd93204f9 = $(`<div id="html_30c215cea3747a222ced949cd93204f9" style="width: 100.0%; height: 100.0%;">Station 61<br>Result: 2.6%<br></div>`)[0];
                popup_dc0c94daf369a1cae321a6ecf2b11ff8.setContent(html_30c215cea3747a222ced949cd93204f9);
            
        

        circle_marker_85565a5aad252f149a642363570f7370.bindPopup(popup_dc0c94daf369a1cae321a6ecf2b11ff8)
        ;

        
    
    
            var circle_marker_ae5bc13fa649dbb422e854c2df7b8799 = L.circleMarker(
                [41.387235, 2.168819],
                {"bubblingMouseEvents": true, "color": "#e48282ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e48282ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ed9d571ab0253833f660138c6aceb23a = L.popup({"maxWidth": "100%"});

        
            
                var html_15cccab0fa29447d74aa526c5f7a5e5c = $(`<div id="html_15cccab0fa29447d74aa526c5f7a5e5c" style="width: 100.0%; height: 100.0%;">Station 62<br>Result: -1.9%<br></div>`)[0];
                popup_ed9d571ab0253833f660138c6aceb23a.setContent(html_15cccab0fa29447d74aa526c5f7a5e5c);
            
        

        circle_marker_ae5bc13fa649dbb422e854c2df7b8799.bindPopup(popup_ed9d571ab0253833f660138c6aceb23a)
        ;

        
    
    
            var circle_marker_0346db9717263ac549ee8088f74d6a91 = L.circleMarker(
                [41.386543, 2.169427],
                {"bubblingMouseEvents": true, "color": "#e96b6bff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e96b6bff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6b7770f3ab06cbbef92e2fb9fe121134 = L.popup({"maxWidth": "100%"});

        
            
                var html_43550a47225f28cb5aa467393df0959b = $(`<div id="html_43550a47225f28cb5aa467393df0959b" style="width: 100.0%; height: 100.0%;">Station 63<br>Result: -2.5%<br></div>`)[0];
                popup_6b7770f3ab06cbbef92e2fb9fe121134.setContent(html_43550a47225f28cb5aa467393df0959b);
            
        

        circle_marker_0346db9717263ac549ee8088f74d6a91.bindPopup(popup_6b7770f3ab06cbbef92e2fb9fe121134)
        ;

        
    
    
            var circle_marker_bf291f3102e8e99ffce52ad0d10983bf = L.circleMarker(
                [41.387493, 2.1690686],
                {"bubblingMouseEvents": true, "color": "#e67979ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e67979ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5df329123735fb001fba927f6e008fab = L.popup({"maxWidth": "100%"});

        
            
                var html_bb647025ad87eec0c76b1d344e358a3c = $(`<div id="html_bb647025ad87eec0c76b1d344e358a3c" style="width: 100.0%; height: 100.0%;">Station 64<br>Result: -2.1%<br></div>`)[0];
                popup_5df329123735fb001fba927f6e008fab.setContent(html_bb647025ad87eec0c76b1d344e358a3c);
            
        

        circle_marker_bf291f3102e8e99ffce52ad0d10983bf.bindPopup(popup_5df329123735fb001fba927f6e008fab)
        ;

        
    
    
            var circle_marker_836d835a4c492d9ed9e48706cbc16019 = L.circleMarker(
                [41.387696, 2.1696543],
                {"bubblingMouseEvents": true, "color": "#e96c6cff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e96c6cff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0c7dd35dc7022c5d03f58db15a05b744 = L.popup({"maxWidth": "100%"});

        
            
                var html_ab1867b2b5d05d86fdcc2189a068b714 = $(`<div id="html_ab1867b2b5d05d86fdcc2189a068b714" style="width: 100.0%; height: 100.0%;">Station 65<br>Result: -2.4%<br></div>`)[0];
                popup_0c7dd35dc7022c5d03f58db15a05b744.setContent(html_ab1867b2b5d05d86fdcc2189a068b714);
            
        

        circle_marker_836d835a4c492d9ed9e48706cbc16019.bindPopup(popup_0c7dd35dc7022c5d03f58db15a05b744)
        ;

        
    
    
            var circle_marker_4cf69a652589cbab562f08cdd7146e64 = L.circleMarker(
                [41.3852864, 2.1454802],
                {"bubblingMouseEvents": true, "color": "#9f9fdeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9f9fdeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_108012343f66565492f923ba9fb2f94d = L.popup({"maxWidth": "100%"});

        
            
                var html_dd224fd5f54030e07fdbd2d39a4adf98 = $(`<div id="html_dd224fd5f54030e07fdbd2d39a4adf98" style="width: 100.0%; height: 100.0%;">Station 67<br>Result: 1.2%<br></div>`)[0];
                popup_108012343f66565492f923ba9fb2f94d.setContent(html_dd224fd5f54030e07fdbd2d39a4adf98);
            
        

        circle_marker_4cf69a652589cbab562f08cdd7146e64.bindPopup(popup_108012343f66565492f923ba9fb2f94d)
        ;

        
    
    
            var circle_marker_d5b820ed7c183e24edd3927a5d491014 = L.circleMarker(
                [41.3953894, 2.1572953],
                {"bubblingMouseEvents": true, "color": "#d5cbcbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5cbcbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b3314fd71d1df84e95cfa2c6e928400b = L.popup({"maxWidth": "100%"});

        
            
                var html_04b4f78392fc31d33a00551430862de8 = $(`<div id="html_04b4f78392fc31d33a00551430862de8" style="width: 100.0%; height: 100.0%;">Station 68<br>Result: -0.2%<br></div>`)[0];
                popup_b3314fd71d1df84e95cfa2c6e928400b.setContent(html_04b4f78392fc31d33a00551430862de8);
            
        

        circle_marker_d5b820ed7c183e24edd3927a5d491014.bindPopup(popup_b3314fd71d1df84e95cfa2c6e928400b)
        ;

        
    
    
            var circle_marker_427f7fb484ce250d5816d931ee4e0de3 = L.circleMarker(
                [41.388507, 2.195073],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_222417b1166d3bebe1b76a2aad2750e0 = L.popup({"maxWidth": "100%"});

        
            
                var html_2c6755e63b791909bc27c1cf20c26f41 = $(`<div id="html_2c6755e63b791909bc27c1cf20c26f41" style="width: 100.0%; height: 100.0%;">Station 69<br>Result: -6.4%<br></div>`)[0];
                popup_222417b1166d3bebe1b76a2aad2750e0.setContent(html_2c6755e63b791909bc27c1cf20c26f41);
            
        

        circle_marker_427f7fb484ce250d5816d931ee4e0de3.bindPopup(popup_222417b1166d3bebe1b76a2aad2750e0)
        ;

        
    
    
            var circle_marker_903f3384b80104ecd8703af639368658 = L.circleMarker(
                [41.380393, 2.1606506],
                {"bubblingMouseEvents": true, "color": "#6161ebff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6161ebff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d05f570240f0001c95c0bbd7d71fb082 = L.popup({"maxWidth": "100%"});

        
            
                var html_f109e0a6cdaf7fa1466a1e153f50d7d2 = $(`<div id="html_f109e0a6cdaf7fa1466a1e153f50d7d2" style="width: 100.0%; height: 100.0%;">Station 70<br>Result: 2.7%<br></div>`)[0];
                popup_d05f570240f0001c95c0bbd7d71fb082.setContent(html_f109e0a6cdaf7fa1466a1e153f50d7d2);
            
        

        circle_marker_903f3384b80104ecd8703af639368658.bindPopup(popup_d05f570240f0001c95c0bbd7d71fb082)
        ;

        
    
    
            var circle_marker_442e367dec8841afb2ae5fe3f146e5a5 = L.circleMarker(
                [41.3819459, 2.1629146],
                {"bubblingMouseEvents": true, "color": "#5959edff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5959edff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b603b867ae1e254c5c57521b5803dead = L.popup({"maxWidth": "100%"});

        
            
                var html_c9c62f761fd382f424e9090c9fa343d0 = $(`<div id="html_c9c62f761fd382f424e9090c9fa343d0" style="width: 100.0%; height: 100.0%;">Station 71<br>Result: 2.9%<br></div>`)[0];
                popup_b603b867ae1e254c5c57521b5803dead.setContent(html_c9c62f761fd382f424e9090c9fa343d0);
            
        

        circle_marker_442e367dec8841afb2ae5fe3f146e5a5.bindPopup(popup_b603b867ae1e254c5c57521b5803dead)
        ;

        
    
    
            var circle_marker_b890c5c68ced2e061681249d14bcfb42 = L.circleMarker(
                [41.3927771, 2.1586273],
                {"bubblingMouseEvents": true, "color": "#aeaedbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#aeaedbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0f3f61031699e6479a1122df4efa1ed7 = L.popup({"maxWidth": "100%"});

        
            
                var html_c58d37d0fd3a85db96152fb100b765ac = $(`<div id="html_c58d37d0fd3a85db96152fb100b765ac" style="width: 100.0%; height: 100.0%;">Station 72<br>Result: 0.9%<br></div>`)[0];
                popup_0f3f61031699e6479a1122df4efa1ed7.setContent(html_c58d37d0fd3a85db96152fb100b765ac);
            
        

        circle_marker_b890c5c68ced2e061681249d14bcfb42.bindPopup(popup_0f3f61031699e6479a1122df4efa1ed7)
        ;

        
    
    
            var circle_marker_99f6906cddc4029a564729bcb751ef93 = L.circleMarker(
                [41.392135, 2.1563542],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_71e30b2e40f7afa22f4a9d561fc9bb1b = L.popup({"maxWidth": "100%"});

        
            
                var html_d985ce9b3916b2f3e34b65f864100102 = $(`<div id="html_d985ce9b3916b2f3e34b65f864100102" style="width: 100.0%; height: 100.0%;">Station 73<br>Result: 0.9%<br></div>`)[0];
                popup_71e30b2e40f7afa22f4a9d561fc9bb1b.setContent(html_d985ce9b3916b2f3e34b65f864100102);
            
        

        circle_marker_99f6906cddc4029a564729bcb751ef93.bindPopup(popup_71e30b2e40f7afa22f4a9d561fc9bb1b)
        ;

        
    
    
            var circle_marker_ddfffbe0c5781fe68a5ae5655071333b = L.circleMarker(
                [41.3900085, 2.1432105],
                {"bubblingMouseEvents": true, "color": "#9f9fdeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9f9fdeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2e78ac6afac1bed8268e60c61c9a866f = L.popup({"maxWidth": "100%"});

        
            
                var html_aacc15a23f04a0ec4a15a409bb309324 = $(`<div id="html_aacc15a23f04a0ec4a15a409bb309324" style="width: 100.0%; height: 100.0%;">Station 74<br>Result: 1.2%<br></div>`)[0];
                popup_2e78ac6afac1bed8268e60c61c9a866f.setContent(html_aacc15a23f04a0ec4a15a409bb309324);
            
        

        circle_marker_ddfffbe0c5781fe68a5ae5655071333b.bindPopup(popup_2e78ac6afac1bed8268e60c61c9a866f)
        ;

        
    
    
            var circle_marker_54508b128ba984fef04625cc48da04b2 = L.circleMarker(
                [41.385004, 2.1429115],
                {"bubblingMouseEvents": true, "color": "#9797e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9797e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_85ec444b454b8f09f65653d8a0e58f00 = L.popup({"maxWidth": "100%"});

        
            
                var html_0acd00c768229ce8964b96d6ad389eed = $(`<div id="html_0acd00c768229ce8964b96d6ad389eed" style="width: 100.0%; height: 100.0%;">Station 75<br>Result: 1.4%<br></div>`)[0];
                popup_85ec444b454b8f09f65653d8a0e58f00.setContent(html_0acd00c768229ce8964b96d6ad389eed);
            
        

        circle_marker_54508b128ba984fef04625cc48da04b2.bindPopup(popup_85ec444b454b8f09f65653d8a0e58f00)
        ;

        
    
    
            var circle_marker_8f4328cd3fa19ebb78838dfb0ca4503d = L.circleMarker(
                [41.3917666, 2.1532163],
                {"bubblingMouseEvents": true, "color": "#b9b9d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b9b9d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f4a13b8071708e8604c85a1360b80cfc = L.popup({"maxWidth": "100%"});

        
            
                var html_ed7439b58eda349d02271faae605e64d = $(`<div id="html_ed7439b58eda349d02271faae605e64d" style="width: 100.0%; height: 100.0%;">Station 76<br>Result: 0.6%<br></div>`)[0];
                popup_f4a13b8071708e8604c85a1360b80cfc.setContent(html_ed7439b58eda349d02271faae605e64d);
            
        

        circle_marker_8f4328cd3fa19ebb78838dfb0ca4503d.bindPopup(popup_f4a13b8071708e8604c85a1360b80cfc)
        ;

        
    
    
            var circle_marker_c3d372170be6741aaa0767b9b823412a = L.circleMarker(
                [41.3856474, 2.1634306],
                {"bubblingMouseEvents": true, "color": "#2c2cf6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#2c2cf6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6912d0ba47c33954cc3be9b2eef307b5 = L.popup({"maxWidth": "100%"});

        
            
                var html_cbadd6fcec711845d8e7c5e60d8e88b2 = $(`<div id="html_cbadd6fcec711845d8e7c5e60d8e88b2" style="width: 100.0%; height: 100.0%;">Station 78<br>Result: 4.0%<br></div>`)[0];
                popup_6912d0ba47c33954cc3be9b2eef307b5.setContent(html_cbadd6fcec711845d8e7c5e60d8e88b2);
            
        

        circle_marker_c3d372170be6741aaa0767b9b823412a.bindPopup(popup_6912d0ba47c33954cc3be9b2eef307b5)
        ;

        
    
    
            var circle_marker_f3e1d8ad28f72f4306e9bbcc70560156 = L.circleMarker(
                [41.385503, 2.1634768],
                {"bubblingMouseEvents": true, "color": "#3333f5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#3333f5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a05cfc5e92d61d5dedd61b529fef93f5 = L.popup({"maxWidth": "100%"});

        
            
                var html_cc81f7c2154dd03ad0da61896a938877 = $(`<div id="html_cc81f7c2154dd03ad0da61896a938877" style="width: 100.0%; height: 100.0%;">Station 79<br>Result: 3.8%<br></div>`)[0];
                popup_a05cfc5e92d61d5dedd61b529fef93f5.setContent(html_cc81f7c2154dd03ad0da61896a938877);
            
        

        circle_marker_f3e1d8ad28f72f4306e9bbcc70560156.bindPopup(popup_a05cfc5e92d61d5dedd61b529fef93f5)
        ;

        
    
    
            var circle_marker_f2a12acb16985f1a60a67645804636a8 = L.circleMarker(
                [41.389668, 2.1599078],
                {"bubblingMouseEvents": true, "color": "#3a3af3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#3a3af3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2d51246fbb19885ba43f34aa365c623a = L.popup({"maxWidth": "100%"});

        
            
                var html_7a19f79f6d799a40353f212fd2fc794c = $(`<div id="html_7a19f79f6d799a40353f212fd2fc794c" style="width: 100.0%; height: 100.0%;">Station 80<br>Result: 3.6%<br></div>`)[0];
                popup_2d51246fbb19885ba43f34aa365c623a.setContent(html_7a19f79f6d799a40353f212fd2fc794c);
            
        

        circle_marker_f2a12acb16985f1a60a67645804636a8.bindPopup(popup_2d51246fbb19885ba43f34aa365c623a)
        ;

        
    
    
            var circle_marker_0aa3ca034579df7fdf6c528491f8a04f = L.circleMarker(
                [41.3790718, 2.1490553],
                {"bubblingMouseEvents": true, "color": "#4242f2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#4242f2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_553e2d58f16cefc345b1fe8a795f2235 = L.popup({"maxWidth": "100%"});

        
            
                var html_42907329547a411eb6da5708cf2ef0ca = $(`<div id="html_42907329547a411eb6da5708cf2ef0ca" style="width: 100.0%; height: 100.0%;">Station 81<br>Result: 3.4%<br></div>`)[0];
                popup_553e2d58f16cefc345b1fe8a795f2235.setContent(html_42907329547a411eb6da5708cf2ef0ca);
            
        

        circle_marker_0aa3ca034579df7fdf6c528491f8a04f.bindPopup(popup_553e2d58f16cefc345b1fe8a795f2235)
        ;

        
    
    
            var circle_marker_a177be52b0d5e0307c0c79316b8d8942 = L.circleMarker(
                [41.38031805998654, 2.154437124811396],
                {"bubblingMouseEvents": true, "color": "#8686e3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8686e3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_84e7aad7b064e7e8b4789f7c7c402414 = L.popup({"maxWidth": "100%"});

        
            
                var html_8e35282455d04f5f52d4ad80333a5089 = $(`<div id="html_8e35282455d04f5f52d4ad80333a5089" style="width: 100.0%; height: 100.0%;">Station 82<br>Result: 1.8%<br></div>`)[0];
                popup_84e7aad7b064e7e8b4789f7c7c402414.setContent(html_8e35282455d04f5f52d4ad80333a5089);
            
        

        circle_marker_a177be52b0d5e0307c0c79316b8d8942.bindPopup(popup_84e7aad7b064e7e8b4789f7c7c402414)
        ;

        
    
    
            var circle_marker_bac5e1683c2d8adb03d87635e9471fb1 = L.circleMarker(
                [41.3821658, 2.1520645],
                {"bubblingMouseEvents": true, "color": "#8282e4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8282e4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c3405b95e595f39696ea18d2e169eae0 = L.popup({"maxWidth": "100%"});

        
            
                var html_6d73698a7f7e96ff846032b7cfdc1a3e = $(`<div id="html_6d73698a7f7e96ff846032b7cfdc1a3e" style="width: 100.0%; height: 100.0%;">Station 83<br>Result: 1.9%<br></div>`)[0];
                popup_c3405b95e595f39696ea18d2e169eae0.setContent(html_6d73698a7f7e96ff846032b7cfdc1a3e);
            
        

        circle_marker_bac5e1683c2d8adb03d87635e9471fb1.bindPopup(popup_c3405b95e595f39696ea18d2e169eae0)
        ;

        
    
    
            var circle_marker_b152dd611994adaf9343bf1689607e4c = L.circleMarker(
                [41.3830299, 2.1571646],
                {"bubblingMouseEvents": true, "color": "#0000ffff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#0000ffff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7b84a6f2ea07a91a64f1c99e670f6f10 = L.popup({"maxWidth": "100%"});

        
            
                var html_7d7f553d8874e0229c629436f4bbb208 = $(`<div id="html_7d7f553d8874e0229c629436f4bbb208" style="width: 100.0%; height: 100.0%;">Station 84<br>Result: 6.8%<br></div>`)[0];
                popup_7b84a6f2ea07a91a64f1c99e670f6f10.setContent(html_7d7f553d8874e0229c629436f4bbb208);
            
        

        circle_marker_b152dd611994adaf9343bf1689607e4c.bindPopup(popup_7b84a6f2ea07a91a64f1c99e670f6f10)
        ;

        
    
    
            var circle_marker_22d2bf8cfc8491fb0105df6e6111cf33 = L.circleMarker(
                [41.3751852, 2.1592394],
                {"bubblingMouseEvents": true, "color": "#5555eeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5555eeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f888455e60c0457b8f4a8c65e048a09b = L.popup({"maxWidth": "100%"});

        
            
                var html_394a04f282b0032e9fccb321c21a7108 = $(`<div id="html_394a04f282b0032e9fccb321c21a7108" style="width: 100.0%; height: 100.0%;">Station 85<br>Result: 3.0%<br></div>`)[0];
                popup_f888455e60c0457b8f4a8c65e048a09b.setContent(html_394a04f282b0032e9fccb321c21a7108);
            
        

        circle_marker_22d2bf8cfc8491fb0105df6e6111cf33.bindPopup(popup_f888455e60c0457b8f4a8c65e048a09b)
        ;

        
    
    
            var circle_marker_d4b0336b28e06f90b5a05da22d900525 = L.circleMarker(
                [41.3755747, 2.1629349],
                {"bubblingMouseEvents": true, "color": "#7070e8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7070e8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_45484b86d9125a33be1620942e3edc8b = L.popup({"maxWidth": "100%"});

        
            
                var html_544f8ae86a8327fb8feb9a8712de496c = $(`<div id="html_544f8ae86a8327fb8feb9a8712de496c" style="width: 100.0%; height: 100.0%;">Station 86<br>Result: 2.4%<br></div>`)[0];
                popup_45484b86d9125a33be1620942e3edc8b.setContent(html_544f8ae86a8327fb8feb9a8712de496c);
            
        

        circle_marker_d4b0336b28e06f90b5a05da22d900525.bindPopup(popup_45484b86d9125a33be1620942e3edc8b)
        ;

        
    
    
            var circle_marker_9d307eea25d85fb95d3a84ab435253dd = L.circleMarker(
                [41.38322238887374, 2.147993191629656],
                {"bubblingMouseEvents": true, "color": "#8989e3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8989e3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_318c6ddc53281773a492d8c6c39bc193 = L.popup({"maxWidth": "100%"});

        
            
                var html_73aab39d334881fbca13ae9f83b11d0c = $(`<div id="html_73aab39d334881fbca13ae9f83b11d0c" style="width: 100.0%; height: 100.0%;">Station 87<br>Result: 1.8%<br></div>`)[0];
                popup_318c6ddc53281773a492d8c6c39bc193.setContent(html_73aab39d334881fbca13ae9f83b11d0c);
            
        

        circle_marker_9d307eea25d85fb95d3a84ab435253dd.bindPopup(popup_318c6ddc53281773a492d8c6c39bc193)
        ;

        
    
    
            var circle_marker_048a4ebe4edbb2e4268ef508e4517cea = L.circleMarker(
                [41.3936144, 2.1507739],
                {"bubblingMouseEvents": true, "color": "#aaaadcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#aaaadcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7b5b92edae96a333792cd774f923d700 = L.popup({"maxWidth": "100%"});

        
            
                var html_609e6ca1359e383caa690328fefe54cc = $(`<div id="html_609e6ca1359e383caa690328fefe54cc" style="width: 100.0%; height: 100.0%;">Station 88<br>Result: 1.0%<br></div>`)[0];
                popup_7b5b92edae96a333792cd774f923d700.setContent(html_609e6ca1359e383caa690328fefe54cc);
            
        

        circle_marker_048a4ebe4edbb2e4268ef508e4517cea.bindPopup(popup_7b5b92edae96a333792cd774f923d700)
        ;

        
    
    
            var circle_marker_dbccf5eb9f0ae2c344b8329e07d0d697 = L.circleMarker(
                [41.3871904, 2.149131],
                {"bubblingMouseEvents": true, "color": "#7272e8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7272e8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ad7425462f9f519360aea4fc908ba15c = L.popup({"maxWidth": "100%"});

        
            
                var html_839187890a326610161d6c14b31f9601 = $(`<div id="html_839187890a326610161d6c14b31f9601" style="width: 100.0%; height: 100.0%;">Station 89<br>Result: 2.3%<br></div>`)[0];
                popup_ad7425462f9f519360aea4fc908ba15c.setContent(html_839187890a326610161d6c14b31f9601);
            
        

        circle_marker_dbccf5eb9f0ae2c344b8329e07d0d697.bindPopup(popup_ad7425462f9f519360aea4fc908ba15c)
        ;

        
    
    
            var circle_marker_4dccfbde2da44b7bb4dc5a76fd5767d5 = L.circleMarker(
                [41.388296, 2.150878],
                {"bubblingMouseEvents": true, "color": "#bcbcd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bcbcd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_258aef10c8ee005b88ffbf2e795b3c9f = L.popup({"maxWidth": "100%"});

        
            
                var html_035d99480af6222808614a7037a9864d = $(`<div id="html_035d99480af6222808614a7037a9864d" style="width: 100.0%; height: 100.0%;">Station 90<br>Result: 0.5%<br></div>`)[0];
                popup_258aef10c8ee005b88ffbf2e795b3c9f.setContent(html_035d99480af6222808614a7037a9864d);
            
        

        circle_marker_4dccfbde2da44b7bb4dc5a76fd5767d5.bindPopup(popup_258aef10c8ee005b88ffbf2e795b3c9f)
        ;

        
    
    
            var circle_marker_83ed2d3744fb518e2687de6fa5a0899a = L.circleMarker(
                [41.3938861, 2.1601641],
                {"bubblingMouseEvents": true, "color": "#9292e1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9292e1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d5765e894de972695c4914cc7a7c56bd = L.popup({"maxWidth": "100%"});

        
            
                var html_d8ae477c10a23e4e4f9a6a4d043e8012 = $(`<div id="html_d8ae477c10a23e4e4f9a6a4d043e8012" style="width: 100.0%; height: 100.0%;">Station 92<br>Result: 1.5%<br></div>`)[0];
                popup_d5765e894de972695c4914cc7a7c56bd.setContent(html_d8ae477c10a23e4e4f9a6a4d043e8012);
            
        

        circle_marker_83ed2d3744fb518e2687de6fa5a0899a.bindPopup(popup_d5765e894de972695c4914cc7a7c56bd)
        ;

        
    
    
            var circle_marker_08b24f2e9a6ebedfbd97258578dffddf = L.circleMarker(
                [41.3763948, 2.1473272],
                {"bubblingMouseEvents": true, "color": "#a7a7ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a7a7ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d3a8e0a509d2f727a68793a73f23e320 = L.popup({"maxWidth": "100%"});

        
            
                var html_5eeb169e85075e6af4464cb69c8bd5b4 = $(`<div id="html_5eeb169e85075e6af4464cb69c8bd5b4" style="width: 100.0%; height: 100.0%;">Station 95<br>Result: 1.0%<br></div>`)[0];
                popup_d3a8e0a509d2f727a68793a73f23e320.setContent(html_5eeb169e85075e6af4464cb69c8bd5b4);
            
        

        circle_marker_08b24f2e9a6ebedfbd97258578dffddf.bindPopup(popup_d3a8e0a509d2f727a68793a73f23e320)
        ;

        
    
    
            var circle_marker_6db4a9d729c20c5ba8176c2259d86a3a = L.circleMarker(
                [41.3779613, 2.1450491],
                {"bubblingMouseEvents": true, "color": "#adaddbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#adaddbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_057e0aaf99de2e373a3129c7d6e76f44 = L.popup({"maxWidth": "100%"});

        
            
                var html_83886fb8cd973c414cb20fac2af8a962 = $(`<div id="html_83886fb8cd973c414cb20fac2af8a962" style="width: 100.0%; height: 100.0%;">Station 97<br>Result: 0.9%<br></div>`)[0];
                popup_057e0aaf99de2e373a3129c7d6e76f44.setContent(html_83886fb8cd973c414cb20fac2af8a962);
            
        

        circle_marker_6db4a9d729c20c5ba8176c2259d86a3a.bindPopup(popup_057e0aaf99de2e373a3129c7d6e76f44)
        ;

        
    
    
            var circle_marker_bd0cd83ef726318d0a65c65c2a137310 = L.circleMarker(
                [41.3806074, 2.1408633],
                {"bubblingMouseEvents": true, "color": "#c6c6d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c6c6d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_abd5461ab0b9a7d1a7ab82aaca581b02 = L.popup({"maxWidth": "100%"});

        
            
                var html_d063b38e1c61b51a48414c512918020c = $(`<div id="html_d063b38e1c61b51a48414c512918020c" style="width: 100.0%; height: 100.0%;">Station 98<br>Result: 0.3%<br></div>`)[0];
                popup_abd5461ab0b9a7d1a7ab82aaca581b02.setContent(html_d063b38e1c61b51a48414c512918020c);
            
        

        circle_marker_bd0cd83ef726318d0a65c65c2a137310.bindPopup(popup_abd5461ab0b9a7d1a7ab82aaca581b02)
        ;

        
    
    
            var circle_marker_c1b4cbadd5bcd6fc35344f51d1d77bdc = L.circleMarker(
                [41.3808222, 2.141539],
                {"bubblingMouseEvents": true, "color": "#a7a7ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a7a7ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_aa0870713f298d76258cd4028f45dc34 = L.popup({"maxWidth": "100%"});

        
            
                var html_4566471fff1a608662be70ab671517b4 = $(`<div id="html_4566471fff1a608662be70ab671517b4" style="width: 100.0%; height: 100.0%;">Station 99<br>Result: 1.1%<br></div>`)[0];
                popup_aa0870713f298d76258cd4028f45dc34.setContent(html_4566471fff1a608662be70ab671517b4);
            
        

        circle_marker_c1b4cbadd5bcd6fc35344f51d1d77bdc.bindPopup(popup_aa0870713f298d76258cd4028f45dc34)
        ;

        
    
    
            var circle_marker_f53b445de23ac238aaecbd14ee151441 = L.circleMarker(
                [41.379363, 2.143868],
                {"bubblingMouseEvents": true, "color": "#adaddbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#adaddbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5ea5b90aed509e46aa30cf9d4541d428 = L.popup({"maxWidth": "100%"});

        
            
                var html_70cdfa1ab7012ae08c45586e1355d78d = $(`<div id="html_70cdfa1ab7012ae08c45586e1355d78d" style="width: 100.0%; height: 100.0%;">Station 100<br>Result: 0.9%<br></div>`)[0];
                popup_5ea5b90aed509e46aa30cf9d4541d428.setContent(html_70cdfa1ab7012ae08c45586e1355d78d);
            
        

        circle_marker_f53b445de23ac238aaecbd14ee151441.bindPopup(popup_5ea5b90aed509e46aa30cf9d4541d428)
        ;

        
    
    
            var circle_marker_f232c34bccdf8839d56c9e3c9ed602f8 = L.circleMarker(
                [41.392878, 2.143411],
                {"bubblingMouseEvents": true, "color": "#dbb0b0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dbb0b0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b7e42843c5d0d7bac1bba7935215cf22 = L.popup({"maxWidth": "100%"});

        
            
                var html_6b61e1de497178db74d3a10b7d4e1504 = $(`<div id="html_6b61e1de497178db74d3a10b7d4e1504" style="width: 100.0%; height: 100.0%;">Station 101<br>Result: -0.8%<br></div>`)[0];
                popup_b7e42843c5d0d7bac1bba7935215cf22.setContent(html_6b61e1de497178db74d3a10b7d4e1504);
            
        

        circle_marker_f232c34bccdf8839d56c9e3c9ed602f8.bindPopup(popup_b7e42843c5d0d7bac1bba7935215cf22)
        ;

        
    
    
            var circle_marker_f12f84efb92f496db987b6787e08a4eb = L.circleMarker(
                [41.392567, 2.1422174],
                {"bubblingMouseEvents": true, "color": "#d2d2d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d2d2d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c0ce15834c0cadf3265e88dc19c27560 = L.popup({"maxWidth": "100%"});

        
            
                var html_a224a691486d9875425f5b909e434597 = $(`<div id="html_a224a691486d9875425f5b909e434597" style="width: 100.0%; height: 100.0%;">Station 102<br>Result: 0.0%<br></div>`)[0];
                popup_c0ce15834c0cadf3265e88dc19c27560.setContent(html_a224a691486d9875425f5b909e434597);
            
        

        circle_marker_f12f84efb92f496db987b6787e08a4eb.bindPopup(popup_c0ce15834c0cadf3265e88dc19c27560)
        ;

        
    
    
            var circle_marker_cfcf531db2646f66da3800952f7ca847 = L.circleMarker(
                [41.410098, 2.1884487],
                {"bubblingMouseEvents": true, "color": "#8b8be2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8b8be2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_55ce8d3be10a2c446cd15a3cc5e80f06 = L.popup({"maxWidth": "100%"});

        
            
                var html_07494acced1f2adb21b3990cc68f8baf = $(`<div id="html_07494acced1f2adb21b3990cc68f8baf" style="width: 100.0%; height: 100.0%;">Station 103<br>Result: 1.7%<br></div>`)[0];
                popup_55ce8d3be10a2c446cd15a3cc5e80f06.setContent(html_07494acced1f2adb21b3990cc68f8baf);
            
        

        circle_marker_cfcf531db2646f66da3800952f7ca847.bindPopup(popup_55ce8d3be10a2c446cd15a3cc5e80f06)
        ;

        
    
    
            var circle_marker_d02b5aa435c69f6b24dbf7168e417124 = L.circleMarker(
                [41.4108005, 2.1872438],
                {"bubblingMouseEvents": true, "color": "#8a8ae3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8a8ae3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6b46ef2d70c259707215cb2d3f459362 = L.popup({"maxWidth": "100%"});

        
            
                var html_e066aba34ebc07cef2e32ce0613299e8 = $(`<div id="html_e066aba34ebc07cef2e32ce0613299e8" style="width: 100.0%; height: 100.0%;">Station 104<br>Result: 1.7%<br></div>`)[0];
                popup_6b46ef2d70c259707215cb2d3f459362.setContent(html_e066aba34ebc07cef2e32ce0613299e8);
            
        

        circle_marker_d02b5aa435c69f6b24dbf7168e417124.bindPopup(popup_6b46ef2d70c259707215cb2d3f459362)
        ;

        
    
    
            var circle_marker_9bb7ca5331cb55acc66884f8031bce9a = L.circleMarker(
                [41.389492, 2.17425],
                {"bubblingMouseEvents": true, "color": "#cfcfd4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cfcfd4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e16ee95d1f4daee8206a22281fc1e582 = L.popup({"maxWidth": "100%"});

        
            
                var html_c3d7fb1cd055c0b9453cac60dd457ac9 = $(`<div id="html_c3d7fb1cd055c0b9453cac60dd457ac9" style="width: 100.0%; height: 100.0%;">Station 105<br>Result: 0.1%<br></div>`)[0];
                popup_e16ee95d1f4daee8206a22281fc1e582.setContent(html_c3d7fb1cd055c0b9453cac60dd457ac9);
            
        

        circle_marker_9bb7ca5331cb55acc66884f8031bce9a.bindPopup(popup_e16ee95d1f4daee8206a22281fc1e582)
        ;

        
    
    
            var circle_marker_1e2ba6f2d08e98cbc25f0b285aff1d2b = L.circleMarker(
                [41.4055198, 2.1622548],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f00e614c1cc1111ab87740545c846c29 = L.popup({"maxWidth": "100%"});

        
            
                var html_c3321174e41846150ca6d59d4f0d885a = $(`<div id="html_c3321174e41846150ca6d59d4f0d885a" style="width: 100.0%; height: 100.0%;">Station 106<br>Result: 0.9%<br></div>`)[0];
                popup_f00e614c1cc1111ab87740545c846c29.setContent(html_c3321174e41846150ca6d59d4f0d885a);
            
        

        circle_marker_1e2ba6f2d08e98cbc25f0b285aff1d2b.bindPopup(popup_f00e614c1cc1111ab87740545c846c29)
        ;

        
    
    
            var circle_marker_22ac0510f60c9c4da57a684e7b23a295 = L.circleMarker(
                [41.3982304, 2.1531031],
                {"bubblingMouseEvents": true, "color": "#d5ceceff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5ceceff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b8f8adbf4abcdce022a006b64c3eb2ee = L.popup({"maxWidth": "100%"});

        
            
                var html_4c12c958a9fddb2d81302c1e37221d88 = $(`<div id="html_4c12c958a9fddb2d81302c1e37221d88" style="width: 100.0%; height: 100.0%;">Station 107<br>Result: -0.1%<br></div>`)[0];
                popup_b8f8adbf4abcdce022a006b64c3eb2ee.setContent(html_4c12c958a9fddb2d81302c1e37221d88);
            
        

        circle_marker_22ac0510f60c9c4da57a684e7b23a295.bindPopup(popup_b8f8adbf4abcdce022a006b64c3eb2ee)
        ;

        
    
    
            var circle_marker_b09acb809b486a7e25a2be22fed8bfb5 = L.circleMarker(
                [41.4022081, 2.1649035],
                {"bubblingMouseEvents": true, "color": "#a3a3ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a3a3ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5ceb2ba58a1cd25215fa94bdfc3d6c52 = L.popup({"maxWidth": "100%"});

        
            
                var html_e48e395c5d66d5e520b1fc4606f9d993 = $(`<div id="html_e48e395c5d66d5e520b1fc4606f9d993" style="width: 100.0%; height: 100.0%;">Station 108<br>Result: 1.1%<br></div>`)[0];
                popup_5ceb2ba58a1cd25215fa94bdfc3d6c52.setContent(html_e48e395c5d66d5e520b1fc4606f9d993);
            
        

        circle_marker_b09acb809b486a7e25a2be22fed8bfb5.bindPopup(popup_5ceb2ba58a1cd25215fa94bdfc3d6c52)
        ;

        
    
    
            var circle_marker_a5aff9084826a4318a70fcb0f35f6d87 = L.circleMarker(
                [41.3912605, 2.1476308],
                {"bubblingMouseEvents": true, "color": "#a4a4ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a4a4ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ac6c061b242fadd1d8787a769e106008 = L.popup({"maxWidth": "100%"});

        
            
                var html_434d80c3cd48baa4096042194669e75a = $(`<div id="html_434d80c3cd48baa4096042194669e75a" style="width: 100.0%; height: 100.0%;">Station 109<br>Result: 1.1%<br></div>`)[0];
                popup_ac6c061b242fadd1d8787a769e106008.setContent(html_434d80c3cd48baa4096042194669e75a);
            
        

        circle_marker_a5aff9084826a4318a70fcb0f35f6d87.bindPopup(popup_ac6c061b242fadd1d8787a769e106008)
        ;

        
    
    
            var circle_marker_6aa104e42b487fa92a7bbcdd16a59b1c = L.circleMarker(
                [41.3852585, 2.155089],
                {"bubblingMouseEvents": true, "color": "#0909feff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#0909feff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ea375d1f04e38cc7d08e9ed3be86fe58 = L.popup({"maxWidth": "100%"});

        
            
                var html_34325a8bc87dda9cadde1c25b0ce99a5 = $(`<div id="html_34325a8bc87dda9cadde1c25b0ce99a5" style="width: 100.0%; height: 100.0%;">Station 110<br>Result: 4.8%<br></div>`)[0];
                popup_ea375d1f04e38cc7d08e9ed3be86fe58.setContent(html_34325a8bc87dda9cadde1c25b0ce99a5);
            
        

        circle_marker_6aa104e42b487fa92a7bbcdd16a59b1c.bindPopup(popup_ea375d1f04e38cc7d08e9ed3be86fe58)
        ;

        
    
    
            var circle_marker_8677dab5051a2db007cfcf63ff02f82e = L.circleMarker(
                [41.3847528, 2.1546746],
                {"bubblingMouseEvents": true, "color": "#1616fbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#1616fbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_addddc2c69740fe711ce56acc13c1ac5 = L.popup({"maxWidth": "100%"});

        
            
                var html_25fb202c0300bc2e662f3c5a73b750d2 = $(`<div id="html_25fb202c0300bc2e662f3c5a73b750d2" style="width: 100.0%; height: 100.0%;">Station 111<br>Result: 4.5%<br></div>`)[0];
                popup_addddc2c69740fe711ce56acc13c1ac5.setContent(html_25fb202c0300bc2e662f3c5a73b750d2);
            
        

        circle_marker_8677dab5051a2db007cfcf63ff02f82e.bindPopup(popup_addddc2c69740fe711ce56acc13c1ac5)
        ;

        
    
    
            var circle_marker_240ba5ca7636086f1df5dc03e8c42c90 = L.circleMarker(
                [41.3776721, 2.157233],
                {"bubblingMouseEvents": true, "color": "#b0b0dbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b0b0dbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e855ed01dcb5c01a8da05a445ff7c04e = L.popup({"maxWidth": "100%"});

        
            
                var html_a29403739ed831448b7c928ee93adc31 = $(`<div id="html_a29403739ed831448b7c928ee93adc31" style="width: 100.0%; height: 100.0%;">Station 112<br>Result: 0.8%<br></div>`)[0];
                popup_e855ed01dcb5c01a8da05a445ff7c04e.setContent(html_a29403739ed831448b7c928ee93adc31);
            
        

        circle_marker_240ba5ca7636086f1df5dc03e8c42c90.bindPopup(popup_e855ed01dcb5c01a8da05a445ff7c04e)
        ;

        
    
    
            var circle_marker_43ad4b4ea3d726c54d6f9749b167f135 = L.circleMarker(
                [41.3773113, 2.1646742],
                {"bubblingMouseEvents": true, "color": "#7979e6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7979e6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9b0ce18edc89101fb78214b17d384185 = L.popup({"maxWidth": "100%"});

        
            
                var html_dbba3a4d4d015fc269e5b59246b4a30e = $(`<div id="html_dbba3a4d4d015fc269e5b59246b4a30e" style="width: 100.0%; height: 100.0%;">Station 113<br>Result: 2.1%<br></div>`)[0];
                popup_9b0ce18edc89101fb78214b17d384185.setContent(html_dbba3a4d4d015fc269e5b59246b4a30e);
            
        

        circle_marker_43ad4b4ea3d726c54d6f9749b167f135.bindPopup(popup_9b0ce18edc89101fb78214b17d384185)
        ;

        
    
    
            var circle_marker_8d345c12f93c479e4e47098bc2e34158 = L.circleMarker(
                [41.376735, 2.1740082],
                {"bubblingMouseEvents": true, "color": "#2323f8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#2323f8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0af8890a2bb39e582589e8cf1d63e091 = L.popup({"maxWidth": "100%"});

        
            
                var html_ae12e6e0efd8b885737cbcf21a4ed1e1 = $(`<div id="html_ae12e6e0efd8b885737cbcf21a4ed1e1" style="width: 100.0%; height: 100.0%;">Station 114<br>Result: 4.2%<br></div>`)[0];
                popup_0af8890a2bb39e582589e8cf1d63e091.setContent(html_ae12e6e0efd8b885737cbcf21a4ed1e1);
            
        

        circle_marker_8d345c12f93c479e4e47098bc2e34158.bindPopup(popup_0af8890a2bb39e582589e8cf1d63e091)
        ;

        
    
    
            var circle_marker_311275928fa328d259de7f8ec70f3f59 = L.circleMarker(
                [41.383597, 2.184171],
                {"bubblingMouseEvents": true, "color": "#d7c4c4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c4c4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_489f59975028516a197efd1fb086c83c = L.popup({"maxWidth": "100%"});

        
            
                var html_b46f4d274f05c9be91564ac69c6b5d24 = $(`<div id="html_b46f4d274f05c9be91564ac69c6b5d24" style="width: 100.0%; height: 100.0%;">Station 115<br>Result: -0.4%<br></div>`)[0];
                popup_489f59975028516a197efd1fb086c83c.setContent(html_b46f4d274f05c9be91564ac69c6b5d24);
            
        

        circle_marker_311275928fa328d259de7f8ec70f3f59.bindPopup(popup_489f59975028516a197efd1fb086c83c)
        ;

        
    
    
            var circle_marker_bfef2a7e8e11eab3481281d0d6998346 = L.circleMarker(
                [41.3838369, 2.1914756],
                {"bubblingMouseEvents": true, "color": "#f14747ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#f14747ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e6bfa25720301edfc93eadbc6351ac2e = L.popup({"maxWidth": "100%"});

        
            
                var html_dc83bbcc8fb87403f82d51e4c60ab3a6 = $(`<div id="html_dc83bbcc8fb87403f82d51e4c60ab3a6" style="width: 100.0%; height: 100.0%;">Station 116<br>Result: -3.3%<br></div>`)[0];
                popup_e6bfa25720301edfc93eadbc6351ac2e.setContent(html_dc83bbcc8fb87403f82d51e4c60ab3a6);
            
        

        circle_marker_bfef2a7e8e11eab3481281d0d6998346.bindPopup(popup_e6bfa25720301edfc93eadbc6351ac2e)
        ;

        
    
    
            var circle_marker_2548d4b56081a2fd9d47c3534d2b3e97 = L.circleMarker(
                [41.3906051, 2.1972309],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2e834745269ced295707bd95919a06a0 = L.popup({"maxWidth": "100%"});

        
            
                var html_d086a5d80561621d6955084c11c8a7ee = $(`<div id="html_d086a5d80561621d6955084c11c8a7ee" style="width: 100.0%; height: 100.0%;">Station 117<br>Result: -5.9%<br></div>`)[0];
                popup_2e834745269ced295707bd95919a06a0.setContent(html_d086a5d80561621d6955084c11c8a7ee);
            
        

        circle_marker_2548d4b56081a2fd9d47c3534d2b3e97.bindPopup(popup_2e834745269ced295707bd95919a06a0)
        ;

        
    
    
            var circle_marker_04235970283fab55c09f771f1f98088d = L.circleMarker(
                [41.39212, 2.1874966],
                {"bubblingMouseEvents": true, "color": "#e19090ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e19090ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_14a63a5befde271195e4a159894fb628 = L.popup({"maxWidth": "100%"});

        
            
                var html_58562b9ebd01e01cb0248fee79fa5e65 = $(`<div id="html_58562b9ebd01e01cb0248fee79fa5e65" style="width: 100.0%; height: 100.0%;">Station 118<br>Result: -1.6%<br></div>`)[0];
                popup_14a63a5befde271195e4a159894fb628.setContent(html_58562b9ebd01e01cb0248fee79fa5e65);
            
        

        circle_marker_04235970283fab55c09f771f1f98088d.bindPopup(popup_14a63a5befde271195e4a159894fb628)
        ;

        
    
    
            var circle_marker_0c0d13181746aa790a630cbf0f343395 = L.circleMarker(
                [41.3967169, 2.1825085],
                {"bubblingMouseEvents": true, "color": "#5b5becff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5b5becff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c15ae90a37161adc97cd15f761b84f36 = L.popup({"maxWidth": "100%"});

        
            
                var html_b0776dd790b49b18e38af9fb27ad553e = $(`<div id="html_b0776dd790b49b18e38af9fb27ad553e" style="width: 100.0%; height: 100.0%;">Station 119<br>Result: 2.8%<br></div>`)[0];
                popup_c15ae90a37161adc97cd15f761b84f36.setContent(html_b0776dd790b49b18e38af9fb27ad553e);
            
        

        circle_marker_0c0d13181746aa790a630cbf0f343395.bindPopup(popup_c15ae90a37161adc97cd15f761b84f36)
        ;

        
    
    
            var circle_marker_d76e1210c31ad69aae8ba294c184caeb = L.circleMarker(
                [41.4047056, 2.1765126],
                {"bubblingMouseEvents": true, "color": "#8a8ae3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8a8ae3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b6e29bf62c325d94612d5405c2f88240 = L.popup({"maxWidth": "100%"});

        
            
                var html_63d5213144a116b2ad0ebb7c6e433041 = $(`<div id="html_63d5213144a116b2ad0ebb7c6e433041" style="width: 100.0%; height: 100.0%;">Station 120<br>Result: 1.7%<br></div>`)[0];
                popup_b6e29bf62c325d94612d5405c2f88240.setContent(html_63d5213144a116b2ad0ebb7c6e433041);
            
        

        circle_marker_d76e1210c31ad69aae8ba294c184caeb.bindPopup(popup_b6e29bf62c325d94612d5405c2f88240)
        ;

        
    
    
            var circle_marker_540f4cedec3eb91300db4484fa344ca3 = L.circleMarker(
                [41.4064529, 2.1785364],
                {"bubblingMouseEvents": true, "color": "#5151efff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5151efff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_caa6dac3f7a0f68b653b6d209be5b7c7 = L.popup({"maxWidth": "100%"});

        
            
                var html_015c7bede6243218270cf067f09b01ae = $(`<div id="html_015c7bede6243218270cf067f09b01ae" style="width: 100.0%; height: 100.0%;">Station 121<br>Result: 3.1%<br></div>`)[0];
                popup_caa6dac3f7a0f68b653b6d209be5b7c7.setContent(html_015c7bede6243218270cf067f09b01ae);
            
        

        circle_marker_540f4cedec3eb91300db4484fa344ca3.bindPopup(popup_caa6dac3f7a0f68b653b6d209be5b7c7)
        ;

        
    
    
            var circle_marker_70a75c6b9f48b6e980161d8cd5ab12dc = L.circleMarker(
                [41.4054458, 2.1663172],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_60023f4c5b629515ccc86f53975dd36f = L.popup({"maxWidth": "100%"});

        
            
                var html_2c668e2907ad6c86783468c2a23171db = $(`<div id="html_2c668e2907ad6c86783468c2a23171db" style="width: 100.0%; height: 100.0%;">Station 122<br>Result: 0.9%<br></div>`)[0];
                popup_60023f4c5b629515ccc86f53975dd36f.setContent(html_2c668e2907ad6c86783468c2a23171db);
            
        

        circle_marker_70a75c6b9f48b6e980161d8cd5ab12dc.bindPopup(popup_60023f4c5b629515ccc86f53975dd36f)
        ;

        
    
    
            var circle_marker_ffe8db623cd0e72dc256386125cea6fb = L.circleMarker(
                [41.3988184485363, 2.166735224916682],
                {"bubblingMouseEvents": true, "color": "#8787e3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8787e3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_45c4c3f56c28fb698dc5f50f61ed4c1a = L.popup({"maxWidth": "100%"});

        
            
                var html_4f4c09fca4d457b9d60640ee4e373549 = $(`<div id="html_4f4c09fca4d457b9d60640ee4e373549" style="width: 100.0%; height: 100.0%;">Station 123<br>Result: 1.8%<br></div>`)[0];
                popup_45c4c3f56c28fb698dc5f50f61ed4c1a.setContent(html_4f4c09fca4d457b9d60640ee4e373549);
            
        

        circle_marker_ffe8db623cd0e72dc256386125cea6fb.bindPopup(popup_45c4c3f56c28fb698dc5f50f61ed4c1a)
        ;

        
    
    
            var circle_marker_ba9d0496df52e81348694d9fd3086144 = L.circleMarker(
                [41.3702483, 2.1878126],
                {"bubblingMouseEvents": true, "color": "#fc0e0eff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#fc0e0eff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_84eca5793449fc357eabe97b4b909242 = L.popup({"maxWidth": "100%"});

        
            
                var html_2021768392a123020b6db94fb85ace6d = $(`<div id="html_2021768392a123020b6db94fb85ace6d" style="width: 100.0%; height: 100.0%;">Station 124<br>Result: -4.7%<br></div>`)[0];
                popup_84eca5793449fc357eabe97b4b909242.setContent(html_2021768392a123020b6db94fb85ace6d);
            
        

        circle_marker_ba9d0496df52e81348694d9fd3086144.bindPopup(popup_84eca5793449fc357eabe97b4b909242)
        ;

        
    
    
            var circle_marker_38461c5ef17af2e6550a77790a2a8bd2 = L.circleMarker(
                [41.3834753, 2.194735],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6819b2f96b473f43267ad6eeccb61ff8 = L.popup({"maxWidth": "100%"});

        
            
                var html_b47e721d2021e2e8e45e68caef7f13a3 = $(`<div id="html_b47e721d2021e2e8e45e68caef7f13a3" style="width: 100.0%; height: 100.0%;">Station 125<br>Result: -6.1%<br></div>`)[0];
                popup_6819b2f96b473f43267ad6eeccb61ff8.setContent(html_b47e721d2021e2e8e45e68caef7f13a3);
            
        

        circle_marker_38461c5ef17af2e6550a77790a2a8bd2.bindPopup(popup_6819b2f96b473f43267ad6eeccb61ff8)
        ;

        
    
    
            var circle_marker_ba0538045e160d7cfd36c48555d425b7 = L.circleMarker(
                [41.380628, 2.1822815],
                {"bubblingMouseEvents": true, "color": "#e67c7cff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e67c7cff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0e4c2d2775be6519f1b0ab56122344ba = L.popup({"maxWidth": "100%"});

        
            
                var html_a4a4a41a0a2be600d90a903e9494ea25 = $(`<div id="html_a4a4a41a0a2be600d90a903e9494ea25" style="width: 100.0%; height: 100.0%;">Station 126<br>Result: -2.1%<br></div>`)[0];
                popup_0e4c2d2775be6519f1b0ab56122344ba.setContent(html_a4a4a41a0a2be600d90a903e9494ea25);
            
        

        circle_marker_ba0538045e160d7cfd36c48555d425b7.bindPopup(popup_0e4c2d2775be6519f1b0ab56122344ba)
        ;

        
    
    
            var circle_marker_297c5ec6117d39e1ab2da101cf8ff71a = L.circleMarker(
                [41.4120681, 2.1907524],
                {"bubblingMouseEvents": true, "color": "#9090e1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9090e1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9c873c7695da5c97532ce3e5acbbb8bf = L.popup({"maxWidth": "100%"});

        
            
                var html_966f598f00ffa2b443b5c24b6e3d023d = $(`<div id="html_966f598f00ffa2b443b5c24b6e3d023d" style="width: 100.0%; height: 100.0%;">Station 127<br>Result: 1.6%<br></div>`)[0];
                popup_9c873c7695da5c97532ce3e5acbbb8bf.setContent(html_966f598f00ffa2b443b5c24b6e3d023d);
            
        

        circle_marker_297c5ec6117d39e1ab2da101cf8ff71a.bindPopup(popup_9c873c7695da5c97532ce3e5acbbb8bf)
        ;

        
    
    
            var circle_marker_a52281933e085db9fdffcb70a35251a4 = L.circleMarker(
                [41.4158412, 2.1959771],
                {"bubblingMouseEvents": true, "color": "#bdbdd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bdbdd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7bcb21c1a0fe4924f0730d70ceac2084 = L.popup({"maxWidth": "100%"});

        
            
                var html_c1ee7f88e1eaf15c4c60e5b653d1f219 = $(`<div id="html_c1ee7f88e1eaf15c4c60e5b653d1f219" style="width: 100.0%; height: 100.0%;">Station 128<br>Result: 0.5%<br></div>`)[0];
                popup_7bcb21c1a0fe4924f0730d70ceac2084.setContent(html_c1ee7f88e1eaf15c4c60e5b653d1f219);
            
        

        circle_marker_a52281933e085db9fdffcb70a35251a4.bindPopup(popup_7bcb21c1a0fe4924f0730d70ceac2084)
        ;

        
    
    
            var circle_marker_eccb73adf8ed5d82f30544c1f32e9a82 = L.circleMarker(
                [41.377046, 2.16113608],
                {"bubblingMouseEvents": true, "color": "#4747f1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#4747f1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e07b2203661037a96a9c6beec5004a82 = L.popup({"maxWidth": "100%"});

        
            
                var html_05fa20ce39099ead825fd08c52403223 = $(`<div id="html_05fa20ce39099ead825fd08c52403223" style="width: 100.0%; height: 100.0%;">Station 129<br>Result: 3.3%<br></div>`)[0];
                popup_e07b2203661037a96a9c6beec5004a82.setContent(html_05fa20ce39099ead825fd08c52403223);
            
        

        circle_marker_eccb73adf8ed5d82f30544c1f32e9a82.bindPopup(popup_e07b2203661037a96a9c6beec5004a82)
        ;

        
    
    
            var circle_marker_10f34940e9e49b1c4aad6a8938f8b972 = L.circleMarker(
                [41.4200135, 2.2016699],
                {"bubblingMouseEvents": true, "color": "#6464ebff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6464ebff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_16899963e72ca6dade071813f906e581 = L.popup({"maxWidth": "100%"});

        
            
                var html_0ab121a16f6a767724d72cba4801c64b = $(`<div id="html_0ab121a16f6a767724d72cba4801c64b" style="width: 100.0%; height: 100.0%;">Station 130<br>Result: 2.6%<br></div>`)[0];
                popup_16899963e72ca6dade071813f906e581.setContent(html_0ab121a16f6a767724d72cba4801c64b);
            
        

        circle_marker_10f34940e9e49b1c4aad6a8938f8b972.bindPopup(popup_16899963e72ca6dade071813f906e581)
        ;

        
    
    
            var circle_marker_5b8853456a5ad30f416b818a4fba1448 = L.circleMarker(
                [41.4227912, 2.2060317],
                {"bubblingMouseEvents": true, "color": "#a7a7ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a7a7ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_996f5b1ede8e1b60be223b4d84bb07d5 = L.popup({"maxWidth": "100%"});

        
            
                var html_8176af30ff34c11d3c7e58142de2fc23 = $(`<div id="html_8176af30ff34c11d3c7e58142de2fc23" style="width: 100.0%; height: 100.0%;">Station 131<br>Result: 1.0%<br></div>`)[0];
                popup_996f5b1ede8e1b60be223b4d84bb07d5.setContent(html_8176af30ff34c11d3c7e58142de2fc23);
            
        

        circle_marker_5b8853456a5ad30f416b818a4fba1448.bindPopup(popup_996f5b1ede8e1b60be223b4d84bb07d5)
        ;

        
    
    
            var circle_marker_c8e93c56e608f95f0699f456b4e39e1e = L.circleMarker(
                [41.4084796, 2.192042],
                {"bubblingMouseEvents": true, "color": "#c5c5d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c5c5d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f70a209626fe8696ebfcda287dde82fb = L.popup({"maxWidth": "100%"});

        
            
                var html_c62a96263294c76e49bf5935b9015997 = $(`<div id="html_c62a96263294c76e49bf5935b9015997" style="width: 100.0%; height: 100.0%;">Station 132<br>Result: 0.3%<br></div>`)[0];
                popup_f70a209626fe8696ebfcda287dde82fb.setContent(html_c62a96263294c76e49bf5935b9015997);
            
        

        circle_marker_c8e93c56e608f95f0699f456b4e39e1e.bindPopup(popup_f70a209626fe8696ebfcda287dde82fb)
        ;

        
    
    
            var circle_marker_8c783848e8a8d1d803e6c9f0b016e838 = L.circleMarker(
                [41.4075013, 2.1930174],
                {"bubblingMouseEvents": true, "color": "#d4cfcfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4cfcfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_dedfdf775032c98f072cdc27d238e1d7 = L.popup({"maxWidth": "100%"});

        
            
                var html_3e0feb3ae7085d5642efa93873d1fe5c = $(`<div id="html_3e0feb3ae7085d5642efa93873d1fe5c" style="width: 100.0%; height: 100.0%;">Station 133<br>Result: -0.1%<br></div>`)[0];
                popup_dedfdf775032c98f072cdc27d238e1d7.setContent(html_3e0feb3ae7085d5642efa93873d1fe5c);
            
        

        circle_marker_8c783848e8a8d1d803e6c9f0b016e838.bindPopup(popup_dedfdf775032c98f072cdc27d238e1d7)
        ;

        
    
    
            var circle_marker_5b661670bab86a567107346b9790a250 = L.circleMarker(
                [41.4113024, 2.1987258],
                {"bubblingMouseEvents": true, "color": "#d3d3d3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d3d3d3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0f791d2afdc7490cea5f733de9b6276d = L.popup({"maxWidth": "100%"});

        
            
                var html_2e132982101ce9f7bd34f80903fb385d = $(`<div id="html_2e132982101ce9f7bd34f80903fb385d" style="width: 100.0%; height: 100.0%;">Station 134<br>Result: 0.0%<br></div>`)[0];
                popup_0f791d2afdc7490cea5f733de9b6276d.setContent(html_2e132982101ce9f7bd34f80903fb385d);
            
        

        circle_marker_5b661670bab86a567107346b9790a250.bindPopup(popup_0f791d2afdc7490cea5f733de9b6276d)
        ;

        
    
    
            var circle_marker_0232d2cdc90bfeec3c90c7e525667578 = L.circleMarker(
                [41.4120452, 2.1972673],
                {"bubblingMouseEvents": true, "color": "#a9a9dcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a9a9dcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_75a938b4fd80bc0be291a6162af10d42 = L.popup({"maxWidth": "100%"});

        
            
                var html_689cdf22dd90c295cdd7f6711c4360d8 = $(`<div id="html_689cdf22dd90c295cdd7f6711c4360d8" style="width: 100.0%; height: 100.0%;">Station 135<br>Result: 1.0%<br></div>`)[0];
                popup_75a938b4fd80bc0be291a6162af10d42.setContent(html_689cdf22dd90c295cdd7f6711c4360d8);
            
        

        circle_marker_0232d2cdc90bfeec3c90c7e525667578.bindPopup(popup_75a938b4fd80bc0be291a6162af10d42)
        ;

        
    
    
            var circle_marker_1f9be418a91c771b486c123e3a21bc64 = L.circleMarker(
                [41.4139298, 2.2017955],
                {"bubblingMouseEvents": true, "color": "#babad9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#babad9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2fbbe472bab20938c737ecf896a49c41 = L.popup({"maxWidth": "100%"});

        
            
                var html_5fd64a94679fcab8f38397dc8aeefa2b = $(`<div id="html_5fd64a94679fcab8f38397dc8aeefa2b" style="width: 100.0%; height: 100.0%;">Station 136<br>Result: 0.6%<br></div>`)[0];
                popup_2fbbe472bab20938c737ecf896a49c41.setContent(html_5fd64a94679fcab8f38397dc8aeefa2b);
            
        

        circle_marker_1f9be418a91c771b486c123e3a21bc64.bindPopup(popup_2fbbe472bab20938c737ecf896a49c41)
        ;

        
    
    
            var circle_marker_6d811033a2935e0a22e063083b402b52 = L.circleMarker(
                [41.4145805, 2.2008139],
                {"bubblingMouseEvents": true, "color": "#9595e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9595e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e449230713d80a6d566be23b0b7e97c0 = L.popup({"maxWidth": "100%"});

        
            
                var html_18ba0482a3a7903c57bc0b11457d1299 = $(`<div id="html_18ba0482a3a7903c57bc0b11457d1299" style="width: 100.0%; height: 100.0%;">Station 137<br>Result: 1.5%<br></div>`)[0];
                popup_e449230713d80a6d566be23b0b7e97c0.setContent(html_18ba0482a3a7903c57bc0b11457d1299);
            
        

        circle_marker_6d811033a2935e0a22e063083b402b52.bindPopup(popup_e449230713d80a6d566be23b0b7e97c0)
        ;

        
    
    
            var circle_marker_839357fc7b176abd47b7dd8b5521909c = L.circleMarker(
                [41.4167933, 2.2058345],
                {"bubblingMouseEvents": true, "color": "#a7a7ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a7a7ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4a8347b7aaf8d2ac4fdd986e27120956 = L.popup({"maxWidth": "100%"});

        
            
                var html_dfb853aeb74352a0ee7a045ee893080d = $(`<div id="html_dfb853aeb74352a0ee7a045ee893080d" style="width: 100.0%; height: 100.0%;">Station 138<br>Result: 1.0%<br></div>`)[0];
                popup_4a8347b7aaf8d2ac4fdd986e27120956.setContent(html_dfb853aeb74352a0ee7a045ee893080d);
            
        

        circle_marker_839357fc7b176abd47b7dd8b5521909c.bindPopup(popup_4a8347b7aaf8d2ac4fdd986e27120956)
        ;

        
    
    
            var circle_marker_70ed343d9ee9cae2a5dbb7c508187f61 = L.circleMarker(
                [41.4183999, 2.2058133],
                {"bubblingMouseEvents": true, "color": "#d1d1d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d1d1d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6c7b5e877a7a9046e8602536288b03e3 = L.popup({"maxWidth": "100%"});

        
            
                var html_b10c49ebf6d071161d39ea03bc61a447 = $(`<div id="html_b10c49ebf6d071161d39ea03bc61a447" style="width: 100.0%; height: 100.0%;">Station 139<br>Result: 0.1%<br></div>`)[0];
                popup_6c7b5e877a7a9046e8602536288b03e3.setContent(html_b10c49ebf6d071161d39ea03bc61a447);
            
        

        circle_marker_70ed343d9ee9cae2a5dbb7c508187f61.bindPopup(popup_6c7b5e877a7a9046e8602536288b03e3)
        ;

        
    
    
            var circle_marker_73e68a7022b3abd3d249cdf7a7cacb43 = L.circleMarker(
                [41.3808772, 2.1559939],
                {"bubblingMouseEvents": true, "color": "#6464ebff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6464ebff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_dd1300eefbc26f1b69ed1abb0e63e69e = L.popup({"maxWidth": "100%"});

        
            
                var html_b3901fb017e43d87b51ba4eb9938af73 = $(`<div id="html_b3901fb017e43d87b51ba4eb9938af73" style="width: 100.0%; height: 100.0%;">Station 140<br>Result: 2.6%<br></div>`)[0];
                popup_dd1300eefbc26f1b69ed1abb0e63e69e.setContent(html_b3901fb017e43d87b51ba4eb9938af73);
            
        

        circle_marker_73e68a7022b3abd3d249cdf7a7cacb43.bindPopup(popup_dd1300eefbc26f1b69ed1abb0e63e69e)
        ;

        
    
    
            var circle_marker_5606e80e825c23a8932f385a6f259a31 = L.circleMarker(
                [41.4090202, 2.1954152],
                {"bubblingMouseEvents": true, "color": "#d2d2d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d2d2d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_270ac65a239bbb1705aed7e76f52003a = L.popup({"maxWidth": "100%"});

        
            
                var html_2dafe851881208800a568db2e3b820f9 = $(`<div id="html_2dafe851881208800a568db2e3b820f9" style="width: 100.0%; height: 100.0%;">Station 141<br>Result: 0.0%<br></div>`)[0];
                popup_270ac65a239bbb1705aed7e76f52003a.setContent(html_2dafe851881208800a568db2e3b820f9);
            
        

        circle_marker_5606e80e825c23a8932f385a6f259a31.bindPopup(popup_270ac65a239bbb1705aed7e76f52003a)
        ;

        
    
    
            var circle_marker_dbd697704b3a87d3d776e9027f059c5c = L.circleMarker(
                [41.4003793, 2.1924144],
                {"bubblingMouseEvents": true, "color": "#d6c5c5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c5c5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_48d3ab60f2149ae5b3b4d5c1d79ae420 = L.popup({"maxWidth": "100%"});

        
            
                var html_365d75cf61ca794a263bfbc0f76f4aab = $(`<div id="html_365d75cf61ca794a263bfbc0f76f4aab" style="width: 100.0%; height: 100.0%;">Station 142<br>Result: -0.3%<br></div>`)[0];
                popup_48d3ab60f2149ae5b3b4d5c1d79ae420.setContent(html_365d75cf61ca794a263bfbc0f76f4aab);
            
        

        circle_marker_dbd697704b3a87d3d776e9027f059c5c.bindPopup(popup_48d3ab60f2149ae5b3b4d5c1d79ae420)
        ;

        
    
    
            var circle_marker_525f9ba5d1e3f2b5e8c59fbd579061b8 = L.circleMarker(
                [41.4027907, 2.1956161],
                {"bubblingMouseEvents": true, "color": "#d6c6c6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c6c6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_25deedc0b1b93a9db97fc16ee024132f = L.popup({"maxWidth": "100%"});

        
            
                var html_90d6937896f6d048672bd785a68ac79f = $(`<div id="html_90d6937896f6d048672bd785a68ac79f" style="width: 100.0%; height: 100.0%;">Station 143<br>Result: -0.3%<br></div>`)[0];
                popup_25deedc0b1b93a9db97fc16ee024132f.setContent(html_90d6937896f6d048672bd785a68ac79f);
            
        

        circle_marker_525f9ba5d1e3f2b5e8c59fbd579061b8.bindPopup(popup_25deedc0b1b93a9db97fc16ee024132f)
        ;

        
    
    
            var circle_marker_be1a139d0ffcd41424b217a6641b9257 = L.circleMarker(
                [41.4056269, 2.1977119],
                {"bubblingMouseEvents": true, "color": "#dbadadff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dbadadff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f89c36181f5eaf3cf921dbc59d4745fd = L.popup({"maxWidth": "100%"});

        
            
                var html_afc7d0b46bff476c07fe919db8866175 = $(`<div id="html_afc7d0b46bff476c07fe919db8866175" style="width: 100.0%; height: 100.0%;">Station 144<br>Result: -0.9%<br></div>`)[0];
                popup_f89c36181f5eaf3cf921dbc59d4745fd.setContent(html_afc7d0b46bff476c07fe919db8866175);
            
        

        circle_marker_be1a139d0ffcd41424b217a6641b9257.bindPopup(popup_f89c36181f5eaf3cf921dbc59d4745fd)
        ;

        
    
    
            var circle_marker_d78fa39afd67d44b6df2d63801c95b6b = L.circleMarker(
                [41.4093405, 2.2024461],
                {"bubblingMouseEvents": true, "color": "#d7c1c1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c1c1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_bd1e09381aa201051d3102cfb0d0aa96 = L.popup({"maxWidth": "100%"});

        
            
                var html_d6f24127533d34c759e673de4afea536 = $(`<div id="html_d6f24127533d34c759e673de4afea536" style="width: 100.0%; height: 100.0%;">Station 145<br>Result: -0.4%<br></div>`)[0];
                popup_bd1e09381aa201051d3102cfb0d0aa96.setContent(html_d6f24127533d34c759e673de4afea536);
            
        

        circle_marker_d78fa39afd67d44b6df2d63801c95b6b.bindPopup(popup_bd1e09381aa201051d3102cfb0d0aa96)
        ;

        
    
    
            var circle_marker_4a2acab4dbae764a0d163a0baeb7f142 = L.circleMarker(
                [41.4148983, 2.207186],
                {"bubblingMouseEvents": true, "color": "#d6c6c6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c6c6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_99f46942dc96338ff06d8205c65a6ec2 = L.popup({"maxWidth": "100%"});

        
            
                var html_ca2c552ddfa972305c5221d721eb9144 = $(`<div id="html_ca2c552ddfa972305c5221d721eb9144" style="width: 100.0%; height: 100.0%;">Station 146<br>Result: -0.3%<br></div>`)[0];
                popup_99f46942dc96338ff06d8205c65a6ec2.setContent(html_ca2c552ddfa972305c5221d721eb9144);
            
        

        circle_marker_4a2acab4dbae764a0d163a0baeb7f142.bindPopup(popup_99f46942dc96338ff06d8205c65a6ec2)
        ;

        
    
    
            var circle_marker_1c2e8f566d5444d213806f83f4f96c2b = L.circleMarker(
                [41.416043, 2.2124993],
                {"bubblingMouseEvents": true, "color": "#dda7a7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dda7a7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8ab84418a1a29833249487abc5f26301 = L.popup({"maxWidth": "100%"});

        
            
                var html_c827065565ed511535aa40a71fa5e6a2 = $(`<div id="html_c827065565ed511535aa40a71fa5e6a2" style="width: 100.0%; height: 100.0%;">Station 147<br>Result: -1.0%<br></div>`)[0];
                popup_8ab84418a1a29833249487abc5f26301.setContent(html_c827065565ed511535aa40a71fa5e6a2);
            
        

        circle_marker_1c2e8f566d5444d213806f83f4f96c2b.bindPopup(popup_8ab84418a1a29833249487abc5f26301)
        ;

        
    
    
            var circle_marker_60db8ef134c96b5b969c024191838d07 = L.circleMarker(
                [41.3783467, 2.1633139],
                {"bubblingMouseEvents": true, "color": "#8282e4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8282e4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8ee8b9dcc54ad8564f9de2e6ccef9dc0 = L.popup({"maxWidth": "100%"});

        
            
                var html_ff8d88d138d4d0a850a0ac8716991784 = $(`<div id="html_ff8d88d138d4d0a850a0ac8716991784" style="width: 100.0%; height: 100.0%;">Station 148<br>Result: 1.9%<br></div>`)[0];
                popup_8ee8b9dcc54ad8564f9de2e6ccef9dc0.setContent(html_ff8d88d138d4d0a850a0ac8716991784);
            
        

        circle_marker_60db8ef134c96b5b969c024191838d07.bindPopup(popup_8ee8b9dcc54ad8564f9de2e6ccef9dc0)
        ;

        
    
    
            var circle_marker_e4ce7be1e816f17214f404030899d047 = L.circleMarker(
                [41.3958685, 2.192952],
                {"bubblingMouseEvents": true, "color": "#d2d2d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d2d2d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c1bc00b632310370f207d23903afc265 = L.popup({"maxWidth": "100%"});

        
            
                var html_cc4e8fe43dfd780ab3337499a8bf3903 = $(`<div id="html_cc4e8fe43dfd780ab3337499a8bf3903" style="width: 100.0%; height: 100.0%;">Station 149<br>Result: 0.0%<br></div>`)[0];
                popup_c1bc00b632310370f207d23903afc265.setContent(html_cc4e8fe43dfd780ab3337499a8bf3903);
            
        

        circle_marker_e4ce7be1e816f17214f404030899d047.bindPopup(popup_c1bc00b632310370f207d23903afc265)
        ;

        
    
    
            var circle_marker_64e59202a0c96424545863bd97fe0324 = L.circleMarker(
                [41.4065912, 2.203028],
                {"bubblingMouseEvents": true, "color": "#f24040ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#f24040ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_33e459ffbb1cdbee9873c866a5dfc829 = L.popup({"maxWidth": "100%"});

        
            
                var html_c3fa8e2dcf2eeb04ebb8e37216270c72 = $(`<div id="html_c3fa8e2dcf2eeb04ebb8e37216270c72" style="width: 100.0%; height: 100.0%;">Station 150<br>Result: -3.5%<br></div>`)[0];
                popup_33e459ffbb1cdbee9873c866a5dfc829.setContent(html_c3fa8e2dcf2eeb04ebb8e37216270c72);
            
        

        circle_marker_64e59202a0c96424545863bd97fe0324.bindPopup(popup_33e459ffbb1cdbee9873c866a5dfc829)
        ;

        
    
    
            var circle_marker_5396582b6c046da46e3bd3465633b6ac = L.circleMarker(
                [41.4003471, 2.1969105],
                {"bubblingMouseEvents": true, "color": "#f24141ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#f24141ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f4685973c1ce0989168bf43491ca448b = L.popup({"maxWidth": "100%"});

        
            
                var html_3972b090989719b9608130248c60025f = $(`<div id="html_3972b090989719b9608130248c60025f" style="width: 100.0%; height: 100.0%;">Station 151<br>Result: -3.5%<br></div>`)[0];
                popup_f4685973c1ce0989168bf43491ca448b.setContent(html_3972b090989719b9608130248c60025f);
            
        

        circle_marker_5396582b6c046da46e3bd3465633b6ac.bindPopup(popup_f4685973c1ce0989168bf43491ca448b)
        ;

        
    
    
            var circle_marker_6d425a4e7bf7e73e18f05e2de1ec0e21 = L.circleMarker(
                [41.3993329, 2.1974184],
                {"bubblingMouseEvents": true, "color": "#e77575ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e77575ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_05b37f291c2d0be392a1edb5f870e893 = L.popup({"maxWidth": "100%"});

        
            
                var html_6d8d9724cb7163b9a30ca39bed72b7d5 = $(`<div id="html_6d8d9724cb7163b9a30ca39bed72b7d5" style="width: 100.0%; height: 100.0%;">Station 152<br>Result: -2.2%<br></div>`)[0];
                popup_05b37f291c2d0be392a1edb5f870e893.setContent(html_6d8d9724cb7163b9a30ca39bed72b7d5);
            
        

        circle_marker_6d425a4e7bf7e73e18f05e2de1ec0e21.bindPopup(popup_05b37f291c2d0be392a1edb5f870e893)
        ;

        
    
    
            var circle_marker_646f478549b6918fd4086ee72c1a1aef = L.circleMarker(
                [41.4018686, 2.20077],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f780d69c20d13a6b813b2164c9d6820d = L.popup({"maxWidth": "100%"});

        
            
                var html_ccdee7c52e8217d162ac06b958b079d1 = $(`<div id="html_ccdee7c52e8217d162ac06b958b079d1" style="width: 100.0%; height: 100.0%;">Station 153<br>Result: -5.2%<br></div>`)[0];
                popup_f780d69c20d13a6b813b2164c9d6820d.setContent(html_ccdee7c52e8217d162ac06b958b079d1);
            
        

        circle_marker_646f478549b6918fd4086ee72c1a1aef.bindPopup(popup_f780d69c20d13a6b813b2164c9d6820d)
        ;

        
    
    
            var circle_marker_0e584557011d4b1cc369d9ad009d0a46 = L.circleMarker(
                [41.4026275, 2.2017694],
                {"bubblingMouseEvents": true, "color": "#ff0202ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0202ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0d1310883abcc88616f7de2fa8ad67c1 = L.popup({"maxWidth": "100%"});

        
            
                var html_342ac69845fe49910179fd309935b1ef = $(`<div id="html_342ac69845fe49910179fd309935b1ef" style="width: 100.0%; height: 100.0%;">Station 154<br>Result: -5.0%<br></div>`)[0];
                popup_0d1310883abcc88616f7de2fa8ad67c1.setContent(html_342ac69845fe49910179fd309935b1ef);
            
        

        circle_marker_0e584557011d4b1cc369d9ad009d0a46.bindPopup(popup_0d1310883abcc88616f7de2fa8ad67c1)
        ;

        
    
    
            var circle_marker_d274b841fd2cfcea4646687edf523683 = L.circleMarker(
                [41.4070139, 2.2074469],
                {"bubblingMouseEvents": true, "color": "#c7c7d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c7c7d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c47aa6057d0152d7aa7f6a6900a28f72 = L.popup({"maxWidth": "100%"});

        
            
                var html_73473f7167cc38cf92cf2747554005ba = $(`<div id="html_73473f7167cc38cf92cf2747554005ba" style="width: 100.0%; height: 100.0%;">Station 155<br>Result: 0.3%<br></div>`)[0];
                popup_c47aa6057d0152d7aa7f6a6900a28f72.setContent(html_73473f7167cc38cf92cf2747554005ba);
            
        

        circle_marker_d274b841fd2cfcea4646687edf523683.bindPopup(popup_c47aa6057d0152d7aa7f6a6900a28f72)
        ;

        
    
    
            var circle_marker_338b57c30e43cf539f7fa02dd5337e5e = L.circleMarker(
                [41.4091355, 2.2088179],
                {"bubblingMouseEvents": true, "color": "#e19494ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e19494ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_34bcf7407f01c93d6681708471964c0f = L.popup({"maxWidth": "100%"});

        
            
                var html_68a25fd69587861603930e5b36bf06c4 = $(`<div id="html_68a25fd69587861603930e5b36bf06c4" style="width: 100.0%; height: 100.0%;">Station 156<br>Result: -1.5%<br></div>`)[0];
                popup_34bcf7407f01c93d6681708471964c0f.setContent(html_68a25fd69587861603930e5b36bf06c4);
            
        

        circle_marker_338b57c30e43cf539f7fa02dd5337e5e.bindPopup(popup_34bcf7407f01c93d6681708471964c0f)
        ;

        
    
    
            var circle_marker_f3adea96f6b04b4237a8c64c525f3136 = L.circleMarker(
                [41.4132316, 2.2177652],
                {"bubblingMouseEvents": true, "color": "#df9d9dff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#df9d9dff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_15139d90289c122ac191c379192b99a3 = L.popup({"maxWidth": "100%"});

        
            
                var html_d48bd772d246421be9013481488ec117 = $(`<div id="html_d48bd772d246421be9013481488ec117" style="width: 100.0%; height: 100.0%;">Station 157<br>Result: -1.3%<br></div>`)[0];
                popup_15139d90289c122ac191c379192b99a3.setContent(html_d48bd772d246421be9013481488ec117);
            
        

        circle_marker_f3adea96f6b04b4237a8c64c525f3136.bindPopup(popup_15139d90289c122ac191c379192b99a3)
        ;

        
    
    
            var circle_marker_3864192ce4c290dbc0bca4ca203358ca = L.circleMarker(
                [41.4116634, 2.2183313],
                {"bubblingMouseEvents": true, "color": "#e48181ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e48181ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_256dd88775a8305c896fe3215bb8b05b = L.popup({"maxWidth": "100%"});

        
            
                var html_6cad1046ea3dd10c09a0816756d4461e = $(`<div id="html_6cad1046ea3dd10c09a0816756d4461e" style="width: 100.0%; height: 100.0%;">Station 158<br>Result: -1.9%<br></div>`)[0];
                popup_256dd88775a8305c896fe3215bb8b05b.setContent(html_6cad1046ea3dd10c09a0816756d4461e);
            
        

        circle_marker_3864192ce4c290dbc0bca4ca203358ca.bindPopup(popup_256dd88775a8305c896fe3215bb8b05b)
        ;

        
    
    
            var circle_marker_7b55b89b086ea7665793f6e6a490e786 = L.circleMarker(
                [41.4110822, 2.2163136],
                {"bubblingMouseEvents": true, "color": "#e48383ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e48383ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d87bd0881924f99f464b0e45b9989858 = L.popup({"maxWidth": "100%"});

        
            
                var html_25bf67e58cf26394660f17ba3d7fee00 = $(`<div id="html_25bf67e58cf26394660f17ba3d7fee00" style="width: 100.0%; height: 100.0%;">Station 159<br>Result: -1.9%<br></div>`)[0];
                popup_d87bd0881924f99f464b0e45b9989858.setContent(html_25bf67e58cf26394660f17ba3d7fee00);
            
        

        circle_marker_7b55b89b086ea7665793f6e6a490e786.bindPopup(popup_d87bd0881924f99f464b0e45b9989858)
        ;

        
    
    
            var circle_marker_e0f82de19e3ba0f564c5f3eaf2153ba4 = L.circleMarker(
                [41.3953011, 2.1965965],
                {"bubblingMouseEvents": true, "color": "#e87272ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e87272ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_060796bf6bc552fb431ae269260c9fe0 = L.popup({"maxWidth": "100%"});

        
            
                var html_f2419fe7d4aa7a5fef7c4db83b1cf35d = $(`<div id="html_f2419fe7d4aa7a5fef7c4db83b1cf35d" style="width: 100.0%; height: 100.0%;">Station 161<br>Result: -2.3%<br></div>`)[0];
                popup_060796bf6bc552fb431ae269260c9fe0.setContent(html_f2419fe7d4aa7a5fef7c4db83b1cf35d);
            
        

        circle_marker_e0f82de19e3ba0f564c5f3eaf2153ba4.bindPopup(popup_060796bf6bc552fb431ae269260c9fe0)
        ;

        
    
    
            var circle_marker_e5ad22455f3743460f23bedf9a0a7b5b = L.circleMarker(
                [41.4038559, 2.2084257],
                {"bubblingMouseEvents": true, "color": "#f53030ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#f53030ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_be2908d9afe944f75fb457389ddfeac5 = L.popup({"maxWidth": "100%"});

        
            
                var html_48520a6fa632748a1d39d5cce9079bc9 = $(`<div id="html_48520a6fa632748a1d39d5cce9079bc9" style="width: 100.0%; height: 100.0%;">Station 162<br>Result: -3.9%<br></div>`)[0];
                popup_be2908d9afe944f75fb457389ddfeac5.setContent(html_48520a6fa632748a1d39d5cce9079bc9);
            
        

        circle_marker_e5ad22455f3743460f23bedf9a0a7b5b.bindPopup(popup_be2908d9afe944f75fb457389ddfeac5)
        ;

        
    
    
            var circle_marker_b187dc7611d40347aecaa04c3d854797 = L.circleMarker(
                [41.4118378, 2.1778852],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7af25d0b7cd38dc9b82c21218f419ae4 = L.popup({"maxWidth": "100%"});

        
            
                var html_3a6359e8d7b6e8a80f8a74a726e20c77 = $(`<div id="html_3a6359e8d7b6e8a80f8a74a726e20c77" style="width: 100.0%; height: 100.0%;">Station 164<br>Result: 0.9%<br></div>`)[0];
                popup_7af25d0b7cd38dc9b82c21218f419ae4.setContent(html_3a6359e8d7b6e8a80f8a74a726e20c77);
            
        

        circle_marker_b187dc7611d40347aecaa04c3d854797.bindPopup(popup_7af25d0b7cd38dc9b82c21218f419ae4)
        ;

        
    
    
            var circle_marker_7d5d75d1a4bb7f1f5ce61e8cbdfd92b7 = L.circleMarker(
                [41.3992169, 2.2041415],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8c823560682f2de959393ecea8128bc6 = L.popup({"maxWidth": "100%"});

        
            
                var html_313caeed30172592b8eb3fef420dd5c8 = $(`<div id="html_313caeed30172592b8eb3fef420dd5c8" style="width: 100.0%; height: 100.0%;">Station 165<br>Result: -5.9%<br></div>`)[0];
                popup_8c823560682f2de959393ecea8128bc6.setContent(html_313caeed30172592b8eb3fef420dd5c8);
            
        

        circle_marker_7d5d75d1a4bb7f1f5ce61e8cbdfd92b7.bindPopup(popup_8c823560682f2de959393ecea8128bc6)
        ;

        
    
    
            var circle_marker_ce757ce53bc89e493e1e23957213389b = L.circleMarker(
                [41.4008312, 2.206645],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c0dce26d12472ba3f5a51d6a4c2e7a24 = L.popup({"maxWidth": "100%"});

        
            
                var html_e5425199a901bd423babe9b2f5f85151 = $(`<div id="html_e5425199a901bd423babe9b2f5f85151" style="width: 100.0%; height: 100.0%;">Station 166<br>Result: -6.8%<br></div>`)[0];
                popup_c0dce26d12472ba3f5a51d6a4c2e7a24.setContent(html_e5425199a901bd423babe9b2f5f85151);
            
        

        circle_marker_ce757ce53bc89e493e1e23957213389b.bindPopup(popup_c0dce26d12472ba3f5a51d6a4c2e7a24)
        ;

        
    
    
            var circle_marker_e48923903126ac5b3b50717b29101b28 = L.circleMarker(
                [41.4023354, 2.2105777],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_df8a6a9edd764d2cc1dded66dd03305a = L.popup({"maxWidth": "100%"});

        
            
                var html_ed0d1954702bf85c0a3c390ff16b6578 = $(`<div id="html_ed0d1954702bf85c0a3c390ff16b6578" style="width: 100.0%; height: 100.0%;">Station 167<br>Result: -11.4%<br></div>`)[0];
                popup_df8a6a9edd764d2cc1dded66dd03305a.setContent(html_ed0d1954702bf85c0a3c390ff16b6578);
            
        

        circle_marker_e48923903126ac5b3b50717b29101b28.bindPopup(popup_df8a6a9edd764d2cc1dded66dd03305a)
        ;

        
    
    
            var circle_marker_1ece6f1aa6c8fc8d9d1f27cab7c4ff87 = L.circleMarker(
                [41.4053697, 2.2135818],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_931b7de30101009d45b6b5bb891802b5 = L.popup({"maxWidth": "100%"});

        
            
                var html_8a19ad271629075ab6efab46bbc64262 = $(`<div id="html_8a19ad271629075ab6efab46bbc64262" style="width: 100.0%; height: 100.0%;">Station 168<br>Result: -7.6%<br></div>`)[0];
                popup_931b7de30101009d45b6b5bb891802b5.setContent(html_8a19ad271629075ab6efab46bbc64262);
            
        

        circle_marker_1ece6f1aa6c8fc8d9d1f27cab7c4ff87.bindPopup(popup_931b7de30101009d45b6b5bb891802b5)
        ;

        
    
    
            var circle_marker_775720c7cefe0165e8375c9d381e0d53 = L.circleMarker(
                [41.3896642, 2.1999572],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2f3790c8338de35f0ed2881fa2be81a0 = L.popup({"maxWidth": "100%"});

        
            
                var html_174a28e35ebeb5c1ba5d2790e787351a = $(`<div id="html_174a28e35ebeb5c1ba5d2790e787351a" style="width: 100.0%; height: 100.0%;">Station 170<br>Result: -6.5%<br></div>`)[0];
                popup_2f3790c8338de35f0ed2881fa2be81a0.setContent(html_174a28e35ebeb5c1ba5d2790e787351a);
            
        

        circle_marker_775720c7cefe0165e8375c9d381e0d53.bindPopup(popup_2f3790c8338de35f0ed2881fa2be81a0)
        ;

        
    
    
            var circle_marker_2ca2947c6187bc5f8acafa1e0f664a6f = L.circleMarker(
                [41.3919877, 2.2037136],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8dc4ec349fd284ada8cba9db98c54a67 = L.popup({"maxWidth": "100%"});

        
            
                var html_f2797385646e67d3ad8750f28f2325fa = $(`<div id="html_f2797385646e67d3ad8750f28f2325fa" style="width: 100.0%; height: 100.0%;">Station 171<br>Result: -5.9%<br></div>`)[0];
                popup_8dc4ec349fd284ada8cba9db98c54a67.setContent(html_f2797385646e67d3ad8750f28f2325fa);
            
        

        circle_marker_2ca2947c6187bc5f8acafa1e0f664a6f.bindPopup(popup_8dc4ec349fd284ada8cba9db98c54a67)
        ;

        
    
    
            var circle_marker_d11f060d155e089c65fe71c365a51c31 = L.circleMarker(
                [41.3979002, 2.2088454],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_905158b840c4070309a15b011519daaa = L.popup({"maxWidth": "100%"});

        
            
                var html_b636ce6004cbd7303522288c6b361788 = $(`<div id="html_b636ce6004cbd7303522288c6b361788" style="width: 100.0%; height: 100.0%;">Station 173<br>Result: -8.0%<br></div>`)[0];
                popup_905158b840c4070309a15b011519daaa.setContent(html_b636ce6004cbd7303522288c6b361788);
            
        

        circle_marker_d11f060d155e089c65fe71c365a51c31.bindPopup(popup_905158b840c4070309a15b011519daaa)
        ;

        
    
    
            var circle_marker_4d33623e0f217d031d6f4965db1afaa2 = L.circleMarker(
                [41.400654, 2.210191],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_dbf17d954dc823c802cfcf1030a9a54f = L.popup({"maxWidth": "100%"});

        
            
                var html_ace4f6573164eeae13a4e8b578a418cd = $(`<div id="html_ace4f6573164eeae13a4e8b578a418cd" style="width: 100.0%; height: 100.0%;">Station 174<br>Result: -6.0%<br></div>`)[0];
                popup_dbf17d954dc823c802cfcf1030a9a54f.setContent(html_ace4f6573164eeae13a4e8b578a418cd);
            
        

        circle_marker_4d33623e0f217d031d6f4965db1afaa2.bindPopup(popup_dbf17d954dc823c802cfcf1030a9a54f)
        ;

        
    
    
            var circle_marker_89c5723031d5eebb6b847f7e106b9c69 = L.circleMarker(
                [41.4065291, 2.2091221],
                {"bubblingMouseEvents": true, "color": "#e77575ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e77575ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b6daa8000ea75f66acdf5af216d75a8a = L.popup({"maxWidth": "100%"});

        
            
                var html_1862b1cafc6197ae2922d6c5fc0fbfc1 = $(`<div id="html_1862b1cafc6197ae2922d6c5fc0fbfc1" style="width: 100.0%; height: 100.0%;">Station 175<br>Result: -2.2%<br></div>`)[0];
                popup_b6daa8000ea75f66acdf5af216d75a8a.setContent(html_1862b1cafc6197ae2922d6c5fc0fbfc1);
            
        

        circle_marker_89c5723031d5eebb6b847f7e106b9c69.bindPopup(popup_b6daa8000ea75f66acdf5af216d75a8a)
        ;

        
    
    
            var circle_marker_82bebe2ebd8266163031dcb9e217d017 = L.circleMarker(
                [41.403216, 2.2136],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_189fb139207b780b518d0ffcf92c1568 = L.popup({"maxWidth": "100%"});

        
            
                var html_78f5a58e9ee114d2c4c4b9f090930328 = $(`<div id="html_78f5a58e9ee114d2c4c4b9f090930328" style="width: 100.0%; height: 100.0%;">Station 176<br>Result: -5.6%<br></div>`)[0];
                popup_189fb139207b780b518d0ffcf92c1568.setContent(html_78f5a58e9ee114d2c4c4b9f090930328);
            
        

        circle_marker_82bebe2ebd8266163031dcb9e217d017.bindPopup(popup_189fb139207b780b518d0ffcf92c1568)
        ;

        
    
    
            var circle_marker_dfa4692da251fc26ff8d852f90f2f7ac = L.circleMarker(
                [41.4110754, 2.1809764],
                {"bubblingMouseEvents": true, "color": "#3a3af3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#3a3af3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4c64f5118804ab40f7df6ca37984f7e6 = L.popup({"maxWidth": "100%"});

        
            
                var html_45ab0ad65c6e80766c1c5aa2972a7732 = $(`<div id="html_45ab0ad65c6e80766c1c5aa2972a7732" style="width: 100.0%; height: 100.0%;">Station 177<br>Result: 3.6%<br></div>`)[0];
                popup_4c64f5118804ab40f7df6ca37984f7e6.setContent(html_45ab0ad65c6e80766c1c5aa2972a7732);
            
        

        circle_marker_dfa4692da251fc26ff8d852f90f2f7ac.bindPopup(popup_4c64f5118804ab40f7df6ca37984f7e6)
        ;

        
    
    
            var circle_marker_971044b9ab2289b79e2a3c640ff50de5 = L.circleMarker(
                [41.4053649, 2.2162094],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_05282f527cdceeebe2512f3f20ec38f4 = L.popup({"maxWidth": "100%"});

        
            
                var html_584ec6045596e0991b8c300cc1d405e1 = $(`<div id="html_584ec6045596e0991b8c300cc1d405e1" style="width: 100.0%; height: 100.0%;">Station 178<br>Result: -5.0%<br></div>`)[0];
                popup_05282f527cdceeebe2512f3f20ec38f4.setContent(html_584ec6045596e0991b8c300cc1d405e1);
            
        

        circle_marker_971044b9ab2289b79e2a3c640ff50de5.bindPopup(popup_05282f527cdceeebe2512f3f20ec38f4)
        ;

        
    
    
            var circle_marker_7b382343246bda333e2de9f4d0a17102 = L.circleMarker(
                [41.36352, 2.1369015],
                {"bubblingMouseEvents": true, "color": "#b7b7d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b7b7d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4ea0411f90c77315c2a121a8ccd36dd0 = L.popup({"maxWidth": "100%"});

        
            
                var html_b054ad24ab0305942afcbe1807835f7c = $(`<div id="html_b054ad24ab0305942afcbe1807835f7c" style="width: 100.0%; height: 100.0%;">Station 179<br>Result: 0.7%<br></div>`)[0];
                popup_4ea0411f90c77315c2a121a8ccd36dd0.setContent(html_b054ad24ab0305942afcbe1807835f7c);
            
        

        circle_marker_7b382343246bda333e2de9f4d0a17102.bindPopup(popup_4ea0411f90c77315c2a121a8ccd36dd0)
        ;

        
    
    
            var circle_marker_28e2ec853e33de5adaaef96dbed16bee = L.circleMarker(
                [41.3675574, 2.1388216],
                {"bubblingMouseEvents": true, "color": "#d6c8c8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c8c8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_31ffbb3a0e1f597ec07ebb2a5c9d818d = L.popup({"maxWidth": "100%"});

        
            
                var html_582cc82aea6f115d77f10dcddf0a3cc3 = $(`<div id="html_582cc82aea6f115d77f10dcddf0a3cc3" style="width: 100.0%; height: 100.0%;">Station 180<br>Result: -0.3%<br></div>`)[0];
                popup_31ffbb3a0e1f597ec07ebb2a5c9d818d.setContent(html_582cc82aea6f115d77f10dcddf0a3cc3);
            
        

        circle_marker_28e2ec853e33de5adaaef96dbed16bee.bindPopup(popup_31ffbb3a0e1f597ec07ebb2a5c9d818d)
        ;

        
    
    
            var circle_marker_ffa5d69045225306a86400efb5d9a9b3 = L.circleMarker(
                [41.371366, 2.143565],
                {"bubblingMouseEvents": true, "color": "#c0c0d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c0c0d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e707073204c72fa25dbb608fc491c385 = L.popup({"maxWidth": "100%"});

        
            
                var html_3dcc089d5d7f63a3f0cb1c11f9134ddd = $(`<div id="html_3dcc089d5d7f63a3f0cb1c11f9134ddd" style="width: 100.0%; height: 100.0%;">Station 182<br>Result: 0.5%<br></div>`)[0];
                popup_e707073204c72fa25dbb608fc491c385.setContent(html_3dcc089d5d7f63a3f0cb1c11f9134ddd);
            
        

        circle_marker_ffa5d69045225306a86400efb5d9a9b3.bindPopup(popup_e707073204c72fa25dbb608fc491c385)
        ;

        
    
    
            var circle_marker_813a4700efd48374606785b9d5cf8b94 = L.circleMarker(
                [41.3723682, 2.1419494],
                {"bubblingMouseEvents": true, "color": "#aeaedbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#aeaedbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_79fa5191b96ddc4612526cf6138389bf = L.popup({"maxWidth": "100%"});

        
            
                var html_02bd90bdea9463a5a76f1cbada011890 = $(`<div id="html_02bd90bdea9463a5a76f1cbada011890" style="width: 100.0%; height: 100.0%;">Station 183<br>Result: 0.9%<br></div>`)[0];
                popup_79fa5191b96ddc4612526cf6138389bf.setContent(html_02bd90bdea9463a5a76f1cbada011890);
            
        

        circle_marker_813a4700efd48374606785b9d5cf8b94.bindPopup(popup_79fa5191b96ddc4612526cf6138389bf)
        ;

        
    
    
            var circle_marker_09f96d92a9c757c03f1fe219946a8146 = L.circleMarker(
                [41.3675438, 2.1342316],
                {"bubblingMouseEvents": true, "color": "#babad9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#babad9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_71af5061a1c9b2af17b019557ab5df44 = L.popup({"maxWidth": "100%"});

        
            
                var html_74bb8bded55ac8b83bb823893a026694 = $(`<div id="html_74bb8bded55ac8b83bb823893a026694" style="width: 100.0%; height: 100.0%;">Station 184<br>Result: 0.6%<br></div>`)[0];
                popup_71af5061a1c9b2af17b019557ab5df44.setContent(html_74bb8bded55ac8b83bb823893a026694);
            
        

        circle_marker_09f96d92a9c757c03f1fe219946a8146.bindPopup(popup_71af5061a1c9b2af17b019557ab5df44)
        ;

        
    
    
            var circle_marker_48389958c2d664803371a76122821a10 = L.circleMarker(
                [41.3703717, 2.1389439],
                {"bubblingMouseEvents": true, "color": "#b5b5daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b5b5daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a76a0154f76e7b7a094e963e54a853e4 = L.popup({"maxWidth": "100%"});

        
            
                var html_f2bc044b5086ad0f8885eaf3f82dd2ae = $(`<div id="html_f2bc044b5086ad0f8885eaf3f82dd2ae" style="width: 100.0%; height: 100.0%;">Station 185<br>Result: 0.7%<br></div>`)[0];
                popup_a76a0154f76e7b7a094e963e54a853e4.setContent(html_f2bc044b5086ad0f8885eaf3f82dd2ae);
            
        

        circle_marker_48389958c2d664803371a76122821a10.bindPopup(popup_a76a0154f76e7b7a094e963e54a853e4)
        ;

        
    
    
            var circle_marker_3974b859e042134122d8f3b3d01a21cb = L.circleMarker(
                [41.3755503, 2.1439036],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_378a7b0b3c2f0c939425d640439c4923 = L.popup({"maxWidth": "100%"});

        
            
                var html_dc24299460bf5511af3ac6077fc01925 = $(`<div id="html_dc24299460bf5511af3ac6077fc01925" style="width: 100.0%; height: 100.0%;">Station 186<br>Result: 0.9%<br></div>`)[0];
                popup_378a7b0b3c2f0c939425d640439c4923.setContent(html_dc24299460bf5511af3ac6077fc01925);
            
        

        circle_marker_3974b859e042134122d8f3b3d01a21cb.bindPopup(popup_378a7b0b3c2f0c939425d640439c4923)
        ;

        
    
    
            var circle_marker_380696fd40ee61ab49981e4233e0d81d = L.circleMarker(
                [41.3768806, 2.1698206],
                {"bubblingMouseEvents": true, "color": "#9494e1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9494e1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_74245f01012e96005c133e658f9cd11f = L.popup({"maxWidth": "100%"});

        
            
                var html_2bcac894445d381a43ea63df6008be9b = $(`<div id="html_2bcac894445d381a43ea63df6008be9b" style="width: 100.0%; height: 100.0%;">Station 187<br>Result: 1.5%<br></div>`)[0];
                popup_74245f01012e96005c133e658f9cd11f.setContent(html_2bcac894445d381a43ea63df6008be9b);
            
        

        circle_marker_380696fd40ee61ab49981e4233e0d81d.bindPopup(popup_74245f01012e96005c133e658f9cd11f)
        ;

        
    
    
            var circle_marker_f5ffc1bce12977f621ced67f5373e812 = L.circleMarker(
                [41.3756948, 2.1358571],
                {"bubblingMouseEvents": true, "color": "#7979e6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7979e6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_874f6f94669097ad6672683e3c314d46 = L.popup({"maxWidth": "100%"});

        
            
                var html_e02548d74a9cd3d5f2d603c29ed3a453 = $(`<div id="html_e02548d74a9cd3d5f2d603c29ed3a453" style="width: 100.0%; height: 100.0%;">Station 188<br>Result: 2.1%<br></div>`)[0];
                popup_874f6f94669097ad6672683e3c314d46.setContent(html_e02548d74a9cd3d5f2d603c29ed3a453);
            
        

        circle_marker_f5ffc1bce12977f621ced67f5373e812.bindPopup(popup_874f6f94669097ad6672683e3c314d46)
        ;

        
    
    
            var circle_marker_52931f5f8305f087f8d4b1f9ef035d5d = L.circleMarker(
                [41.3969839, 2.1661852],
                {"bubblingMouseEvents": true, "color": "#a1a1deff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a1a1deff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_208f965aaa9aa5043d3bf7f9991b74a4 = L.popup({"maxWidth": "100%"});

        
            
                var html_414a4fe4bd4c80fde859373afd8040c9 = $(`<div id="html_414a4fe4bd4c80fde859373afd8040c9" style="width: 100.0%; height: 100.0%;">Station 189<br>Result: 1.2%<br></div>`)[0];
                popup_208f965aaa9aa5043d3bf7f9991b74a4.setContent(html_414a4fe4bd4c80fde859373afd8040c9);
            
        

        circle_marker_52931f5f8305f087f8d4b1f9ef035d5d.bindPopup(popup_208f965aaa9aa5043d3bf7f9991b74a4)
        ;

        
    
    
            var circle_marker_c10edd095a94d874619ba4a98eaef5f1 = L.circleMarker(
                [41.3961412, 2.2078439],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_502e906fd221a03282b46b1625ba4968 = L.popup({"maxWidth": "100%"});

        
            
                var html_efa3a40ffa09bc5eac54510ef501865a = $(`<div id="html_efa3a40ffa09bc5eac54510ef501865a" style="width: 100.0%; height: 100.0%;">Station 190<br>Result: -9.5%<br></div>`)[0];
                popup_502e906fd221a03282b46b1625ba4968.setContent(html_efa3a40ffa09bc5eac54510ef501865a);
            
        

        circle_marker_c10edd095a94d874619ba4a98eaef5f1.bindPopup(popup_502e906fd221a03282b46b1625ba4968)
        ;

        
    
    
            var circle_marker_04de64ca0ab3f9b3438eb5829e25d973 = L.circleMarker(
                [41.3786364, 2.1335494],
                {"bubblingMouseEvents": true, "color": "#8484e4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8484e4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2adae4c9c50376fbe4a342a4f0cd7110 = L.popup({"maxWidth": "100%"});

        
            
                var html_ef1e56c0d6673ba1ff29fcaa64a40026 = $(`<div id="html_ef1e56c0d6673ba1ff29fcaa64a40026" style="width: 100.0%; height: 100.0%;">Station 192<br>Result: 1.9%<br></div>`)[0];
                popup_2adae4c9c50376fbe4a342a4f0cd7110.setContent(html_ef1e56c0d6673ba1ff29fcaa64a40026);
            
        

        circle_marker_04de64ca0ab3f9b3438eb5829e25d973.bindPopup(popup_2adae4c9c50376fbe4a342a4f0cd7110)
        ;

        
    
    
            var circle_marker_2889fd41314de03745d89dfd1902b9de = L.circleMarker(
                [41.3812979, 2.1289917],
                {"bubblingMouseEvents": true, "color": "#b4b4daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b4b4daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_bdc3bf8cfec5624b33b55675c0e67764 = L.popup({"maxWidth": "100%"});

        
            
                var html_a61b18cbb8b634aea19a83b847e8cc29 = $(`<div id="html_a61b18cbb8b634aea19a83b847e8cc29" style="width: 100.0%; height: 100.0%;">Station 193<br>Result: 0.7%<br></div>`)[0];
                popup_bdc3bf8cfec5624b33b55675c0e67764.setContent(html_a61b18cbb8b634aea19a83b847e8cc29);
            
        

        circle_marker_2889fd41314de03745d89dfd1902b9de.bindPopup(popup_bdc3bf8cfec5624b33b55675c0e67764)
        ;

        
    
    
            var circle_marker_6a54ddb10c3538674d203fdb613893ca = L.circleMarker(
                [41.3812001, 2.1323612],
                {"bubblingMouseEvents": true, "color": "#a0a0deff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a0a0deff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f4f976878e42abf50457964740eb8467 = L.popup({"maxWidth": "100%"});

        
            
                var html_f15103665c358d84b260e4edbcadca5a = $(`<div id="html_f15103665c358d84b260e4edbcadca5a" style="width: 100.0%; height: 100.0%;">Station 194<br>Result: 1.2%<br></div>`)[0];
                popup_f4f976878e42abf50457964740eb8467.setContent(html_f15103665c358d84b260e4edbcadca5a);
            
        

        circle_marker_6a54ddb10c3538674d203fdb613893ca.bindPopup(popup_f4f976878e42abf50457964740eb8467)
        ;

        
    
    
            var circle_marker_f3c9b15c0cbd50dba92d953ced0eae99 = L.circleMarker(
                [41.3821371, 2.1354149],
                {"bubblingMouseEvents": true, "color": "#b8b8d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b8b8d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ea405de83516bd8d205f7b91c49ea489 = L.popup({"maxWidth": "100%"});

        
            
                var html_2a237d1165066d8fc62c1555bae928d1 = $(`<div id="html_2a237d1165066d8fc62c1555bae928d1" style="width: 100.0%; height: 100.0%;">Station 195<br>Result: 0.7%<br></div>`)[0];
                popup_ea405de83516bd8d205f7b91c49ea489.setContent(html_2a237d1165066d8fc62c1555bae928d1);
            
        

        circle_marker_f3c9b15c0cbd50dba92d953ced0eae99.bindPopup(popup_ea405de83516bd8d205f7b91c49ea489)
        ;

        
    
    
            var circle_marker_8b2c32610dd2aa68b92f3fdaa5d4ef2b = L.circleMarker(
                [41.3832609, 2.1392662],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9727c246f1d8da71b76122ad4e2e9d40 = L.popup({"maxWidth": "100%"});

        
            
                var html_d3d948821bc426f6bae69d783d5818e6 = $(`<div id="html_d3d948821bc426f6bae69d783d5818e6" style="width: 100.0%; height: 100.0%;">Station 196<br>Result: 0.9%<br></div>`)[0];
                popup_9727c246f1d8da71b76122ad4e2e9d40.setContent(html_d3d948821bc426f6bae69d783d5818e6);
            
        

        circle_marker_8b2c32610dd2aa68b92f3fdaa5d4ef2b.bindPopup(popup_9727c246f1d8da71b76122ad4e2e9d40)
        ;

        
    
    
            var circle_marker_fafcf0767de5b6c88728308b16a3c7ef = L.circleMarker(
                [41.3871579, 2.1410945],
                {"bubblingMouseEvents": true, "color": "#aeaedbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#aeaedbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_43c5335a63084256f98e272a71351dd0 = L.popup({"maxWidth": "100%"});

        
            
                var html_3a8a6dd1c7d7342d311ff12ab7bcea17 = $(`<div id="html_3a8a6dd1c7d7342d311ff12ab7bcea17" style="width: 100.0%; height: 100.0%;">Station 197<br>Result: 0.9%<br></div>`)[0];
                popup_43c5335a63084256f98e272a71351dd0.setContent(html_3a8a6dd1c7d7342d311ff12ab7bcea17);
            
        

        circle_marker_fafcf0767de5b6c88728308b16a3c7ef.bindPopup(popup_43c5335a63084256f98e272a71351dd0)
        ;

        
    
    
            var circle_marker_0050aec3355857fccb2877cc6de2db30 = L.circleMarker(
                [41.3847113, 2.1334379],
                {"bubblingMouseEvents": true, "color": "#c0c0d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c0c0d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f4e6219eb666564dc32bf460f6a42ad2 = L.popup({"maxWidth": "100%"});

        
            
                var html_42ec495e167ee655198cae8c83bf00ed = $(`<div id="html_42ec495e167ee655198cae8c83bf00ed" style="width: 100.0%; height: 100.0%;">Station 198<br>Result: 0.4%<br></div>`)[0];
                popup_f4e6219eb666564dc32bf460f6a42ad2.setContent(html_42ec495e167ee655198cae8c83bf00ed);
            
        

        circle_marker_0050aec3355857fccb2877cc6de2db30.bindPopup(popup_f4e6219eb666564dc32bf460f6a42ad2)
        ;

        
    
    
            var circle_marker_29fb2d393e0288856e81fd3dd9ad8e74 = L.circleMarker(
                [41.3819739, 2.1268625],
                {"bubblingMouseEvents": true, "color": "#b0b0dbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b0b0dbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e1430c081a35357e6d1a699c89242a2f = L.popup({"maxWidth": "100%"});

        
            
                var html_60ec66f0400267aa3c45fa62885fad32 = $(`<div id="html_60ec66f0400267aa3c45fa62885fad32" style="width: 100.0%; height: 100.0%;">Station 199<br>Result: 0.8%<br></div>`)[0];
                popup_e1430c081a35357e6d1a699c89242a2f.setContent(html_60ec66f0400267aa3c45fa62885fad32);
            
        

        circle_marker_29fb2d393e0288856e81fd3dd9ad8e74.bindPopup(popup_e1430c081a35357e6d1a699c89242a2f)
        ;

        
    
    
            var circle_marker_dc4680c5e396793a6601e61f1e8b99cf = L.circleMarker(
                [41.3839045, 2.1312876],
                {"bubblingMouseEvents": true, "color": "#b1b1daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b1b1daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_be2f8fb92302f1c6c759c11eb69c4d87 = L.popup({"maxWidth": "100%"});

        
            
                var html_342a7661a7f2014edf669f6db653eb20 = $(`<div id="html_342a7661a7f2014edf669f6db653eb20" style="width: 100.0%; height: 100.0%;">Station 200<br>Result: 0.8%<br></div>`)[0];
                popup_be2f8fb92302f1c6c759c11eb69c4d87.setContent(html_342a7661a7f2014edf669f6db653eb20);
            
        

        circle_marker_dc4680c5e396793a6601e61f1e8b99cf.bindPopup(popup_be2f8fb92302f1c6c759c11eb69c4d87)
        ;

        
    
    
            var circle_marker_274adcbe25e7cc007366a911e216183f = L.circleMarker(
                [41.3878061, 2.1344218],
                {"bubblingMouseEvents": true, "color": "#c5c5d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c5c5d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7883bcf6d4d47fb145f6c31b5d014018 = L.popup({"maxWidth": "100%"});

        
            
                var html_c0054fcf818dcdd36766221e653b65c2 = $(`<div id="html_c0054fcf818dcdd36766221e653b65c2" style="width: 100.0%; height: 100.0%;">Station 201<br>Result: 0.3%<br></div>`)[0];
                popup_7883bcf6d4d47fb145f6c31b5d014018.setContent(html_c0054fcf818dcdd36766221e653b65c2);
            
        

        circle_marker_274adcbe25e7cc007366a911e216183f.bindPopup(popup_7883bcf6d4d47fb145f6c31b5d014018)
        ;

        
    
    
            var circle_marker_1c1ad83d97cf347c1d690926c3ba532c = L.circleMarker(
                [41.3854466, 2.1288753],
                {"bubblingMouseEvents": true, "color": "#b9b9d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b9b9d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4886e5e91a335cde41358ca19cf16fc1 = L.popup({"maxWidth": "100%"});

        
            
                var html_3c98938c8cea006011b9b88c5300edaf = $(`<div id="html_3c98938c8cea006011b9b88c5300edaf" style="width: 100.0%; height: 100.0%;">Station 202<br>Result: 0.6%<br></div>`)[0];
                popup_4886e5e91a335cde41358ca19cf16fc1.setContent(html_3c98938c8cea006011b9b88c5300edaf);
            
        

        circle_marker_1c1ad83d97cf347c1d690926c3ba532c.bindPopup(popup_4886e5e91a335cde41358ca19cf16fc1)
        ;

        
    
    
            var circle_marker_d38c70cdeebfb4935418b1447cfa0ad7 = L.circleMarker(
                [41.3887069, 2.1285766],
                {"bubblingMouseEvents": true, "color": "#6a6ae9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6a6ae9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8c38a92b10c3a7b7750edbd1fd810b0d = L.popup({"maxWidth": "100%"});

        
            
                var html_daa4aba863dc1402f7f3c47572cb20cf = $(`<div id="html_daa4aba863dc1402f7f3c47572cb20cf" style="width: 100.0%; height: 100.0%;">Station 203<br>Result: 2.5%<br></div>`)[0];
                popup_8c38a92b10c3a7b7750edbd1fd810b0d.setContent(html_daa4aba863dc1402f7f3c47572cb20cf);
            
        

        circle_marker_d38c70cdeebfb4935418b1447cfa0ad7.bindPopup(popup_8c38a92b10c3a7b7750edbd1fd810b0d)
        ;

        
    
    
            var circle_marker_edc6c7c674e5126e12c0f84425e0f0a6 = L.circleMarker(
                [41.3880355, 2.1256248],
                {"bubblingMouseEvents": true, "color": "#babad9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#babad9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4dbdd91a38ed7e925cf0dc3213438566 = L.popup({"maxWidth": "100%"});

        
            
                var html_27660dc03ae285dfb9ba3460c4366229 = $(`<div id="html_27660dc03ae285dfb9ba3460c4366229" style="width: 100.0%; height: 100.0%;">Station 204<br>Result: 0.6%<br></div>`)[0];
                popup_4dbdd91a38ed7e925cf0dc3213438566.setContent(html_27660dc03ae285dfb9ba3460c4366229);
            
        

        circle_marker_edc6c7c674e5126e12c0f84425e0f0a6.bindPopup(popup_4dbdd91a38ed7e925cf0dc3213438566)
        ;

        
    
    
            var circle_marker_1f7ff16c81b73b4cf86d07957a422313 = L.circleMarker(
                [41.387561, 2.1306737],
                {"bubblingMouseEvents": true, "color": "#8e8ee2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8e8ee2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b9e7d5cc3c01d4d0b6c6cb0caef2e6fe = L.popup({"maxWidth": "100%"});

        
            
                var html_0e1dd4cbb95fad6fc9b07cf022a6d131 = $(`<div id="html_0e1dd4cbb95fad6fc9b07cf022a6d131" style="width: 100.0%; height: 100.0%;">Station 205<br>Result: 1.6%<br></div>`)[0];
                popup_b9e7d5cc3c01d4d0b6c6cb0caef2e6fe.setContent(html_0e1dd4cbb95fad6fc9b07cf022a6d131);
            
        

        circle_marker_1f7ff16c81b73b4cf86d07957a422313.bindPopup(popup_b9e7d5cc3c01d4d0b6c6cb0caef2e6fe)
        ;

        
    
    
            var circle_marker_d1c22f18bb2c282355f1c00b37cef384 = L.circleMarker(
                [41.3897943, 2.1328634],
                {"bubblingMouseEvents": true, "color": "#d6c5c5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c5c5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_086f5c316b6d724fdb89226d9ffb0551 = L.popup({"maxWidth": "100%"});

        
            
                var html_71ff7a91bd98f26cfd0fe23451cd60dd = $(`<div id="html_71ff7a91bd98f26cfd0fe23451cd60dd" style="width: 100.0%; height: 100.0%;">Station 206<br>Result: -0.3%<br></div>`)[0];
                popup_086f5c316b6d724fdb89226d9ffb0551.setContent(html_71ff7a91bd98f26cfd0fe23451cd60dd);
            
        

        circle_marker_d1c22f18bb2c282355f1c00b37cef384.bindPopup(popup_086f5c316b6d724fdb89226d9ffb0551)
        ;

        
    
    
            var circle_marker_eb4265ba3a7e6eefb2521225d378287c = L.circleMarker(
                [41.3908477, 2.136579],
                {"bubblingMouseEvents": true, "color": "#d5cbcbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5cbcbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_da11e94bc1c4cf7f01ea8dcbea537b93 = L.popup({"maxWidth": "100%"});

        
            
                var html_8de2305a9f0b5b7446986cbe302ac135 = $(`<div id="html_8de2305a9f0b5b7446986cbe302ac135" style="width: 100.0%; height: 100.0%;">Station 207<br>Result: -0.2%<br></div>`)[0];
                popup_da11e94bc1c4cf7f01ea8dcbea537b93.setContent(html_8de2305a9f0b5b7446986cbe302ac135);
            
        

        circle_marker_eb4265ba3a7e6eefb2521225d378287c.bindPopup(popup_da11e94bc1c4cf7f01ea8dcbea537b93)
        ;

        
    
    
            var circle_marker_ebcedb85c4b17447b6b8f489d16415d0 = L.circleMarker(
                [41.3915195, 2.1390667],
                {"bubblingMouseEvents": true, "color": "#d4d0d0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4d0d0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2b60f46d584c3fe077fdea77659ab523 = L.popup({"maxWidth": "100%"});

        
            
                var html_95c1e998f4efaae412207bfdfa9ec35a = $(`<div id="html_95c1e998f4efaae412207bfdfa9ec35a" style="width: 100.0%; height: 100.0%;">Station 208<br>Result: -0.1%<br></div>`)[0];
                popup_2b60f46d584c3fe077fdea77659ab523.setContent(html_95c1e998f4efaae412207bfdfa9ec35a);
            
        

        circle_marker_ebcedb85c4b17447b6b8f489d16415d0.bindPopup(popup_2b60f46d584c3fe077fdea77659ab523)
        ;

        
    
    
            var circle_marker_900c07e973a5dfbe92fcf725391ad70e = L.circleMarker(
                [41.3857425, 2.1610515],
                {"bubblingMouseEvents": true, "color": "#6363ebff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6363ebff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_40bd15bebbeb6ac55920eb07346be246 = L.popup({"maxWidth": "100%"});

        
            
                var html_f789815027c0c20082da7358a7ee329e = $(`<div id="html_f789815027c0c20082da7358a7ee329e" style="width: 100.0%; height: 100.0%;">Station 209<br>Result: 2.7%<br></div>`)[0];
                popup_40bd15bebbeb6ac55920eb07346be246.setContent(html_f789815027c0c20082da7358a7ee329e);
            
        

        circle_marker_900c07e973a5dfbe92fcf725391ad70e.bindPopup(popup_40bd15bebbeb6ac55920eb07346be246)
        ;

        
    
    
            var circle_marker_e85eba23cdeb03ecebf7399c9c53fc91 = L.circleMarker(
                [41.3745238, 2.1422556],
                {"bubblingMouseEvents": true, "color": "#b8b8d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b8b8d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_107ae7fcf3edd1546e7ee2be7ecd4fa9 = L.popup({"maxWidth": "100%"});

        
            
                var html_ecf2a46cbb2a53d34e49e29a16f1ee47 = $(`<div id="html_ecf2a46cbb2a53d34e49e29a16f1ee47" style="width: 100.0%; height: 100.0%;">Station 210<br>Result: 0.6%<br></div>`)[0];
                popup_107ae7fcf3edd1546e7ee2be7ecd4fa9.setContent(html_ecf2a46cbb2a53d34e49e29a16f1ee47);
            
        

        circle_marker_e85eba23cdeb03ecebf7399c9c53fc91.bindPopup(popup_107ae7fcf3edd1546e7ee2be7ecd4fa9)
        ;

        
    
    
            var circle_marker_99f203d6b95f41f92227e666666f71bf = L.circleMarker(
                [41.3922355, 2.1309272],
                {"bubblingMouseEvents": true, "color": "#d7c4c4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c4c4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d9f9478ab9824e25e86ff3c3257ac742 = L.popup({"maxWidth": "100%"});

        
            
                var html_83608d5012866fc164b905da91592ca8 = $(`<div id="html_83608d5012866fc164b905da91592ca8" style="width: 100.0%; height: 100.0%;">Station 212<br>Result: -0.4%<br></div>`)[0];
                popup_d9f9478ab9824e25e86ff3c3257ac742.setContent(html_83608d5012866fc164b905da91592ca8);
            
        

        circle_marker_99f203d6b95f41f92227e666666f71bf.bindPopup(popup_d9f9478ab9824e25e86ff3c3257ac742)
        ;

        
    
    
            var circle_marker_6f0014c45e0a00e81d31312b095a7262 = L.circleMarker(
                [41.3935816, 2.1345892],
                {"bubblingMouseEvents": true, "color": "#c0c0d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c0c0d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e4c0b3e11f62885c0b5c426e82725873 = L.popup({"maxWidth": "100%"});

        
            
                var html_4c0bda26eafe201a1c8a5e308b0e0f9a = $(`<div id="html_4c0bda26eafe201a1c8a5e308b0e0f9a" style="width: 100.0%; height: 100.0%;">Station 213<br>Result: 0.5%<br></div>`)[0];
                popup_e4c0b3e11f62885c0b5c426e82725873.setContent(html_4c0bda26eafe201a1c8a5e308b0e0f9a);
            
        

        circle_marker_6f0014c45e0a00e81d31312b095a7262.bindPopup(popup_e4c0b3e11f62885c0b5c426e82725873)
        ;

        
    
    
            var circle_marker_c011ddaf3eab73830f6175a5ab62c289 = L.circleMarker(
                [41.3952027, 2.1334873],
                {"bubblingMouseEvents": true, "color": "#a8a8dcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a8a8dcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e9cdbdd6a265a2d630cdda1a65b45dc5 = L.popup({"maxWidth": "100%"});

        
            
                var html_485e7f3e0062c2e043d6989cc7d662f5 = $(`<div id="html_485e7f3e0062c2e043d6989cc7d662f5" style="width: 100.0%; height: 100.0%;">Station 214<br>Result: 1.0%<br></div>`)[0];
                popup_e9cdbdd6a265a2d630cdda1a65b45dc5.setContent(html_485e7f3e0062c2e043d6989cc7d662f5);
            
        

        circle_marker_c011ddaf3eab73830f6175a5ab62c289.bindPopup(popup_e9cdbdd6a265a2d630cdda1a65b45dc5)
        ;

        
    
    
            var circle_marker_cad331ee789b0b260640b8c65e729d32 = L.circleMarker(
                [41.3939378, 2.1380304],
                {"bubblingMouseEvents": true, "color": "#d9b9b9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d9b9b9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_12bea2c28095027344cc4bc6f6d6ae2d = L.popup({"maxWidth": "100%"});

        
            
                var html_8b6d9bdaba58d5e4b65e41c6aeacf3cb = $(`<div id="html_8b6d9bdaba58d5e4b65e41c6aeacf3cb" style="width: 100.0%; height: 100.0%;">Station 215<br>Result: -0.6%<br></div>`)[0];
                popup_12bea2c28095027344cc4bc6f6d6ae2d.setContent(html_8b6d9bdaba58d5e4b65e41c6aeacf3cb);
            
        

        circle_marker_cad331ee789b0b260640b8c65e729d32.bindPopup(popup_12bea2c28095027344cc4bc6f6d6ae2d)
        ;

        
    
    
            var circle_marker_a68d2c4c81c71317b65fd68891559b58 = L.circleMarker(
                [41.3967824, 2.1445567],
                {"bubblingMouseEvents": true, "color": "#c6c6d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c6c6d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ad8d70521325dd906bda0ae701d6094f = L.popup({"maxWidth": "100%"});

        
            
                var html_c44168504ac1bb878551dfb1bc961a58 = $(`<div id="html_c44168504ac1bb878551dfb1bc961a58" style="width: 100.0%; height: 100.0%;">Station 216<br>Result: 0.3%<br></div>`)[0];
                popup_ad8d70521325dd906bda0ae701d6094f.setContent(html_c44168504ac1bb878551dfb1bc961a58);
            
        

        circle_marker_a68d2c4c81c71317b65fd68891559b58.bindPopup(popup_ad8d70521325dd906bda0ae701d6094f)
        ;

        
    
    
            var circle_marker_2e599599ea917ac7a4f55f7e897bcccb = L.circleMarker(
                [41.3985735, 2.1440826],
                {"bubblingMouseEvents": true, "color": "#bfbfd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bfbfd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f1cbfdeb6fd88592f6b3c9c0ba923197 = L.popup({"maxWidth": "100%"});

        
            
                var html_639dc1d4886242c74dd97fa9b9b5f421 = $(`<div id="html_639dc1d4886242c74dd97fa9b9b5f421" style="width: 100.0%; height: 100.0%;">Station 217<br>Result: 0.5%<br></div>`)[0];
                popup_f1cbfdeb6fd88592f6b3c9c0ba923197.setContent(html_639dc1d4886242c74dd97fa9b9b5f421);
            
        

        circle_marker_2e599599ea917ac7a4f55f7e897bcccb.bindPopup(popup_f1cbfdeb6fd88592f6b3c9c0ba923197)
        ;

        
    
    
            var circle_marker_cd36ecd09df3e8df8b0ddb24ccd716be = L.circleMarker(
                [41.4040364, 2.183145],
                {"bubblingMouseEvents": true, "color": "#2424f8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#2424f8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_265ee0224e5afd96138c691230f20c3d = L.popup({"maxWidth": "100%"});

        
            
                var html_904a8d9f91cb1cc812066d39bff2e3c4 = $(`<div id="html_904a8d9f91cb1cc812066d39bff2e3c4" style="width: 100.0%; height: 100.0%;">Station 218<br>Result: 4.1%<br></div>`)[0];
                popup_265ee0224e5afd96138c691230f20c3d.setContent(html_904a8d9f91cb1cc812066d39bff2e3c4);
            
        

        circle_marker_cd36ecd09df3e8df8b0ddb24ccd716be.bindPopup(popup_265ee0224e5afd96138c691230f20c3d)
        ;

        
    
    
            var circle_marker_2619e942bedd133b872cb023bd7c8173 = L.circleMarker(
                [41.3976165, 2.1471724],
                {"bubblingMouseEvents": true, "color": "#a1a1deff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a1a1deff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4dbb46de2c95c6802bc32291fe8ec8a0 = L.popup({"maxWidth": "100%"});

        
            
                var html_41970f2a0907ef1af642c9dbf3615654 = $(`<div id="html_41970f2a0907ef1af642c9dbf3615654" style="width: 100.0%; height: 100.0%;">Station 219<br>Result: 1.2%<br></div>`)[0];
                popup_4dbb46de2c95c6802bc32291fe8ec8a0.setContent(html_41970f2a0907ef1af642c9dbf3615654);
            
        

        circle_marker_2619e942bedd133b872cb023bd7c8173.bindPopup(popup_4dbb46de2c95c6802bc32291fe8ec8a0)
        ;

        
    
    
            var circle_marker_ec4e444334150f201f8aa2a413278fab = L.circleMarker(
                [41.3960982, 2.1513154],
                {"bubblingMouseEvents": true, "color": "#3131f5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#3131f5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_bd30eb6ab7f30d4578136b9e961a6336 = L.popup({"maxWidth": "100%"});

        
            
                var html_cb377a8e19f8db90961fb5210382d169 = $(`<div id="html_cb377a8e19f8db90961fb5210382d169" style="width: 100.0%; height: 100.0%;">Station 220<br>Result: 3.8%<br></div>`)[0];
                popup_bd30eb6ab7f30d4578136b9e961a6336.setContent(html_cb377a8e19f8db90961fb5210382d169);
            
        

        circle_marker_ec4e444334150f201f8aa2a413278fab.bindPopup(popup_bd30eb6ab7f30d4578136b9e961a6336)
        ;

        
    
    
            var circle_marker_ae55a4f4bfdaf4a284fe41bc312e5e8b = L.circleMarker(
                [41.4025392, 2.1524704],
                {"bubblingMouseEvents": true, "color": "#d4cfcfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4cfcfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c84d91a8a2ab8d8fda44b54816b86a0e = L.popup({"maxWidth": "100%"});

        
            
                var html_e7d9b82fd64d1fa9f511ad3e4ee8b85d = $(`<div id="html_e7d9b82fd64d1fa9f511ad3e4ee8b85d" style="width: 100.0%; height: 100.0%;">Station 221<br>Result: -0.1%<br></div>`)[0];
                popup_c84d91a8a2ab8d8fda44b54816b86a0e.setContent(html_e7d9b82fd64d1fa9f511ad3e4ee8b85d);
            
        

        circle_marker_ae55a4f4bfdaf4a284fe41bc312e5e8b.bindPopup(popup_c84d91a8a2ab8d8fda44b54816b86a0e)
        ;

        
    
    
            var circle_marker_0f9aecbe63e3e8b29228d3600b45d088 = L.circleMarker(
                [41.4013296, 2.1574439],
                {"bubblingMouseEvents": true, "color": "#b6b6d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b6b6d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2eabe38f9a434f93af19af835c026ea8 = L.popup({"maxWidth": "100%"});

        
            
                var html_b8c4ce5ee0465b7e5c0fe432e6f23f27 = $(`<div id="html_b8c4ce5ee0465b7e5c0fe432e6f23f27" style="width: 100.0%; height: 100.0%;">Station 222<br>Result: 0.7%<br></div>`)[0];
                popup_2eabe38f9a434f93af19af835c026ea8.setContent(html_b8c4ce5ee0465b7e5c0fe432e6f23f27);
            
        

        circle_marker_0f9aecbe63e3e8b29228d3600b45d088.bindPopup(popup_2eabe38f9a434f93af19af835c026ea8)
        ;

        
    
    
            var circle_marker_b289820806b26220fe412a35a758da0c = L.circleMarker(
                [41.3983444, 2.1598243],
                {"bubblingMouseEvents": true, "color": "#5353eeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5353eeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_03ed3771463aaa697a57f3c7c77b3659 = L.popup({"maxWidth": "100%"});

        
            
                var html_766ac4242209e5a7a2da3414f242047a = $(`<div id="html_766ac4242209e5a7a2da3414f242047a" style="width: 100.0%; height: 100.0%;">Station 223<br>Result: 3.0%<br></div>`)[0];
                popup_03ed3771463aaa697a57f3c7c77b3659.setContent(html_766ac4242209e5a7a2da3414f242047a);
            
        

        circle_marker_b289820806b26220fe412a35a758da0c.bindPopup(popup_03ed3771463aaa697a57f3c7c77b3659)
        ;

        
    
    
            var circle_marker_759ecb92ab2d0eb48af285e093908f30 = L.circleMarker(
                [41.3999967, 2.1644531],
                {"bubblingMouseEvents": true, "color": "#bbbbd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bbbbd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_31c9643419cff55acdff671f01a3ba67 = L.popup({"maxWidth": "100%"});

        
            
                var html_0eef57c62efd75e1ad16fb6b4b637401 = $(`<div id="html_0eef57c62efd75e1ad16fb6b4b637401" style="width: 100.0%; height: 100.0%;">Station 224<br>Result: 0.6%<br></div>`)[0];
                popup_31c9643419cff55acdff671f01a3ba67.setContent(html_0eef57c62efd75e1ad16fb6b4b637401);
            
        

        circle_marker_759ecb92ab2d0eb48af285e093908f30.bindPopup(popup_31c9643419cff55acdff671f01a3ba67)
        ;

        
    
    
            var circle_marker_92ae434eea354b22392bf99cfe5e7bd6 = L.circleMarker(
                [41.38481021146711, 2.1508071246452154],
                {"bubblingMouseEvents": true, "color": "#8686e4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8686e4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_042ffc5469c2cb928abe2fe8e2b29d4a = L.popup({"maxWidth": "100%"});

        
            
                var html_0f1c39db6b80f4b8d4079e3bbd04cbeb = $(`<div id="html_0f1c39db6b80f4b8d4079e3bbd04cbeb" style="width: 100.0%; height: 100.0%;">Station 225<br>Result: 1.8%<br></div>`)[0];
                popup_042ffc5469c2cb928abe2fe8e2b29d4a.setContent(html_0f1c39db6b80f4b8d4079e3bbd04cbeb);
            
        

        circle_marker_92ae434eea354b22392bf99cfe5e7bd6.bindPopup(popup_042ffc5469c2cb928abe2fe8e2b29d4a)
        ;

        
    
    
            var circle_marker_70a4531126fad77feb574ca53ad45e8d = L.circleMarker(
                [41.4035608, 2.1609345],
                {"bubblingMouseEvents": true, "color": "#cdcdd5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cdcdd5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_1591368114d5b5f9c44bc695a70cd700 = L.popup({"maxWidth": "100%"});

        
            
                var html_25204424ff0b53aa6c320bf6c188c0c5 = $(`<div id="html_25204424ff0b53aa6c320bf6c188c0c5" style="width: 100.0%; height: 100.0%;">Station 226<br>Result: 0.1%<br></div>`)[0];
                popup_1591368114d5b5f9c44bc695a70cd700.setContent(html_25204424ff0b53aa6c320bf6c188c0c5);
            
        

        circle_marker_70a4531126fad77feb574ca53ad45e8d.bindPopup(popup_1591368114d5b5f9c44bc695a70cd700)
        ;

        
    
    
            var circle_marker_5929b710641419658270c10df1e0f565 = L.circleMarker(
                [41.4078456, 2.1586704],
                {"bubblingMouseEvents": true, "color": "#c4c4d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c4c4d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5c806a4dc8e0278d45eebbe10eea8ed9 = L.popup({"maxWidth": "100%"});

        
            
                var html_7a0f2b3d3cba16321db9ccc9ef75ea73 = $(`<div id="html_7a0f2b3d3cba16321db9ccc9ef75ea73" style="width: 100.0%; height: 100.0%;">Station 227<br>Result: 0.4%<br></div>`)[0];
                popup_5c806a4dc8e0278d45eebbe10eea8ed9.setContent(html_7a0f2b3d3cba16321db9ccc9ef75ea73);
            
        

        circle_marker_5929b710641419658270c10df1e0f565.bindPopup(popup_5c806a4dc8e0278d45eebbe10eea8ed9)
        ;

        
    
    
            var circle_marker_e4901e27b753c1905d98a48b9fbafd1a = L.circleMarker(
                [41.4068417, 2.1558354],
                {"bubblingMouseEvents": true, "color": "#c0c0d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c0c0d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2d961643202bfd8248a989aed20506a5 = L.popup({"maxWidth": "100%"});

        
            
                var html_52ac4d1484035737e9783e3fd05b97ec = $(`<div id="html_52ac4d1484035737e9783e3fd05b97ec" style="width: 100.0%; height: 100.0%;">Station 228<br>Result: 0.4%<br></div>`)[0];
                popup_2d961643202bfd8248a989aed20506a5.setContent(html_52ac4d1484035737e9783e3fd05b97ec);
            
        

        circle_marker_e4901e27b753c1905d98a48b9fbafd1a.bindPopup(popup_2d961643202bfd8248a989aed20506a5)
        ;

        
    
    
            var circle_marker_d6e01ed2b219b26ea52dd028259428b1 = L.circleMarker(
                [41.4050968, 2.1569161],
                {"bubblingMouseEvents": true, "color": "#cbcbd5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cbcbd5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2cf8d22c7b4e836288fb19178978f7cd = L.popup({"maxWidth": "100%"});

        
            
                var html_6f9e6b6930463b6d697eb9ada492b290 = $(`<div id="html_6f9e6b6930463b6d697eb9ada492b290" style="width: 100.0%; height: 100.0%;">Station 229<br>Result: 0.2%<br></div>`)[0];
                popup_2cf8d22c7b4e836288fb19178978f7cd.setContent(html_6f9e6b6930463b6d697eb9ada492b290);
            
        

        circle_marker_d6e01ed2b219b26ea52dd028259428b1.bindPopup(popup_2cf8d22c7b4e836288fb19178978f7cd)
        ;

        
    
    
            var circle_marker_5abf7580558309fcc817bfe7ce81ec72 = L.circleMarker(
                [41.4059356, 2.1517977],
                {"bubblingMouseEvents": true, "color": "#d8bbbbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d8bbbbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_109296e5f6d547e243637f70f9e6fed4 = L.popup({"maxWidth": "100%"});

        
            
                var html_bf4463ba3a89f30d2d857713177c2f96 = $(`<div id="html_bf4463ba3a89f30d2d857713177c2f96" style="width: 100.0%; height: 100.0%;">Station 230<br>Result: -0.6%<br></div>`)[0];
                popup_109296e5f6d547e243637f70f9e6fed4.setContent(html_bf4463ba3a89f30d2d857713177c2f96);
            
        

        circle_marker_5abf7580558309fcc817bfe7ce81ec72.bindPopup(popup_109296e5f6d547e243637f70f9e6fed4)
        ;

        
    
    
            var circle_marker_88d8e15b96ef3e26402cdb72c8f2b625 = L.circleMarker(
                [41.37449997033759, 2.1730255457161096],
                {"bubblingMouseEvents": true, "color": "#a4a4ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a4a4ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_34303f6ae2dc9ce7d4e4ce108c2da09d = L.popup({"maxWidth": "100%"});

        
            
                var html_7556b9aa487250f378a8fb6c1f08fc2c = $(`<div id="html_7556b9aa487250f378a8fb6c1f08fc2c" style="width: 100.0%; height: 100.0%;">Station 232<br>Result: 1.1%<br></div>`)[0];
                popup_34303f6ae2dc9ce7d4e4ce108c2da09d.setContent(html_7556b9aa487250f378a8fb6c1f08fc2c);
            
        

        circle_marker_88d8e15b96ef3e26402cdb72c8f2b625.bindPopup(popup_34303f6ae2dc9ce7d4e4ce108c2da09d)
        ;

        
    
    
            var circle_marker_830a7d20c0c126b1c07ea8d72b4744f3 = L.circleMarker(
                [41.3719688, 2.1667829],
                {"bubblingMouseEvents": true, "color": "#b8b8d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b8b8d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6a56c3a650188f941a52609a88e7baa0 = L.popup({"maxWidth": "100%"});

        
            
                var html_d1c3e330ac1c5b9f721cc0225b96a6cf = $(`<div id="html_d1c3e330ac1c5b9f721cc0225b96a6cf" style="width: 100.0%; height: 100.0%;">Station 233<br>Result: 0.6%<br></div>`)[0];
                popup_6a56c3a650188f941a52609a88e7baa0.setContent(html_d1c3e330ac1c5b9f721cc0225b96a6cf);
            
        

        circle_marker_830a7d20c0c126b1c07ea8d72b4744f3.bindPopup(popup_6a56c3a650188f941a52609a88e7baa0)
        ;

        
    
    
            var circle_marker_cbff5254d80a93b628308261d5241271 = L.circleMarker(
                [41.3751767, 2.1658972],
                {"bubblingMouseEvents": true, "color": "#4d4defff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#4d4defff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_dabcca1fa8d748df594086b948039d2f = L.popup({"maxWidth": "100%"});

        
            
                var html_cc7a0b52a1549265689977b9df82ff32 = $(`<div id="html_cc7a0b52a1549265689977b9df82ff32" style="width: 100.0%; height: 100.0%;">Station 235<br>Result: 3.2%<br></div>`)[0];
                popup_dabcca1fa8d748df594086b948039d2f.setContent(html_cc7a0b52a1549265689977b9df82ff32);
            
        

        circle_marker_cbff5254d80a93b628308261d5241271.bindPopup(popup_dabcca1fa8d748df594086b948039d2f)
        ;

        
    
    
            var circle_marker_ebb67342e6d5442a58adf92b2ce26323 = L.circleMarker(
                [41.3751161, 2.1523091],
                {"bubblingMouseEvents": true, "color": "#9595e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9595e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_463f4c59176911e4d0d6b98b2a8439bf = L.popup({"maxWidth": "100%"});

        
            
                var html_08d8205ec16842927f8315e3f1bb177b = $(`<div id="html_08d8205ec16842927f8315e3f1bb177b" style="width: 100.0%; height: 100.0%;">Station 236<br>Result: 1.5%<br></div>`)[0];
                popup_463f4c59176911e4d0d6b98b2a8439bf.setContent(html_08d8205ec16842927f8315e3f1bb177b);
            
        

        circle_marker_ebb67342e6d5442a58adf92b2ce26323.bindPopup(popup_463f4c59176911e4d0d6b98b2a8439bf)
        ;

        
    
    
            var circle_marker_f8d66fd4eba90828735033dbd687854e = L.circleMarker(
                [41.3727426, 2.1539198],
                {"bubblingMouseEvents": true, "color": "#d6c6c6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c6c6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_08d61713a576977be72c1eb00a62b0ab = L.popup({"maxWidth": "100%"});

        
            
                var html_eb3baba47f3eb14ad4e0adfaacb47cbb = $(`<div id="html_eb3baba47f3eb14ad4e0adfaacb47cbb" style="width: 100.0%; height: 100.0%;">Station 237<br>Result: -0.3%<br></div>`)[0];
                popup_08d61713a576977be72c1eb00a62b0ab.setContent(html_eb3baba47f3eb14ad4e0adfaacb47cbb);
            
        

        circle_marker_f8d66fd4eba90828735033dbd687854e.bindPopup(popup_08d61713a576977be72c1eb00a62b0ab)
        ;

        
    
    
            var circle_marker_7f018719ec8e3a47358a47c96ddd2614 = L.circleMarker(
                [41.4158807, 2.1908473],
                {"bubblingMouseEvents": true, "color": "#9c9cdfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9c9cdfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_579bea64f0a9339dcb30e2a4ee74fc52 = L.popup({"maxWidth": "100%"});

        
            
                var html_d56330499340ecd54a47a1fa2bbfd92f = $(`<div id="html_d56330499340ecd54a47a1fa2bbfd92f" style="width: 100.0%; height: 100.0%;">Station 238<br>Result: 1.3%<br></div>`)[0];
                popup_579bea64f0a9339dcb30e2a4ee74fc52.setContent(html_d56330499340ecd54a47a1fa2bbfd92f);
            
        

        circle_marker_7f018719ec8e3a47358a47c96ddd2614.bindPopup(popup_579bea64f0a9339dcb30e2a4ee74fc52)
        ;

        
    
    
            var circle_marker_5607b25916b4ff1193217ac7e83f8c8d = L.circleMarker(
                [41.4172922, 2.1844769],
                {"bubblingMouseEvents": true, "color": "#8989e3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8989e3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a4c44a4988a69f3ff548ce7825601acb = L.popup({"maxWidth": "100%"});

        
            
                var html_fcae0a5331b46e8550c7e80eabe38b10 = $(`<div id="html_fcae0a5331b46e8550c7e80eabe38b10" style="width: 100.0%; height: 100.0%;">Station 239<br>Result: 1.8%<br></div>`)[0];
                popup_a4c44a4988a69f3ff548ce7825601acb.setContent(html_fcae0a5331b46e8550c7e80eabe38b10);
            
        

        circle_marker_5607b25916b4ff1193217ac7e83f8c8d.bindPopup(popup_a4c44a4988a69f3ff548ce7825601acb)
        ;

        
    
    
            var circle_marker_cd8e0d222fe224738c3e2d565460bd93 = L.circleMarker(
                [41.4175595, 2.1877153],
                {"bubblingMouseEvents": true, "color": "#5252eeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5252eeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0c66e53c107c24df1b6b167ba88daf74 = L.popup({"maxWidth": "100%"});

        
            
                var html_0da6d505c06e3e690ba01a8f2500a022 = $(`<div id="html_0da6d505c06e3e690ba01a8f2500a022" style="width: 100.0%; height: 100.0%;">Station 240<br>Result: 3.1%<br></div>`)[0];
                popup_0c66e53c107c24df1b6b167ba88daf74.setContent(html_0da6d505c06e3e690ba01a8f2500a022);
            
        

        circle_marker_cd8e0d222fe224738c3e2d565460bd93.bindPopup(popup_0c66e53c107c24df1b6b167ba88daf74)
        ;

        
    
    
            var circle_marker_5c237ab4ea8277bb9f4f5e9e0d13928a = L.circleMarker(
                [41.419178, 2.18018],
                {"bubblingMouseEvents": true, "color": "#c9c9d5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c9c9d5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_967302f7d05f0ed8165801287004d2aa = L.popup({"maxWidth": "100%"});

        
            
                var html_3764f70b8f49573c6fdb8ba8e280c289 = $(`<div id="html_3764f70b8f49573c6fdb8ba8e280c289" style="width: 100.0%; height: 100.0%;">Station 241<br>Result: 0.2%<br></div>`)[0];
                popup_967302f7d05f0ed8165801287004d2aa.setContent(html_3764f70b8f49573c6fdb8ba8e280c289);
            
        

        circle_marker_5c237ab4ea8277bb9f4f5e9e0d13928a.bindPopup(popup_967302f7d05f0ed8165801287004d2aa)
        ;

        
    
    
            var circle_marker_a359605293129095141e61f262e75d98 = L.circleMarker(
                [41.4244527, 2.1773157],
                {"bubblingMouseEvents": true, "color": "#b5b5daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b5b5daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a2b82835c241c22e1a57a644d4711990 = L.popup({"maxWidth": "100%"});

        
            
                var html_de807ef3dbb4479221b6a41410157fe0 = $(`<div id="html_de807ef3dbb4479221b6a41410157fe0" style="width: 100.0%; height: 100.0%;">Station 242<br>Result: 0.7%<br></div>`)[0];
                popup_a2b82835c241c22e1a57a644d4711990.setContent(html_de807ef3dbb4479221b6a41410157fe0);
            
        

        circle_marker_a359605293129095141e61f262e75d98.bindPopup(popup_a2b82835c241c22e1a57a644d4711990)
        ;

        
    
    
            var circle_marker_32f74ffdbd2845bfe593eb5cf64a78d2 = L.circleMarker(
                [41.4239719, 2.1812399],
                {"bubblingMouseEvents": true, "color": "#a3a3ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a3a3ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_fb4d0dba04a81eccb9e92c5b7b5c7e18 = L.popup({"maxWidth": "100%"});

        
            
                var html_f776f9aaf913659b85426be278f0591e = $(`<div id="html_f776f9aaf913659b85426be278f0591e" style="width: 100.0%; height: 100.0%;">Station 243<br>Result: 1.2%<br></div>`)[0];
                popup_fb4d0dba04a81eccb9e92c5b7b5c7e18.setContent(html_f776f9aaf913659b85426be278f0591e);
            
        

        circle_marker_32f74ffdbd2845bfe593eb5cf64a78d2.bindPopup(popup_fb4d0dba04a81eccb9e92c5b7b5c7e18)
        ;

        
    
    
            var circle_marker_87dcc556a2c97f18e90fce4974a01de4 = L.circleMarker(
                [41.426925, 2.1786224],
                {"bubblingMouseEvents": true, "color": "#b8b8d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b8b8d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_438dea6948915eccc7555731b6793b7b = L.popup({"maxWidth": "100%"});

        
            
                var html_50ba5bfe8996e162c9c311607a689a1a = $(`<div id="html_50ba5bfe8996e162c9c311607a689a1a" style="width: 100.0%; height: 100.0%;">Station 244<br>Result: 0.6%<br></div>`)[0];
                popup_438dea6948915eccc7555731b6793b7b.setContent(html_50ba5bfe8996e162c9c311607a689a1a);
            
        

        circle_marker_87dcc556a2c97f18e90fce4974a01de4.bindPopup(popup_438dea6948915eccc7555731b6793b7b)
        ;

        
    
    
            var circle_marker_c73b70bea45f7aa9a8814c7bb776bd48 = L.circleMarker(
                [41.4228449, 2.1866363],
                {"bubblingMouseEvents": true, "color": "#8080e5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8080e5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0c68896fe47e2e58c9568d0f2e3244d9 = L.popup({"maxWidth": "100%"});

        
            
                var html_88496f566053fa590100c326a7f8af10 = $(`<div id="html_88496f566053fa590100c326a7f8af10" style="width: 100.0%; height: 100.0%;">Station 246<br>Result: 2.0%<br></div>`)[0];
                popup_0c68896fe47e2e58c9568d0f2e3244d9.setContent(html_88496f566053fa590100c326a7f8af10);
            
        

        circle_marker_c73b70bea45f7aa9a8814c7bb776bd48.bindPopup(popup_0c68896fe47e2e58c9568d0f2e3244d9)
        ;

        
    
    
            var circle_marker_d433301ee98be5718e012269cdadc3a9 = L.circleMarker(
                [41.4219291, 2.1849107],
                {"bubblingMouseEvents": true, "color": "#9898e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9898e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_81f41756559f07b7806cd6577bf8fcf6 = L.popup({"maxWidth": "100%"});

        
            
                var html_ccd5e833b3bda59fc8bb0996d58546fc = $(`<div id="html_ccd5e833b3bda59fc8bb0996d58546fc" style="width: 100.0%; height: 100.0%;">Station 247<br>Result: 1.4%<br></div>`)[0];
                popup_81f41756559f07b7806cd6577bf8fcf6.setContent(html_ccd5e833b3bda59fc8bb0996d58546fc);
            
        

        circle_marker_d433301ee98be5718e012269cdadc3a9.bindPopup(popup_81f41756559f07b7806cd6577bf8fcf6)
        ;

        
    
    
            var circle_marker_642f85c47a0e5133a14b9f143d701f33 = L.circleMarker(
                [41.4182129, 2.1904005],
                {"bubblingMouseEvents": true, "color": "#a4a4ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a4a4ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_62984b593dcff724f5687329621f2dfd = L.popup({"maxWidth": "100%"});

        
            
                var html_fb9b2e5f2dc1892164387f2ab68abd0c = $(`<div id="html_fb9b2e5f2dc1892164387f2ab68abd0c" style="width: 100.0%; height: 100.0%;">Station 248<br>Result: 1.1%<br></div>`)[0];
                popup_62984b593dcff724f5687329621f2dfd.setContent(html_fb9b2e5f2dc1892164387f2ab68abd0c);
            
        

        circle_marker_642f85c47a0e5133a14b9f143d701f33.bindPopup(popup_62984b593dcff724f5687329621f2dfd)
        ;

        
    
    
            var circle_marker_9a2f515f6078017939db6be13e499c8a = L.circleMarker(
                [41.4250835, 2.1872818],
                {"bubblingMouseEvents": true, "color": "#a0a0deff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a0a0deff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5a43068dc51f2acffa10be041263cc68 = L.popup({"maxWidth": "100%"});

        
            
                var html_50c75572e08e2a3afa59c3b16819790b = $(`<div id="html_50c75572e08e2a3afa59c3b16819790b" style="width: 100.0%; height: 100.0%;">Station 249<br>Result: 1.2%<br></div>`)[0];
                popup_5a43068dc51f2acffa10be041263cc68.setContent(html_50c75572e08e2a3afa59c3b16819790b);
            
        

        circle_marker_9a2f515f6078017939db6be13e499c8a.bindPopup(popup_5a43068dc51f2acffa10be041263cc68)
        ;

        
    
    
            var circle_marker_0304f337e6fd3abba7564144546f9dcd = L.circleMarker(
                [41.4258248, 2.191206],
                {"bubblingMouseEvents": true, "color": "#b3b3daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b3b3daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9d33117e6dd274209e0c088c574a811a = L.popup({"maxWidth": "100%"});

        
            
                var html_eb4a4739c6a1f8490fda2af1a444b6ce = $(`<div id="html_eb4a4739c6a1f8490fda2af1a444b6ce" style="width: 100.0%; height: 100.0%;">Station 250<br>Result: 0.8%<br></div>`)[0];
                popup_9d33117e6dd274209e0c088c574a811a.setContent(html_eb4a4739c6a1f8490fda2af1a444b6ce);
            
        

        circle_marker_0304f337e6fd3abba7564144546f9dcd.bindPopup(popup_9d33117e6dd274209e0c088c574a811a)
        ;

        
    
    
            var circle_marker_f193d3e482265345d018ae684533c6f9 = L.circleMarker(
                [41.4253643, 2.1852073],
                {"bubblingMouseEvents": true, "color": "#a9a9dcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a9a9dcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8e9dec906f5284023b6fbdd82b27fe25 = L.popup({"maxWidth": "100%"});

        
            
                var html_839911eaa7c1964d426d3791e5c602b9 = $(`<div id="html_839911eaa7c1964d426d3791e5c602b9" style="width: 100.0%; height: 100.0%;">Station 251<br>Result: 1.0%<br></div>`)[0];
                popup_8e9dec906f5284023b6fbdd82b27fe25.setContent(html_839911eaa7c1964d426d3791e5c602b9);
            
        

        circle_marker_f193d3e482265345d018ae684533c6f9.bindPopup(popup_8e9dec906f5284023b6fbdd82b27fe25)
        ;

        
    
    
            var circle_marker_fedcd8c7727cb6be4a0d44464c9decca = L.circleMarker(
                [41.4298991, 2.1932159],
                {"bubblingMouseEvents": true, "color": "#d4cfcfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4cfcfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4ca653a72b2e02e40474931d372481f5 = L.popup({"maxWidth": "100%"});

        
            
                var html_b3b769768dd06e65457dbafd885d76a6 = $(`<div id="html_b3b769768dd06e65457dbafd885d76a6" style="width: 100.0%; height: 100.0%;">Station 252<br>Result: -0.1%<br></div>`)[0];
                popup_4ca653a72b2e02e40474931d372481f5.setContent(html_b3b769768dd06e65457dbafd885d76a6);
            
        

        circle_marker_fedcd8c7727cb6be4a0d44464c9decca.bindPopup(popup_4ca653a72b2e02e40474931d372481f5)
        ;

        
    
    
            var circle_marker_da4578fa379c157269fb56511cc62faa = L.circleMarker(
                [41.4298614, 2.1922011],
                {"bubblingMouseEvents": true, "color": "#cfcfd4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cfcfd4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a9471552434ae57dbd57cf09b7f9247d = L.popup({"maxWidth": "100%"});

        
            
                var html_a5f5fecbc8b6923be1c2085fe46d7d69 = $(`<div id="html_a5f5fecbc8b6923be1c2085fe46d7d69" style="width: 100.0%; height: 100.0%;">Station 253<br>Result: 0.1%<br></div>`)[0];
                popup_a9471552434ae57dbd57cf09b7f9247d.setContent(html_a5f5fecbc8b6923be1c2085fe46d7d69);
            
        

        circle_marker_da4578fa379c157269fb56511cc62faa.bindPopup(popup_a9471552434ae57dbd57cf09b7f9247d)
        ;

        
    
    
            var circle_marker_f8d81d2ee2012cb9a5cc264ba7adde16 = L.circleMarker(
                [41.4299999, 2.190246],
                {"bubblingMouseEvents": true, "color": "#c2c2d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c2c2d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_fa4559f0636b74800ff9a0d237164ca2 = L.popup({"maxWidth": "100%"});

        
            
                var html_64d6448537d9b5e48a7949905bea7157 = $(`<div id="html_64d6448537d9b5e48a7949905bea7157" style="width: 100.0%; height: 100.0%;">Station 254<br>Result: 0.4%<br></div>`)[0];
                popup_fa4559f0636b74800ff9a0d237164ca2.setContent(html_64d6448537d9b5e48a7949905bea7157);
            
        

        circle_marker_f8d81d2ee2012cb9a5cc264ba7adde16.bindPopup(popup_fa4559f0636b74800ff9a0d237164ca2)
        ;

        
    
    
            var circle_marker_35e259e92fce3908841becd2ce3d411e = L.circleMarker(
                [41.4315, 2.18579],
                {"bubblingMouseEvents": true, "color": "#8b8be3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8b8be3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_66e321c60c89fbf8c3030562021ec4bc = L.popup({"maxWidth": "100%"});

        
            
                var html_26f8e9a81f5f28eb79991ce0025db671 = $(`<div id="html_26f8e9a81f5f28eb79991ce0025db671" style="width: 100.0%; height: 100.0%;">Station 255<br>Result: 1.7%<br></div>`)[0];
                popup_66e321c60c89fbf8c3030562021ec4bc.setContent(html_26f8e9a81f5f28eb79991ce0025db671);
            
        

        circle_marker_35e259e92fce3908841becd2ce3d411e.bindPopup(popup_66e321c60c89fbf8c3030562021ec4bc)
        ;

        
    
    
            var circle_marker_bb48efbb03d7907cbac2cdd5e05476c2 = L.circleMarker(
                [41.4361251, 2.1894423],
                {"bubblingMouseEvents": true, "color": "#b8b8d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b8b8d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_fdcc72894f9436a98fab96c41aa6d925 = L.popup({"maxWidth": "100%"});

        
            
                var html_83ad7631ba65c8a482070cdbd4f470f1 = $(`<div id="html_83ad7631ba65c8a482070cdbd4f470f1" style="width: 100.0%; height: 100.0%;">Station 256<br>Result: 0.6%<br></div>`)[0];
                popup_fdcc72894f9436a98fab96c41aa6d925.setContent(html_83ad7631ba65c8a482070cdbd4f470f1);
            
        

        circle_marker_bb48efbb03d7907cbac2cdd5e05476c2.bindPopup(popup_fdcc72894f9436a98fab96c41aa6d925)
        ;

        
    
    
            var circle_marker_45b4b6642cb63f079ae240e6187f9bd6 = L.circleMarker(
                [41.433934, 2.1896502],
                {"bubblingMouseEvents": true, "color": "#c0c0d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c0c0d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d26324ea7bdf7e0f3860cbe16e5e5bdd = L.popup({"maxWidth": "100%"});

        
            
                var html_c13082556b4d03cc5750fdbb3863a47f = $(`<div id="html_c13082556b4d03cc5750fdbb3863a47f" style="width: 100.0%; height: 100.0%;">Station 257<br>Result: 0.4%<br></div>`)[0];
                popup_d26324ea7bdf7e0f3860cbe16e5e5bdd.setContent(html_c13082556b4d03cc5750fdbb3863a47f);
            
        

        circle_marker_45b4b6642cb63f079ae240e6187f9bd6.bindPopup(popup_d26324ea7bdf7e0f3860cbe16e5e5bdd)
        ;

        
    
    
            var circle_marker_0eef5a4db082861695022d439048ffb4 = L.circleMarker(
                [41.441986663902426, 2.192957641716178],
                {"bubblingMouseEvents": true, "color": "#d1d1d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d1d1d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ea34467780bebb1915449841f9684a43 = L.popup({"maxWidth": "100%"});

        
            
                var html_02cf9384a66c0cdc9ca2a881be1c6c8c = $(`<div id="html_02cf9384a66c0cdc9ca2a881be1c6c8c" style="width: 100.0%; height: 100.0%;">Station 258<br>Result: 0.0%<br></div>`)[0];
                popup_ea34467780bebb1915449841f9684a43.setContent(html_02cf9384a66c0cdc9ca2a881be1c6c8c);
            
        

        circle_marker_0eef5a4db082861695022d439048ffb4.bindPopup(popup_ea34467780bebb1915449841f9684a43)
        ;

        
    
    
            var circle_marker_6bfe35c203864ff64f3a7b9393b46649 = L.circleMarker(
                [41.4391174, 2.1858025],
                {"bubblingMouseEvents": true, "color": "#b0b0dbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b0b0dbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9accef60fe1b3a9f6174d9aa1ada0b32 = L.popup({"maxWidth": "100%"});

        
            
                var html_377615f2348a2834c779edd67ce4e153 = $(`<div id="html_377615f2348a2834c779edd67ce4e153" style="width: 100.0%; height: 100.0%;">Station 259<br>Result: 0.8%<br></div>`)[0];
                popup_9accef60fe1b3a9f6174d9aa1ada0b32.setContent(html_377615f2348a2834c779edd67ce4e153);
            
        

        circle_marker_6bfe35c203864ff64f3a7b9393b46649.bindPopup(popup_9accef60fe1b3a9f6174d9aa1ada0b32)
        ;

        
    
    
            var circle_marker_2d0e4cd63fc97771f26c3a2658889b48 = L.circleMarker(
                [41.4356895, 2.1920873],
                {"bubblingMouseEvents": true, "color": "#bfbfd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bfbfd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8392499d6379dce09cd92ede57dcc18b = L.popup({"maxWidth": "100%"});

        
            
                var html_3bbaece843020516d4e408d6d77a9356 = $(`<div id="html_3bbaece843020516d4e408d6d77a9356" style="width: 100.0%; height: 100.0%;">Station 260<br>Result: 0.5%<br></div>`)[0];
                popup_8392499d6379dce09cd92ede57dcc18b.setContent(html_3bbaece843020516d4e408d6d77a9356);
            
        

        circle_marker_2d0e4cd63fc97771f26c3a2658889b48.bindPopup(popup_8392499d6379dce09cd92ede57dcc18b)
        ;

        
    
    
            var circle_marker_c865c3b42300c2bb4b6f0fcc380b380b = L.circleMarker(
                [41.3821314, 2.1606534],
                {"bubblingMouseEvents": true, "color": "#6565eaff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6565eaff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5c0ec659ef2ad99a0e5d758ffa819ae6 = L.popup({"maxWidth": "100%"});

        
            
                var html_a97c911271f9f3bf97e387ab8dc0173a = $(`<div id="html_a97c911271f9f3bf97e387ab8dc0173a" style="width: 100.0%; height: 100.0%;">Station 261<br>Result: 2.6%<br></div>`)[0];
                popup_5c0ec659ef2ad99a0e5d758ffa819ae6.setContent(html_a97c911271f9f3bf97e387ab8dc0173a);
            
        

        circle_marker_c865c3b42300c2bb4b6f0fcc380b380b.bindPopup(popup_5c0ec659ef2ad99a0e5d758ffa819ae6)
        ;

        
    
    
            var circle_marker_a1782db0e1072b8e368b70dfaa5835b1 = L.circleMarker(
                [41.3790954665734, 2.1516210083712],
                {"bubblingMouseEvents": true, "color": "#9999e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9999e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a74953376105bb2277584ce1d1d78451 = L.popup({"maxWidth": "100%"});

        
            
                var html_2384b91d0d3f2de72f537fd2b4bdf856 = $(`<div id="html_2384b91d0d3f2de72f537fd2b4bdf856" style="width: 100.0%; height: 100.0%;">Station 262<br>Result: 1.4%<br></div>`)[0];
                popup_a74953376105bb2277584ce1d1d78451.setContent(html_2384b91d0d3f2de72f537fd2b4bdf856);
            
        

        circle_marker_a1782db0e1072b8e368b70dfaa5835b1.bindPopup(popup_a74953376105bb2277584ce1d1d78451)
        ;

        
    
    
            var circle_marker_461646e492cfa91f0678a7ac3f6a56e9 = L.circleMarker(
                [41.4378773, 2.1910691],
                {"bubblingMouseEvents": true, "color": "#cacad5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cacad5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e1573518264f54c23f5fa6f6f0e2cff4 = L.popup({"maxWidth": "100%"});

        
            
                var html_543c4fb64ab3ca15553ec9af787e0284 = $(`<div id="html_543c4fb64ab3ca15553ec9af787e0284" style="width: 100.0%; height: 100.0%;">Station 263<br>Result: 0.2%<br></div>`)[0];
                popup_e1573518264f54c23f5fa6f6f0e2cff4.setContent(html_543c4fb64ab3ca15553ec9af787e0284);
            
        

        circle_marker_461646e492cfa91f0678a7ac3f6a56e9.bindPopup(popup_e1573518264f54c23f5fa6f6f0e2cff4)
        ;

        
    
    
            var circle_marker_d3cee054783b87709fcb95e92178351b = L.circleMarker(
                [41.439929, 2.1970692],
                {"bubblingMouseEvents": true, "color": "#d7c1c1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c1c1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d82f0503f5af5da129c9605ed517f155 = L.popup({"maxWidth": "100%"});

        
            
                var html_f8f47470983e369df4dcf5a71061011a = $(`<div id="html_f8f47470983e369df4dcf5a71061011a" style="width: 100.0%; height: 100.0%;">Station 264<br>Result: -0.4%<br></div>`)[0];
                popup_d82f0503f5af5da129c9605ed517f155.setContent(html_f8f47470983e369df4dcf5a71061011a);
            
        

        circle_marker_d3cee054783b87709fcb95e92178351b.bindPopup(popup_d82f0503f5af5da129c9605ed517f155)
        ;

        
    
    
            var circle_marker_f9842ad4554320fcd1578a563543c1b0 = L.circleMarker(
                [41.3847738, 2.1592566],
                {"bubblingMouseEvents": true, "color": "#6c6ce9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6c6ce9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e43edcebded1d338e99cec6327cf9064 = L.popup({"maxWidth": "100%"});

        
            
                var html_67ebcf17a5e9d9bdd0dc7b8c226a8f6a = $(`<div id="html_67ebcf17a5e9d9bdd0dc7b8c226a8f6a" style="width: 100.0%; height: 100.0%;">Station 265<br>Result: 2.4%<br></div>`)[0];
                popup_e43edcebded1d338e99cec6327cf9064.setContent(html_67ebcf17a5e9d9bdd0dc7b8c226a8f6a);
            
        

        circle_marker_f9842ad4554320fcd1578a563543c1b0.bindPopup(popup_e43edcebded1d338e99cec6327cf9064)
        ;

        
    
    
            var circle_marker_c9e20da590cbfea351b4d78d2db473aa = L.circleMarker(
                [41.4268952, 2.1842572],
                {"bubblingMouseEvents": true, "color": "#9e9edeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9e9edeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_3b0fe0444f9dd7fa163d8cd5611e2bcf = L.popup({"maxWidth": "100%"});

        
            
                var html_f075572e73c2f65c2dabf93eee37ba1d = $(`<div id="html_f075572e73c2f65c2dabf93eee37ba1d" style="width: 100.0%; height: 100.0%;">Station 266<br>Result: 1.3%<br></div>`)[0];
                popup_3b0fe0444f9dd7fa163d8cd5611e2bcf.setContent(html_f075572e73c2f65c2dabf93eee37ba1d);
            
        

        circle_marker_c9e20da590cbfea351b4d78d2db473aa.bindPopup(popup_3b0fe0444f9dd7fa163d8cd5611e2bcf)
        ;

        
    
    
            var circle_marker_381e65e0ccc74f4e93b797a2f7d99f3f = L.circleMarker(
                [41.4433647, 2.1906302],
                {"bubblingMouseEvents": true, "color": "#8787e3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8787e3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ec1892bd200793f35d84c3cc91c3a9be = L.popup({"maxWidth": "100%"});

        
            
                var html_4d26281a17a933ed105e3935eacf189e = $(`<div id="html_4d26281a17a933ed105e3935eacf189e" style="width: 100.0%; height: 100.0%;">Station 267<br>Result: 1.8%<br></div>`)[0];
                popup_ec1892bd200793f35d84c3cc91c3a9be.setContent(html_4d26281a17a933ed105e3935eacf189e);
            
        

        circle_marker_381e65e0ccc74f4e93b797a2f7d99f3f.bindPopup(popup_ec1892bd200793f35d84c3cc91c3a9be)
        ;

        
    
    
            var circle_marker_0bbfea3459306ec98fe846b7740e99e4 = L.circleMarker(
                [41.4457195, 2.1929816],
                {"bubblingMouseEvents": true, "color": "#d0d0d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d0d0d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_711f1b1260c047f33b07d06570f88fac = L.popup({"maxWidth": "100%"});

        
            
                var html_890d38b14eb13e91effc1b9371d8ec3c = $(`<div id="html_890d38b14eb13e91effc1b9371d8ec3c" style="width: 100.0%; height: 100.0%;">Station 268<br>Result: 0.1%<br></div>`)[0];
                popup_711f1b1260c047f33b07d06570f88fac.setContent(html_890d38b14eb13e91effc1b9371d8ec3c);
            
        

        circle_marker_0bbfea3459306ec98fe846b7740e99e4.bindPopup(popup_711f1b1260c047f33b07d06570f88fac)
        ;

        
    
    
            var circle_marker_122cd4d56a53c9844aeb3fcb0a7e1704 = L.circleMarker(
                [41.448152, 2.19294],
                {"bubblingMouseEvents": true, "color": "#ceced4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ceced4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_746ea8111b6c6b98446c44a7cacf1c02 = L.popup({"maxWidth": "100%"});

        
            
                var html_ad7a7cc35e21deb0975d1256653c6312 = $(`<div id="html_ad7a7cc35e21deb0975d1256653c6312" style="width: 100.0%; height: 100.0%;">Station 269<br>Result: 0.1%<br></div>`)[0];
                popup_746ea8111b6c6b98446c44a7cacf1c02.setContent(html_ad7a7cc35e21deb0975d1256653c6312);
            
        

        circle_marker_122cd4d56a53c9844aeb3fcb0a7e1704.bindPopup(popup_746ea8111b6c6b98446c44a7cacf1c02)
        ;

        
    
    
            var circle_marker_3a74a4ea3198034ee4e70d68798206b4 = L.circleMarker(
                [41.4486328, 2.1898372],
                {"bubblingMouseEvents": true, "color": "#b5b5daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b5b5daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b5606ad80b40dbfebd5894b5c89848c9 = L.popup({"maxWidth": "100%"});

        
            
                var html_3fcc05d4b31dfa7de57775551b0cd2dc = $(`<div id="html_3fcc05d4b31dfa7de57775551b0cd2dc" style="width: 100.0%; height: 100.0%;">Station 270<br>Result: 0.7%<br></div>`)[0];
                popup_b5606ad80b40dbfebd5894b5c89848c9.setContent(html_3fcc05d4b31dfa7de57775551b0cd2dc);
            
        

        circle_marker_3a74a4ea3198034ee4e70d68798206b4.bindPopup(popup_b5606ad80b40dbfebd5894b5c89848c9)
        ;

        
    
    
            var circle_marker_2671f3d5b7016034b7ab5e4b4d51d671 = L.circleMarker(
                [41.4519872, 2.1935229],
                {"bubblingMouseEvents": true, "color": "#ceced5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ceced5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d2b31028105fe773e49390ba87dec3ca = L.popup({"maxWidth": "100%"});

        
            
                var html_32a1e7702509ad1b013606ab23b6d09a = $(`<div id="html_32a1e7702509ad1b013606ab23b6d09a" style="width: 100.0%; height: 100.0%;">Station 271<br>Result: 0.1%<br></div>`)[0];
                popup_d2b31028105fe773e49390ba87dec3ca.setContent(html_32a1e7702509ad1b013606ab23b6d09a);
            
        

        circle_marker_2671f3d5b7016034b7ab5e4b4d51d671.bindPopup(popup_d2b31028105fe773e49390ba87dec3ca)
        ;

        
    
    
            var circle_marker_d4b62d2260e19d01a156f594eeb613d9 = L.circleMarker(
                [41.4325013, 2.1842021],
                {"bubblingMouseEvents": true, "color": "#c3c3d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c3c3d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a3d50666de1a6fb9cac7a9cf1955fb3c = L.popup({"maxWidth": "100%"});

        
            
                var html_bd185db17c3ec68b687b95a1c0a4d06a = $(`<div id="html_bd185db17c3ec68b687b95a1c0a4d06a" style="width: 100.0%; height: 100.0%;">Station 272<br>Result: 0.4%<br></div>`)[0];
                popup_a3d50666de1a6fb9cac7a9cf1955fb3c.setContent(html_bd185db17c3ec68b687b95a1c0a4d06a);
            
        

        circle_marker_d4b62d2260e19d01a156f594eeb613d9.bindPopup(popup_a3d50666de1a6fb9cac7a9cf1955fb3c)
        ;

        
    
    
            var circle_marker_df8cbb391ee7b250adafefbf8a0df3e2 = L.circleMarker(
                [41.4304126, 2.1834174],
                {"bubblingMouseEvents": true, "color": "#c6c6d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c6c6d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c57a760055e8d6b4688d355c4478e8dd = L.popup({"maxWidth": "100%"});

        
            
                var html_a3a1cb202b510a6a53c2d13348e1f8a7 = $(`<div id="html_a3a1cb202b510a6a53c2d13348e1f8a7" style="width: 100.0%; height: 100.0%;">Station 273<br>Result: 0.3%<br></div>`)[0];
                popup_c57a760055e8d6b4688d355c4478e8dd.setContent(html_a3a1cb202b510a6a53c2d13348e1f8a7);
            
        

        circle_marker_df8cbb391ee7b250adafefbf8a0df3e2.bindPopup(popup_c57a760055e8d6b4688d355c4478e8dd)
        ;

        
    
    
            var circle_marker_fdc1bac08682e50a755ff3624a574b42 = L.circleMarker(
                [41.4299201, 2.1849813],
                {"bubblingMouseEvents": true, "color": "#c0c0d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c0c0d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f0392bfc0f8b8825d3232bbcc96edd0a = L.popup({"maxWidth": "100%"});

        
            
                var html_baf132925bdb5f891c33d7c8e588ba78 = $(`<div id="html_baf132925bdb5f891c33d7c8e588ba78" style="width: 100.0%; height: 100.0%;">Station 274<br>Result: 0.5%<br></div>`)[0];
                popup_f0392bfc0f8b8825d3232bbcc96edd0a.setContent(html_baf132925bdb5f891c33d7c8e588ba78);
            
        

        circle_marker_fdc1bac08682e50a755ff3624a574b42.bindPopup(popup_f0392bfc0f8b8825d3232bbcc96edd0a)
        ;

        
    
    
            var circle_marker_016294c943237fb2543a76ead256b7ef = L.circleMarker(
                [41.43068, 2.1821802],
                {"bubblingMouseEvents": true, "color": "#b0b0dbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b0b0dbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2be1064944b868c471ae9482a5619898 = L.popup({"maxWidth": "100%"});

        
            
                var html_729d305fe1b409f0509963e18c38a504 = $(`<div id="html_729d305fe1b409f0509963e18c38a504" style="width: 100.0%; height: 100.0%;">Station 275<br>Result: 0.8%<br></div>`)[0];
                popup_2be1064944b868c471ae9482a5619898.setContent(html_729d305fe1b409f0509963e18c38a504);
            
        

        circle_marker_016294c943237fb2543a76ead256b7ef.bindPopup(popup_2be1064944b868c471ae9482a5619898)
        ;

        
    
    
            var circle_marker_c6d6659b1b3fcb233733d5a3d8f3b202 = L.circleMarker(
                [41.4121345, 2.1652216],
                {"bubblingMouseEvents": true, "color": "#c3c3d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c3c3d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2fda86bdb52546d6ee7db6dbb0ed80d1 = L.popup({"maxWidth": "100%"});

        
            
                var html_3b335ab8bb3498c58a42e6a609ebe39b = $(`<div id="html_3b335ab8bb3498c58a42e6a609ebe39b" style="width: 100.0%; height: 100.0%;">Station 276<br>Result: 0.4%<br></div>`)[0];
                popup_2fda86bdb52546d6ee7db6dbb0ed80d1.setContent(html_3b335ab8bb3498c58a42e6a609ebe39b);
            
        

        circle_marker_c6d6659b1b3fcb233733d5a3d8f3b202.bindPopup(popup_2fda86bdb52546d6ee7db6dbb0ed80d1)
        ;

        
    
    
            var circle_marker_7615518a2640a5a918e35fc128e9aa67 = L.circleMarker(
                [41.4082107, 2.1689962],
                {"bubblingMouseEvents": true, "color": "#b6b6d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b6b6d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9700f65962c4b2b4c6dfb2f1de3f5ba7 = L.popup({"maxWidth": "100%"});

        
            
                var html_fade79e8d81aa756808afc623922d0b0 = $(`<div id="html_fade79e8d81aa756808afc623922d0b0" style="width: 100.0%; height: 100.0%;">Station 277<br>Result: 0.7%<br></div>`)[0];
                popup_9700f65962c4b2b4c6dfb2f1de3f5ba7.setContent(html_fade79e8d81aa756808afc623922d0b0);
            
        

        circle_marker_7615518a2640a5a918e35fc128e9aa67.bindPopup(popup_9700f65962c4b2b4c6dfb2f1de3f5ba7)
        ;

        
    
    
            var circle_marker_51faf88e18ba941058e1dc5e88a4dfbf = L.circleMarker(
                [41.4098842, 2.1715285],
                {"bubblingMouseEvents": true, "color": "#9191e1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9191e1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ef5599e913aff26d003f9f7dda9056d7 = L.popup({"maxWidth": "100%"});

        
            
                var html_b0cce58824e628c7e9d6fbb59030f136 = $(`<div id="html_b0cce58824e628c7e9d6fbb59030f136" style="width: 100.0%; height: 100.0%;">Station 278<br>Result: 1.6%<br></div>`)[0];
                popup_ef5599e913aff26d003f9f7dda9056d7.setContent(html_b0cce58824e628c7e9d6fbb59030f136);
            
        

        circle_marker_51faf88e18ba941058e1dc5e88a4dfbf.bindPopup(popup_ef5599e913aff26d003f9f7dda9056d7)
        ;

        
    
    
            var circle_marker_5ec3cacf8672e88b493e8470e19dead8 = L.circleMarker(
                [41.4158995, 2.1745567],
                {"bubblingMouseEvents": true, "color": "#c3c3d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c3c3d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_81734de650000a11497d753db3120133 = L.popup({"maxWidth": "100%"});

        
            
                var html_d1190a4d087040ace1a5da40ed983fb9 = $(`<div id="html_d1190a4d087040ace1a5da40ed983fb9" style="width: 100.0%; height: 100.0%;">Station 279<br>Result: 0.4%<br></div>`)[0];
                popup_81734de650000a11497d753db3120133.setContent(html_d1190a4d087040ace1a5da40ed983fb9);
            
        

        circle_marker_5ec3cacf8672e88b493e8470e19dead8.bindPopup(popup_81734de650000a11497d753db3120133)
        ;

        
    
    
            var circle_marker_dc56276007408aa400c22040a81485a8 = L.circleMarker(
                [41.4138664, 2.1777274],
                {"bubblingMouseEvents": true, "color": "#c9c9d5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c9c9d5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8eac065184ca153a9f025bfef6837c33 = L.popup({"maxWidth": "100%"});

        
            
                var html_01cb0f9f17da8bcd1f87cbe89baa8aac = $(`<div id="html_01cb0f9f17da8bcd1f87cbe89baa8aac" style="width: 100.0%; height: 100.0%;">Station 280<br>Result: 0.2%<br></div>`)[0];
                popup_8eac065184ca153a9f025bfef6837c33.setContent(html_01cb0f9f17da8bcd1f87cbe89baa8aac);
            
        

        circle_marker_dc56276007408aa400c22040a81485a8.bindPopup(popup_8eac065184ca153a9f025bfef6837c33)
        ;

        
    
    
            var circle_marker_a1110af6d36382d7ea5d0930c13bd085 = L.circleMarker(
                [41.4180789, 2.1763994],
                {"bubblingMouseEvents": true, "color": "#b3b3daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b3b3daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_114f2bb2dfc897e5f0718a1dddfd076b = L.popup({"maxWidth": "100%"});

        
            
                var html_a9cd4f0e8d324a57a9e5c57b7ef46fda = $(`<div id="html_a9cd4f0e8d324a57a9e5c57b7ef46fda" style="width: 100.0%; height: 100.0%;">Station 281<br>Result: 0.8%<br></div>`)[0];
                popup_114f2bb2dfc897e5f0718a1dddfd076b.setContent(html_a9cd4f0e8d324a57a9e5c57b7ef46fda);
            
        

        circle_marker_a1110af6d36382d7ea5d0930c13bd085.bindPopup(popup_114f2bb2dfc897e5f0718a1dddfd076b)
        ;

        
    
    
            var circle_marker_3a6e9332c47ae5cd41558db474090e82 = L.circleMarker(
                [41.4275514, 2.1659881],
                {"bubblingMouseEvents": true, "color": "#c5c5d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c5c5d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ee9836d26baf543f2983a2f61395fa84 = L.popup({"maxWidth": "100%"});

        
            
                var html_a5b76b662c569ae3bf48a404207bfb3f = $(`<div id="html_a5b76b662c569ae3bf48a404207bfb3f" style="width: 100.0%; height: 100.0%;">Station 282<br>Result: 0.3%<br></div>`)[0];
                popup_ee9836d26baf543f2983a2f61395fa84.setContent(html_a5b76b662c569ae3bf48a404207bfb3f);
            
        

        circle_marker_3a6e9332c47ae5cd41558db474090e82.bindPopup(popup_ee9836d26baf543f2983a2f61395fa84)
        ;

        
    
    
            var circle_marker_8a034f4b688a34afab63bc382464b87d = L.circleMarker(
                [41.4297231, 2.1617032],
                {"bubblingMouseEvents": true, "color": "#bfbfd7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bfbfd7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_bbf714f8767d3c44ce12d215ac18392d = L.popup({"maxWidth": "100%"});

        
            
                var html_9f4b9585f5db3c68d3bb142c85658558 = $(`<div id="html_9f4b9585f5db3c68d3bb142c85658558" style="width: 100.0%; height: 100.0%;">Station 283<br>Result: 0.5%<br></div>`)[0];
                popup_bbf714f8767d3c44ce12d215ac18392d.setContent(html_9f4b9585f5db3c68d3bb142c85658558);
            
        

        circle_marker_8a034f4b688a34afab63bc382464b87d.bindPopup(popup_bbf714f8767d3c44ce12d215ac18392d)
        ;

        
    
    
            var circle_marker_336566e9de046fe9afbc25d6f8327756 = L.circleMarker(
                [41.389462, 2.1314948],
                {"bubblingMouseEvents": true, "color": "#6868eaff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6868eaff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7f4c72053d017472c36d2eea9dc7225e = L.popup({"maxWidth": "100%"});

        
            
                var html_9e7cf92553c37c3d70b8b1d64a30df93 = $(`<div id="html_9e7cf92553c37c3d70b8b1d64a30df93" style="width: 100.0%; height: 100.0%;">Station 284<br>Result: 2.5%<br></div>`)[0];
                popup_7f4c72053d017472c36d2eea9dc7225e.setContent(html_9e7cf92553c37c3d70b8b1d64a30df93);
            
        

        circle_marker_336566e9de046fe9afbc25d6f8327756.bindPopup(popup_7f4c72053d017472c36d2eea9dc7225e)
        ;

        
    
    
            var circle_marker_f7562df07968b0350bdca3c9886f1ccf = L.circleMarker(
                [41.4366708, 2.186105],
                {"bubblingMouseEvents": true, "color": "#a2a2deff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a2a2deff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ef1d88919327200f68804c3669459a72 = L.popup({"maxWidth": "100%"});

        
            
                var html_191b046851e878e2f19c9bf4d5e47403 = $(`<div id="html_191b046851e878e2f19c9bf4d5e47403" style="width: 100.0%; height: 100.0%;">Station 285<br>Result: 1.2%<br></div>`)[0];
                popup_ef1d88919327200f68804c3669459a72.setContent(html_191b046851e878e2f19c9bf4d5e47403);
            
        

        circle_marker_f7562df07968b0350bdca3c9886f1ccf.bindPopup(popup_ef1d88919327200f68804c3669459a72)
        ;

        
    
    
            var circle_marker_8ea1e231669441d12ac1fcfa9574b692 = L.circleMarker(
                [41.4030225, 2.1913538],
                {"bubblingMouseEvents": true, "color": "#7f7fe5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7f7fe5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_929f1f71b39a901ccba05c5bbfbeba1a = L.popup({"maxWidth": "100%"});

        
            
                var html_fd0778409c524b2c2c063627ee946cd2 = $(`<div id="html_fd0778409c524b2c2c063627ee946cd2" style="width: 100.0%; height: 100.0%;">Station 286<br>Result: 2.0%<br></div>`)[0];
                popup_929f1f71b39a901ccba05c5bbfbeba1a.setContent(html_fd0778409c524b2c2c063627ee946cd2);
            
        

        circle_marker_8ea1e231669441d12ac1fcfa9574b692.bindPopup(popup_929f1f71b39a901ccba05c5bbfbeba1a)
        ;

        
    
    
            var circle_marker_14c11ecb25cd210e62da9cd6e0a0b380 = L.circleMarker(
                [41.4296439, 2.174444],
                {"bubblingMouseEvents": true, "color": "#d2d2d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d2d2d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b7cdef49dc8d82cadb95f781023a184d = L.popup({"maxWidth": "100%"});

        
            
                var html_71662b3732f23e60f3a146522e9e17c9 = $(`<div id="html_71662b3732f23e60f3a146522e9e17c9" style="width: 100.0%; height: 100.0%;">Station 288<br>Result: 0.0%<br></div>`)[0];
                popup_b7cdef49dc8d82cadb95f781023a184d.setContent(html_71662b3732f23e60f3a146522e9e17c9);
            
        

        circle_marker_14c11ecb25cd210e62da9cd6e0a0b380.bindPopup(popup_b7cdef49dc8d82cadb95f781023a184d)
        ;

        
    
    
            var circle_marker_ebdcb08b3551a01b85f8da3f8f4387d2 = L.circleMarker(
                [41.4166982, 2.1909952],
                {"bubblingMouseEvents": true, "color": "#a9a9dcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a9a9dcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_484cd724651559ef27a9422bec3dd3e8 = L.popup({"maxWidth": "100%"});

        
            
                var html_e71acd6246ef1bc276f85e203bc9ee17 = $(`<div id="html_e71acd6246ef1bc276f85e203bc9ee17" style="width: 100.0%; height: 100.0%;">Station 289<br>Result: 1.0%<br></div>`)[0];
                popup_484cd724651559ef27a9422bec3dd3e8.setContent(html_e71acd6246ef1bc276f85e203bc9ee17);
            
        

        circle_marker_ebdcb08b3551a01b85f8da3f8f4387d2.bindPopup(popup_484cd724651559ef27a9422bec3dd3e8)
        ;

        
    
    
            var circle_marker_6d13f41cb2c2b5f8ddea5bc7cdc0d63d = L.circleMarker(
                [41.4373376, 2.1740962],
                {"bubblingMouseEvents": true, "color": "#9898e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9898e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f2560ee05903470fae954e5a76bd9433 = L.popup({"maxWidth": "100%"});

        
            
                var html_07c0b9148522bacfbd22c14e5206d346 = $(`<div id="html_07c0b9148522bacfbd22c14e5206d346" style="width: 100.0%; height: 100.0%;">Station 290<br>Result: 1.4%<br></div>`)[0];
                popup_f2560ee05903470fae954e5a76bd9433.setContent(html_07c0b9148522bacfbd22c14e5206d346);
            
        

        circle_marker_6d13f41cb2c2b5f8ddea5bc7cdc0d63d.bindPopup(popup_f2560ee05903470fae954e5a76bd9433)
        ;

        
    
    
            var circle_marker_db5005c764081af233e120842a707955 = L.circleMarker(
                [41.426078, 2.1751572],
                {"bubblingMouseEvents": true, "color": "#b3b3daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b3b3daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6398ce5f3e3d9cde5e69b13140d26850 = L.popup({"maxWidth": "100%"});

        
            
                var html_f6a77492a2e3bb6f1cf70496eff085f9 = $(`<div id="html_f6a77492a2e3bb6f1cf70496eff085f9" style="width: 100.0%; height: 100.0%;">Station 291<br>Result: 0.8%<br></div>`)[0];
                popup_6398ce5f3e3d9cde5e69b13140d26850.setContent(html_f6a77492a2e3bb6f1cf70496eff085f9);
            
        

        circle_marker_db5005c764081af233e120842a707955.bindPopup(popup_6398ce5f3e3d9cde5e69b13140d26850)
        ;

        
    
    
            var circle_marker_e313fb6f2eb1d81bc3ff2a0a4eb50146 = L.circleMarker(
                [41.4300161, 2.1720191],
                {"bubblingMouseEvents": true, "color": "#d4d1d1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4d1d1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_dcc56a245935c728d00fa5d114d656f7 = L.popup({"maxWidth": "100%"});

        
            
                var html_175477b3af73049592cd23d87006b420 = $(`<div id="html_175477b3af73049592cd23d87006b420" style="width: 100.0%; height: 100.0%;">Station 292<br>Result: -0.1%<br></div>`)[0];
                popup_dcc56a245935c728d00fa5d114d656f7.setContent(html_175477b3af73049592cd23d87006b420);
            
        

        circle_marker_e313fb6f2eb1d81bc3ff2a0a4eb50146.bindPopup(popup_dcc56a245935c728d00fa5d114d656f7)
        ;

        
    
    
            var circle_marker_a997ab56346310c055859b08e11668aa = L.circleMarker(
                [41.4283127, 2.1629889],
                {"bubblingMouseEvents": true, "color": "#9c9cdfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9c9cdfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_35d2378681a1a3495be87251ad0c1b0c = L.popup({"maxWidth": "100%"});

        
            
                var html_d28c88f9c94b10474fa04fcd44681489 = $(`<div id="html_d28c88f9c94b10474fa04fcd44681489" style="width: 100.0%; height: 100.0%;">Station 293<br>Result: 1.3%<br></div>`)[0];
                popup_35d2378681a1a3495be87251ad0c1b0c.setContent(html_d28c88f9c94b10474fa04fcd44681489);
            
        

        circle_marker_a997ab56346310c055859b08e11668aa.bindPopup(popup_35d2378681a1a3495be87251ad0c1b0c)
        ;

        
    
    
            var circle_marker_15527023c8f1bc6474faef63d26eb0b1 = L.circleMarker(
                [41.4363473, 2.1706752],
                {"bubblingMouseEvents": true, "color": "#d4cfcfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4cfcfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_cbd25f74376336fbe004f40b1c5841e0 = L.popup({"maxWidth": "100%"});

        
            
                var html_4cbbb28c7d70c8061bfd47ec169349ec = $(`<div id="html_4cbbb28c7d70c8061bfd47ec169349ec" style="width: 100.0%; height: 100.0%;">Station 294<br>Result: -0.1%<br></div>`)[0];
                popup_cbd25f74376336fbe004f40b1c5841e0.setContent(html_4cbbb28c7d70c8061bfd47ec169349ec);
            
        

        circle_marker_15527023c8f1bc6474faef63d26eb0b1.bindPopup(popup_cbd25f74376336fbe004f40b1c5841e0)
        ;

        
    
    
            var circle_marker_8a98e84a996fcd717e1fa434df92884a = L.circleMarker(
                [41.433384, 2.1716309],
                {"bubblingMouseEvents": true, "color": "#c9c9d5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c9c9d5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c21a428cb27456200eb5c602e903190a = L.popup({"maxWidth": "100%"});

        
            
                var html_6a22f570777f36e78e12ae042da3f303 = $(`<div id="html_6a22f570777f36e78e12ae042da3f303" style="width: 100.0%; height: 100.0%;">Station 295<br>Result: 0.2%<br></div>`)[0];
                popup_c21a428cb27456200eb5c602e903190a.setContent(html_6a22f570777f36e78e12ae042da3f303);
            
        

        circle_marker_8a98e84a996fcd717e1fa434df92884a.bindPopup(popup_c21a428cb27456200eb5c602e903190a)
        ;

        
    
    
            var circle_marker_b948d5146f09cfeee2b77db27b3d7661 = L.circleMarker(
                [41.4364887, 2.1841014],
                {"bubblingMouseEvents": true, "color": "#c3c3d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c3c3d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f7de80a4b63dde18b56b8431f1ea24e8 = L.popup({"maxWidth": "100%"});

        
            
                var html_a8fabda9e2f47c032e423d0acc46623d = $(`<div id="html_a8fabda9e2f47c032e423d0acc46623d" style="width: 100.0%; height: 100.0%;">Station 296<br>Result: 0.4%<br></div>`)[0];
                popup_f7de80a4b63dde18b56b8431f1ea24e8.setContent(html_a8fabda9e2f47c032e423d0acc46623d);
            
        

        circle_marker_b948d5146f09cfeee2b77db27b3d7661.bindPopup(popup_f7de80a4b63dde18b56b8431f1ea24e8)
        ;

        
    
    
            var circle_marker_9d5c6e09c8ee9957447483e756f35b85 = L.circleMarker(
                [41.4388223, 2.1767828],
                {"bubblingMouseEvents": true, "color": "#bfbfd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bfbfd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8be213e443e55002a612487d4fe92b82 = L.popup({"maxWidth": "100%"});

        
            
                var html_d41018dfe85b130df752c8e1bb2ea44b = $(`<div id="html_d41018dfe85b130df752c8e1bb2ea44b" style="width: 100.0%; height: 100.0%;">Station 297<br>Result: 0.5%<br></div>`)[0];
                popup_8be213e443e55002a612487d4fe92b82.setContent(html_d41018dfe85b130df752c8e1bb2ea44b);
            
        

        circle_marker_9d5c6e09c8ee9957447483e756f35b85.bindPopup(popup_8be213e443e55002a612487d4fe92b82)
        ;

        
    
    
            var circle_marker_d7e9af1e1eb3765486957d21e76f2f6f = L.circleMarker(
                [41.4347233, 2.1817718],
                {"bubblingMouseEvents": true, "color": "#d5cdcdff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5cdcdff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_206797c41be534636335f2a7fb0b2f23 = L.popup({"maxWidth": "100%"});

        
            
                var html_a074594a59709730339602c51cca7f65 = $(`<div id="html_a074594a59709730339602c51cca7f65" style="width: 100.0%; height: 100.0%;">Station 298<br>Result: -0.2%<br></div>`)[0];
                popup_206797c41be534636335f2a7fb0b2f23.setContent(html_a074594a59709730339602c51cca7f65);
            
        

        circle_marker_d7e9af1e1eb3765486957d21e76f2f6f.bindPopup(popup_206797c41be534636335f2a7fb0b2f23)
        ;

        
    
    
            var circle_marker_5b4129415b4413a195c611759a0db513 = L.circleMarker(
                [41.4340849, 2.1748267],
                {"bubblingMouseEvents": true, "color": "#acacdcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#acacdcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4b6f80f145a260322e66d7eb84faa0ce = L.popup({"maxWidth": "100%"});

        
            
                var html_460f9aed87f291e4889cad6eb0d31cc2 = $(`<div id="html_460f9aed87f291e4889cad6eb0d31cc2" style="width: 100.0%; height: 100.0%;">Station 299<br>Result: 0.9%<br></div>`)[0];
                popup_4b6f80f145a260322e66d7eb84faa0ce.setContent(html_460f9aed87f291e4889cad6eb0d31cc2);
            
        

        circle_marker_5b4129415b4413a195c611759a0db513.bindPopup(popup_4b6f80f145a260322e66d7eb84faa0ce)
        ;

        
    
    
            var circle_marker_1abaf71f5dd3c86c417cd5de9522dfe0 = L.circleMarker(
                [41.4315843, 2.1769107],
                {"bubblingMouseEvents": true, "color": "#aaaadcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#aaaadcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d686d167f246c8144416d6d642669163 = L.popup({"maxWidth": "100%"});

        
            
                var html_cadbd7256a876acffc848f73a0785a44 = $(`<div id="html_cadbd7256a876acffc848f73a0785a44" style="width: 100.0%; height: 100.0%;">Station 300<br>Result: 1.0%<br></div>`)[0];
                popup_d686d167f246c8144416d6d642669163.setContent(html_cadbd7256a876acffc848f73a0785a44);
            
        

        circle_marker_1abaf71f5dd3c86c417cd5de9522dfe0.bindPopup(popup_d686d167f246c8144416d6d642669163)
        ;

        
    
    
            var circle_marker_23535880467b6e6e585a6f847fa1f0da = L.circleMarker(
                [41.4366871, 2.1693134],
                {"bubblingMouseEvents": true, "color": "#bebed8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bebed8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9144469867a078fb83d340dd41a742ad = L.popup({"maxWidth": "100%"});

        
            
                var html_ce2421789a904b2b0ffe0f05cec08957 = $(`<div id="html_ce2421789a904b2b0ffe0f05cec08957" style="width: 100.0%; height: 100.0%;">Station 301<br>Result: 0.5%<br></div>`)[0];
                popup_9144469867a078fb83d340dd41a742ad.setContent(html_ce2421789a904b2b0ffe0f05cec08957);
            
        

        circle_marker_23535880467b6e6e585a6f847fa1f0da.bindPopup(popup_9144469867a078fb83d340dd41a742ad)
        ;

        
    
    
            var circle_marker_35555ab6a8ab765f0037ce69088a11f3 = L.circleMarker(
                [41.3906352, 2.111541],
                {"bubblingMouseEvents": true, "color": "#d4d2d2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4d2d2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f77e93c814d50f79a2330546b3ab8ff1 = L.popup({"maxWidth": "100%"});

        
            
                var html_d2f33b7f4b13127567eba95ab588ab71 = $(`<div id="html_d2f33b7f4b13127567eba95ab588ab71" style="width: 100.0%; height: 100.0%;">Station 302<br>Result: -0.0%<br></div>`)[0];
                popup_f77e93c814d50f79a2330546b3ab8ff1.setContent(html_d2f33b7f4b13127567eba95ab588ab71);
            
        

        circle_marker_35555ab6a8ab765f0037ce69088a11f3.bindPopup(popup_f77e93c814d50f79a2330546b3ab8ff1)
        ;

        
    
    
            var circle_marker_bf9f0f1ea713797ae22df49508162e9a = L.circleMarker(
                [41.3934324, 2.115107],
                {"bubblingMouseEvents": true, "color": "#d5cbcbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5cbcbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_fe47ec23575f78efa81d334f03c64ebb = L.popup({"maxWidth": "100%"});

        
            
                var html_6189c5f42eae016f0266f403708ca635 = $(`<div id="html_6189c5f42eae016f0266f403708ca635" style="width: 100.0%; height: 100.0%;">Station 303<br>Result: -0.2%<br></div>`)[0];
                popup_fe47ec23575f78efa81d334f03c64ebb.setContent(html_6189c5f42eae016f0266f403708ca635);
            
        

        circle_marker_bf9f0f1ea713797ae22df49508162e9a.bindPopup(popup_fe47ec23575f78efa81d334f03c64ebb)
        ;

        
    
    
            var circle_marker_110eed3601881e278e3a61e8bd28428c = L.circleMarker(
                [41.39038, 2.121],
                {"bubblingMouseEvents": true, "color": "#bebed8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bebed8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c60370ff84a10df538133ce720173465 = L.popup({"maxWidth": "100%"});

        
            
                var html_5562bce9d7ecf29b2e825e6ce727e3eb = $(`<div id="html_5562bce9d7ecf29b2e825e6ce727e3eb" style="width: 100.0%; height: 100.0%;">Station 304<br>Result: 0.5%<br></div>`)[0];
                popup_c60370ff84a10df538133ce720173465.setContent(html_5562bce9d7ecf29b2e825e6ce727e3eb);
            
        

        circle_marker_110eed3601881e278e3a61e8bd28428c.bindPopup(popup_c60370ff84a10df538133ce720173465)
        ;

        
    
    
            var circle_marker_ddf59e07f1cc975081419f5972c8590e = L.circleMarker(
                [41.3875297, 2.1237141],
                {"bubblingMouseEvents": true, "color": "#cbcbd5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cbcbd5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_64ef1cbb4bcd44a5e69463467a01ca87 = L.popup({"maxWidth": "100%"});

        
            
                var html_d24984d6ad3145caa145518e234ae20e = $(`<div id="html_d24984d6ad3145caa145518e234ae20e" style="width: 100.0%; height: 100.0%;">Station 305<br>Result: 0.2%<br></div>`)[0];
                popup_64ef1cbb4bcd44a5e69463467a01ca87.setContent(html_d24984d6ad3145caa145518e234ae20e);
            
        

        circle_marker_ddf59e07f1cc975081419f5972c8590e.bindPopup(popup_64ef1cbb4bcd44a5e69463467a01ca87)
        ;

        
    
    
            var circle_marker_53f3349ee453b8c66675ad39411a6b7a = L.circleMarker(
                [41.3853868, 2.122893],
                {"bubblingMouseEvents": true, "color": "#c9c9d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c9c9d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_35b2ed8cadd580b705b24f79d42583ce = L.popup({"maxWidth": "100%"});

        
            
                var html_e7e602532e3381370eb8e04841447941 = $(`<div id="html_e7e602532e3381370eb8e04841447941" style="width: 100.0%; height: 100.0%;">Station 306<br>Result: 0.3%<br></div>`)[0];
                popup_35b2ed8cadd580b705b24f79d42583ce.setContent(html_e7e602532e3381370eb8e04841447941);
            
        

        circle_marker_53f3349ee453b8c66675ad39411a6b7a.bindPopup(popup_35b2ed8cadd580b705b24f79d42583ce)
        ;

        
    
    
            var circle_marker_d1d2fb13f2f83ab75939d9942ee58376 = L.circleMarker(
                [41.3791986, 2.1135824],
                {"bubblingMouseEvents": true, "color": "#c7c7d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c7c7d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_97175196234f08e333f65bbcae008819 = L.popup({"maxWidth": "100%"});

        
            
                var html_2bbbf232102d15b62227d52bafd315df = $(`<div id="html_2bbbf232102d15b62227d52bafd315df" style="width: 100.0%; height: 100.0%;">Station 307<br>Result: 0.3%<br></div>`)[0];
                popup_97175196234f08e333f65bbcae008819.setContent(html_2bbbf232102d15b62227d52bafd315df);
            
        

        circle_marker_d1d2fb13f2f83ab75939d9942ee58376.bindPopup(popup_97175196234f08e333f65bbcae008819)
        ;

        
    
    
            var circle_marker_e8e04ae9fffcac66f89673c1207c41fb = L.circleMarker(
                [41.37684, 2.114029],
                {"bubblingMouseEvents": true, "color": "#c2c2d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c2c2d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ce82c98e6c5eec95a373f7538863dcf7 = L.popup({"maxWidth": "100%"});

        
            
                var html_79668cb3b098f7239f2995906f702ac7 = $(`<div id="html_79668cb3b098f7239f2995906f702ac7" style="width: 100.0%; height: 100.0%;">Station 308<br>Result: 0.4%<br></div>`)[0];
                popup_ce82c98e6c5eec95a373f7538863dcf7.setContent(html_79668cb3b098f7239f2995906f702ac7);
            
        

        circle_marker_e8e04ae9fffcac66f89673c1207c41fb.bindPopup(popup_ce82c98e6c5eec95a373f7538863dcf7)
        ;

        
    
    
            var circle_marker_4465305127b31e7b56a4c1577573ec10 = L.circleMarker(
                [41.3770199, 2.1169828],
                {"bubblingMouseEvents": true, "color": "#bbbbd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bbbbd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_fd90ba4938d1d4b2312e0bb2cba49beb = L.popup({"maxWidth": "100%"});

        
            
                var html_bbd9f515a7ac27c4373d3652d9a24857 = $(`<div id="html_bbd9f515a7ac27c4373d3652d9a24857" style="width: 100.0%; height: 100.0%;">Station 309<br>Result: 0.6%<br></div>`)[0];
                popup_fd90ba4938d1d4b2312e0bb2cba49beb.setContent(html_bbd9f515a7ac27c4373d3652d9a24857);
            
        

        circle_marker_4465305127b31e7b56a4c1577573ec10.bindPopup(popup_fd90ba4938d1d4b2312e0bb2cba49beb)
        ;

        
    
    
            var circle_marker_da40bf094af5c07a4b74968bcedf386a = L.circleMarker(
                [41.3812111, 2.1190863],
                {"bubblingMouseEvents": true, "color": "#8686e3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8686e3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_3e424e92be29c2806652a0c03a39fe87 = L.popup({"maxWidth": "100%"});

        
            
                var html_4bccb6ba5091b1045db4feaba5b9431f = $(`<div id="html_4bccb6ba5091b1045db4feaba5b9431f" style="width: 100.0%; height: 100.0%;">Station 310<br>Result: 1.8%<br></div>`)[0];
                popup_3e424e92be29c2806652a0c03a39fe87.setContent(html_4bccb6ba5091b1045db4feaba5b9431f);
            
        

        circle_marker_da40bf094af5c07a4b74968bcedf386a.bindPopup(popup_3e424e92be29c2806652a0c03a39fe87)
        ;

        
    
    
            var circle_marker_843def4f4fb3e27cb2ba75ec5528c105 = L.circleMarker(
                [41.3789061, 2.1233038],
                {"bubblingMouseEvents": true, "color": "#b2b2daff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b2b2daff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9f7bfdfc3276c57cb705effa84e1862e = L.popup({"maxWidth": "100%"});

        
            
                var html_ee1adbe851a5a0254c59c4d4ae45b798 = $(`<div id="html_ee1adbe851a5a0254c59c4d4ae45b798" style="width: 100.0%; height: 100.0%;">Station 312<br>Result: 0.8%<br></div>`)[0];
                popup_9f7bfdfc3276c57cb705effa84e1862e.setContent(html_ee1adbe851a5a0254c59c4d4ae45b798);
            
        

        circle_marker_843def4f4fb3e27cb2ba75ec5528c105.bindPopup(popup_9f7bfdfc3276c57cb705effa84e1862e)
        ;

        
    
    
            var circle_marker_69127d4123479f43db7864dc82db677e = L.circleMarker(
                [41.3754188, 2.1297823],
                {"bubblingMouseEvents": true, "color": "#a1a1deff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a1a1deff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_a8634a8b973626ae03a6b7837e027133 = L.popup({"maxWidth": "100%"});

        
            
                var html_c731c444861f0d760c080177ee8383cf = $(`<div id="html_c731c444861f0d760c080177ee8383cf" style="width: 100.0%; height: 100.0%;">Station 313<br>Result: 1.2%<br></div>`)[0];
                popup_a8634a8b973626ae03a6b7837e027133.setContent(html_c731c444861f0d760c080177ee8383cf);
            
        

        circle_marker_69127d4123479f43db7864dc82db677e.bindPopup(popup_a8634a8b973626ae03a6b7837e027133)
        ;

        
    
    
            var circle_marker_18c5a8326f511beb78fed2d9fff57fd4 = L.circleMarker(
                [41.3783067, 2.1297303],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_88373d09b0678dc6e57273eb932abae3 = L.popup({"maxWidth": "100%"});

        
            
                var html_67a9b31015e22a1e365b283aa80dddcb = $(`<div id="html_67a9b31015e22a1e365b283aa80dddcb" style="width: 100.0%; height: 100.0%;">Station 314<br>Result: 0.9%<br></div>`)[0];
                popup_88373d09b0678dc6e57273eb932abae3.setContent(html_67a9b31015e22a1e365b283aa80dddcb);
            
        

        circle_marker_18c5a8326f511beb78fed2d9fff57fd4.bindPopup(popup_88373d09b0678dc6e57273eb932abae3)
        ;

        
    
    
            var circle_marker_fe8224b7db777c5060a09fd1f6e44fcc = L.circleMarker(
                [41.4156285, 2.1817876],
                {"bubblingMouseEvents": true, "color": "#ababdcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ababdcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_20e825579613a5a4c9749f97e151ae06 = L.popup({"maxWidth": "100%"});

        
            
                var html_51d09714e2695d15c7b7bb3d20380a6b = $(`<div id="html_51d09714e2695d15c7b7bb3d20380a6b" style="width: 100.0%; height: 100.0%;">Station 315<br>Result: 1.0%<br></div>`)[0];
                popup_20e825579613a5a4c9749f97e151ae06.setContent(html_51d09714e2695d15c7b7bb3d20380a6b);
            
        

        circle_marker_fe8224b7db777c5060a09fd1f6e44fcc.bindPopup(popup_20e825579613a5a4c9749f97e151ae06)
        ;

        
    
    
            var circle_marker_697d27113afac198a108b2331b9be70e = L.circleMarker(
                [41.4224015, 2.198071],
                {"bubblingMouseEvents": true, "color": "#9898e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9898e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b3121c2d14d386177721f5600ec9c517 = L.popup({"maxWidth": "100%"});

        
            
                var html_57e773144c2883c7c43a202e35e5d726 = $(`<div id="html_57e773144c2883c7c43a202e35e5d726" style="width: 100.0%; height: 100.0%;">Station 316<br>Result: 1.4%<br></div>`)[0];
                popup_b3121c2d14d386177721f5600ec9c517.setContent(html_57e773144c2883c7c43a202e35e5d726);
            
        

        circle_marker_697d27113afac198a108b2331b9be70e.bindPopup(popup_b3121c2d14d386177721f5600ec9c517)
        ;

        
    
    
            var circle_marker_b7ea22936f0bbd8e9be9fd113dc7aa94 = L.circleMarker(
                [41.4256626, 2.2008632],
                {"bubblingMouseEvents": true, "color": "#e38989ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e38989ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6425dadcc17f81a087677ee660539ac3 = L.popup({"maxWidth": "100%"});

        
            
                var html_e6d2e1f7e26c203951a4952e6846931d = $(`<div id="html_e6d2e1f7e26c203951a4952e6846931d" style="width: 100.0%; height: 100.0%;">Station 317<br>Result: -1.8%<br></div>`)[0];
                popup_6425dadcc17f81a087677ee660539ac3.setContent(html_e6d2e1f7e26c203951a4952e6846931d);
            
        

        circle_marker_b7ea22936f0bbd8e9be9fd113dc7aa94.bindPopup(popup_6425dadcc17f81a087677ee660539ac3)
        ;

        
    
    
            var circle_marker_c7f92c666055098ba32a79e9e93a288c = L.circleMarker(
                [41.412427, 2.170592],
                {"bubblingMouseEvents": true, "color": "#ceced4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ceced4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_361b9cd74b2c2a26d587919f0bcd6497 = L.popup({"maxWidth": "100%"});

        
            
                var html_9b00abdb5f8809ce3dc55d35b9c6fa36 = $(`<div id="html_9b00abdb5f8809ce3dc55d35b9c6fa36" style="width: 100.0%; height: 100.0%;">Station 318<br>Result: 0.1%<br></div>`)[0];
                popup_361b9cd74b2c2a26d587919f0bcd6497.setContent(html_9b00abdb5f8809ce3dc55d35b9c6fa36);
            
        

        circle_marker_c7f92c666055098ba32a79e9e93a288c.bindPopup(popup_361b9cd74b2c2a26d587919f0bcd6497)
        ;

        
    
    
            var circle_marker_2d7e5840c3e9e0afc8fd176861857929 = L.circleMarker(
                [41.3937414, 2.1455022],
                {"bubblingMouseEvents": true, "color": "#afafdbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#afafdbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2a1f315b8640aabd8e2ca01523fe63d1 = L.popup({"maxWidth": "100%"});

        
            
                var html_126bb6b96ab9f9ece05eb0ee39611488 = $(`<div id="html_126bb6b96ab9f9ece05eb0ee39611488" style="width: 100.0%; height: 100.0%;">Station 319<br>Result: 0.8%<br></div>`)[0];
                popup_2a1f315b8640aabd8e2ca01523fe63d1.setContent(html_126bb6b96ab9f9ece05eb0ee39611488);
            
        

        circle_marker_2d7e5840c3e9e0afc8fd176861857929.bindPopup(popup_2a1f315b8640aabd8e2ca01523fe63d1)
        ;

        
    
    
            var circle_marker_87b59b32d8e996a2d9f75bd48ede3dda = L.circleMarker(
                [41.400305, 2.149144],
                {"bubblingMouseEvents": true, "color": "#e38a8aff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e38a8aff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_430dc288d2e39a505ba1de6418f8188b = L.popup({"maxWidth": "100%"});

        
            
                var html_cfe96326d23e57a3ecc542264bf85184 = $(`<div id="html_cfe96326d23e57a3ecc542264bf85184" style="width: 100.0%; height: 100.0%;">Station 320<br>Result: -1.7%<br></div>`)[0];
                popup_430dc288d2e39a505ba1de6418f8188b.setContent(html_cfe96326d23e57a3ecc542264bf85184);
            
        

        circle_marker_87b59b32d8e996a2d9f75bd48ede3dda.bindPopup(popup_430dc288d2e39a505ba1de6418f8188b)
        ;

        
    
    
            var circle_marker_b2423ced0c3fb0899f63d49751d4de9f = L.circleMarker(
                [41.4031529, 2.1445843],
                {"bubblingMouseEvents": true, "color": "#dda3a3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dda3a3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f753c22602c14ae7f051f17904fbea73 = L.popup({"maxWidth": "100%"});

        
            
                var html_fa26a603e8c4872ed53c33c3de6ba330 = $(`<div id="html_fa26a603e8c4872ed53c33c3de6ba330" style="width: 100.0%; height: 100.0%;">Station 321<br>Result: -1.1%<br></div>`)[0];
                popup_f753c22602c14ae7f051f17904fbea73.setContent(html_fa26a603e8c4872ed53c33c3de6ba330);
            
        

        circle_marker_b2423ced0c3fb0899f63d49751d4de9f.bindPopup(popup_f753c22602c14ae7f051f17904fbea73)
        ;

        
    
    
            var circle_marker_76d5f688adb86282b439968e0160c7d4 = L.circleMarker(
                [41.4009, 2.13892],
                {"bubblingMouseEvents": true, "color": "#d4ceceff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4ceceff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e3adc0d71ce5298325de68fbe1da76a2 = L.popup({"maxWidth": "100%"});

        
            
                var html_ad9a86918f9d679a1c36c45df990d1ca = $(`<div id="html_ad9a86918f9d679a1c36c45df990d1ca" style="width: 100.0%; height: 100.0%;">Station 322<br>Result: -0.1%<br></div>`)[0];
                popup_e3adc0d71ce5298325de68fbe1da76a2.setContent(html_ad9a86918f9d679a1c36c45df990d1ca);
            
        

        circle_marker_76d5f688adb86282b439968e0160c7d4.bindPopup(popup_e3adc0d71ce5298325de68fbe1da76a2)
        ;

        
    
    
            var circle_marker_624ca6338a5e46979b410002566ffb0a = L.circleMarker(
                [41.3981616, 2.1386719],
                {"bubblingMouseEvents": true, "color": "#d2d2d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d2d2d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_1e92959cd8af6edd5206435e1977e44b = L.popup({"maxWidth": "100%"});

        
            
                var html_2f8df6c96b9265e6af8a117dc30fc0fa = $(`<div id="html_2f8df6c96b9265e6af8a117dc30fc0fa" style="width: 100.0%; height: 100.0%;">Station 323<br>Result: 0.0%<br></div>`)[0];
                popup_1e92959cd8af6edd5206435e1977e44b.setContent(html_2f8df6c96b9265e6af8a117dc30fc0fa);
            
        

        circle_marker_624ca6338a5e46979b410002566ffb0a.bindPopup(popup_1e92959cd8af6edd5206435e1977e44b)
        ;

        
    
    
            var circle_marker_1ddf8fc703e865cfbf683d250e31acf8 = L.circleMarker(
                [41.3969455, 2.136346],
                {"bubblingMouseEvents": true, "color": "#c3c3d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c3c3d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_bda1052ab68c422ff067289b026d807f = L.popup({"maxWidth": "100%"});

        
            
                var html_4774fe55ad2b7b2b0aeeef498eea7cd0 = $(`<div id="html_4774fe55ad2b7b2b0aeeef498eea7cd0" style="width: 100.0%; height: 100.0%;">Station 324<br>Result: 0.4%<br></div>`)[0];
                popup_bda1052ab68c422ff067289b026d807f.setContent(html_4774fe55ad2b7b2b0aeeef498eea7cd0);
            
        

        circle_marker_1ddf8fc703e865cfbf683d250e31acf8.bindPopup(popup_bda1052ab68c422ff067289b026d807f)
        ;

        
    
    
            var circle_marker_80ef40cef5deab310a905faa604f0537 = L.circleMarker(
                [41.3949601, 2.1302775],
                {"bubblingMouseEvents": true, "color": "#b7b7d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b7b7d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8b3c400a271d601cff82e80aa9004be4 = L.popup({"maxWidth": "100%"});

        
            
                var html_a643be40be0f300b5cdfc3821fa9f0c9 = $(`<div id="html_a643be40be0f300b5cdfc3821fa9f0c9" style="width: 100.0%; height: 100.0%;">Station 325<br>Result: 0.7%<br></div>`)[0];
                popup_8b3c400a271d601cff82e80aa9004be4.setContent(html_a643be40be0f300b5cdfc3821fa9f0c9);
            
        

        circle_marker_80ef40cef5deab310a905faa604f0537.bindPopup(popup_8b3c400a271d601cff82e80aa9004be4)
        ;

        
    
    
            var circle_marker_28d892f52eca88c991a1e2c6465f187f = L.circleMarker(
                [41.4074131, 2.1381069],
                {"bubblingMouseEvents": true, "color": "#d4d2d2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4d2d2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b996fa246b2510fd04f90700548a362a = L.popup({"maxWidth": "100%"});

        
            
                var html_067a049f0cf5eb6cbf43c5dabec5a88d = $(`<div id="html_067a049f0cf5eb6cbf43c5dabec5a88d" style="width: 100.0%; height: 100.0%;">Station 326<br>Result: -0.0%<br></div>`)[0];
                popup_b996fa246b2510fd04f90700548a362a.setContent(html_067a049f0cf5eb6cbf43c5dabec5a88d);
            
        

        circle_marker_28d892f52eca88c991a1e2c6465f187f.bindPopup(popup_b996fa246b2510fd04f90700548a362a)
        ;

        
    
    
            var circle_marker_96678554e81e1e012b712d5fca98b0b0 = L.circleMarker(
                [41.4050074, 2.134603],
                {"bubblingMouseEvents": true, "color": "#d4cfcfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4cfcfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8571b6da6e2b14e4445d7dd7b975e740 = L.popup({"maxWidth": "100%"});

        
            
                var html_1a983f29ca86c416168296116f9f486c = $(`<div id="html_1a983f29ca86c416168296116f9f486c" style="width: 100.0%; height: 100.0%;">Station 327<br>Result: -0.1%<br></div>`)[0];
                popup_8571b6da6e2b14e4445d7dd7b975e740.setContent(html_1a983f29ca86c416168296116f9f486c);
            
        

        circle_marker_96678554e81e1e012b712d5fca98b0b0.bindPopup(popup_8571b6da6e2b14e4445d7dd7b975e740)
        ;

        
    
    
            var circle_marker_dac070cce69164c7bc2992dd49acaba2 = L.circleMarker(
                [41.402988, 2.1344691],
                {"bubblingMouseEvents": true, "color": "#cbcbd5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cbcbd5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e6e39406456d31e9c51170cd978200bc = L.popup({"maxWidth": "100%"});

        
            
                var html_a16eae5bd86304c85b8ceace99e50d77 = $(`<div id="html_a16eae5bd86304c85b8ceace99e50d77" style="width: 100.0%; height: 100.0%;">Station 328<br>Result: 0.2%<br></div>`)[0];
                popup_e6e39406456d31e9c51170cd978200bc.setContent(html_a16eae5bd86304c85b8ceace99e50d77);
            
        

        circle_marker_dac070cce69164c7bc2992dd49acaba2.bindPopup(popup_e6e39406456d31e9c51170cd978200bc)
        ;

        
    
    
            var circle_marker_34a7d8cc4c75fd82f051a9b39fa915d7 = L.circleMarker(
                [41.4029965, 2.1283866],
                {"bubblingMouseEvents": true, "color": "#d3d3d3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d3d3d3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b8d6213261d3f7a608897eeb82350e65 = L.popup({"maxWidth": "100%"});

        
            
                var html_3df961b1f923ae1f4f3ce160ba3e290f = $(`<div id="html_3df961b1f923ae1f4f3ce160ba3e290f" style="width: 100.0%; height: 100.0%;">Station 329<br>Result: -0.0%<br></div>`)[0];
                popup_b8d6213261d3f7a608897eeb82350e65.setContent(html_3df961b1f923ae1f4f3ce160ba3e290f);
            
        

        circle_marker_34a7d8cc4c75fd82f051a9b39fa915d7.bindPopup(popup_b8d6213261d3f7a608897eeb82350e65)
        ;

        
    
    
            var circle_marker_2529cefe9eb97266549c3d28bda0bbd2 = L.circleMarker(
                [41.3970497, 2.1279409],
                {"bubblingMouseEvents": true, "color": "#cacad5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cacad5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_23bc91675d4e9a145b4fa5e696fa8b5c = L.popup({"maxWidth": "100%"});

        
            
                var html_95a98645108b4d96acca62d5c7c4deae = $(`<div id="html_95a98645108b4d96acca62d5c7c4deae" style="width: 100.0%; height: 100.0%;">Station 331<br>Result: 0.2%<br></div>`)[0];
                popup_23bc91675d4e9a145b4fa5e696fa8b5c.setContent(html_95a98645108b4d96acca62d5c7c4deae);
            
        

        circle_marker_2529cefe9eb97266549c3d28bda0bbd2.bindPopup(popup_23bc91675d4e9a145b4fa5e696fa8b5c)
        ;

        
    
    
            var circle_marker_5d05d278a461036df8ce8efc8e1f581b = L.circleMarker(
                [41.3998981, 2.1281922],
                {"bubblingMouseEvents": true, "color": "#d5cbcbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5cbcbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2a1257ed2bf6a4105acf64c648e2c260 = L.popup({"maxWidth": "100%"});

        
            
                var html_6f5a016980e63411812fae7ec1498c21 = $(`<div id="html_6f5a016980e63411812fae7ec1498c21" style="width: 100.0%; height: 100.0%;">Station 332<br>Result: -0.2%<br></div>`)[0];
                popup_2a1257ed2bf6a4105acf64c648e2c260.setContent(html_6f5a016980e63411812fae7ec1498c21);
            
        

        circle_marker_5d05d278a461036df8ce8efc8e1f581b.bindPopup(popup_2a1257ed2bf6a4105acf64c648e2c260)
        ;

        
    
    
            var circle_marker_a7849a781ed5ea3d143bffb42b16ac83 = L.circleMarker(
                [41.3954723, 2.1250451],
                {"bubblingMouseEvents": true, "color": "#d5cdcdff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5cdcdff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0eca9f8ba8c5bc3fb42718ea11146353 = L.popup({"maxWidth": "100%"});

        
            
                var html_c38e8bfeb58431942111467049d8ef3c = $(`<div id="html_c38e8bfeb58431942111467049d8ef3c" style="width: 100.0%; height: 100.0%;">Station 333<br>Result: -0.1%<br></div>`)[0];
                popup_0eca9f8ba8c5bc3fb42718ea11146353.setContent(html_c38e8bfeb58431942111467049d8ef3c);
            
        

        circle_marker_a7849a781ed5ea3d143bffb42b16ac83.bindPopup(popup_0eca9f8ba8c5bc3fb42718ea11146353)
        ;

        
    
    
            var circle_marker_d5050cb41c4f43f9d5bd0bb274c7cb3e = L.circleMarker(
                [41.400793, 2.122889],
                {"bubblingMouseEvents": true, "color": "#d7c0c0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c0c0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_3d0ff83963bb9adf6714ae886c5f20e4 = L.popup({"maxWidth": "100%"});

        
            
                var html_7eff9e899a0f4ba0dbe7760c3a1e4969 = $(`<div id="html_7eff9e899a0f4ba0dbe7760c3a1e4969" style="width: 100.0%; height: 100.0%;">Station 334<br>Result: -0.5%<br></div>`)[0];
                popup_3d0ff83963bb9adf6714ae886c5f20e4.setContent(html_7eff9e899a0f4ba0dbe7760c3a1e4969);
            
        

        circle_marker_d5050cb41c4f43f9d5bd0bb274c7cb3e.bindPopup(popup_3d0ff83963bb9adf6714ae886c5f20e4)
        ;

        
    
    
            var circle_marker_3a6f2b71cb0785df9003da76a022a656 = L.circleMarker(
                [41.3935355, 2.1231228],
                {"bubblingMouseEvents": true, "color": "#dab3b3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dab3b3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e9e6b2fa088e3183738d45217190e885 = L.popup({"maxWidth": "100%"});

        
            
                var html_5d0e85dc7fbc6dd7a73d0efc754593cb = $(`<div id="html_5d0e85dc7fbc6dd7a73d0efc754593cb" style="width: 100.0%; height: 100.0%;">Station 335<br>Result: -0.8%<br></div>`)[0];
                popup_e9e6b2fa088e3183738d45217190e885.setContent(html_5d0e85dc7fbc6dd7a73d0efc754593cb);
            
        

        circle_marker_3a6f2b71cb0785df9003da76a022a656.bindPopup(popup_e9e6b2fa088e3183738d45217190e885)
        ;

        
    
    
            var circle_marker_560fad8f90e32fea35882cd34b7478aa = L.circleMarker(
                [41.3948771, 2.1205394],
                {"bubblingMouseEvents": true, "color": "#d0d0d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d0d0d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2f537eec74fafc7560bdc2ae99039171 = L.popup({"maxWidth": "100%"});

        
            
                var html_74fa8e6644f723a5b142086021541061 = $(`<div id="html_74fa8e6644f723a5b142086021541061" style="width: 100.0%; height: 100.0%;">Station 336<br>Result: 0.1%<br></div>`)[0];
                popup_2f537eec74fafc7560bdc2ae99039171.setContent(html_74fa8e6644f723a5b142086021541061);
            
        

        circle_marker_560fad8f90e32fea35882cd34b7478aa.bindPopup(popup_2f537eec74fafc7560bdc2ae99039171)
        ;

        
    
    
            var circle_marker_ed85cd821b0fa3d4f98ddd0218126253 = L.circleMarker(
                [41.3986238, 2.1204941],
                {"bubblingMouseEvents": true, "color": "#ceced5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ceced5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4e52bd70dd4f2608e090a8dffdf65a7e = L.popup({"maxWidth": "100%"});

        
            
                var html_054918a693b87368cf1e5c9ce1f71103 = $(`<div id="html_054918a693b87368cf1e5c9ce1f71103" style="width: 100.0%; height: 100.0%;">Station 337<br>Result: 0.1%<br></div>`)[0];
                popup_4e52bd70dd4f2608e090a8dffdf65a7e.setContent(html_054918a693b87368cf1e5c9ce1f71103);
            
        

        circle_marker_ed85cd821b0fa3d4f98ddd0218126253.bindPopup(popup_4e52bd70dd4f2608e090a8dffdf65a7e)
        ;

        
    
    
            var circle_marker_f8addfb6f01df2b534c2349f7602c444 = L.circleMarker(
                [41.3977227, 2.1194557],
                {"bubblingMouseEvents": true, "color": "#c6c6d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c6c6d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_494e582d6def75a10fa6dbdf7b48e8b3 = L.popup({"maxWidth": "100%"});

        
            
                var html_c52c2fa3ef5859609c5c86d9c4a90200 = $(`<div id="html_c52c2fa3ef5859609c5c86d9c4a90200" style="width: 100.0%; height: 100.0%;">Station 338<br>Result: 0.3%<br></div>`)[0];
                popup_494e582d6def75a10fa6dbdf7b48e8b3.setContent(html_c52c2fa3ef5859609c5c86d9c4a90200);
            
        

        circle_marker_f8addfb6f01df2b534c2349f7602c444.bindPopup(popup_494e582d6def75a10fa6dbdf7b48e8b3)
        ;

        
    
    
            var circle_marker_8c03243d610c88762d44d1b3db50a013 = L.circleMarker(
                [41.4017084, 2.2053803],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_70283c97524fd8a9c9da08ac68e21297 = L.popup({"maxWidth": "100%"});

        
            
                var html_db4a1044e953721f0670804edb18118b = $(`<div id="html_db4a1044e953721f0670804edb18118b" style="width: 100.0%; height: 100.0%;">Station 339<br>Result: -6.0%<br></div>`)[0];
                popup_70283c97524fd8a9c9da08ac68e21297.setContent(html_db4a1044e953721f0670804edb18118b);
            
        

        circle_marker_8c03243d610c88762d44d1b3db50a013.bindPopup(popup_70283c97524fd8a9c9da08ac68e21297)
        ;

        
    
    
            var circle_marker_49245d83482613777595754759567a32 = L.circleMarker(
                [41.4361782, 2.2047037],
                {"bubblingMouseEvents": true, "color": "#bcbcd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bcbcd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6acd4d2d6f9a36c2927fee49a85377c4 = L.popup({"maxWidth": "100%"});

        
            
                var html_0ddb40ac9859a25a17039dad0296a136 = $(`<div id="html_0ddb40ac9859a25a17039dad0296a136" style="width: 100.0%; height: 100.0%;">Station 340<br>Result: 0.6%<br></div>`)[0];
                popup_6acd4d2d6f9a36c2927fee49a85377c4.setContent(html_0ddb40ac9859a25a17039dad0296a136);
            
        

        circle_marker_49245d83482613777595754759567a32.bindPopup(popup_6acd4d2d6f9a36c2927fee49a85377c4)
        ;

        
    
    
            var circle_marker_fe2a96cc2c0643cb892014e922ba6f60 = L.circleMarker(
                [41.4339212, 2.2062245],
                {"bubblingMouseEvents": true, "color": "#d3d3d3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d3d3d3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_14922c00bfd470c099ed4ce16871d7e7 = L.popup({"maxWidth": "100%"});

        
            
                var html_36874e91f34c74ff5b6d6c5bc101bcad = $(`<div id="html_36874e91f34c74ff5b6d6c5bc101bcad" style="width: 100.0%; height: 100.0%;">Station 341<br>Result: 0.0%<br></div>`)[0];
                popup_14922c00bfd470c099ed4ce16871d7e7.setContent(html_36874e91f34c74ff5b6d6c5bc101bcad);
            
        

        circle_marker_fe2a96cc2c0643cb892014e922ba6f60.bindPopup(popup_14922c00bfd470c099ed4ce16871d7e7)
        ;

        
    
    
            var circle_marker_3a0a5f352fcc75e4faa03e9e669f3138 = L.circleMarker(
                [41.4034967, 2.1936584],
                {"bubblingMouseEvents": true, "color": "#dab5b5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dab5b5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_576ab642db59cad40b1e5358f1631a32 = L.popup({"maxWidth": "100%"});

        
            
                var html_9ddad1ca755f0a37a1c27bc862faf05b = $(`<div id="html_9ddad1ca755f0a37a1c27bc862faf05b" style="width: 100.0%; height: 100.0%;">Station 342<br>Result: -0.7%<br></div>`)[0];
                popup_576ab642db59cad40b1e5358f1631a32.setContent(html_9ddad1ca755f0a37a1c27bc862faf05b);
            
        

        circle_marker_3a0a5f352fcc75e4faa03e9e669f3138.bindPopup(popup_576ab642db59cad40b1e5358f1631a32)
        ;

        
    
    
            var circle_marker_48ae74fae232ba8b073f83757597ee58 = L.circleMarker(
                [41.4389609, 2.1996179],
                {"bubblingMouseEvents": true, "color": "#dab3b3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dab3b3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7c3f1beea30b7c536495fc7709b8c15a = L.popup({"maxWidth": "100%"});

        
            
                var html_21b54701d200f6ec5f167885c9d58483 = $(`<div id="html_21b54701d200f6ec5f167885c9d58483" style="width: 100.0%; height: 100.0%;">Station 343<br>Result: -0.8%<br></div>`)[0];
                popup_7c3f1beea30b7c536495fc7709b8c15a.setContent(html_21b54701d200f6ec5f167885c9d58483);
            
        

        circle_marker_48ae74fae232ba8b073f83757597ee58.bindPopup(popup_7c3f1beea30b7c536495fc7709b8c15a)
        ;

        
    
    
            var circle_marker_0a86f026671ec6e5edef638cd850d54f = L.circleMarker(
                [41.4431441, 2.1996045],
                {"bubblingMouseEvents": true, "color": "#dda3a3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dda3a3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5cebbfd27684a5dd3c364dd88a866b97 = L.popup({"maxWidth": "100%"});

        
            
                var html_ef6a74e2966348a9431481274805abca = $(`<div id="html_ef6a74e2966348a9431481274805abca" style="width: 100.0%; height: 100.0%;">Station 344<br>Result: -1.1%<br></div>`)[0];
                popup_5cebbfd27684a5dd3c364dd88a866b97.setContent(html_ef6a74e2966348a9431481274805abca);
            
        

        circle_marker_0a86f026671ec6e5edef638cd850d54f.bindPopup(popup_5cebbfd27684a5dd3c364dd88a866b97)
        ;

        
    
    
            var circle_marker_e2f78993dd4fe607b61d5b9739ce9c11 = L.circleMarker(
                [41.3631066, 2.1398322],
                {"bubblingMouseEvents": true, "color": "#d7c4c4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c4c4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ff77af726d215f43e03240b77024304c = L.popup({"maxWidth": "100%"});

        
            
                var html_8397d3c678377371abb0ffa050e1996d = $(`<div id="html_8397d3c678377371abb0ffa050e1996d" style="width: 100.0%; height: 100.0%;">Station 345<br>Result: -0.4%<br></div>`)[0];
                popup_ff77af726d215f43e03240b77024304c.setContent(html_8397d3c678377371abb0ffa050e1996d);
            
        

        circle_marker_e2f78993dd4fe607b61d5b9739ce9c11.bindPopup(popup_ff77af726d215f43e03240b77024304c)
        ;

        
    
    
            var circle_marker_c403eb487bc1fc8a8c63b173a67f9ae5 = L.circleMarker(
                [41.360798, 2.138931],
                {"bubblingMouseEvents": true, "color": "#d5c9c9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5c9c9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_184916ad4b853097cbaaee374b43ec7d = L.popup({"maxWidth": "100%"});

        
            
                var html_d5247fca39c7d3a759980cfdb26fae27 = $(`<div id="html_d5247fca39c7d3a759980cfdb26fae27" style="width: 100.0%; height: 100.0%;">Station 346<br>Result: -0.2%<br></div>`)[0];
                popup_184916ad4b853097cbaaee374b43ec7d.setContent(html_d5247fca39c7d3a759980cfdb26fae27);
            
        

        circle_marker_c403eb487bc1fc8a8c63b173a67f9ae5.bindPopup(popup_184916ad4b853097cbaaee374b43ec7d)
        ;

        
    
    
            var circle_marker_ef9ebc9a57d636c29767516b41a983e3 = L.circleMarker(
                [41.3595484, 2.1417765],
                {"bubblingMouseEvents": true, "color": "#d4d0d0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4d0d0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f5be9840be4e9918485901d3c45a5976 = L.popup({"maxWidth": "100%"});

        
            
                var html_e00dba9a12bf13199f7ef57725dda4df = $(`<div id="html_e00dba9a12bf13199f7ef57725dda4df" style="width: 100.0%; height: 100.0%;">Station 347<br>Result: -0.1%<br></div>`)[0];
                popup_f5be9840be4e9918485901d3c45a5976.setContent(html_e00dba9a12bf13199f7ef57725dda4df);
            
        

        circle_marker_ef9ebc9a57d636c29767516b41a983e3.bindPopup(popup_f5be9840be4e9918485901d3c45a5976)
        ;

        
    
    
            var circle_marker_05caf220747302ea60c62ccf9e11472b = L.circleMarker(
                [41.357067, 2.141563],
                {"bubblingMouseEvents": true, "color": "#d6c7c7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c7c7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_756542b103fdc5960817d3287f201c43 = L.popup({"maxWidth": "100%"});

        
            
                var html_dd1072395a322e830d7dc5c7459556f2 = $(`<div id="html_dd1072395a322e830d7dc5c7459556f2" style="width: 100.0%; height: 100.0%;">Station 348<br>Result: -0.3%<br></div>`)[0];
                popup_756542b103fdc5960817d3287f201c43.setContent(html_dd1072395a322e830d7dc5c7459556f2);
            
        

        circle_marker_05caf220747302ea60c62ccf9e11472b.bindPopup(popup_756542b103fdc5960817d3287f201c43)
        ;

        
    
    
            var circle_marker_277586b47c277af7dba6481fbf042387 = L.circleMarker(
                [41.3573288, 2.1371996],
                {"bubblingMouseEvents": true, "color": "#d7c1c1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c1c1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_395e5acc8affa99adb872f3255691038 = L.popup({"maxWidth": "100%"});

        
            
                var html_173a3e9106354a19eec631e24faf2aa5 = $(`<div id="html_173a3e9106354a19eec631e24faf2aa5" style="width: 100.0%; height: 100.0%;">Station 349<br>Result: -0.4%<br></div>`)[0];
                popup_395e5acc8affa99adb872f3255691038.setContent(html_173a3e9106354a19eec631e24faf2aa5);
            
        

        circle_marker_277586b47c277af7dba6481fbf042387.bindPopup(popup_395e5acc8affa99adb872f3255691038)
        ;

        
    
    
            var circle_marker_c6552e0893f0b9b139e316c7558395f8 = L.circleMarker(
                [41.391756, 2.148291],
                {"bubblingMouseEvents": true, "color": "#a9a9dcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a9a9dcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_69a92392e31039b49a5bdb9ea6b410a5 = L.popup({"maxWidth": "100%"});

        
            
                var html_8c6dea10c00721ea31c1134662663fef = $(`<div id="html_8c6dea10c00721ea31c1134662663fef" style="width: 100.0%; height: 100.0%;">Station 350<br>Result: 1.0%<br></div>`)[0];
                popup_69a92392e31039b49a5bdb9ea6b410a5.setContent(html_8c6dea10c00721ea31c1134662663fef);
            
        

        circle_marker_c6552e0893f0b9b139e316c7558395f8.bindPopup(popup_69a92392e31039b49a5bdb9ea6b410a5)
        ;

        
    
    
            var circle_marker_9d28bdf5fe30a29a9c0ad3d906f99c66 = L.circleMarker(
                [41.3621232, 2.1356187],
                {"bubblingMouseEvents": true, "color": "#d5cbcbff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5cbcbff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_846e1e9d9c39ce0e20a15b18aade0fac = L.popup({"maxWidth": "100%"});

        
            
                var html_c81c53762002b7f6ea7b1020831910d2 = $(`<div id="html_c81c53762002b7f6ea7b1020831910d2" style="width: 100.0%; height: 100.0%;">Station 351<br>Result: -0.2%<br></div>`)[0];
                popup_846e1e9d9c39ce0e20a15b18aade0fac.setContent(html_c81c53762002b7f6ea7b1020831910d2);
            
        

        circle_marker_9d28bdf5fe30a29a9c0ad3d906f99c66.bindPopup(popup_846e1e9d9c39ce0e20a15b18aade0fac)
        ;

        
    
    
            var circle_marker_22577633be55cc79c4ed3e572c444b22 = L.circleMarker(
                [41.363279, 2.1341586],
                {"bubblingMouseEvents": true, "color": "#d2d2d4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d2d2d4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_54fee6054c959878f365dc4dbbf3c15c = L.popup({"maxWidth": "100%"});

        
            
                var html_3b949c87cf63ac7a84157e148133511c = $(`<div id="html_3b949c87cf63ac7a84157e148133511c" style="width: 100.0%; height: 100.0%;">Station 352<br>Result: 0.0%<br></div>`)[0];
                popup_54fee6054c959878f365dc4dbbf3c15c.setContent(html_3b949c87cf63ac7a84157e148133511c);
            
        

        circle_marker_22577633be55cc79c4ed3e572c444b22.bindPopup(popup_54fee6054c959878f365dc4dbbf3c15c)
        ;

        
    
    
            var circle_marker_2f4ae17066dd1f33deb670aa505b23a1 = L.circleMarker(
                [41.37541, 2.1232547],
                {"bubblingMouseEvents": true, "color": "#a5a5ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a5a5ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c72cd354e5e2c020332bf80ac4ee779c = L.popup({"maxWidth": "100%"});

        
            
                var html_df7d41bfa3bf3599a579cee3d6a4f8e8 = $(`<div id="html_df7d41bfa3bf3599a579cee3d6a4f8e8" style="width: 100.0%; height: 100.0%;">Station 353<br>Result: 1.1%<br></div>`)[0];
                popup_c72cd354e5e2c020332bf80ac4ee779c.setContent(html_df7d41bfa3bf3599a579cee3d6a4f8e8);
            
        

        circle_marker_2f4ae17066dd1f33deb670aa505b23a1.bindPopup(popup_c72cd354e5e2c020332bf80ac4ee779c)
        ;

        
    
    
            var circle_marker_bd49661db94f965521172f3c2f3d81c6 = L.circleMarker(
                [41.3759419, 2.1299539],
                {"bubblingMouseEvents": true, "color": "#a7a7dcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a7a7dcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_c40e2ca8efb086327b5a4cc929f0e15a = L.popup({"maxWidth": "100%"});

        
            
                var html_01f5813009dd119f37e82df3af16b24f = $(`<div id="html_01f5813009dd119f37e82df3af16b24f" style="width: 100.0%; height: 100.0%;">Station 354<br>Result: 1.0%<br></div>`)[0];
                popup_c40e2ca8efb086327b5a4cc929f0e15a.setContent(html_01f5813009dd119f37e82df3af16b24f);
            
        

        circle_marker_bd49661db94f965521172f3c2f3d81c6.bindPopup(popup_c40e2ca8efb086327b5a4cc929f0e15a)
        ;

        
    
    
            var circle_marker_9f3a2504ae3f3c337e9b30970551ffec = L.circleMarker(
                [41.4134503, 2.1631012],
                {"bubblingMouseEvents": true, "color": "#a9a9dcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a9a9dcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_22a6cd945585135cdf235a3db8679628 = L.popup({"maxWidth": "100%"});

        
            
                var html_8a12d523ae1ec3009bfd8eb67d2f06cb = $(`<div id="html_8a12d523ae1ec3009bfd8eb67d2f06cb" style="width: 100.0%; height: 100.0%;">Station 356<br>Result: 1.0%<br></div>`)[0];
                popup_22a6cd945585135cdf235a3db8679628.setContent(html_8a12d523ae1ec3009bfd8eb67d2f06cb);
            
        

        circle_marker_9f3a2504ae3f3c337e9b30970551ffec.bindPopup(popup_22a6cd945585135cdf235a3db8679628)
        ;

        
    
    
            var circle_marker_65e494f0f8759c4f851be958343e32ea = L.circleMarker(
                [41.4105956, 2.1579897],
                {"bubblingMouseEvents": true, "color": "#bfbfd7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bfbfd7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9a8de068924408be0e7b9e6247ffa428 = L.popup({"maxWidth": "100%"});

        
            
                var html_76aa027cb55e7b47ab3738119bff481f = $(`<div id="html_76aa027cb55e7b47ab3738119bff481f" style="width: 100.0%; height: 100.0%;">Station 357<br>Result: 0.5%<br></div>`)[0];
                popup_9a8de068924408be0e7b9e6247ffa428.setContent(html_76aa027cb55e7b47ab3738119bff481f);
            
        

        circle_marker_65e494f0f8759c4f851be958343e32ea.bindPopup(popup_9a8de068924408be0e7b9e6247ffa428)
        ;

        
    
    
            var circle_marker_6904ac5f2cdcbcbf2057598f4d57d6fd = L.circleMarker(
                [41.3872437, 2.1793035],
                {"bubblingMouseEvents": true, "color": "#8b8be3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8b8be3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_18d553a5c6dc392589421502cb6346bd = L.popup({"maxWidth": "100%"});

        
            
                var html_b53f68a0e5103a51269b1101d9bcc0ad = $(`<div id="html_b53f68a0e5103a51269b1101d9bcc0ad" style="width: 100.0%; height: 100.0%;">Station 358<br>Result: 1.7%<br></div>`)[0];
                popup_18d553a5c6dc392589421502cb6346bd.setContent(html_b53f68a0e5103a51269b1101d9bcc0ad);
            
        

        circle_marker_6904ac5f2cdcbcbf2057598f4d57d6fd.bindPopup(popup_18d553a5c6dc392589421502cb6346bd)
        ;

        
    
    
            var circle_marker_7e91854e0c7db6a22f43fac3bbb165a7 = L.circleMarker(
                [41.3900544, 2.1775594],
                {"bubblingMouseEvents": true, "color": "#cdcdd5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cdcdd5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6435f19b52738021ad53b55768b4b193 = L.popup({"maxWidth": "100%"});

        
            
                var html_8721118215db919996fde88d744aeb64 = $(`<div id="html_8721118215db919996fde88d744aeb64" style="width: 100.0%; height: 100.0%;">Station 359<br>Result: 0.1%<br></div>`)[0];
                popup_6435f19b52738021ad53b55768b4b193.setContent(html_8721118215db919996fde88d744aeb64);
            
        

        circle_marker_7e91854e0c7db6a22f43fac3bbb165a7.bindPopup(popup_6435f19b52738021ad53b55768b4b193)
        ;

        
    
    
            var circle_marker_caa63a1db25c894d2824376b2477cc39 = L.circleMarker(
                [41.3952527, 2.1730023],
                {"bubblingMouseEvents": true, "color": "#8383e4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8383e4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9744000e9353b3bd6b4ba355eb499ff3 = L.popup({"maxWidth": "100%"});

        
            
                var html_28a47e545a44677a2fdca7d717378b77 = $(`<div id="html_28a47e545a44677a2fdca7d717378b77" style="width: 100.0%; height: 100.0%;">Station 360<br>Result: 1.9%<br></div>`)[0];
                popup_9744000e9353b3bd6b4ba355eb499ff3.setContent(html_28a47e545a44677a2fdca7d717378b77);
            
        

        circle_marker_caa63a1db25c894d2824376b2477cc39.bindPopup(popup_9744000e9353b3bd6b4ba355eb499ff3)
        ;

        
    
    
            var circle_marker_27efb8157b2a34f6cac5033ea29f3c39 = L.circleMarker(
                [41.37652, 2.17881],
                {"bubblingMouseEvents": true, "color": "#d3d3d3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d3d3d3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_da18b91d4d5479de1456fabef51fad58 = L.popup({"maxWidth": "100%"});

        
            
                var html_93c35ae656872913b34b59768d68df94 = $(`<div id="html_93c35ae656872913b34b59768d68df94" style="width: 100.0%; height: 100.0%;">Station 361<br>Result: -0.0%<br></div>`)[0];
                popup_da18b91d4d5479de1456fabef51fad58.setContent(html_93c35ae656872913b34b59768d68df94);
            
        

        circle_marker_27efb8157b2a34f6cac5033ea29f3c39.bindPopup(popup_da18b91d4d5479de1456fabef51fad58)
        ;

        
    
    
            var circle_marker_4d38f5a925f76964625bcfd474d842af = L.circleMarker(
                [41.396994, 2.1706323],
                {"bubblingMouseEvents": true, "color": "#9d9ddfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9d9ddfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_1763022601090acc36d172eb1c6dcc78 = L.popup({"maxWidth": "100%"});

        
            
                var html_9586aa506da9554bc0936dbe331ac06a = $(`<div id="html_9586aa506da9554bc0936dbe331ac06a" style="width: 100.0%; height: 100.0%;">Station 362<br>Result: 1.3%<br></div>`)[0];
                popup_1763022601090acc36d172eb1c6dcc78.setContent(html_9586aa506da9554bc0936dbe331ac06a);
            
        

        circle_marker_4d38f5a925f76964625bcfd474d842af.bindPopup(popup_1763022601090acc36d172eb1c6dcc78)
        ;

        
    
    
            var circle_marker_d73a1d22e0772c374571900689aeb1fa = L.circleMarker(
                [41.3908381, 2.1743743],
                {"bubblingMouseEvents": true, "color": "#cdcdd5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#cdcdd5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_975d620c44b30d3a214a40677f600148 = L.popup({"maxWidth": "100%"});

        
            
                var html_dd2eb05fa731ed04b54a06785bc065e0 = $(`<div id="html_dd2eb05fa731ed04b54a06785bc065e0" style="width: 100.0%; height: 100.0%;">Station 363<br>Result: 0.1%<br></div>`)[0];
                popup_975d620c44b30d3a214a40677f600148.setContent(html_dd2eb05fa731ed04b54a06785bc065e0);
            
        

        circle_marker_d73a1d22e0772c374571900689aeb1fa.bindPopup(popup_975d620c44b30d3a214a40677f600148)
        ;

        
    
    
            var circle_marker_725c4e8fb5e78b8ca5450fbc1153fb39 = L.circleMarker(
                [41.393062, 2.1633226],
                {"bubblingMouseEvents": true, "color": "#5656eeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5656eeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_866f8ef7396a92c49fa07fc8cb844b92 = L.popup({"maxWidth": "100%"});

        
            
                var html_c24ab3017eb57df08fb30a34a40b4345 = $(`<div id="html_c24ab3017eb57df08fb30a34a40b4345" style="width: 100.0%; height: 100.0%;">Station 364<br>Result: 3.0%<br></div>`)[0];
                popup_866f8ef7396a92c49fa07fc8cb844b92.setContent(html_c24ab3017eb57df08fb30a34a40b4345);
            
        

        circle_marker_725c4e8fb5e78b8ca5450fbc1153fb39.bindPopup(popup_866f8ef7396a92c49fa07fc8cb844b92)
        ;

        
    
    
            var circle_marker_379ae41904eb5b4093b50d17f854fb47 = L.circleMarker(
                [41.3875712, 2.1469336],
                {"bubblingMouseEvents": true, "color": "#9898e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9898e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_772e0d721f3983395909ac1e148c55a7 = L.popup({"maxWidth": "100%"});

        
            
                var html_8e318e471e1f0421a3ee96ef7d6a18e4 = $(`<div id="html_8e318e471e1f0421a3ee96ef7d6a18e4" style="width: 100.0%; height: 100.0%;">Station 365<br>Result: 1.4%<br></div>`)[0];
                popup_772e0d721f3983395909ac1e148c55a7.setContent(html_8e318e471e1f0421a3ee96ef7d6a18e4);
            
        

        circle_marker_379ae41904eb5b4093b50d17f854fb47.bindPopup(popup_772e0d721f3983395909ac1e148c55a7)
        ;

        
    
    
            var circle_marker_72156dedf4f1b51aaaf8ddd4f8c50a44 = L.circleMarker(
                [41.384972, 2.1376205],
                {"bubblingMouseEvents": true, "color": "#b6b6d9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#b6b6d9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f08a266925379e9fa1ff3f07f4b88806 = L.popup({"maxWidth": "100%"});

        
            
                var html_14d495ca805701c1a073cf14770867aa = $(`<div id="html_14d495ca805701c1a073cf14770867aa" style="width: 100.0%; height: 100.0%;">Station 367<br>Result: 0.7%<br></div>`)[0];
                popup_f08a266925379e9fa1ff3f07f4b88806.setContent(html_14d495ca805701c1a073cf14770867aa);
            
        

        circle_marker_72156dedf4f1b51aaaf8ddd4f8c50a44.bindPopup(popup_f08a266925379e9fa1ff3f07f4b88806)
        ;

        
    
    
            var circle_marker_65ed5cd86036a527338906f60483353f = L.circleMarker(
                [41.3968391, 2.1756598],
                {"bubblingMouseEvents": true, "color": "#7373e7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7373e7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6202f2684b216184727704431b356bac = L.popup({"maxWidth": "100%"});

        
            
                var html_3a4aa0627da49d70eff5b997440189f2 = $(`<div id="html_3a4aa0627da49d70eff5b997440189f2" style="width: 100.0%; height: 100.0%;">Station 368<br>Result: 2.3%<br></div>`)[0];
                popup_6202f2684b216184727704431b356bac.setContent(html_3a4aa0627da49d70eff5b997440189f2);
            
        

        circle_marker_65ed5cd86036a527338906f60483353f.bindPopup(popup_6202f2684b216184727704431b356bac)
        ;

        
    
    
            var circle_marker_4b6c26b515c422c1ca0094181f99dafe = L.circleMarker(
                [41.40013, 2.1780175],
                {"bubblingMouseEvents": true, "color": "#7070e8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#7070e8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_40dc9b7f67f20e132ece4c8d034e5805 = L.popup({"maxWidth": "100%"});

        
            
                var html_3ac6326228c4be4f68d2cd6f991ffd07 = $(`<div id="html_3ac6326228c4be4f68d2cd6f991ffd07" style="width: 100.0%; height: 100.0%;">Station 369<br>Result: 2.3%<br></div>`)[0];
                popup_40dc9b7f67f20e132ece4c8d034e5805.setContent(html_3ac6326228c4be4f68d2cd6f991ffd07);
            
        

        circle_marker_4b6c26b515c422c1ca0094181f99dafe.bindPopup(popup_40dc9b7f67f20e132ece4c8d034e5805)
        ;

        
    
    
            var circle_marker_5157af0d679af03d3280e8b6e3eb7352 = L.circleMarker(
                [41.4039698, 2.1729061],
                {"bubblingMouseEvents": true, "color": "#9d9ddfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9d9ddfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_974ae87b119a67e2016e7e3de92b957d = L.popup({"maxWidth": "100%"});

        
            
                var html_4111af6b29fba636368ad23ac9ab1326 = $(`<div id="html_4111af6b29fba636368ad23ac9ab1326" style="width: 100.0%; height: 100.0%;">Station 370<br>Result: 1.3%<br></div>`)[0];
                popup_974ae87b119a67e2016e7e3de92b957d.setContent(html_4111af6b29fba636368ad23ac9ab1326);
            
        

        circle_marker_5157af0d679af03d3280e8b6e3eb7352.bindPopup(popup_974ae87b119a67e2016e7e3de92b957d)
        ;

        
    
    
            var circle_marker_b67b5adf70aa3f72f10752223206760a = L.circleMarker(
                [41.4040525, 2.181199],
                {"bubblingMouseEvents": true, "color": "#3131f5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#3131f5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_eb0cd26cc9bc6452e27ed895f28aaccd = L.popup({"maxWidth": "100%"});

        
            
                var html_f9f5724fb1201f8f35caffce982b349a = $(`<div id="html_f9f5724fb1201f8f35caffce982b349a" style="width: 100.0%; height: 100.0%;">Station 371<br>Result: 3.8%<br></div>`)[0];
                popup_eb0cd26cc9bc6452e27ed895f28aaccd.setContent(html_f9f5724fb1201f8f35caffce982b349a);
            
        

        circle_marker_b67b5adf70aa3f72f10752223206760a.bindPopup(popup_eb0cd26cc9bc6452e27ed895f28aaccd)
        ;

        
    
    
            var circle_marker_73096ef2abf9ef610348ceed66f04d02 = L.circleMarker(
                [41.4001015, 2.1841711],
                {"bubblingMouseEvents": true, "color": "#8080e5ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8080e5ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_fc544165222f6c42756c0b326e8cb792 = L.popup({"maxWidth": "100%"});

        
            
                var html_c8d0b2ba96612b5f537ac3fc971683fa = $(`<div id="html_c8d0b2ba96612b5f537ac3fc971683fa" style="width: 100.0%; height: 100.0%;">Station 372<br>Result: 2.0%<br></div>`)[0];
                popup_fc544165222f6c42756c0b326e8cb792.setContent(html_c8d0b2ba96612b5f537ac3fc971683fa);
            
        

        circle_marker_73096ef2abf9ef610348ceed66f04d02.bindPopup(popup_fc544165222f6c42756c0b326e8cb792)
        ;

        
    
    
            var circle_marker_047923bf37a0ab518345ed7cebb785ec = L.circleMarker(
                [41.3750995, 2.1613897],
                {"bubblingMouseEvents": true, "color": "#5555eeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5555eeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_751e53c69d388806253eb9d74c1e520a = L.popup({"maxWidth": "100%"});

        
            
                var html_795ad30cabcaa70bdbf68094e7d0a5f2 = $(`<div id="html_795ad30cabcaa70bdbf68094e7d0a5f2" style="width: 100.0%; height: 100.0%;">Station 373<br>Result: 3.0%<br></div>`)[0];
                popup_751e53c69d388806253eb9d74c1e520a.setContent(html_795ad30cabcaa70bdbf68094e7d0a5f2);
            
        

        circle_marker_047923bf37a0ab518345ed7cebb785ec.bindPopup(popup_751e53c69d388806253eb9d74c1e520a)
        ;

        
    
    
            var circle_marker_57b1a53991efcf1234f641a8d6645306 = L.circleMarker(
                [41.3949729, 2.1612814],
                {"bubblingMouseEvents": true, "color": "#9a9adfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9a9adfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ac823608e63ac32a89b624e44b1ccf1f = L.popup({"maxWidth": "100%"});

        
            
                var html_62e99fb11540c7d4d3ba57396f185c99 = $(`<div id="html_62e99fb11540c7d4d3ba57396f185c99" style="width: 100.0%; height: 100.0%;">Station 374<br>Result: 1.4%<br></div>`)[0];
                popup_ac823608e63ac32a89b624e44b1ccf1f.setContent(html_62e99fb11540c7d4d3ba57396f185c99);
            
        

        circle_marker_57b1a53991efcf1234f641a8d6645306.bindPopup(popup_ac823608e63ac32a89b624e44b1ccf1f)
        ;

        
    
    
            var circle_marker_cf0161ddd52f43400c08bd8509229df1 = L.circleMarker(
                [41.3720293, 2.1804468],
                {"bubblingMouseEvents": true, "color": "#d7c2c2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c2c2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_971828bb38e9173000fe04ef408bd177 = L.popup({"maxWidth": "100%"});

        
            
                var html_c84cca0947ff58fcfdfd822a3e0320ab = $(`<div id="html_c84cca0947ff58fcfdfd822a3e0320ab" style="width: 100.0%; height: 100.0%;">Station 375<br>Result: -0.4%<br></div>`)[0];
                popup_971828bb38e9173000fe04ef408bd177.setContent(html_c84cca0947ff58fcfdfd822a3e0320ab);
            
        

        circle_marker_cf0161ddd52f43400c08bd8509229df1.bindPopup(popup_971828bb38e9173000fe04ef408bd177)
        ;

        
    
    
            var circle_marker_0e687273d1259f479b5854ac926df512 = L.circleMarker(
                [41.3718728, 2.180302],
                {"bubblingMouseEvents": true, "color": "#dab3b3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dab3b3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b35f61a76c005a0dbf78feb91ea5554c = L.popup({"maxWidth": "100%"});

        
            
                var html_407ae9b11ef37d9646c51ff056372192 = $(`<div id="html_407ae9b11ef37d9646c51ff056372192" style="width: 100.0%; height: 100.0%;">Station 376<br>Result: -0.8%<br></div>`)[0];
                popup_b35f61a76c005a0dbf78feb91ea5554c.setContent(html_407ae9b11ef37d9646c51ff056372192);
            
        

        circle_marker_0e687273d1259f479b5854ac926df512.bindPopup(popup_b35f61a76c005a0dbf78feb91ea5554c)
        ;

        
    
    
            var circle_marker_32b4b504ca6520983340d7dc306d623e = L.circleMarker(
                [41.3776292, 2.1836886],
                {"bubblingMouseEvents": true, "color": "#df9b9bff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#df9b9bff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_556431e79b923fb9cfe62a540f741cf7 = L.popup({"maxWidth": "100%"});

        
            
                var html_a249066cfb031677d40fef0e57b9a6e8 = $(`<div id="html_a249066cfb031677d40fef0e57b9a6e8" style="width: 100.0%; height: 100.0%;">Station 377<br>Result: -1.3%<br></div>`)[0];
                popup_556431e79b923fb9cfe62a540f741cf7.setContent(html_a249066cfb031677d40fef0e57b9a6e8);
            
        

        circle_marker_32b4b504ca6520983340d7dc306d623e.bindPopup(popup_556431e79b923fb9cfe62a540f741cf7)
        ;

        
    
    
            var circle_marker_b92532743f38813a501830de1083ca59 = L.circleMarker(
                [41.3785379, 2.1767427],
                {"bubblingMouseEvents": true, "color": "#5656eeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#5656eeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_66b68b271fcf954205ff78fa3bc5c440 = L.popup({"maxWidth": "100%"});

        
            
                var html_8d3ac1c7e8671fe353b5a0685d1996ff = $(`<div id="html_8d3ac1c7e8671fe353b5a0685d1996ff" style="width: 100.0%; height: 100.0%;">Station 378<br>Result: 3.0%<br></div>`)[0];
                popup_66b68b271fcf954205ff78fa3bc5c440.setContent(html_8d3ac1c7e8671fe353b5a0685d1996ff);
            
        

        circle_marker_b92532743f38813a501830de1083ca59.bindPopup(popup_66b68b271fcf954205ff78fa3bc5c440)
        ;

        
    
    
            var circle_marker_f7b23e88b1d8950ca32419bf8da0365e = L.circleMarker(
                [41.3854094, 2.1740155],
                {"bubblingMouseEvents": true, "color": "#dab4b4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dab4b4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_850a1af65bcf03a3367284dd1612556d = L.popup({"maxWidth": "100%"});

        
            
                var html_4b4cf5ea800b03c2d1926d09fc48a817 = $(`<div id="html_4b4cf5ea800b03c2d1926d09fc48a817" style="width: 100.0%; height: 100.0%;">Station 380<br>Result: -0.7%<br></div>`)[0];
                popup_850a1af65bcf03a3367284dd1612556d.setContent(html_4b4cf5ea800b03c2d1926d09fc48a817);
            
        

        circle_marker_f7b23e88b1d8950ca32419bf8da0365e.bindPopup(popup_850a1af65bcf03a3367284dd1612556d)
        ;

        
    
    
            var circle_marker_36e66f935a09857a18c1d6a92fd51eac = L.circleMarker(
                [41.381635534627016, 2.1677294668647606],
                {"bubblingMouseEvents": true, "color": "#c8c8d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c8c8d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5470ca0ff78dc0a3e21b68dba88b34be = L.popup({"maxWidth": "100%"});

        
            
                var html_c39ba05bc03971030403851705f7c6ab = $(`<div id="html_c39ba05bc03971030403851705f7c6ab" style="width: 100.0%; height: 100.0%;">Station 381<br>Result: 0.3%<br></div>`)[0];
                popup_5470ca0ff78dc0a3e21b68dba88b34be.setContent(html_c39ba05bc03971030403851705f7c6ab);
            
        

        circle_marker_36e66f935a09857a18c1d6a92fd51eac.bindPopup(popup_5470ca0ff78dc0a3e21b68dba88b34be)
        ;

        
    
    
            var circle_marker_1aa1605cd81eac79ad9dc45099dab7ad = L.circleMarker(
                [41.4038902, 2.2041137],
                {"bubblingMouseEvents": true, "color": "#f23e3eff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#f23e3eff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_60814cf201f61bec05bc09e0478efc63 = L.popup({"maxWidth": "100%"});

        
            
                var html_2e20251d3e810c781bc250f7119e4765 = $(`<div id="html_2e20251d3e810c781bc250f7119e4765" style="width: 100.0%; height: 100.0%;">Station 382<br>Result: -3.5%<br></div>`)[0];
                popup_60814cf201f61bec05bc09e0478efc63.setContent(html_2e20251d3e810c781bc250f7119e4765);
            
        

        circle_marker_1aa1605cd81eac79ad9dc45099dab7ad.bindPopup(popup_60814cf201f61bec05bc09e0478efc63)
        ;

        
    
    
            var circle_marker_3e8dee8ec953e9bb76cc75f89f3dbe6a = L.circleMarker(
                [41.3807072, 2.1468381],
                {"bubblingMouseEvents": true, "color": "#9090e1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9090e1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8fe19964d412329a22326ec9a830a1e7 = L.popup({"maxWidth": "100%"});

        
            
                var html_9eb985a9a97708692e50b4aed421e0ff = $(`<div id="html_9eb985a9a97708692e50b4aed421e0ff" style="width: 100.0%; height: 100.0%;">Station 384<br>Result: 1.6%<br></div>`)[0];
                popup_8fe19964d412329a22326ec9a830a1e7.setContent(html_9eb985a9a97708692e50b4aed421e0ff);
            
        

        circle_marker_3e8dee8ec953e9bb76cc75f89f3dbe6a.bindPopup(popup_8fe19964d412329a22326ec9a830a1e7)
        ;

        
    
    
            var circle_marker_d1181fa0ee7180643fd41d9f2676c441 = L.circleMarker(
                [41.387888, 2.1552902],
                {"bubblingMouseEvents": true, "color": "#9a9adfff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9a9adfff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ef7176b125574ccefcd7a24c8c5b00b3 = L.popup({"maxWidth": "100%"});

        
            
                var html_3cfb29bc1b33dc95e834cd148169634e = $(`<div id="html_3cfb29bc1b33dc95e834cd148169634e" style="width: 100.0%; height: 100.0%;">Station 385<br>Result: 1.4%<br></div>`)[0];
                popup_ef7176b125574ccefcd7a24c8c5b00b3.setContent(html_3cfb29bc1b33dc95e834cd148169634e);
            
        

        circle_marker_d1181fa0ee7180643fd41d9f2676c441.bindPopup(popup_ef7176b125574ccefcd7a24c8c5b00b3)
        ;

        
    
    
            var circle_marker_c70645a712f07ff1666b5461d6f70ee6 = L.circleMarker(
                [41.3751866, 2.1568773],
                {"bubblingMouseEvents": true, "color": "#1919faff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#1919faff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_43811f298654310c59eafa656a1fe06b = L.popup({"maxWidth": "100%"});

        
            
                var html_fdf09fca666012c0fc7f093fef51baea = $(`<div id="html_fdf09fca666012c0fc7f093fef51baea" style="width: 100.0%; height: 100.0%;">Station 386<br>Result: 4.4%<br></div>`)[0];
                popup_43811f298654310c59eafa656a1fe06b.setContent(html_fdf09fca666012c0fc7f093fef51baea);
            
        

        circle_marker_c70645a712f07ff1666b5461d6f70ee6.bindPopup(popup_43811f298654310c59eafa656a1fe06b)
        ;

        
    
    
            var circle_marker_6ee62b45da3be006938a866908c3c62d = L.circleMarker(
                [41.3957813, 2.1787074],
                {"bubblingMouseEvents": true, "color": "#0e0efcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#0e0efcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8566669d1dca81ee9e04a9c49e2e4e8e = L.popup({"maxWidth": "100%"});

        
            
                var html_aba4270c3ceee3ba269f989e55a2b089 = $(`<div id="html_aba4270c3ceee3ba269f989e55a2b089" style="width: 100.0%; height: 100.0%;">Station 387<br>Result: 4.7%<br></div>`)[0];
                popup_8566669d1dca81ee9e04a9c49e2e4e8e.setContent(html_aba4270c3ceee3ba269f989e55a2b089);
            
        

        circle_marker_6ee62b45da3be006938a866908c3c62d.bindPopup(popup_8566669d1dca81ee9e04a9c49e2e4e8e)
        ;

        
    
    
            var circle_marker_00d77eb989dce319c1944ca98a4bdcac = L.circleMarker(
                [41.3806411, 2.1671611],
                {"bubblingMouseEvents": true, "color": "#bdbdd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bdbdd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_81c7e32f9667b9f40c23d87876025514 = L.popup({"maxWidth": "100%"});

        
            
                var html_6537a99936a8bb159d0eefb6ad8b0d2a = $(`<div id="html_6537a99936a8bb159d0eefb6ad8b0d2a" style="width: 100.0%; height: 100.0%;">Station 388<br>Result: 0.5%<br></div>`)[0];
                popup_81c7e32f9667b9f40c23d87876025514.setContent(html_6537a99936a8bb159d0eefb6ad8b0d2a);
            
        

        circle_marker_00d77eb989dce319c1944ca98a4bdcac.bindPopup(popup_81c7e32f9667b9f40c23d87876025514)
        ;

        
    
    
            var circle_marker_a74ce9c9810f8863095a6c1a7590999a = L.circleMarker(
                [41.3873901, 2.1875446],
                {"bubblingMouseEvents": true, "color": "#e09595ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e09595ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_331bdf8a5774bd477147b771a74a024e = L.popup({"maxWidth": "100%"});

        
            
                var html_47ae5a9afc6d4323ec3fec88d2f5c0be = $(`<div id="html_47ae5a9afc6d4323ec3fec88d2f5c0be" style="width: 100.0%; height: 100.0%;">Station 389<br>Result: -1.5%<br></div>`)[0];
                popup_331bdf8a5774bd477147b771a74a024e.setContent(html_47ae5a9afc6d4323ec3fec88d2f5c0be);
            
        

        circle_marker_a74ce9c9810f8863095a6c1a7590999a.bindPopup(popup_331bdf8a5774bd477147b771a74a024e)
        ;

        
    
    
            var circle_marker_6bb818741a130f26596e59557f91d88c = L.circleMarker(
                [41.3869612, 2.1820169],
                {"bubblingMouseEvents": true, "color": "#d6c7c7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c7c7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_99fd36c1f271bb3f1689a138ef9b9671 = L.popup({"maxWidth": "100%"});

        
            
                var html_b6ae2ce9ede7fe385d9123b9ffc290b9 = $(`<div id="html_b6ae2ce9ede7fe385d9123b9ffc290b9" style="width: 100.0%; height: 100.0%;">Station 390<br>Result: -0.3%<br></div>`)[0];
                popup_99fd36c1f271bb3f1689a138ef9b9671.setContent(html_b6ae2ce9ede7fe385d9123b9ffc290b9);
            
        

        circle_marker_6bb818741a130f26596e59557f91d88c.bindPopup(popup_99fd36c1f271bb3f1689a138ef9b9671)
        ;

        
    
    
            var circle_marker_797972b6aa0c8156b55aa20fa9e0bcd0 = L.circleMarker(
                [41.4230551, 2.1913753],
                {"bubblingMouseEvents": true, "color": "#bbbbd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bbbbd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_07549afed9078ae39648e681bd7a2ef9 = L.popup({"maxWidth": "100%"});

        
            
                var html_b2f9ffdeab384e8ac29053ee4194b9b9 = $(`<div id="html_b2f9ffdeab384e8ac29053ee4194b9b9" style="width: 100.0%; height: 100.0%;">Station 391<br>Result: 0.6%<br></div>`)[0];
                popup_07549afed9078ae39648e681bd7a2ef9.setContent(html_b2f9ffdeab384e8ac29053ee4194b9b9);
            
        

        circle_marker_797972b6aa0c8156b55aa20fa9e0bcd0.bindPopup(popup_07549afed9078ae39648e681bd7a2ef9)
        ;

        
    
    
            var circle_marker_fa74a225eb117ca14a7882febe37c93e = L.circleMarker(
                [41.3905303, 2.1906339],
                {"bubblingMouseEvents": true, "color": "#dea2a2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dea2a2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9369991f2a768220932922c2cd1992b7 = L.popup({"maxWidth": "100%"});

        
            
                var html_83fbcbf21a666a0dc81655f53fd86e3d = $(`<div id="html_83fbcbf21a666a0dc81655f53fd86e3d" style="width: 100.0%; height: 100.0%;">Station 392<br>Result: -1.2%<br></div>`)[0];
                popup_9369991f2a768220932922c2cd1992b7.setContent(html_83fbcbf21a666a0dc81655f53fd86e3d);
            
        

        circle_marker_fa74a225eb117ca14a7882febe37c93e.bindPopup(popup_9369991f2a768220932922c2cd1992b7)
        ;

        
    
    
            var circle_marker_4f6668ca3ff51a0e62c8e88160fd9907 = L.circleMarker(
                [41.3873057, 2.1631263],
                {"bubblingMouseEvents": true, "color": "#8585e4ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8585e4ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_30bf5739eb75abe672e82f90fa1f9c2f = L.popup({"maxWidth": "100%"});

        
            
                var html_68877afa637fd86216bbc793e7769069 = $(`<div id="html_68877afa637fd86216bbc793e7769069" style="width: 100.0%; height: 100.0%;">Station 394<br>Result: 1.8%<br></div>`)[0];
                popup_30bf5739eb75abe672e82f90fa1f9c2f.setContent(html_68877afa637fd86216bbc793e7769069);
            
        

        circle_marker_4f6668ca3ff51a0e62c8e88160fd9907.bindPopup(popup_30bf5739eb75abe672e82f90fa1f9c2f)
        ;

        
    
    
            var circle_marker_8e154f0a0b3f5cd4597dd680678ca263 = L.circleMarker(
                [41.3860607, 2.1702467],
                {"bubblingMouseEvents": true, "color": "#d6c8c8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d6c8c8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_918999ec21070efd55ffd944504e5293 = L.popup({"maxWidth": "100%"});

        
            
                var html_d036675a1d0a1c19677898338f9c484e = $(`<div id="html_d036675a1d0a1c19677898338f9c484e" style="width: 100.0%; height: 100.0%;">Station 395<br>Result: -0.3%<br></div>`)[0];
                popup_918999ec21070efd55ffd944504e5293.setContent(html_d036675a1d0a1c19677898338f9c484e);
            
        

        circle_marker_8e154f0a0b3f5cd4597dd680678ca263.bindPopup(popup_918999ec21070efd55ffd944504e5293)
        ;

        
    
    
            var circle_marker_b96cf4c0bc54d9e6f680d1446ebf9841 = L.circleMarker(
                [41.3890253, 2.1968267],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8e5068af436bfb5d2cde8aad03aac2b3 = L.popup({"maxWidth": "100%"});

        
            
                var html_7f153094e76b317ae8dfdaf06dc12df1 = $(`<div id="html_7f153094e76b317ae8dfdaf06dc12df1" style="width: 100.0%; height: 100.0%;">Station 396<br>Result: -9.0%<br></div>`)[0];
                popup_8e5068af436bfb5d2cde8aad03aac2b3.setContent(html_7f153094e76b317ae8dfdaf06dc12df1);
            
        

        circle_marker_b96cf4c0bc54d9e6f680d1446ebf9841.bindPopup(popup_8e5068af436bfb5d2cde8aad03aac2b3)
        ;

        
    
    
            var circle_marker_89fbda751728bbc97eac271dc11dd9cc = L.circleMarker(
                [41.3889129, 2.1993105],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b4bc425829bd3e79c4965330447664fa = L.popup({"maxWidth": "100%"});

        
            
                var html_1f356206d04164a15562576ffe9f1da2 = $(`<div id="html_1f356206d04164a15562576ffe9f1da2" style="width: 100.0%; height: 100.0%;">Station 397<br>Result: -5.7%<br></div>`)[0];
                popup_b4bc425829bd3e79c4965330447664fa.setContent(html_1f356206d04164a15562576ffe9f1da2);
            
        

        circle_marker_89fbda751728bbc97eac271dc11dd9cc.bindPopup(popup_b4bc425829bd3e79c4965330447664fa)
        ;

        
    
    
            var circle_marker_317ec2695620483a63d77571637cbf83 = L.circleMarker(
                [41.380955, 2.1934636],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_1a5405f3d9f76945f5f7189406a1f310 = L.popup({"maxWidth": "100%"});

        
            
                var html_55f03e4f231ebe3e7d3ec744f2543f3a = $(`<div id="html_55f03e4f231ebe3e7d3ec744f2543f3a" style="width: 100.0%; height: 100.0%;">Station 398<br>Result: -10.5%<br></div>`)[0];
                popup_1a5405f3d9f76945f5f7189406a1f310.setContent(html_55f03e4f231ebe3e7d3ec744f2543f3a);
            
        

        circle_marker_317ec2695620483a63d77571637cbf83.bindPopup(popup_1a5405f3d9f76945f5f7189406a1f310)
        ;

        
    
    
            var circle_marker_6de9d32da795cd2dbba236d99970553a = L.circleMarker(
                [41.3694508, 2.1879597],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_7ad40c65264d386e7ff0108d88d494ad = L.popup({"maxWidth": "100%"});

        
            
                var html_bd6bd9e34506a65436368df5332b5785 = $(`<div id="html_bd6bd9e34506a65436368df5332b5785" style="width: 100.0%; height: 100.0%;">Station 400<br>Result: -13.5%<br></div>`)[0];
                popup_7ad40c65264d386e7ff0108d88d494ad.setContent(html_bd6bd9e34506a65436368df5332b5785);
            
        

        circle_marker_6de9d32da795cd2dbba236d99970553a.bindPopup(popup_7ad40c65264d386e7ff0108d88d494ad)
        ;

        
    
    
            var circle_marker_3e366ca347a0e361597dd90527eb6de7 = L.circleMarker(
                [41.382418, 2.183723],
                {"bubblingMouseEvents": true, "color": "#dbaeaeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#dbaeaeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f3ef753d559a594d7db8429f68062e36 = L.popup({"maxWidth": "100%"});

        
            
                var html_afc29ffe6c3ad50ebfd284e867551b82 = $(`<div id="html_afc29ffe6c3ad50ebfd284e867551b82" style="width: 100.0%; height: 100.0%;">Station 401<br>Result: -0.9%<br></div>`)[0];
                popup_f3ef753d559a594d7db8429f68062e36.setContent(html_afc29ffe6c3ad50ebfd284e867551b82);
            
        

        circle_marker_3e366ca347a0e361597dd90527eb6de7.bindPopup(popup_f3ef753d559a594d7db8429f68062e36)
        ;

        
    
    
            var circle_marker_191d268758c9c4e1df0d7d2916a2e3a4 = L.circleMarker(
                [41.380628, 2.1821917],
                {"bubblingMouseEvents": true, "color": "#e38888ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e38888ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8a32dbec208ee69b81897a4cf872f890 = L.popup({"maxWidth": "100%"});

        
            
                var html_3cff2cc3d27a759573171b7f395cf494 = $(`<div id="html_3cff2cc3d27a759573171b7f395cf494" style="width: 100.0%; height: 100.0%;">Station 402<br>Result: -1.8%<br></div>`)[0];
                popup_8a32dbec208ee69b81897a4cf872f890.setContent(html_3cff2cc3d27a759573171b7f395cf494);
            
        

        circle_marker_191d268758c9c4e1df0d7d2916a2e3a4.bindPopup(popup_8a32dbec208ee69b81897a4cf872f890)
        ;

        
    
    
            var circle_marker_c06d6b3e27246d833ccb8998eca4bfc3 = L.circleMarker(
                [41.3653426, 2.1331357],
                {"bubblingMouseEvents": true, "color": "#c2c2d7ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c2c2d7ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2612eed57833a37d6d69a66f0e118b4f = L.popup({"maxWidth": "100%"});

        
            
                var html_aac145bc9d218ab2b33f7ea992c6bbc9 = $(`<div id="html_aac145bc9d218ab2b33f7ea992c6bbc9" style="width: 100.0%; height: 100.0%;">Station 404<br>Result: 0.4%<br></div>`)[0];
                popup_2612eed57833a37d6d69a66f0e118b4f.setContent(html_aac145bc9d218ab2b33f7ea992c6bbc9);
            
        

        circle_marker_c06d6b3e27246d833ccb8998eca4bfc3.bindPopup(popup_2612eed57833a37d6d69a66f0e118b4f)
        ;

        
    
    
            var circle_marker_4f01f8ed073b7a3256a1368a60f061d7 = L.circleMarker(
                [41.3854003, 2.1521802],
                {"bubblingMouseEvents": true, "color": "#6767eaff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6767eaff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f95126be07d275dd21c3b8d87aa9fa3a = L.popup({"maxWidth": "100%"});

        
            
                var html_722e2d5d80d47d0e912ac40346d9af24 = $(`<div id="html_722e2d5d80d47d0e912ac40346d9af24" style="width: 100.0%; height: 100.0%;">Station 405<br>Result: 2.6%<br></div>`)[0];
                popup_f95126be07d275dd21c3b8d87aa9fa3a.setContent(html_722e2d5d80d47d0e912ac40346d9af24);
            
        

        circle_marker_4f01f8ed073b7a3256a1368a60f061d7.bindPopup(popup_f95126be07d275dd21c3b8d87aa9fa3a)
        ;

        
    
    
            var circle_marker_d4523822256a9bd588cfc20b6d8b34f6 = L.circleMarker(
                [41.3863747, 2.1646697],
                {"bubblingMouseEvents": true, "color": "#9696e0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9696e0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_53db80af3d3aff7a34ae7c04b77b6b5b = L.popup({"maxWidth": "100%"});

        
            
                var html_aa366071e68128c3ea5ad9fe3d1f7ee1 = $(`<div id="html_aa366071e68128c3ea5ad9fe3d1f7ee1" style="width: 100.0%; height: 100.0%;">Station 406<br>Result: 1.5%<br></div>`)[0];
                popup_53db80af3d3aff7a34ae7c04b77b6b5b.setContent(html_aa366071e68128c3ea5ad9fe3d1f7ee1);
            
        

        circle_marker_d4523822256a9bd588cfc20b6d8b34f6.bindPopup(popup_53db80af3d3aff7a34ae7c04b77b6b5b)
        ;

        
    
    
            var circle_marker_863e039751d9061a1289f937f1673474 = L.circleMarker(
                [41.3889972, 2.1923283],
                {"bubblingMouseEvents": true, "color": "#ec5d5dff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ec5d5dff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9a9dd03da92fa7c11c576e4b67ed4f7b = L.popup({"maxWidth": "100%"});

        
            
                var html_bad1434adaa6bcd1441e7c3576f17303 = $(`<div id="html_bad1434adaa6bcd1441e7c3576f17303" style="width: 100.0%; height: 100.0%;">Station 408<br>Result: -2.8%<br></div>`)[0];
                popup_9a9dd03da92fa7c11c576e4b67ed4f7b.setContent(html_bad1434adaa6bcd1441e7c3576f17303);
            
        

        circle_marker_863e039751d9061a1289f937f1673474.bindPopup(popup_9a9dd03da92fa7c11c576e4b67ed4f7b)
        ;

        
    
    
            var circle_marker_a006b436e767c4bdf90a71fef1b20618 = L.circleMarker(
                [41.392384, 2.1925059],
                {"bubblingMouseEvents": true, "color": "#e19191ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e19191ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_4829a04205e3d1261b0936d5fb44e941 = L.popup({"maxWidth": "100%"});

        
            
                var html_c14c344ccd07bd82035628c4989ceb16 = $(`<div id="html_c14c344ccd07bd82035628c4989ceb16" style="width: 100.0%; height: 100.0%;">Station 409<br>Result: -1.6%<br></div>`)[0];
                popup_4829a04205e3d1261b0936d5fb44e941.setContent(html_c14c344ccd07bd82035628c4989ceb16);
            
        

        circle_marker_a006b436e767c4bdf90a71fef1b20618.bindPopup(popup_4829a04205e3d1261b0936d5fb44e941)
        ;

        
    
    
            var circle_marker_f63f53a2ed00c34bc71483ace602d008 = L.circleMarker(
                [41.376433, 2.17871],
                {"bubblingMouseEvents": true, "color": "#c6c6d6ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#c6c6d6ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_8925df839074c0290a444ba38758d5a3 = L.popup({"maxWidth": "100%"});

        
            
                var html_1768d9528ef152b4f8d16f82cd6c9eab = $(`<div id="html_1768d9528ef152b4f8d16f82cd6c9eab" style="width: 100.0%; height: 100.0%;">Station 410<br>Result: 0.3%<br></div>`)[0];
                popup_8925df839074c0290a444ba38758d5a3.setContent(html_1768d9528ef152b4f8d16f82cd6c9eab);
            
        

        circle_marker_f63f53a2ed00c34bc71483ace602d008.bindPopup(popup_8925df839074c0290a444ba38758d5a3)
        ;

        
    
    
            var circle_marker_1146013d7ba5b677fc93e4e03cbbca00 = L.circleMarker(
                [41.3893094, 2.1727457],
                {"bubblingMouseEvents": true, "color": "#d3d3d3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d3d3d3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_6999929e88dd2ec443886cf74472c4f1 = L.popup({"maxWidth": "100%"});

        
            
                var html_b4a7635c0f3b8b98e905f1db3d3310d7 = $(`<div id="html_b4a7635c0f3b8b98e905f1db3d3310d7" style="width: 100.0%; height: 100.0%;">Station 412<br>Result: -0.0%<br></div>`)[0];
                popup_6999929e88dd2ec443886cf74472c4f1.setContent(html_b4a7635c0f3b8b98e905f1db3d3310d7);
            
        

        circle_marker_1146013d7ba5b677fc93e4e03cbbca00.bindPopup(popup_6999929e88dd2ec443886cf74472c4f1)
        ;

        
    
    
            var circle_marker_3b844fa6b1a041377e75d403b2c392ca = L.circleMarker(
                [41.393489, 2.1707419],
                {"bubblingMouseEvents": true, "color": "#9292e1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9292e1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b3c56e898468da1135fc6d15ecb055be = L.popup({"maxWidth": "100%"});

        
            
                var html_893650f536a25f67bd6b91dcdfadef27 = $(`<div id="html_893650f536a25f67bd6b91dcdfadef27" style="width: 100.0%; height: 100.0%;">Station 413<br>Result: 1.6%<br></div>`)[0];
                popup_b3c56e898468da1135fc6d15ecb055be.setContent(html_893650f536a25f67bd6b91dcdfadef27);
            
        

        circle_marker_3b844fa6b1a041377e75d403b2c392ca.bindPopup(popup_b3c56e898468da1135fc6d15ecb055be)
        ;

        
    
    
            var circle_marker_a412fdc8066efaa10b6d9d04272558b8 = L.circleMarker(
                [41.3937234, 2.1764275],
                {"bubblingMouseEvents": true, "color": "#6a6ae9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#6a6ae9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_2e49ed68dfb7d7510b0c7911af65261d = L.popup({"maxWidth": "100%"});

        
            
                var html_d6f2e9374147624e6a98a92cc62452fd = $(`<div id="html_d6f2e9374147624e6a98a92cc62452fd" style="width: 100.0%; height: 100.0%;">Station 414<br>Result: 2.5%<br></div>`)[0];
                popup_2e49ed68dfb7d7510b0c7911af65261d.setContent(html_d6f2e9374147624e6a98a92cc62452fd);
            
        

        circle_marker_a412fdc8066efaa10b6d9d04272558b8.bindPopup(popup_2e49ed68dfb7d7510b0c7911af65261d)
        ;

        
    
    
            var circle_marker_3abcc70baad1c2aa75771dedea2fc654 = L.circleMarker(
                [41.3793558, 2.1689592],
                {"bubblingMouseEvents": true, "color": "#8d8de2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8d8de2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_787cf6f6960ff8b69efc632351f84283 = L.popup({"maxWidth": "100%"});

        
            
                var html_d7a7b32554135bc5afc08d5a5084dc78 = $(`<div id="html_d7a7b32554135bc5afc08d5a5084dc78" style="width: 100.0%; height: 100.0%;">Station 415<br>Result: 1.6%<br></div>`)[0];
                popup_787cf6f6960ff8b69efc632351f84283.setContent(html_d7a7b32554135bc5afc08d5a5084dc78);
            
        

        circle_marker_3abcc70baad1c2aa75771dedea2fc654.bindPopup(popup_787cf6f6960ff8b69efc632351f84283)
        ;

        
    
    
            var circle_marker_816ab771476c8f894d8e7e8a8934b108 = L.circleMarker(
                [41.3781065, 2.1696744],
                {"bubblingMouseEvents": true, "color": "#8a8ae3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8a8ae3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0edd1d047eeaa7d8a1cf5e5b8b76f48f = L.popup({"maxWidth": "100%"});

        
            
                var html_ef2e6522ba4653b5746f04a35c08719a = $(`<div id="html_ef2e6522ba4653b5746f04a35c08719a" style="width: 100.0%; height: 100.0%;">Station 416<br>Result: 1.7%<br></div>`)[0];
                popup_0edd1d047eeaa7d8a1cf5e5b8b76f48f.setContent(html_ef2e6522ba4653b5746f04a35c08719a);
            
        

        circle_marker_816ab771476c8f894d8e7e8a8934b108.bindPopup(popup_0edd1d047eeaa7d8a1cf5e5b8b76f48f)
        ;

        
    
    
            var circle_marker_17b88230023a1a0933d0ae56322fa0e0 = L.circleMarker(
                [41.391062, 2.1801142],
                {"bubblingMouseEvents": true, "color": "#8a8ae3ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#8a8ae3ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0c977f64e80d6173977496a615b740e8 = L.popup({"maxWidth": "100%"});

        
            
                var html_6a5319a9b6a0219a3999b67230b5b1b9 = $(`<div id="html_6a5319a9b6a0219a3999b67230b5b1b9" style="width: 100.0%; height: 100.0%;">Station 418<br>Result: 1.7%<br></div>`)[0];
                popup_0c977f64e80d6173977496a615b740e8.setContent(html_6a5319a9b6a0219a3999b67230b5b1b9);
            
        

        circle_marker_17b88230023a1a0933d0ae56322fa0e0.bindPopup(popup_0c977f64e80d6173977496a615b740e8)
        ;

        
    
    
            var circle_marker_22342ca2c41abeae7aa907f52e1217a6 = L.circleMarker(
                [41.391313, 2.1808391],
                {"bubblingMouseEvents": true, "color": "#df9c9cff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#df9c9cff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_b3601b30f24440c891eaf9001c110616 = L.popup({"maxWidth": "100%"});

        
            
                var html_ab68e123a2012a094686911d33399079 = $(`<div id="html_ab68e123a2012a094686911d33399079" style="width: 100.0%; height: 100.0%;">Station 419<br>Result: -1.3%<br></div>`)[0];
                popup_b3601b30f24440c891eaf9001c110616.setContent(html_ab68e123a2012a094686911d33399079);
            
        

        circle_marker_22342ca2c41abeae7aa907f52e1217a6.bindPopup(popup_b3601b30f24440c891eaf9001c110616)
        ;

        
    
    
            var circle_marker_fcd164bcfb7e0f078cd33bdf498aff41 = L.circleMarker(
                [41.378118, 2.1378667],
                {"bubblingMouseEvents": true, "color": "#9f9fdeff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#9f9fdeff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_9ce8bff795cc63625e9c127143dc0a5d = L.popup({"maxWidth": "100%"});

        
            
                var html_dadbbc3e49bae88d6c7335f77e793c3b = $(`<div id="html_dadbbc3e49bae88d6c7335f77e793c3b" style="width: 100.0%; height: 100.0%;">Station 421<br>Result: 1.2%<br></div>`)[0];
                popup_9ce8bff795cc63625e9c127143dc0a5d.setContent(html_dadbbc3e49bae88d6c7335f77e793c3b);
            
        

        circle_marker_fcd164bcfb7e0f078cd33bdf498aff41.bindPopup(popup_9ce8bff795cc63625e9c127143dc0a5d)
        ;

        
    
    
            var circle_marker_7b9386649532402e7f94ef330c02bf73 = L.circleMarker(
                [41.4202459, 2.1894852],
                {"bubblingMouseEvents": true, "color": "#a3a3ddff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a3a3ddff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_da7376b839669a78b14c9bf85bcaff8f = L.popup({"maxWidth": "100%"});

        
            
                var html_e733921fc0b9d4575bb5637cf78bbecc = $(`<div id="html_e733921fc0b9d4575bb5637cf78bbecc" style="width: 100.0%; height: 100.0%;">Station 423<br>Result: 1.1%<br></div>`)[0];
                popup_da7376b839669a78b14c9bf85bcaff8f.setContent(html_e733921fc0b9d4575bb5637cf78bbecc);
            
        

        circle_marker_7b9386649532402e7f94ef330c02bf73.bindPopup(popup_da7376b839669a78b14c9bf85bcaff8f)
        ;

        
    
    
            var circle_marker_e8c4559734dc5b8d372e2f715bc9da63 = L.circleMarker(
                [41.3795862, 2.1925198],
                {"bubblingMouseEvents": true, "color": "#ff0000ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ff0000ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_f81cb0a5aec3553204ca604532a67ddb = L.popup({"maxWidth": "100%"});

        
            
                var html_389d21a8f183748a143d152a82839ef2 = $(`<div id="html_389d21a8f183748a143d152a82839ef2" style="width: 100.0%; height: 100.0%;">Station 424<br>Result: -10.0%<br></div>`)[0];
                popup_f81cb0a5aec3553204ca604532a67ddb.setContent(html_389d21a8f183748a143d152a82839ef2);
            
        

        circle_marker_e8c4559734dc5b8d372e2f715bc9da63.bindPopup(popup_f81cb0a5aec3553204ca604532a67ddb)
        ;

        
    
    
            var circle_marker_9108f9bc75095bd5495566d045270275 = L.circleMarker(
                [41.3765618, 2.1748621],
                {"bubblingMouseEvents": true, "color": "#bdbdd8ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#bdbdd8ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_3fa7589030a1fa055f671906b049cf3c = L.popup({"maxWidth": "100%"});

        
            
                var html_35c413db387eb6e3ba964f0515c81bae = $(`<div id="html_35c413db387eb6e3ba964f0515c81bae" style="width: 100.0%; height: 100.0%;">Station 425<br>Result: 0.5%<br></div>`)[0];
                popup_3fa7589030a1fa055f671906b049cf3c.setContent(html_35c413db387eb6e3ba964f0515c81bae);
            
        

        circle_marker_9108f9bc75095bd5495566d045270275.bindPopup(popup_3fa7589030a1fa055f671906b049cf3c)
        ;

        
    
    
            var circle_marker_31072b1a2526ebf40321ce3169382df8 = L.circleMarker(
                [41.39828, 2.1830315],
                {"bubblingMouseEvents": true, "color": "#4040f2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#4040f2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_e5192c6d70b593f1856d33bb5d6f8652 = L.popup({"maxWidth": "100%"});

        
            
                var html_76e6568a1ddda09766e0fb756571b553 = $(`<div id="html_76e6568a1ddda09766e0fb756571b553" style="width: 100.0%; height: 100.0%;">Station 426<br>Result: 3.5%<br></div>`)[0];
                popup_e5192c6d70b593f1856d33bb5d6f8652.setContent(html_76e6568a1ddda09766e0fb756571b553);
            
        

        circle_marker_31072b1a2526ebf40321ce3169382df8.bindPopup(popup_e5192c6d70b593f1856d33bb5d6f8652)
        ;

        
    
    
            var circle_marker_fe37d84351ce7b5a8163f062722f2e03 = L.circleMarker(
                [41.3754047, 2.1680021],
                {"bubblingMouseEvents": true, "color": "#a2a2deff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a2a2deff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_50a3e1a4de3917ec7900136665d7ccf5 = L.popup({"maxWidth": "100%"});

        
            
                var html_47abbb2bdc65d08fb1bf97528a871998 = $(`<div id="html_47abbb2bdc65d08fb1bf97528a871998" style="width: 100.0%; height: 100.0%;">Station 427<br>Result: 1.2%<br></div>`)[0];
                popup_50a3e1a4de3917ec7900136665d7ccf5.setContent(html_47abbb2bdc65d08fb1bf97528a871998);
            
        

        circle_marker_fe37d84351ce7b5a8163f062722f2e03.bindPopup(popup_50a3e1a4de3917ec7900136665d7ccf5)
        ;

        
    
    
            var circle_marker_bacf66910ae2b7a4c72a25a4a58355e6 = L.circleMarker(
                [41.3983902, 2.1960799],
                {"bubblingMouseEvents": true, "color": "#e09797ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#e09797ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_75290322eaf258c364b1b23bc29bf843 = L.popup({"maxWidth": "100%"});

        
            
                var html_d5e08a4c3948e7fa9471b87622059b3d = $(`<div id="html_d5e08a4c3948e7fa9471b87622059b3d" style="width: 100.0%; height: 100.0%;">Station 428<br>Result: -1.4%<br></div>`)[0];
                popup_75290322eaf258c364b1b23bc29bf843.setContent(html_d5e08a4c3948e7fa9471b87622059b3d);
            
        

        circle_marker_bacf66910ae2b7a4c72a25a4a58355e6.bindPopup(popup_75290322eaf258c364b1b23bc29bf843)
        ;

        
    
    
            var circle_marker_5ed5ad7c17660d947650dc38587ff8c7 = L.circleMarker(
                [41.4417001, 2.1781553],
                {"bubblingMouseEvents": true, "color": "#ee5454ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#ee5454ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_ece7617541192747fae86024e1f0f18e = L.popup({"maxWidth": "100%"});

        
            
                var html_76268967c4d209de32d371b42c29bf94 = $(`<div id="html_76268967c4d209de32d371b42c29bf94" style="width: 100.0%; height: 100.0%;">Station 469<br>Result: -3.0%<br></div>`)[0];
                popup_ece7617541192747fae86024e1f0f18e.setContent(html_76268967c4d209de32d371b42c29bf94);
            
        

        circle_marker_5ed5ad7c17660d947650dc38587ff8c7.bindPopup(popup_ece7617541192747fae86024e1f0f18e)
        ;

        
    
    
            var circle_marker_5b49d2d3893b110deae2d22cb5595292 = L.circleMarker(
                [41.4389014, 2.1715576],
                {"bubblingMouseEvents": true, "color": "#d4d1d1ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d4d1d1ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_790de7798feba457df3c06707381afce = L.popup({"maxWidth": "100%"});

        
            
                var html_e19fd3b0b29b7edd247e20b582f7d5b5 = $(`<div id="html_e19fd3b0b29b7edd247e20b582f7d5b5" style="width: 100.0%; height: 100.0%;">Station 471<br>Result: -0.0%<br></div>`)[0];
                popup_790de7798feba457df3c06707381afce.setContent(html_e19fd3b0b29b7edd247e20b582f7d5b5);
            
        

        circle_marker_5b49d2d3893b110deae2d22cb5595292.bindPopup(popup_790de7798feba457df3c06707381afce)
        ;

        
    
    
            var circle_marker_41b4f52423a5a942c4d3297b4f38aa93 = L.circleMarker(
                [41.4427374, 2.170393],
                {"bubblingMouseEvents": true, "color": "#a8a8dcff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#a8a8dcff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_d497f0cfada98e455ee189bd70703b5b = L.popup({"maxWidth": "100%"});

        
            
                var html_2be45ac75b5d076334062248b9c1fe33 = $(`<div id="html_2be45ac75b5d076334062248b9c1fe33" style="width: 100.0%; height: 100.0%;">Station 472<br>Result: 1.0%<br></div>`)[0];
                popup_d497f0cfada98e455ee189bd70703b5b.setContent(html_2be45ac75b5d076334062248b9c1fe33);
            
        

        circle_marker_41b4f52423a5a942c4d3297b4f38aa93.bindPopup(popup_d497f0cfada98e455ee189bd70703b5b)
        ;

        
    
    
            var circle_marker_ae446c47f1e6334c7e89a10df67a79a3 = L.circleMarker(
                [41.4418604, 2.1664224],
                {"bubblingMouseEvents": true, "color": "#d5cdcdff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d5cdcdff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_fcacf86d34f7930c7e94ae718369625a = L.popup({"maxWidth": "100%"});

        
            
                var html_b9535920eb0e1f64c2496323000e97bb = $(`<div id="html_b9535920eb0e1f64c2496323000e97bb" style="width: 100.0%; height: 100.0%;">Station 474<br>Result: -0.1%<br></div>`)[0];
                popup_fcacf86d34f7930c7e94ae718369625a.setContent(html_b9535920eb0e1f64c2496323000e97bb);
            
        

        circle_marker_ae446c47f1e6334c7e89a10df67a79a3.bindPopup(popup_fcacf86d34f7930c7e94ae718369625a)
        ;

        
    
    
            var circle_marker_2d34664949d4255d212858346daee33e = L.circleMarker(
                [41.3943454, 2.1751709],
                {"bubblingMouseEvents": true, "color": "#3f3ff2ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#3f3ff2ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_951753bdd7a5b76ba6bd2e766cd353ae = L.popup({"maxWidth": "100%"});

        
            
                var html_22ddd86c73c07ce48372f2de47c5aa04 = $(`<div id="html_22ddd86c73c07ce48372f2de47c5aa04" style="width: 100.0%; height: 100.0%;">Station 492<br>Result: 3.5%<br></div>`)[0];
                popup_951753bdd7a5b76ba6bd2e766cd353ae.setContent(html_22ddd86c73c07ce48372f2de47c5aa04);
            
        

        circle_marker_2d34664949d4255d212858346daee33e.bindPopup(popup_951753bdd7a5b76ba6bd2e766cd353ae)
        ;

        
    
    
            var circle_marker_381f8c83feab6a524b35a80b23d7528d = L.circleMarker(
                [41.3896967, 2.1652199],
                {"bubblingMouseEvents": true, "color": "#babad9ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#babad9ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_0f54245acca8393407d1c023cefa7f5b = L.popup({"maxWidth": "100%"});

        
            
                var html_91e1dd51d3e26043353aa9592c31908c = $(`<div id="html_91e1dd51d3e26043353aa9592c31908c" style="width: 100.0%; height: 100.0%;">Station 494<br>Result: 0.6%<br></div>`)[0];
                popup_0f54245acca8393407d1c023cefa7f5b.setContent(html_91e1dd51d3e26043353aa9592c31908c);
            
        

        circle_marker_381f8c83feab6a524b35a80b23d7528d.bindPopup(popup_0f54245acca8393407d1c023cefa7f5b)
        ;

        
    
    
            var circle_marker_ddedb28dd660cb7c9a46952b5a4af1bc = L.circleMarker(
                [41.377846, 2.150523],
                {"bubblingMouseEvents": true, "color": "#d7c0c0ff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#d7c0c0ff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_3dc5b541e14163b6147e91386607e50e = L.popup({"maxWidth": "100%"});

        
            
                var html_0f2a58fadde64f47bdedc7109e06efd5 = $(`<div id="html_0f2a58fadde64f47bdedc7109e06efd5" style="width: 100.0%; height: 100.0%;">Station 495<br>Result: -0.4%<br></div>`)[0];
                popup_3dc5b541e14163b6147e91386607e50e.setContent(html_0f2a58fadde64f47bdedc7109e06efd5);
            
        

        circle_marker_ddedb28dd660cb7c9a46952b5a4af1bc.bindPopup(popup_3dc5b541e14163b6147e91386607e50e)
        ;

        
    
    
            var circle_marker_215331cca25b9619f82d03922c7aa854 = L.circleMarker(
                [41.4048623, 2.174799],
                {"bubblingMouseEvents": true, "color": "#1919faff", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "#1919faff", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8, "stroke": true, "weight": 3}
            ).addTo(map_1c26a2450131341257ad30f4f0561955);
        
    
        var popup_5ccbc6bf325974dfaedd6a0e3ceb81d1 = L.popup({"maxWidth": "100%"});

        
            
                var html_d576590be42bb09c037bf14e9712bf4f = $(`<div id="html_d576590be42bb09c037bf14e9712bf4f" style="width: 100.0%; height: 100.0%;">Station 496<br>Result: 4.4%<br></div>`)[0];
                popup_5ccbc6bf325974dfaedd6a0e3ceb81d1.setContent(html_d576590be42bb09c037bf14e9712bf4f);
            
        

        circle_marker_215331cca25b9619f82d03922c7aa854.bindPopup(popup_5ccbc6bf325974dfaedd6a0e3ceb81d1)
        ;

        
    
</script>
</html>sun_impact_2020-07-02_15_pred_diff_sun_day.html…]()



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

Finalmente hemos analizado el modelo para crear gráfico intereactivos con folium con el código model_explore.ipynb
