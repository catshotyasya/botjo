from collections import _OrderedDictKeysView
import logging

from xml.dom import UserDataHandler
import aiogram.utils.markdown as md
from aiogram import Bot,Dispatcher,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import os
from .states import*




storage=MemoryStorage()


class Form(StatesGroup):
        Photomage=State()
        
        
class Phad(StatesGroup):
        Photodd=State()
        
    
    
    


        
        
           
