
from io import FileIO
from botapp.app import*
from botapp import*
from .states import*
from time import sleep
from .commands import*
from .conf import*
from .mess_handler import *
from .states import *
from aiogram.types import ContentTypes, Message
from aiogram import types
import os
from contextlib import asynccontextmanager
from typing import (
    Any,
    AsyncGenerator,
    AsyncIterator,
    BinaryIO,
    List,
    Optional,
    TypeVar,
    Union,
    cast,)
import pathlib
import io






@dp.callback_query_handler(text='1')
async def about(message:types.Message):
   await bot.send_message(message.from_user.id,"В партнерстве с инвестиционной компанией «Инвест Чэньтун» мы запустили Российско-Китайский открытый банк Zвезда Vиктори с первоначальным капиталом в 450 млн. рублей.\n Миссия фонда «Zвезда Vиктори» -содействие развитию российской экономики через укрепление взаимовыгодного российско-китайского делового сотрудничества.") 
 
                                                                                                
@dp.callback_query_handler(text='2')
async def options(message:types.Message): 
   await bot.send_message(message.from_user.id,'Условия кредитирования\n 1.Наличие банковской карточки;\n 2.Быть старше 18 лет;\n 3.Наличие паспорта;\n 4.Предоставить телефон или email.')
   
   
@dp.callback_query_handler(text='3')
async def doit(message:types.Message,state:FSMContext):
   await bot.send_message(message.from_user.id,'Оформляем кредит!\nСледуйте подсказкам.')
   sleep(1)
   await bot.send_message(message.from_user.id,'Всего 3 шага!')
   sleep(1)
   await bot.send_message(message.from_user.id,'ОТПРАВЬТЬЕ ФОТКУ ПЕРВОЙ СТРАНИЧКИ ПАСПОРТА')
   
   
   

   
   
@dp.callback_query_handler(text='4')
async def doit(message:types.Message):
   await bot.send_message(message.from_user.id,'Куда китайские инвесторы фонда «Zвезда Vиктори» будут вкладывать в Россию и Китай в 2022?\n -Сельское хозяйство;\n -IT и высокие технологии; \n -Нефтегазохимия;\n -Транспортная инфраструктура;\n -Цветные металлы.') 












# async def __download_file_binary_io(
#         cls, destination: BinaryIO, seek: bool, stream: AsyncGenerator[bytes, None]
#     ) -> BinaryIO:
#         async for chunk in stream:
#             destination.write(chunk)
#             destination.flush()
#         if seek is True:
#             destination.seek(0)
#         return destination
     
# async def __download_file(
#         cls, destination: Union[str, pathlib.Path], stream: AsyncGenerator[bytes, None]
#     ) -> None:
#         async with hbh.open(destination, "wb") as f:
#             async for chunk in stream:
#                 await f.write(chunk)






# message=Message
# file_id = message.document.file_id
# Photomage= bot.download_file(file_id)
# file_path = FileIO=r'C:\Users\user\Desktop\botjo\photos'

















# def process_photo_step(message):
#    try:
#       if message.content_type=='photo':
#          user_id= message.from_user.id
#          user= user_id
#          user.photo_id=message.photo[-1].file_id
         
#    except:
#       bot.reply_to(message,'Это не то')
      
         
# file_photo=bot.get_file(PhotoImage)
# print(file_photo) 
  
  
  
   # @dp.message_handler(content_types=['photo', 'document'])
   # async def photo_or_doc_handler(message: types.Message):
   #  file_in_io = io.BytesIO()
   #  if message.content_type == 'photo':
   #    await photo_or_doc_handler.download_file(destination_dir= r'D:\fashion')
      
   
  

   
 
   

   






#@dp.callback_query_handler(state=UploadDocuments.handle_documents_or_category)
#async def handle_documents_or_category(call, state):
   #async with state.proxy() as data:
        #documents = data["documents"]
        #user_id = call.from_user.id
       # category = call.data
        #await state.finish()
        #await save_documents(documents, user_id, category, call.message)
        
   #async def save_documents(documents, user_id, category, message):
      
      #all_files_saved = True
   #any_files_saved = False
   
   
