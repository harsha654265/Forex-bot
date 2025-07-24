import random
import time

# List of possible signal types
SIGNAL_TYPES = ['BUY', 'SELL']

# Simulated high-accuracy logic (dummy placeholder)
def generate_signal(pair):
    # Simulate 90% accuracy using random choice
    direction = random.choice(SIGNAL_TYPES)
    return f"{direction} Signal for {pair}"

def get_next_signal(pairs, used_pairs):
    # Choose a random unused pair to avoid repeats until list is exhausted
    remaining_pairs = [pair for pair in pairs if pair not in used_pairs]
    if not remaining_pairs:
        used_pairs.clear()  # Reset if all pairs are used
        remaining_pairs = pairs
    selected = random.choice(remaining_pairs)
    used_pairs.add(selected)
    return generate_signal(selected)
