#  JC STORE - Arquitectura Orientada a Servicios (SOA)

##  Descripción del Proyecto

JC STORE es una tienda online simple desarrollada con **Python y Flask** utilizando un enfoque de **Arquitectura Orientada a Servicios (SOA)**.

El sistema simula la comunicación entre servicios independientes mediante APIs REST y respuestas en formato JSON.

La aplicación permite:

- Ver productos
- Iniciar sesión
- Crear pedidos
- Consultar pedidos

---

#  Objetivo del Proyecto

Aplicar conceptos básicos de:

- Arquitectura Orientada a Servicios (SOA)
- APIs REST
- Comunicación mediante JSON
- Separación de servicios
- Interoperabilidad entre componentes

---

#  Servicios Implementados

El sistema está dividido en servicios independientes.

---

##  1. User Service

Este servicio administra usuarios y autenticación.

### Endpoints

```http
GET /users
POST /login
```

### Funciones

- Devuelve usuarios registrados
- Valida credenciales de acceso

### Ejemplo Request

```json
{
  "username": "admin",
  "password": "1234"
}
```

### Ejemplo Response

```json
{
  "message": "Login exitoso"
}
```

---

##  2. Product Service

Este servicio proporciona información de productos.

### Endpoint

```http
GET /products
```

### Funciones

- Devuelve catálogo de productos
- Envía información en formato JSON

### Ejemplo Response

```json
{
  "products": [
    {
      "id": 1,
      "name": "Laptop Gamer ASUS",
      "price": 25000
    }
  ]
}
```

---

##  3. Order Service

Este servicio administra pedidos realizados por usuarios.

### Endpoints

```http
GET /orders
POST /orders
```

### Funciones

- Crear pedidos
- Consultar pedidos

### Ejemplo Request

```json
{
  "product": "Laptop Gamer ASUS",
  "quantity": 1
}
```

### Ejemplo Response

```json
{
  "message": "Pedido creado correctamente"
}
```

---

#  Principios SOA Aplicados

##  Loose Coupling (Bajo Acoplamiento)

Cada servicio funciona de manera independiente.

Ejemplo:

- El servicio de productos puede seguir funcionando aunque el login falle.
- Los pedidos se manejan en endpoints separados.

---

##  Abstraction (Abstracción)

Los usuarios no acceden directamente a los datos internos.

La información se expone únicamente mediante APIs REST.

Ejemplo:

```http
GET /products
```

---

##  Reusability (Reutilización)

Los servicios pueden reutilizarse en:

- Aplicaciones móviles
- Sistemas externos
- Paneles administrativos

---

##  Interoperability (Interoperabilidad)

Los servicios se comunican mediante:

- HTTP
- APIs REST
- JSON

Esto permite compatibilidad entre diferentes tecnologías.

---

#  Estándares Utilizados

| Estándar | Uso |
|---|---|
| REST | Comunicación entre servicios |
| JSON | Intercambio de datos |
| HTTP | Comunicación cliente-servidor |

---

# 🛠️ Tecnologías Utilizadas

- Python
- Flask
- HTML5
- CSS
- JavaScrip

---

#  Estructura del Proyecto

```text
project/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── products.html
│   ├── login.html
│   └── order.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
```
