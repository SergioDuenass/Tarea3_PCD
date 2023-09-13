import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Union, List, Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to this API"}

# --------------------------- 1 y 2 ---------------------------

# Diccionario para almacenar los usuarios
users = {}

class User(BaseModel):
    user_name: str
    user_id: int
    user_email: str
    age: Optional[int] = None
    recommendations: List[str] = []
    ZIP: Optional[str] = None


# Hacemos endpoint para crear el usuario nuevo
@app.post("/new_user/")
async def new_user(user: User):
    user_id = user.user_id
    # Verificar si el usuario ya existe
    if user_id in users:
        raise HTTPException(status_code=400, detail="ID de usuario ya existe")

    # Crear un diccionario con los datos del usuario
    user_data = {
        "user_name": user.user_name,
        "user_id": user_id,
        "user_email": user.user_email,
        "age": user.age,
        "recommendations": user.recommendations,
        "ZIP": user.ZIP
    }
    # Agregar el usuario al diccionario usando el ID como clave
    users[user_id] = user_data
    return {"user_id": user_id, "message": "Usuario creado exitosamente"}


# --------------------------- 3 ---------------------------

# Endpoint para actualizar la información de un usuario por su ID
@app.put("/update_user/{user_id}")
async def update_user(user_id: int, user: User):
    # Verificar si el usuario existe en el diccionario
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizar los datos del usuario
    updated_user_data = {
        "user_name": user.user_name,
        "user_email": user.user_email,
        "age": user.age,
        "recommendations": user.recommendations,
        "ZIP": user.ZIP
    }

    users[user_id] = updated_user_data
    return {"user_id": user_id, "message": "Usuario actualizado exitosamente"}

# --------------------------- 4 ---------------------------

# Endpoint para obtener información de un usuario por su ID
@app.get("/get_user/{user_id}")
async def get_user(user_id: int):
    # Verificar si el usuario existe en el diccionario
    user_data = users.get(user_id)
    if user_data is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user_data

# --------------------------- 5 ---------------------------

# Endpoint para eliminar la información de un usuario por su ID
@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    # Verificar si el usuario existe en el diccionario
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Eliminar el usuario
    del users[user_id]
    return {"message": "Usuario eliminado exitosamente"}




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5003, log_level="info", reload=False)

