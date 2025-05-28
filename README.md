# 🏨 Prueba Técnica - Microservicios para Inmobiliaria

## 📌 Descripción

Este proyecto tiene como objetivo desarrollar dos microservicios REST en **Python puro** (sin frameworks ni ORMs) que permitan a una empresa inmobiliaria:

1. Consultar los inmuebles disponibles, vendidos y en proceso de venta.
2. Diseñar el modelo necesario para registrar "Me gusta" por parte de usuarios sobre inmuebles específicos.

---

## ⚙️ Tecnologías Utilizadas

| Tecnología                         | Descripción                                                            |
| ---------------------------------- | ---------------------------------------------------------------------- |
| Python 3.13.2                         | Lenguaje principal para el desarrollo de los microservicios.           |
| http.server / socketserver         | Para implementar un servidor HTTP básico en Python.                    |
| sqlite3 / psycopg2 (según DB real) | Para manejar la conexión y ejecución de SQL directamente desde Python. |
| unittest                           | Para implementar pruebas unitarias.                                    |
| PEP8                               | Guía de estilo usada para mantener el código limpio y consistente.     |

---

## 🧱 Estructura del Proyecto

```
real_estate_api/
│
├── api/
│   ├── server.py         # Servidor HTTP básico
│   ├── routes.py         # Ruteo manual hacia funciones/servicios
│   ├── controller.py     # Lógica de negocio
│   └── utils.py          # Funciones de utilidad (parseo, validaciones)
│
├── database/
│   ├── connection.py     # Conexión directa a base de datos
│   └── schema_extension.sql # Script SQL con modelo de "me gusta" y explicación
│
├── docs/
│   └── like_model_diagram.png # Diagrama entidad-relación del modelo extendido
│
├── test_data/
│   └── sample_filters.json   # Archivo de entrada simulado desde el front para filtros
│
├── tests/
│   └── test_server.py    # Pruebas unitarias para los endpoints
│
├── requirements.txt      # Dependencias (mínimas)
└── README.md             # Esta guía
```

---

## 🧠 Enfoque de Desarrollo

* Se diseñará el microservicio de consulta como funcional, operativo y ejecutable.
* El microservicio de "me gusta" se abordará desde un enfoque **conceptual**: se generará el diagrama E-R, el SQL necesario para su implementación futura y una explicación detallada.
* No se utilizarán frameworks web (como Flask o Django) ni ORMs (como SQLAlchemy), con el fin de demostrar dominio del lenguaje y SQL puro.
* Se respetarán principios de diseño limpio, pruebas unitarias e independencia de componentes.

---

## 📌 Microservicios

### 1. Servicio de Consulta (`GET /properties`)

Permite consultar inmuebles filtrando por:

* Estado (`pre_venta`, `en_venta`, `vendido`) ❌ No se mostrarán inmuebles con estados diferentes.
* Ciudad
* Estado (nombre del estado del inmueble)
* Año de construcción

#### Reglas:

* El estado actual de un inmueble es el **último registro** insertado en la tabla `status_history`.
* Se manejarán posibles **inconsistencias** de datos mediante validaciones y excepciones controladas.
* No se modificará ningún registro existente.

#### Entrada esperada:

Un archivo JSON de ejemplo (`test_data/sample_filters.json`) mostrará la estructura de datos que el frontend enviaría con los filtros deseados.

#### Salida esperada:

Listado de propiedades con: Dirección, Ciudad, Estado, Precio, Descripción.

### 2. Servicio de Me Gusta (**Conceptual**)

Este servicio **no se implementará** como código funcional. En su lugar, se entrega:

* Un **diagrama entidad-relación** que extiende el modelo actual para incluir la funcionalidad de "me gusta".
* Un archivo SQL (`database/schema_extension.sql`) que crea las tablas necesarias.
* Una explicación clara en este README del por qué se diseñó de esa forma.

#### Modelo Propuesto

* Tabla `user_like` con FK a `auth_user` y `property`, con campos como `created_at`.
* Se registra cada "me gusta" como una fila independiente, permitiendo generar un ranking o historial de interacciones.

---

## 🚀 Instrucciones de Ejecución

1. Clona el repositorio:

   ```bash
   git clone https://github.com/JuPaGoTru/habi-tech-test
   cd real_estate_api
   ```

2. Instala dependencias (si las hay):

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el servidor:

   ```bash
   python api/server.py
   ```

4. Ejecuta pruebas:

   ```bash
   python -m unittest discover tests/
   ```

---

## 🧪 Pruebas

Las pruebas cubrirán:

* Correcto filtrado de propiedades.
* Validación de los filtros desde archivo JSON.
* Manejo de estados en `status_history`.

---

## 🖋️ Explicación del Modelo "Me Gusta"

Para permitir que usuarios registrados marquen propiedades con "me gusta", se propone la siguiente estructura:

* Tabla `user_like`:

  * `id` (PK)
  * `user_id` (FK a `auth_user`)
  * `property_id` (FK a `property`)
  * `created_at` (timestamp)

Esta estructura:

* Permite llevar un histórico de interacciones.
* Evita modificar tablas existentes.
* Facilita consultar el ranking de inmuebles más "gustados".

Se incluye el SQL y diagrama en `database/schema_extension.sql` y `docs/like_model_diagram.png`.

---

## 🧾 Licencia

Este proyecto es parte de una prueba técnica con fines de evaluación profesional.
