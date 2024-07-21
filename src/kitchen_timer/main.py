import os
from dotenv import load_dotenv
from aiotraq_bot import TraqHttpBot
from aiotraq_bot.models import (
    MessageCreatedPayload,
    DirectMessageCreatedPayload,
)
from aiotraq_message import TraqMessageManager

from kitchen_timer.timer import component as kt_component


load_dotenv()

BOT_ACCESS_TOKEN = os.getenv("BOT_ACCESS_TOKEN")
BOT_VERIFICATION_TOKEN = os.getenv("BOT_VERIFICATION_TOKEN")
BASE_TRAQ_URL = os.getenv("BASE_TRAQ_URL", "https://q.trap.jp/api/v3")
BASE_CLIENT_URL = os.getenv("BASE_CLIENT_URL", "https://q.trap.jp")
assert BOT_ACCESS_TOKEN is not None

# Create Bot instance
bot = TraqHttpBot(verification_token=BOT_VERIFICATION_TOKEN)
response = TraqMessageManager(bot, BOT_ACCESS_TOKEN, BASE_TRAQ_URL, BASE_CLIENT_URL)


# Register DIRECT_MESSAGE_CREATED event
@bot.event()
async def on_direct_message_created(payload: DirectMessageCreatedPayload) -> None:
    user_id = payload.message.user.id
    message = payload.message.plainText

    await response(kt_component, user_id=user_id, payload=message)


# Register MESSAGE_CREATED event
@bot.event()
async def on_message_created(payload: MessageCreatedPayload) -> None:
    channel_id = payload.message.channelId
    message = payload.message.plainText

    await response(kt_component, channnel_id=channel_id, payload=message)


# Run the bot
if __name__ == "__main__":
    bot.run(port=8080)
