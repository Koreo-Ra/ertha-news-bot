import asyncio
from aiogram import Bot, Dispatcher, types
import requests
from bs4 import BeautifulSoup
from config import token_api

url = 'https://erthium.medium.com'
bot = Bot(token=token_api)
dp = Dispatcher(bot)

active_chats = {}

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    chat_id = message.chat.id
    if chat_id not in active_chats:
        active_chats[chat_id] = None
    await message.delete()
    await some_operation(chat_id)

async def some_operation(chat_id):
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        ertha_link = soup.find(lambda tag: tag.name == 'a' and 'ertha beta' in tag.text.lower())['href']
        ertha_h2 = soup.find(lambda tag: tag.name == 'h2' and 'ertha beta' in tag.text.lower()).text
        ertha_p = soup.find(lambda tag: tag.name == 'p' and 'ertha beta' in tag.text.lower()).text

        #ertha_link = soup.find(lambda tag: tag.name == 'a')['href']
        #ertha_h2 = soup.find(lambda tag: tag.name == 'h2').text
        #ertha_p = soup.find(lambda tag: tag.name == 'p').text
        new_message = f'{ertha_h2}\n\n{ertha_p}\n\n{url}{ertha_link}'

        if new_message != active_chats[chat_id]:
            await bot.send_message(chat_id=chat_id, text=new_message)
            active_chats[chat_id] = new_message

        await asyncio.sleep(10)

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
    print("Active Chats:", active_chats)