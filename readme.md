# 📦 Gestión de Pedidos — Proyecto Web Django

Aplicación web desarrollada con **Django 5** que permite gestionar pedidos, servicios, una tienda online con carrito de compras, un blog y autenticación de usuarios.

---

## 🚀 Funcionalidades

- **Inicio** — Página principal con presentación del negocio
- **Servicios** — Listado de servicios ofrecidos
- **Tienda** — Catálogo de productos con carrito de compras por sesión
- **Pedidos** — Gestión y seguimiento de pedidos realizados
- **Blog** — Artículos organizados por categorías
- **Contacto** — Formulario de contacto con envío de correo vía Gmail SMTP
- **Autenticación** — Registro, login y cierre de sesión de usuarios
- **Panel Admin** — Administración completa en `/admin/`

---

## 🛠️ Tecnologías usadas

| Tecnología | Versión |
|---|---|
| Python | 3.11 |
| Django | 5.2 |
| Bootstrap | 4 |
| crispy-forms + crispy-bootstrap4 | latest |
| SQLite | (base de datos por defecto) |

---

## ⚙️ Instalación y ejecución local

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/proyectoWeb.git
cd proyectoWeb
```

### 2. Crea y activa el entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install django crispy-forms crispy-bootstrap4 pillow
```

### 4. Configura las variables de entorno

Crea un archivo `.env` en la raíz o edita `settings.py` con tus datos:

```python
SECRET_KEY = 'tu-clave-secreta'
EMAIL_HOST_USER = 'tu-correo@gmail.com'
EMAIL_HOST_PASSWORD = 'tu-contraseña-de-aplicacion'
```

> ⚠️ **Nunca subas el `SECRET_KEY` ni contraseñas reales a GitHub.**

### 5. Aplica las migraciones

```bash
python manage.py migrate
```

### 6. Crea un superusuario (para el panel admin)

```bash
python manage.py createsuperuser
```

### 7. Ejecuta el servidor

```bash
python manage.py runserver
```

Abre en el navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Estructura del proyecto

```
proyectoWeb/
│
├── ProyectoWebApp/      # App principal (base, home)
├── autenticacion/       # Registro, login, logout
├── blog/                # Posts y categorías
├── carro/               # Carrito de compras (por sesión)
├── contacto/            # Formulario de contacto
├── pedidos/             # Gestión de pedidos
├── servicios/           # Listado de servicios
├── tienda/              # Catálogo de productos
├── media/               # Imágenes subidas por usuarios
├── proyectoWeb/         # Configuración principal (settings, urls)
└── manage.py
```

---

## 📬 Contacto

Desarrollado por **Andrés** ·