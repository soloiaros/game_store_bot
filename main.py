import logging
from aiogram.types import BotCommandScopeDefault, BotCommand
from aiogram import Bot, Dispatcher, executor
from config import *
from keyboards import *
from shipping import *
from dictionaries import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# Хэндлеры для инлайн-кнопок с выбором жанра
@dp.message_handler(commands=['start'])
async def greeting_page(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://www.dorkaholics.com/wp-content/uploads/2022/07/pexels-evg-kowalievska-1174746.jpeg',
                         caption='Добро пожаловать в наш магазин игр! Чтобы выбрать себе игру, для начала выберите один из жанров ниже:', reply_markup=genre_choice_kb)


@dp.callback_query_handler(text='fighting')
async def fighting_genre(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.message.chat.id, photo='https://images.unsplash.com/photo-1511512578047-dfb367046420?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=871&q=80',
                         caption='Отлично! Теперь выберите интересующую вас игру в жанре файтинги:', reply_markup=fighting_games_kb)


@dp.callback_query_handler(text='strategy')
async def strategy_genre(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.message.chat.id, photo='https://images.unsplash.com/photo-1625805866449-3589fe3f71a3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
                         caption='Отлично! Теперь выберите интересующую вас игру в жанре стратегии:', reply_markup=strategy_games_kb)


@dp.callback_query_handler(text='rpg')
async def strategy_genre(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.message.chat.id, photo='https://images.unsplash.com/photo-1507457379470-08b800bebc67?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1509&q=80',
                         caption='Отлично! Теперь выберите интересующую вас игру в жанре RPG:', reply_markup=rpg_games_kb)


@dp.callback_query_handler(text='simulations')
async def strategy_genre(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.message.chat.id, photo='https://images.unsplash.com/photo-1593277992013-05e17a5f417d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80',
                         caption='Отлично! Теперь выберите интересующую вас игру в жанре симуляторы:', reply_markup=simulation_games_kb)


@dp.callback_query_handler(text='openworld')
async def strategy_genre(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.message.chat.id, photo='https://images.unsplash.com/photo-1539716947714-3295e1074d33?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80',
                         caption='Отлично! Теперь выберите интересующую вас игру в жанре игр с открытым миром:', reply_markup=openworld_games_kb)


# попробуем по другому
@dp.callback_query_handler(text=game_titles)
async def show_invoices_mortal_combat(callback_query: types.CallbackQuery):
    global current_game
    current_game = str(callback_query.data).replace('asdf', '')
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.message.chat.id,
                         photo=photo_urls[current_game],
                         caption=f'Вы выбрали игру {game_titles[current_game]}! Вы можете прочесть '
                                 f'информацию о ней, нажав на "Описание".',
                         reply_markup=game_card_kb)


@dp.callback_query_handler(text='purchase')
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id, **invoices_dict[current_game].generate_invoices(),
                           payload='whatever')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Чтобы купить игру, нажмите на кнопку выше👆\n'
                                'Если вы передумали, можете вернуться на главную страницу и присмотреть что-то ещё 👇:',
                           reply_markup=InlineKeyboardMarkup().add(back_to_main_page))


@dp.callback_query_handler(text='description')
async def show_description(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f'📝 {game_descriptions[current_game]}',
                           reply_markup=InlineKeyboardMarkup().add(back_to_main_page))


@dp.callback_query_handler(text='main_page')
async def greeting_page(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.message.chat.id, photo='https://www.dorkaholics.com/wp-content/uploads/2022/07/pexels-evg-kowalievska-1174746.jpeg',
                         caption='Добро пожаловать в наш магазин игр! Чтобы выбрать себе игру, для начала выберите один из жанров ниже:', reply_markup=genre_choice_kb)


"""обработчик запроса доставки"""
@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code == 'RU':
        await bot.answer_shipping_query(shipping_query_id=query.id, shipping_options=[
            POST_REGULAR_SHIPPING,
            POST_FAST_SHIPPING,
            PICKUP_SHIPPING
        ],ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id, ok=False, error_message='Доставка недоступна')


"""обработчик запроса предварительной проверки"""
@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(query: types.PreCheckoutQuery):
   await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
   await bot.send_message(chat_id=query.from_user.id, text="Спасибо за покупку! Вы можете вернуться на главную страницу"
                                                           " и присмотреть себе что-нибудь ещё",
                          reply_markup=InlineKeyboardMarkup().add(back_to_main_page))


async def set_default_commands(bot: Bot):
   return await bot.set_my_commands(
       commands=[
           BotCommand('start', 'Запустить бота')
       ],
       scope=BotCommandScopeDefault(),
   )


if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)