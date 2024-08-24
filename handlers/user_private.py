from aiogram.filters import CommandStart, Command
from aiogram.tupes import Message
from aiogram import F, Router
 
 
 
 
@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user. full_name} and hevea nace day")
 
 
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("I'm a simple dot that can greet you.  Just type /start to start")
 
 
 
@router.message(F.photo)
async def get_photo(message: Message):
    await message.reply('This is photo but i need some text to help you')
 
@router.message(F.text == "Hello")
async def answer_hello(message: Message):
    await message.answer("Hello! How are you?")