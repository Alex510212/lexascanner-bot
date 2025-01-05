from aiogram import Router, types, Bot
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else "пользователь"
    
    # Приветствие пользователя
    await message.answer(f"Привет, {username}! Я бот. Чем могу помочь?")
