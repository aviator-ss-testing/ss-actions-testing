print("Hello, Aviator! Ok I saw webhook arrive but nothing happened?")

def process_payment(amount, card_number):
    """Process payment with improved error handling"""
    if amount <= 0:
        raise ValueError("Payment amount must be positive")
    if len(card_number) != 16:
        raise ValueError("Invalid card number length")
    return {"status": "success", "transaction_id": "tx_12345"}
