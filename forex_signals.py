import requests
from config import TD_API_KEY
from pairs import FOREX_PAIRS

def generate_signals():
    signal_text = ""
    for pair in FOREX_PAIRS:
        symbol = pair.replace("/", "")
        url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey={TD_API_KEY}"
        try:
            response = requests.get(url).json()
            values = response.get("values")
            if not values or len(values) < 3:
                continue

            close_prices = [float(candle['close']) for candle in values[:3]]
            if close_prices[0] > close_prices[1] > close_prices[2]:
                signal_text += f"🔴 PUT Signal: {pair}\n"
            elif close_prices[0] < close_prices[1] < close_prices[2]:
                signal_text += f"🟢 CALL Signal: {pair}\n"
        except Exception as e:
            print(f"Error fetching data for {pair}: {e}")
    return signal_text if signal_text else "No strong signals found right now."