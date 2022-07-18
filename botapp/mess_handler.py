
from cgitb import text
from botapp.commands import*
from .app import dp
from .app import types
from .keyboard1 import *
from .app import bot 
from.keyboards import*
from .states import*
from .app import*
import io
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentTypes, Message
from time import sleep




    



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
   


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def photo_handler(message: Message,state:Form.Photomage):
  photo = message.photo.pop()
  
  await photo.download(destination_dir=r'C:\Users\user\Desktop\botjo\photos')
  await state.update_data(photo)
  await message.answer('Спасибо, а теперь пожалуйста сфоткайте свое лицо с паспортом\n, чтоб мы знали, что это вы!')
  await Form.Photomage.set()
  
  
# @dp.message_handler(content_types=ContentTypes.PHOTO)
# async def photo_jungle(message:Message,state:Phad.Photodd):
#   photo=message.photo.pop()
#   await photo.download(destination_dir=r'C:\Users\user\Desktop\botjo\photos')
#   await state.update_data()
#   await message.answer('Спасибо, а теперь пожалуйста сфоткайте свое лицо с паспортом\n, чтоб мы знали, что это вы!')
#   await Form.Photodd.set()
  
  
  

  
  
  
  
  
  
# @dp.message_handler(content_types=ContentTypes.PHOTO)
# async def photo_handler(message: Message,state:Form.Photomage):
#  photo1=message.photo1.pop()
#  await photo1.download(destination_dir=r'C:\Users\user\Desktop\botjo\photos')
#  await state.update_data(photo1)
#  await photo1.reply('Спасибо, ваш запрос в обработке')
#  await Form.Photodd.set()
#  await photo1.download(destination_dir=r'C:\Users\user\Desktop\botjo\photos')
#  await state.update_data(photo1)
#  await message.reply('Спасибо, ваш запрос в обработке')
#  await Form.Photodd.set()
 
 
 
# @dp.message_handler(content_types=ContentTypes.PHOTO)
# async def photo_handler(message:types.Message,state:Form.Photodd):
#    photo1=message.photo1.pop()
#    await photo1.download(destination_dir=r'C:\Users\user\Desktop\botjo\photos')
#    await state.update_data(photo1)
#    await message.reply('Спасибо, ваш запрос в обработке')
#    await Form.Photodd.set()
 
    
        
        








    
    
    
    
    
    
    
    
    
    
    
    
    # async def photo_or_doc_handler(message: types.Message):
    #     file_in_io = io.BytesIO()
    # if message.content_type == 'photo':
    #     await message.photo[-1].download(destination_file=PhotoImage)
    #     await bot.answer( 'Ok')











   
   
   
   


    
