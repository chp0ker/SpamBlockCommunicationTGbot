from aiogram import Bot, Dispatcher, executor, types

admin_id = 890570136
token = "TOKEN_TG_BOT"


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id,
        "Приветствую!\nЭто бот для общения с NeverLucky (@Chp0ker1337), если у вас спамблок\n"
        "Вводите сообщение")


@dp.message_handler(commands="msg")
async def start(message: types.Message):
    msg = ""
    text = message.text.split(" ")
    user_id = text[1]
    for i in range(2, len(text)):
        msg += f"{text[i]} "
        
    await bot.send_message(user_id, msg)
    
    await bot.send_message(admin_id,
        f"Пользователю {user_id} вы отправили сообщение:\n"
        f"{msg}")


@dp.message_handler(content_types=['text'])
async def messages(message: types.Message):
    user_id = message.from_user.id
    user_username = message.from_user.username
    
    await bot.send_message(admin_id,
        f"Пользователь @{user_username} ({user_id}) отправил сообщение:\n"
        f"{message.text}")
    
    await bot.send_message(user_id,
        f"Вы отправили сообщение:\n"
        f"{message.text}")



if __name__ == "__main__":
    executor.start_polling(dp)
