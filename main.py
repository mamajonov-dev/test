from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import  RegisterUserState
from keyboards import *

storage = MemoryStorage()
api = '6487583369:AAELjgDAFRTQmIORQq4FXydcK61QAu5CU6g'
bot = Bot(api)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Xush kelibsiz', reply_markup=asosiymenubutton())

@dp.message_handler(text='Royxatdan otish')
async def registeruser(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Ismingizni kiriting', reply_markup=orqagabutton())
    await RegisterUserState.name.set()

@dp.message_handler(state=RegisterUserState.name)
async def getname(message: Message, state: FSMContext):
    chatid = message.chat.id
    name = message.text
    if message.text == '/start' or message.text == 'Orqaga':
        await state.finish()
        await bot.send_message(chat_id=chatid, text='Asosiy menu', reply_markup=asosiymenubutton())
    else:
        await state.update_data(
            {'name': name}
        )
        await bot.send_message(chat_id=chatid, text='Yoshingizni kiriting', reply_markup=orqagabutton())
        await RegisterUserState.yosh.set()


@dp.message_handler(state=RegisterUserState.yosh)
async def getage(message: Message, state: FSMContext):
    chatid = message.chat.id
    age = message.text
    if message.text == '/start' or message.text == 'Orqaga':
        await state.finish()
        await bot.send_message(chat_id=chatid, text='Asosiy menu', reply_markup=asosiymenubutton())
    else:
        await state.update_data(
            {'age': age}
        )
        await bot.send_message(chat_id=chatid, text='Manzil kiriting', reply_markup=orqagabutton())
        await RegisterUserState.adres.set()


@dp.message_handler(state=RegisterUserState.adres)
async def getaddress(message: Message, state: FSMContext):
    chatid = message.chat.id
    adres = message.text
    if message.text == '/start' or message.text == 'Orqaga':
        await state.finish()
        await bot.send_message(chat_id=chatid, text='Asosiy menu', reply_markup=asosiymenubutton())
    else:
        await state.update_data(
            {'addres': adres}
        )
        await bot.send_message(chat_id=chatid, text='Telefon kiriting', reply_markup=orqagabutton())
        await RegisterUserState.telefon.set()


@dp.message_handler(state=RegisterUserState.telefon)
async def gettelefon(message: Message, state: FSMContext):
    chatid = message.chat.id
    telefon = message.text
    if message.text == '/start' or message.text == 'Orqaga':
        await state.finish()
        await bot.send_message(chat_id=chatid, text='Asosiy menu', reply_markup=asosiymenubutton())
    else:
        user = await state.get_data()
        text = (f"ISmi: {user['name']}\n"
                f"Yoshi: {user['age']}\n"
                f"Manzil: {user['addres']}\n"
                f"Telfon: {telefon}\n"
                f"Username: @{message.from_user.username}\n"
                f"Chatid: {chatid}")

        await bot.send_message(chat_id=chatid, text='Royxatdan otdingiz', reply_markup=asosiymenubutton())
        await state.finish()
        await bot.send_message(chat_id=659237008, text=text)

@dp.message_handler(content_types=[types.ContentType.NEW_CHAT_MEMBERS, types.ContentType.LEFT_CHAT_MEMBER])
async def echo(message: Message):
    chatid = message.chat.id

    await bot.send_message(chat_id=chatid, text=message)
executor.start_polling(dp, skip_updates=True)