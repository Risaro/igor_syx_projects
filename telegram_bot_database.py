import logging
from aiogram import Bot, Dispatcher, executor, types
import pymysql

bot = Bot(token="5973283722:AAEdw61X_VhNefFmm8gjI4Zp0PiubrmYVzM")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["test1"])
async def cmd_test1(message: types.Message):
    await message.answer("Test 1")
@dp.message_handler(commands=["getPos"])
async def cmd_getPos(message: types.Message):
    await message.answer('я не знаю такое, я не ячмень')
    await message.answer('я твой первый кот')

@dp.message_handler(commands=['create'])
async def cmd_create_user(message: types.Message):
    con = pymysql.connect(host="185.231.153.103", user="study", password="study123", database="egor")
    with con:
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        await bot.send_message(message.from_user.id, str(version[0]))
@dp.message_handler(commands=['show_user'])
async  def cmd_show_user(message: types.message):
    con = pymysql.connect(host="185.231.153.103", user="study", password="study123", database="egor")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            await  bot.send_message(message.from_user.id, f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
users = {1,1}
@dp.message_handler(commands=["insert"])
async  def cmd_insert(message: types.Message):
    users.add(message.from_user.id)
    await bot.send_message(message.from_user.id, "\n".join(f"* {user_id}" for user_id in users))
if __name__ == "__main__":
    executor.start_polling(dp)