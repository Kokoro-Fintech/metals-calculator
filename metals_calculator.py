# Purpose: calculate current value of my metal portfolio

from get_prices import get_prices  # Import the function from get_prices.py

# Fetch the live prices for gold, silver, and platinum once
gold_price_per_ounce, silver_price_per_ounce, platinum_price_per_ounce = get_prices()

# Leave a space after spot price
print()

# Check if the prices were fetched successfully
if gold_price_per_ounce is not None and silver_price_per_ounce is not None and platinum_price_per_ounce is not None:
    # Get weights first
    gold_weight_in_grams = float(input("Enter the weight of your gold in grams: "))
    silver_weight_in_ounces = float(input("Enter the weight of your silver in ounces: "))
    platinum_weight_in_grams = float(input("Enter the weight of your platinum in grams: "))

    # Leave a space after input
    print()

    # Store the value of the metals and calculate sum
    metals = []
    def calculate_sum_metals():
        total_value = sum(metals)  # This will add up all the values in the metals list
        resale = total_value * 1.15
        print(f"\nTotal value of all metals: ${total_value:.2f}")
        print(f'Resell for 15% markup: ${resale:.2f}')


    # Calculate the values
    def calculate_gold_value(weight_in_grams):
        if gold_price_per_ounce is not None:
            # Convert gold price from per ounce to per gram
            gold_price_per_gram = gold_price_per_ounce / 31.1035  # 1 ounce = 31.1035 grams

            # Calculate the value of the gold by weight in grams
            total_gold_value = weight_in_grams * gold_price_per_gram
            metals.append(total_gold_value)
            print(f"The current value of {weight_in_grams}g of gold is: ${total_gold_value:.2f}")
        else:
            print("Could not retrieve gold price. Please check the API connection.")

    def calculate_silver_value(weight_in_ounces):
        if silver_price_per_ounce is not None:
            # Calculate the value of the silver by weight in ounces
            total_silver_value = weight_in_ounces * silver_price_per_ounce
            metals.append(total_silver_value)
            print(f"The current value of {weight_in_ounces} oz of silver is: ${total_silver_value:.2f}")
        else:
            print("Could not retrieve silver price. Please check the API connection.")


    def calculate_platinum_value(weight_in_grams):
        if platinum_price_per_ounce is not None:
            # Convert platinum price from per ounce to per gram
            platinum_price_per_gram = platinum_price_per_ounce / 31.1035  # 1 ounce = 31.1035 grams

            # Calculate the value of the platinum by weight in grams
            total_platinum_value = weight_in_grams * platinum_price_per_gram
            metals.append(total_platinum_value)
            print(f"The current value of {weight_in_grams}g of platinum is: ${total_platinum_value:.2f}")
        else:
            print("Could not retrieve platinum price. Please check the API connection.")

    # Perform calculations
    calculate_gold_value(gold_weight_in_grams)
    calculate_silver_value(silver_weight_in_ounces)
    calculate_platinum_value(platinum_weight_in_grams)
    calculate_sum_metals()

else:
    print("Error fetching metal prices. Please check the API connection.")