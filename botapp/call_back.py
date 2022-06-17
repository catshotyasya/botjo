from email import message
from botapp.app import*
from botapp import*











@dp.callback_query_handler(text='1')
async def about(message:types.Message):
  
   
   
   await bot.send_message(message.from_user.id,"В партнерстве с инвестиционной компанией  «Инвест Чэньтун» мы запустили Российско-Китайский открытый паевой инвестиционный фонд Zвезда Vиктори с первоначальным капиталом в 450 млн. рублей. Миссия фонда «Zвезда Vиктори» -содействие развитию российской экономики через укрепление взаимовыгодного российско-китайского делового сотрудничества.") 
 
                                                                                                      

   




@dp.callback_query_handler(text='2')
async def options(message:types.Message):
   

   
   await bot.send_message(message.from_user.id,'YSLOVIA')
   
   





@dp.callback_query_handler(text='3')
async def doit(message:types.Message):
   
   
   
   await bot.send_message(message.from_user.id,'Ok do it')
   
   
   
   
   
@dp.callback_query_handler(text='4')
async def doit(message:types.Message):
   
   
   
   await bot.send_message(message.from_user.id,'Куда китайские инвесторы фонда «Zвезда Vиктори» будут вкладывать в Россию и Китай в 2022?') 

   