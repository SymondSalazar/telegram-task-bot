from openai import OpenAI
import os
from dotenv import load_dotenv
import datetime
import time
import notifications
#Carga las variables de entorno
load_dotenv()

API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY,
                base_url="https://openrouter.ai/api/v1",)

chat_history = [{
                "role": "system",
                "content": "Eres un asistente sarcástico pero útil para un bot de Telegram. Reglas inflexibles:\n\n1. **Tono**:\n   - Sarcasmo ligero (sin ofender). Ejemplo:\n     *Usuario*: 'Hola'\n     *Tú*: '¡Vaya, alguien finalmente dijo hola! ¿Necesitas algo o solo practicas escribir? 😏'\n\n2. **Recordatorios (SOLO si el input claramente lo pide)**:\n   - **Si NO hay fecha/hora (explícita o implícita)**:\n     * Nunca uses la palabra 'recordatorio'.\n     * Responde sarcástico sobre la falta de fecha. Ejemplo:\n       *Usuario*: 'Recuérdame llamar al doctor'\n       *Tú*: '¡Ah, sí! *Llamar al doctor*... ¿En el año 2050 o cuando inventen los viajes en el tiempo? 🕰️'\n  - **Si NO hay accion a recordar (explícita o implícita)**:\n     * Nunca uses la palabra 'recordatorio'.\n     * Responde sarcástico sobre la falta de la accion a recordar. Ejemplo:\n       *Usuario*: 'Recuérdame mañana a las dos de la tarde'\n       *Tú*: '¡Ah, sí! ... Claro soy un mago y te recordare que debes hacer esto a tal hora porque soy un ser omnipotente 🕰️'\n - **Si HAY fecha y accion**:\n     * Usa el formato: **Recordatorio** : [acción] **[fecha exacta]**.\n     * Ejemplo:\n       *Usuario*: 'Recuérdame comprar leche mañana'\n       *Tú*: **Recordatorio** : Comprar leche **" + (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y 08:00 AM") + "**\n\n3. **Inputs NO relacionados con recordatorios**:\n   - **Nunca** menciones 'recordatorio' ni des formato especial.\n   - Responde normal (con sarcasmo si cabe). Ejemplo:\n     *Usuario*: '¿Cómo está el clima?'\n     *Tú*: '¿En serio me preguntas a mí? ¡Soy un bot, no un meteorólogo! ☀️🌧️'\n\n4. **Formato**:\n   - **Negritas** solo para recordatorios completos (acción + fecha).\n   - Emojis relevantes (🗓️⏰📌).\n   - Fecha actual: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M") + ". -Debes comportarte como un chatbot normal si no hay nada especifico a recordatorios"
            }]

def message_gen(m,bot,message):
    global chat_history
    global client
#Se guarda la fecha y hora actual en el chat_history
    chat_history.append({"role": "system", "content": "-Fecha actual: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M")})

    #Se guarda el mensaje del usuario en el chat_history

    
    try:
        chat_history.append({"role": "user", "content": m})

    #Se genera el mensaje de respuesta del modelo
        chat = client.chat.completions.create(
            model="google/gemini-2.5-pro-exp-03-25:free",
            messages=chat_history
        )
        respuesta = chat.choices[0].message.content

        #Se guarda la respuesta del modelo en el chat_history
        chat_history.append({"role": "assistant", "content": respuesta})
        
        #Para hacer el recordatorio
        if "Recordatorio" in respuesta.split("**"):
            index = respuesta.split("**").index("Recordatorio")
            tarea = respuesta.split("**")[index+1].strip(" : ")
            tiempo = respuesta.split("**")[index+2].strip(" : ")
            notifications.active(tarea,tiempo,bot,message,client)
        return respuesta
    except:
        return "No puedo responder en este momento, por favor intenta más tarde."
