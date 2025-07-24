import time
from telegram_bot import send_signal
from forex_signals import get_next_signal
from pairs import CURRENCY_PAIRS
from config import TELEGRAM_CHAT_ID

used_pairs = set()

def main():
    while True:
        try:
            signal = get_next_signal(CURRENCY_PAIRS, used_pairs)
            send_signal(TELEGRAM_CHAT_ID, signal)
            print(f"✅ Sent: {signal}")
            time.sleep(120)  # Wait 2 minutes (120 seconds) before next signal
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
