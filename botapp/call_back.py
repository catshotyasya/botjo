from email import message
from botapp.app import*
from botapp import*











@dp.callback_query_handler(text='1')
async def about(message:types.Message):
  
   
   
   await bot.send_message(message.from_user.id,"В партнерстве с инвестиционной компанией «Инвест Чэньтун» мы запустили Российско-Китайский открытый банк Zвезда Vиктори с первоначальным капиталом в 450 млн. рублей.\n Миссия фонда «Zвезда Vиктори» -содействие развитию российской экономики через укрепление взаимовыгодного российско-китайского делового сотрудничества.") 
 
                                                                                                      

   




@dp.callback_query_handler(text='2')
async def options(message:types.Message):
   

   
   await bot.send_message(message.from_user.id,'Условия кредитирования\n 1.Наличие банковской карточки;\n 2.Быть старше 18 лет;\n 3.Наличие паспорта;\n 4.Предоставить телефон или email.')
   
   





@dp.callback_query_handler(text='3')
async def doit(message:types.Message):
   
   
   
   await bot.send_message(message.from_user.id,'Оформляем кредит!\nСледуйте подсказкам.')
   
   
   
   
   
@dp.callback_query_handler(text='4')
async def doit(message:types.Message):
   
   
   
   await bot.send_message(message.from_user.id,'Куда китайские инвесторы фонда «Zвезда Vиктори» будут вкладывать в Россию и Китай в 2022?\n -Сельское хозяйство;\n -IT и высокие технологии; \n -Нефтегазохимия;\n -Транспортная инфраструктура;\n -Цветные металлы.') 

   