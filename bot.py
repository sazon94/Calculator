import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from calculator import calc, correct_opening_of_brackets
from scanner import Scanner


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


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())