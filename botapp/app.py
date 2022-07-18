
from aiogram import Bot,Dispatcher,types
from .conf import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os



bot=Bot(token=API_TOKEN)

storage = MemoryStorage()

dp=Dispatcher(bot, storage=storage)


    
