from .app import *
from aiogram import types
from .keyboard1 import*
from .keyboards import *


    

    
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    faq = types.InlineKeyboardMarkup()
    faq.add(types.InlineKeyboardButton(text="О нас", callback_data='1'))
    await message.answer('Вас приветствует китайский онлайн банк *«ZВЕЗДА VИКТОРИ*»',parse_mode="MarkdownV2",reply_markup=start_buttons)
    await message.answer_dice(emoji='🎯')
    
    
    
@dp.message_handler(commands="faq")
async def cmd_start(message: types.Message):
   credit1 = types.InlineKeyboardMarkup()
   credit1.add(types.InlineKeyboardButton(text="Условия кредитирования", callback_data='2'))
   await message.answer('Условия кредитирования',reply_markup=start_buttons)
   


# @dp.message_handler(commands="credit1")
# async def credit1(message: types.Message):
#     await message.answer("Теперь нам нужен фотография первой странички вашего паспорта:")





# @dp.message_handler(commands="help")
# async def cmd_help(message: types.Message):
#    await help.set()
#    await message.reply('Send pic')
   
   
   

