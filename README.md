# Refianando Codigo

### Introduccion
En este trabajo "Refinando Codigo, PP5 - Calidad y Archivos", se trabaja con la limpieza y reestructuracion el codigo utilizando los conocimientos dado en clases, pylint y pytest.

Al final, este trabajo sera presentado a traves de GitHub.

### Refactorizacion 
Dividi el codigo en tres funciones: list_costs, t_price y main.

1. list_costs: Recibe la ruta del archivo de costos como entrada y devuelve una lista con los costos en formato numerico.
2. t_price: Recibe la lista de los costos como entrada y devuelve el precio total. Decide cuales son los regalos que necesitan pagar impuestos al superar RD$1000  
3. main: Funcion principal que llama a las funciones list_gift_costs y total_price. Luego imprime el precio total de los regalos en pantalla

### Limpieza 
Para purificar el codigo utilize pylint, donde me faltaban algunos docstrings, nombre de variables que estaban mal, espacios y lienas en blanco que no iban.

### Gestion de errores

1. Control de Errores:
Entre otros errores que me salieron fueron como, error en la direccion del archivo que fue arreglado facilmemte, poniendo la direccion donde es, otro error fue por el tipo de dato que tenia el archivo "ValueError", que fue arreglado con "try and except", y por ultimo otro error tonto fue por el nombre de las funciones que fueron puestos mal, pero fue arreglado muy sencillamemte.

2. Pruebas Unitarias:
Utilice Pytest, para realizar todas las pruebas; las 3 pruebas salieron buen con un maximo de 0.04s cada una.

### Control de versiones 
Link

1. capturas: pylint

- Antes: (https://user-images.githubusercontent.com/115515648/206586377-1c842710-b4dc-4c76-9934-a3de557677ed.png)

- Despues: (https://user-images.githubusercontent.com/115515648/206586916-06f2edc3-75f8-4418-8e47-6aa58bac58da.png)

2. Capturas: commit

- Todos los commit: (https://user-images.githubusercontent.com/115515648/206585909-6186714e-9be5-4fa8-93c1-23d39da66f1b.png)

3. Enlace Permanente:

https://github.com/danelly10/Refinando-codigo/blob/e52f3f78d214532f501c6c38c9ffd31874e353d6/test.py#L1-L11
