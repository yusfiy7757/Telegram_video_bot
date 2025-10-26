from aiogram import Bot, Dispatcher, types, executor

# Bot token va admin ID
TOKEN = "8297807416:AAEDT419nOZfgWAATrfE-ufGFPizLxXPfi0"
ADMIN_ID = 1025705317

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Salom! Promt yozing, biz sizga video yaratamiz 🎥")

@dp.message_handler()
async def handle_prompt(message: types.Message):
    prompt = message.text
    await message.reply(f"Promt qabul qilindi: \"{prompt}\". Video tayyorlanmoqda...")

    # Bu yerda video generator API chaqiriladi (hozircha test link)
    video_url = "https://example.com/generated_video.mp4"
    await message.reply_video(video=video_url)

    # Adminga xabar yuborish
    await bot.send_message(ADMIN_ID, f"Foydalanuvchi {message.from_user.full_name} promt yubordi:\n{prompt}")

executor.start_polling(dp)
