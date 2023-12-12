from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



fighting_games_menu_button = InlineKeyboardButton('👊 Файтинги', callback_data='fighting')
strategy_games_menu_button = InlineKeyboardButton('👑 Стратегии', callback_data='strategy')
rpg_games_menu_button = InlineKeyboardButton('🧙🏼‍♂️ RPG (а также MMORPG)', callback_data='rpg')
simulations_games_menu_button = InlineKeyboardButton('🏙 Симуляторы', callback_data='simulations')
openworld_games_menu_button = InlineKeyboardButton('🏃🏻‍♂️ Игры с открытым миром', callback_data='openworld')
genre_choice_kb = InlineKeyboardMarkup().add(fighting_games_menu_button).add(
   strategy_games_menu_button).add(rpg_games_menu_button).add(
   simulations_games_menu_button).add(openworld_games_menu_button)

back_to_main_page = InlineKeyboardButton('⬅️ Вернуться на главную', callback_data='main_page')

fighting_games = [InlineKeyboardButton('👊 Mortal Combat', callback_data='mortal_combat'),
                  InlineKeyboardButton('👊 Street Fighter', callback_data='street_fighter')]
strategy_games = [InlineKeyboardButton('👑 Crusader Kings III', callback_data='crusader_kings'),
                  InlineKeyboardButton('👑 The Civilization VI', callback_data='civilization')]
rpg_games = [InlineKeyboardButton('🧙🏼‍♂️ The Elder Scrolls V: Skyrim', callback_data='skyrim'),
             InlineKeyboardButton('🧙🏼‍♂️ World of Warcraft', callback_data='warcraft')]
simulation_games = [InlineKeyboardButton('🏙 Cities Skylines', callback_data='cities_skylines'),
                    InlineKeyboardButton('⛏ Minecraft', callback_data='minecraft')]
openworld_games = [InlineKeyboardButton('🚗 Grand Theft Auto V', callback_data='gta'),
                   InlineKeyboardButton('🤠‍️ Red Dead Redemption II', callback_data='rdr')]

fighting_games_kb = InlineKeyboardMarkup().add(*fighting_games).add(back_to_main_page)
strategy_games_kb = InlineKeyboardMarkup().add(*strategy_games).add(back_to_main_page)
rpg_games_kb = InlineKeyboardMarkup().add(*rpg_games).add(back_to_main_page)
simulation_games_kb = InlineKeyboardMarkup().add(*simulation_games).add(back_to_main_page)
openworld_games_kb = InlineKeyboardMarkup().add(*openworld_games).add(back_to_main_page)


game_card_kb = InlineKeyboardMarkup().row(InlineKeyboardButton('💰 Купить', callback_data='purchase')).row(
    InlineKeyboardButton('📝 Описание', callback_data='description')).row(
    InlineKeyboardButton('⬅️ Вернуться на главную', callback_data='main_page'))