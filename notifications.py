import threading
import time
from datetime import datetime



def recordatorio(tarea,tiempo,bot,message,client):
    time.sleep(tiempo)
    chat = client.chat.completions.create(
        model="google/gemini-2.5-pro-exp-03-25:free",
        messages=[{"role": "user", "content": "¿Me puedes recordar que tengo que hacer esto de la manera mas sarcastica posible y usando emojis? {}".format(tarea)}]
        )
    bot.send_message(message.chat.id, chat.choices[0].message.content)

def active(tarea,tiempo,bot,message,client):
    tiempo = tiempo.strip("PM AM")
    fecha = datetime.strptime(tiempo, "%d/%m/%Y %H:%M")
    tiempo = (fecha - datetime.now()).total_seconds()
    hilo_recordatorio = threading.Thread(target=recordatorio, args=(tarea, tiempo,bot,message,client))
    hilo_recordatorio.start()



