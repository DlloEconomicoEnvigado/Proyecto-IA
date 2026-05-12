# 🏛️ Anexo Técnico: Sistema Desacoplado de Gestión Documental con IA

![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_LPU-F26522?style=for-the-badge&logo=groq&logoColor=white)
![Llama 3.3](https://img.shields.io/badge/Llama_3.3_8B-0467DF?style=for-the-badge&logo=meta&logoColor=white)
![Power Automate](https://img.shields.io/badge/Power_Automate-0078D4?style=for-the-badge&logo=powerautomate&logoColor=white)

> **Nota Académica e Institucional:** Este repositorio constituye el Anexo Técnico del proyecto de grado de Maestría. Por políticas de ciberseguridad, protección de datos (Ley 1581) y reserva del sumario institucional de la Secretaría de Desarrollo Económico, el código fuente presentado ha sido **sanitizado**. Las credenciales, *API Keys*, URLs de producción y datos de funcionarios han sido reemplazados por variables de entorno y datos ficticios.

---

## 1. Arquitectura del Sistema (Diagrama de Flujo)

El siguiente diagrama detalla la extrapolación del flujo de datos desde el ecosistema cerrado de Microsoft 365 hacia la infraestructura de inferencia externa (Groq) utilizando este *middleware* como puente.

```mermaid
graph TD
    subgraph "Capa de Orquestación (Microsoft 365)"
    A[Power Apps: Interfaz y Captura] --> B[Power Automate: Orquestador Central]
    end

    B -- "Conector HTTP Request" --> C

    subgraph "Capa de Integración y Lógica (Middleware en Node.js)"
    C[Endpoint API REST] --> D[Knor: Validación de Esquema JSON]
    C --> E[Inyección de Prompt Sistémico]
    end

    subgraph "Capa Cognitiva de Alta Velocidad"
    D --> F[Groq API: Motor de Inferencia]
    E --> F
    F --> G[Llama 3.3 8B: NLP y Resumen]
    end

    G -- "Respuesta Estructurada" --> C
    C -- "HTTP Response (200 OK)" --> B