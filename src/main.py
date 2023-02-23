import logging

from telegram.ext import Application
import yaml

from modules.start_conversation import hey_diva_handler
from utils.project_paths import DIR_config, DIR_resources


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    with open(DIR_config / "telegram_token.yaml", "r") as stream:
        TOKEN = yaml.safe_load(stream)["TOKEN"]

    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Add all the functions that te bot can handle
    application.add_handler(hey_diva_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
