# API Backend Python - Modulo 11

Proyecto base en Python con Flask y estructura por carpetas.

## Estructura

- `src/controllers`: logica de negocio
- `src/routes`: definicion de rutas
- `src/config`: configuracion de entorno
- `tests`: pruebas

## Endpoint disponible

- `GET /ping` -> `{ "message": "pong" }`
- `GET /health/db` -> valida la conexion a PostgreSQL

## Ejecutar local

1. Crear entorno virtual:
   ```bash
   python -m venv .venv
   ```
2. Activar entorno:
   - Windows PowerShell:
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecutar API:
   ```bash
   python -m src.main
   ```

## Probar endpoint

```bash
curl http://localhost:5000/ping
```

## Ejecutar pruebas

```bash
pytest
```

## CI con GitHub Actions

El proyecto incluye un pipeline de integracion continua en [.github/workflows/ci.yml](.github/workflows/ci.yml).

Este workflow:

- Se ejecuta en cada `push` a `main` o `master`
- Se ejecuta en cada `pull request` hacia `main` o `master`
- Instala dependencias desde `requirements.txt`
- Ejecuta `pytest -q`

## Ejercicio practico: validacion y correccion de pipeline

Para esta practica se agrego el workflow [.github/workflows/ci-practice.yml](.github/workflows/ci-practice.yml).

Este workflow incluye:

- Fallo intencional con `exit 1` (solo en ejecucion manual)
- Paso condicional con `if: ${{ success() }}`
- Paso condicional con `if: ${{ failure() }}`
- Triggers: `push`, `pull_request`, `schedule`, `workflow_dispatch`

### Como ejecutar la practica

1. Hacer push de cambios a GitHub.
2. Ir a Actions y abrir **CI Practice - Validation and Fix**.
3. Ejecutar con **workflow_dispatch** y `simulate_failure=true`.
4. Verificar que falle en el paso **Simulate intentional failure (exercise)**.
5. Revisar el log y confirmar que el error es intencional (`exit 1`).
6. Ejecutar nuevamente con `simulate_failure=false`.
7. Verificar que el pipeline finaliza en estado exitoso.

### Evidencia sugerida para la entrega

- Captura del run fallido (con el paso de fallo intencional).
- Captura del log donde aparece `exit 1`.
- Captura del run exitoso posterior.
- Captura de los pasos condicionales de exito/fallo ejecutados.
- Captura de la configuracion de triggers del workflow.

## CD con Railway

El despliegue a Railway se realiza con [\.github/workflows/deploy.yml](.github/workflows/deploy.yml).

Este workflow:

- Se ejecuta cuando hay `push` a `main`
- Construye la app (instala dependencias y compila `src`)
- Despliega automaticamente a Railway

Para produccion, el proyecto usa `gunicorn` y el comando de arranque definido en [Procfile](Procfile):

```txt
web: gunicorn --bind 0.0.0.0:${PORT:-8000} src.main:app
```

## GitHub Secrets requeridos

Configura estos secrets en tu repositorio de GitHub antes de ejecutar el pipeline de CD:

- `RAILWAY_TOKEN`: token de acceso de Railway
- `RAILWAY_PROJECT_ID`: id del proyecto en Railway
- `RAILWAY_ENVIRONMENT_NAME`: nombre o id del entorno, por ejemplo `production`
- `RAILWAY_SERVICE_NAME`: nombre o id del servicio donde se desplegara la API

Si luego agregas variables de aplicacion, puedes guardarlas tambien como secrets de GitHub y utilizarlas en el workflow o cargarlas directamente en Railway.

## Variables de entorno

Puedes usar el archivo [.env.example](.env.example) como referencia.

- `PORT`: puerto local de la API
- `ENV`: entorno de ejecucion
- `DATABASE_URL`: cadena de conexion PostgreSQL

Estas variables se cargan automaticamente desde [.env](.env) mediante `load_dotenv()` y luego se exponen a traves de la instancia `settings` en [src/config/settings.py](src/config/settings.py).
