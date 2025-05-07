from aiogram import types, Dispatcher

async def start_handler(message: types.Message):
    await message.answer("Привет! Пожалуйста, укажи юридическое лицо, контакт и адрес доставки, чтобы оформить заказ.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
