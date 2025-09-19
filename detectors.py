def is_spam(message):
    spam_keywords = ['win', 'free', 'offer', 'winner', 'click', 'buy now']
    message = message.lower()

    for keyword in spam_keywords:
        if keyword in message:
            return True
    return False

# Test cases
messages = [
    "You have won a free iPhone!",
    "Let's catch up for coffee tomorrow.",
    "Exclusive offer: Buy now and save 50%!"
]

for msg in messages:
    print(f"Message: '{msg}'")
    print("Spam Detected!" if is_spam(msg) else "Not Spam.")
    print()