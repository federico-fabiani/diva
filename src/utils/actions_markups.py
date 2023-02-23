from telegram import InlineKeyboardButton, InlineKeyboardMarkup

basic_actions = [
    [
        InlineKeyboardButton("🪙 Entrata", callback_data="Compra"),
        InlineKeyboardButton("🏦 PAC", callback_data="Verifica"),
    ],
    [
        InlineKeyboardButton("👧🏼 Sapo!?", callback_data="Sapo"),
        InlineKeyboardButton("⚙️ Settings", callback_data="Settings"),
        InlineKeyboardButton("⬅️ Esci", callback_data="Esci")
    ],
]
basic_actions_markup = InlineKeyboardMarkup(basic_actions)