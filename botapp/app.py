from contextvars import Token
from aiogram import Bot,Dispatcher,types
from .conf import TOKEN

bot=Bot(token=TOKEN)
dp=Dispatcher(bot)

