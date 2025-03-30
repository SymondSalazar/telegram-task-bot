# 📌 Bot de Telegram para Recordar Tareas

Este repositorio contiene el código de un bot básico de Telegram que te notificará cuando tengas que hacer tareas. Además, puedes interactuar con él mediante chat, ya que utiliza un modelo de lenguaje (LLM) en segundo plano.

## 🚀 Configuración

Sigue estos pasos para configurar y ejecutar el bot en tu entorno:

1. **Clona este repositorio**
   ```bash
   git clone https://github.com/SymondSalazar/telegram-task-bot.git
   cd telegram-task-bot
   ```

2. **Instala las dependencias necesarias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Obtén una API Key de OpenRouter**
   - Regístrate en [OpenRouter](https://openrouter.ai/) y genera una API Key.

4. **Crea un bot en Telegram**
   - Usa [BotFather](https://t.me/BotFather) en Telegram para crear un bot y obtener su token de acceso.

5. **Configura las variables de entorno**
   - Crea un archivo `.env` en la raíz del proyecto y añade:
     ```
     API_KEY=TU_API_KEY
     BOT_KEY=TU_BOT_KEY
     ```

6. **Ejecuta el bot**
   ```bash
   python bot.py
   ```

## ✨ Funcionalidades

✅ **Gestión de tareas**
- Guarda tareas pendientes y te notificará cuando sea el momento de realizarlas.

✅ **Chat interactivo**
- Puedes conversar con el bot, ya que integra un modelo de lenguaje para responder preguntas.

✅ **Recordatorios automáticos**
- Te enviará mensajes notificandote de tus tareas en Telegram según los tiempos que hayas configurado.

## 🛠️ Tecnologías utilizadas
- **Python**
- **Telegram Bot API** (`pyTelegramBotAPI`)
- **OpenRouter API** (para el modelo de lenguaje)
- **dotenv** (para la gestión de variables de entorno)

---

