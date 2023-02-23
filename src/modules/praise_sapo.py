import logging
import random

import yaml
from telegram import Update
from telegram.ext import ContextTypes

from utils.project_paths import DIR_resources
from utils.actions_markups import basic_actions_markup

logger = logging.getLogger(__name__)

with open(DIR_resources / "praise_sapo/ovations.yaml", "r", encoding="utf8") as stream:
    OVATIONS = yaml.safe_load(stream)["OVATIONS"]


async def praise_sapo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Retrieve the user configurations"""
    # Get user that sent the command and log his name
    query = update.callback_query
    await query.answer()

    user = query.from_user.username
    logger.info(f"{user} is prasing the sacred Sapo...")

    message = random.choice(OVATIONS)

    await query.message.reply_text(message)  # , reply_markup=basic_actions_markup)

    # # Update the ConversationHandler state
    # return 0
