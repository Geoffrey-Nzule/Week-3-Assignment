def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return round(discounted_price, 2)
    else:
        return price

# Prompt user for input
original_price = 10000
discount_percent = 20

# Calculate and display the final price
final_price = calculate_discount(original_price, discount_percent)

if final_price == original_price:
    print(f"No discount applied. The price remains ${final_price:.2f}")
else:
    print(f"The final price after applying the {discount_percent}% discount is ${final_price:.2f}")