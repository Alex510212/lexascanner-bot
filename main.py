import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import user_commands

BOT_TOKEN = '8108150284:AAFgORr0fnvfoYhVhaZDCAdEN2q818s2dUA'
USER_ID = 7696356901  # The user ID to forward messages to

# Array of keywords to watch for
KEYWORDS = ["привет", "пока", "здравствуйте", "помощь", "спасибо"]

class TelegramBot:
    def __init__(self, token):
        self.bot = Bot(token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher()
        self.dp.include_routers(user_commands.router)  # Your custom command handlers (if any)
        self.dp.message.register(self.handle_keywords)

    async def handle_keywords(self, message: types.Message):
        # Check if any of the keywords are present in the message text
        text = message.text.lower()

        # If any keyword is found, forward the message to the specific user
        if any(keyword in text for keyword in KEYWORDS):
            try:
                # Forward the message to the specific user
                await self.bot.forward_message(USER_ID, message.chat.id, message.message_id)
                logging.info(f"Message forwarded to user {USER_ID}.")
            except Exception as e:
                logging.error(f"Failed to forward message: {e}")

    async def start_polling(self):
        try:
            await self.dp.start_polling(self.bot, allowed_updates=["message", "chat_member"])
        finally:
            await self.bot.close()

async def main() -> None:
    bot = TelegramBot(BOT_TOKEN)
    await bot.start_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
