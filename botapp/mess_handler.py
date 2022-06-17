from email.message import Message

from .app import dp
from .app import types
from .keyboard1 import *
from .app import bot 
from.keyboards import*




@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    faq = types.InlineKeyboardMarkup()
    faq.add(types.InlineKeyboardButton(text="О нас", callback_data='1'))
    await message.answer('Вас приветствует Китайский открытый паевой инвестиционный фонд «ZВЕЗДА VИКТОРИ»',reply_markup=start_buttons)
    
    
    
    
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
   credit1 = types.InlineKeyboardMarkup()
   credit1.add(types.InlineKeyboardButton(text="Условия кредитирования", callback_data='2'))
   await message.answer('Условия кредитирования',reply_markup=start_buttons)
   
   
   
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
   credit3 = types.InlineKeyboardMarkup()
   credit3.add(types.InlineKeyboardButton(text="Оформить кредит", callback_data='3'))
   await message.answer('Оформить кредит',reply_markup=start_buttons)
    
    
    
    
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
   credit2 = types.InlineKeyboardMarkup()
   credit2.add(types.InlineKeyboardButton(text="Инвестиционные приоритеты", callback_data='3'))
   await message.answer('Инвестиционные приоритеты', reply_markup=start_buttons)
    







   
   
   
   


    
