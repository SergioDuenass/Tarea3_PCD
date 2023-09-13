# Tarea3_PCD
En este repositorio se encuentra el main.py de una api creada para almacenar usuarios.

Fue creado como parte de la tarea 3 del curso de Proyecto de Ciencia de Datos. Los requerimientos fueron:

Crear una nueva API, la cuál contenga cuatro endpoints con las siguientes consideraciones:

    Un endpoint para crear un diccionario en donde las llaves de dicho diccionario sea un id de tipo entero como identificador único para una lista de usuarios. El valor de dicha llave será otro diccionario con la siguiente estructura:

    {"user_name": "name",
    "user_id": id,
    "user_email": "email",
    "age" (optiona): age,
    "recommendations": list[str],
    "ZIP" (optional): ZIP
    }

    Cada vez que se haga un request a este endpoint, se debe actualizar el diccionario. Hint: Definir un diccionario vacío fuera del endpoint. La respuesta de este endpoint debe enviar el id del usuario creado y una descripción de usuario creado exitosamente.

    Si se envía datos con un id ya repetido, se debe regresar un mensaje de error que mencione este hecho.

    Un endpoint para actualizar la información de un usuario específico buscándolo por id. Si el id no existe, debe regresar un mensaje de error que mencione este hecho.

    Un endpoint para obtener la información de un usuario específico buscándolo por id. Si el id no existe, debe regresar un mensaje de error que mencione este hecho.

    Un endpoint para eliminar la información de un usuario específico buscándolo por id. Si el id no existe, debe regresar un mensaje de error que mencione este hecho.

