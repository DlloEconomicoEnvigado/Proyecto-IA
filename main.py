import os
import json
import base64
import fitz  
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

# 1. Configuración inicial
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

app = FastAPI(title="Servidor de Resúmenes de PDFs para SharePoint")
@app.get("/")
def health_check():
    return {"status": "¡El servidor de Envigado está despierto y listo! ☀️"}
client = Groq(api_key=api_key)

class SolicitudDocumento(BaseModel):
    id_registro: str
    nombre_archivo: str
    archivo_base64: str

@app.post("/procesar-resumen")
async def resumir_documento(data: SolicitudDocumento):
    try:
        print(f"Recibiendo el archivo: {data.nombre_archivo}...")

        # PASO A: Decodificar el PDF desde Base64
        base64_limpio = data.archivo_base64.replace('\n', '').replace('\r', '')
        pdf_bytes = base64.b64decode(base64_limpio)
        
        # PASO B: Leer el PDF en la memoria RAM y extraer el texto
        texto_extraido = ""
        with fitz.open("pdf", pdf_bytes) as doc:
            for numero_pagina, pagina in enumerate(doc):
                texto_extraido += pagina.get_text()
                
        print(f"Texto extraído con éxito. Longitud: {len(texto_extraido)} caracteres.")

        texto_procesar = texto_extraido[:25000] 

        # PASO C: Enviar el texto a la IA (Groq)
        print("Enviando a Llama 3.3 en Groq...")
        respuesta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un analista de datos experto. "
                        "Responde ÚNICAMENTE en formato JSON válido. "
                        "El JSON debe contener exactamente dos claves: "
                        "1. 'resumen': Un resumen en prosa del texto, muy analítico y estructurado, de máximo 500 palabras. "
                        "2. 'palabras_clave': Una cadena de texto con 5 a 7 palabras clave separadas por comas."
                    )
                },
                {
                    "role": "user",
                    "content": f"Documento: {data.nombre_archivo}\n\nTexto extraído: {texto_procesar}"
                }
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        # PASO D: Procesar la respuesta y enviarla de vuelta a Power Automate
        contenido_ia = json.loads(respuesta.choices[0].message.content)
        print("¡Resumen generado con éxito!")
        
        return {
            "status": "success",
            "id": data.id_registro,
            "resumen": contenido_ia.get("resumen", "No se pudo generar el resumen."),
            "palabras_clave": contenido_ia.get("palabras_clave", "Sin palabras clave.")
        }

    except Exception as e:
        print(f"--- ERROR DETECTADO ---")
        print(str(e)) 
        print(f"------------------------")
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")