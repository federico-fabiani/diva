import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    filters,
    MessageHandler,
)

from modules.praise_sapo import praise_sapo
from utils.actions_markups import basic_actions_markup

logger = logging.getLogger(__name__)

# Stages
WAITING = range(1)


async def user_check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Retrieve the user configurations"""
    # Get user that sent the command and log his name
    user_first_name = update.message.from_user.first_name
    user = update.message.from_user.username
    logger.info(f"{user} joined the conversation...")

    await update.message.reply_text(
        f"Hey! Ciao {user_first_name}. Cosa possiamo fare?", reply_markup=basic_actions_markup
    )

    # Update the ConversationHandler state
    return WAITING


async def leave(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Close the conversation"""
    query = update.callback_query
    await query.answer()
    user = update.callback_query.from_user.username
    logger.info(f'{user} is leaving the conversation...')
    await query.edit_message_text(text='Fammi sapere se ti serve altro!')
    return ConversationHandler.END


hey_diva_handler = ConversationHandler(
    entry_points=[CommandHandler("hey_diva", user_check)],
    states={
        WAITING: [
            CallbackQueryHandler(praise_sapo, pattern="^" + "Sapo" + "$"),
            CallbackQueryHandler(leave, pattern="^" + "Esci" + "$"),
        ]
    },
    fallbacks=[CommandHandler("leave", leave)],
)
