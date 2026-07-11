import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from calculator import calc, correct_opening_of_brackets
from scanner import Scanner
from aiohttp import web

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Приветствую, дорогой пользователь! Это калькулятор.\n"
                         "Вводи математический пример, разделяя числа и знаки пробелами.\n"
                         "Дробное число: 1/2 (слитно)\n"
                         "Отрицательное число записывай без скобок и слитно: -1/2; -2,5\n"
                         "Вид математического примера: ( ( 12 - -1/2 * -1,2 ) - 23/98 + 12")


@dp.message()
async def calculate_message(message: types.Message):
    math_example = message.text

    if not (Scanner._check_correct_math_operation(math_example)) \
            or not (Scanner._check_correct_placement_of_parentheses(math_example)):
        await message.answer('Вы ввели некорректный математический пример!')
        return

    try:
        processed_string = correct_opening_of_brackets(math_example)
        result = calc(processed_string)
        await message.answer(f'Результат: *{result}*', parse_mode='Markdown')
    except ZeroDivisionError:
        await message.answer('Ошибка: Деление на ноль в математике запрещено!')
    except Exception as e:
        await message.answer('Что-то пошло не так при вычислении...')
        print(f'Лог ошибки: {e}')


async def handle_index(request):
    return web.Response(text="Bot is running!")


async def main():
    app = web.Application()
    app.router.add_get('/', handle_index)
    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    asyncio.create_task(site.start())

    print(f"Dummy web server started on port {port}")


    print("Starting bot polling...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())