# 🏛️ Anexo Técnico: Sistema Desacoplado de Gestión Documental con IA

![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_LPU-F26522?style=for-the-badge&logo=groq&logoColor=white)
![Llama 3.3](https://img.shields.io/badge/Llama_3.3_8B-0467DF?style=for-the-badge&logo=meta&logoColor=white)
![Power Automate](https://img.shields.io/badge/Power_Automate-0078D4?style=for-the-badge&logo=powerautomate&logoColor=white)

> **Nota Académica e Institucional:** Este repositorio constituye el Anexo Técnico del proyecto de grado de Maestría. Por políticas de ciberseguridad, protección de datos (Ley 1581) y reserva del sumario institucional de la Secretaría de Desarrollo Económico, el código fuente presentado ha sido **sanitizado**. Las credenciales, *API Keys*, URLs de producción y datos de funcionarios han sido reemplazados por variables de entorno y datos ficticios.

---

## 1. Arquitectura del Sistema (Diagrama de Flujo)

El siguiente diagrama detalla la orquestación completa. Se destaca cómo el entorno de Microsoft 365 actúa como capa de persistencia y visualización, mientras que el procesamiento cognitivo se delega a una infraestructura externa de alto rendimiento.

```mermaid
graph TD
    subgraph "Capa de Orquestación y Persistencia (Microsoft 365)"
    A[Power Apps: Interfaz y Captura] --> B[Power Automate: Orquestador Central]
    B --> H[(SharePoint: Registro y Almacenamiento)]
    end

    B -- "1. Petición HTTP (PDF + Metadata)" --> C

    subgraph "Capa de Integración y Lógica (Middleware en Node.js)"
    C[Endpoint API REST] --> D[Knor: Validación de Esquema JSON]
    C --> E[Inyección de Prompt Sistémico]
    end

    subgraph "Capa Cognitiva de Alta Velocidad"
    D --> F[Groq API: Motor de Inferencia]
    E --> F
    F --> G[Llama 3.3 8B: Generación de Resumen y Tags]
    end

    G -- "Respuesta Estructurada" --> C
    C -- "2. HTTP Response (JSON con resultados)" --> B
    B -- "3. Actualización de Registro: Resumen y Palabras Clave" --> H

## 2. Manual de Usuario (Guía Visual de Operación)

La interfaz de usuario fue diseñada bajo el principio de **abstracción arquitectónica**. El funcionario de la Secretaría de Desarrollo Económico no interactúa con líneas de código, ni percibe el enrutamiento de datos hacia servidores externos; todo el ciclo de vida del documento ocurre dentro del entorno seguro y familiar de Power Apps y Microsoft 365.

### 2.1. Interfaz de Captura y Validación Documental
El sistema actúa como el primer anillo de seguridad. La interfaz valida en tiempo real la integridad de la carga, restringiendo la extensión de los archivos exclusivamente a formato `.pdf` y garantizando que se procese un único documento por transacción para no saturar la ventana de contexto del modelo de inteligencia artificial.

![Pantalla de Captura y Validación](docs/img/01-captura-validacion.png)

### 2.3. Visualización de Resultados en Tiempo Real
Una vez el usuario autorizado envía el acta, el sistema entra en un estado de procesamiento. En cuestión de segundos, la interfaz consulta el registro actualizado en SharePoint y renderiza en pantalla el **Resumen Ejecutivo** y las **Palabras Clave** generadas semánticamente por Llama 3.3, permitiendo al funcionario validar la extracción cognitiva inmediatamente.

![Visualización de Resultados](docs/img/02-resultados-ia.png)