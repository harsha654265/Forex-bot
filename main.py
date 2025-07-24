from forex_signals import generate_signals
from telegram_bot import send_telegram_message
from config import TELEGRAM_CHAT_ID

if __name__ == "__main__":
    signal = generate_signals()
    if signal:
        send_telegram_message(TELEGRAM_CHAT_ID, signal)