#изменения
import telebot
from openai import OpenAI

# Инициализация клиента OpenAI
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",  # <-- Не забудьте заменить на ваш реальный API ключ
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Токен Telegram-бота
TOKEN = '7168335770:AAG2Y7MCrptZShFraN25TEgAfhSQKQUrpjg'  # <-- Поместите сюда токен вашего Telegram бота
bot = telebot.TeleBot(TOKEN)

def ask_to_openai(question):
  try:
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": question}]
      )
      # Правильный способ извлечения ответа: обращение к атрибутам объекта
      # Предполагаем что текст ответа находится в текстовом формате в объекте message
      if 'message' in response['choices'][0] and 'content' in response['choices'][0]['message']:
         return response['choices'][0]['message']['content']
      else:
          # Или можно выбрать другой способ обращения к данным, если предыдущий не подходит
          return "Не удалось получить ответ"
  except Exception as e:
      return f"Произошла ошибка: {str(e)}"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Напишите что-нибудь, и я отвечу.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получение ответа от нейросети
    response = ask_to_openai(message.text)
    bot.reply_to(message, response)

if __name__ == "__main__":
    bot.polling()  # Запуск бота
