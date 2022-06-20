from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

faq=InlineKeyboardButton(text='О нас',callback_data='1')
credit1=InlineKeyboardButton(text='Условия кредита',callback_data='2')
credit2=InlineKeyboardButton(text='Оформить кредит',callback_data='3')
credit3=InlineKeyboardButton(text='Инвестиционные приоритеты',callback_data=4)


start_buttons=InlineKeyboardMarkup(row_width=1).add(faq,credit1,credit2,credit3)



