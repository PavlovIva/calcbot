from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexica.lexica_en import START

router = Router()


@router.message(Command(commands='start'))
async def welcome(msg: Message):
    await msg.answer(START)

