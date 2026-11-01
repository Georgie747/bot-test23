```python
import asyncio, random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

BOT_TOKEN = "9254840303:AAFGVsOt-QSYGClLhCIG-PPIBPstF63jeCU"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

База заказов: user_id -> список заказов
orders_db = {}

============ КЛАВИАТУРЫ ============
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📦 Каталог", callback_data="catalog")],
        [InlineKeyboardButton(text="📋 Мои заказы", callback_data="my_orders")],
        [InlineKeyboardButton(text="💼 Хочу работать", callback_data="work")],
        [InlineKeyboardButton(text="🪟 Витрина", callback_data="showcase")],
        [