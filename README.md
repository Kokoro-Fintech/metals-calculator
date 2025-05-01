# metals-calculator

A Python-based tool that fetches real-time precious metal prices (gold, silver, platinum) using the OANDA API, then calculates the total USD value of your holdings based on weight (grams for gold/platinum and ounces for silver).

---

## 🧾 Features

- ✅ Fetch live prices via the [OANDA API](https://developer.oanda.com/)
- ✅ Support for gold, silver, and platinum
- ✅ Accepts input in grams: gold and platinum
- ✅ Accepts input in ounces: silver
- ✅ Calculate total holding and estimated resale of physical bullions (assuming 15% markup)
- ✅ Modular design with separate scripts for fetching data and performing calculations
- ✅ Demonstrates clean cross-script function imports
- ✅ API key secured via **Mac Keychain Access**

---

## 📌 Note

Secure API encryption is detailed in the [`demo-for-encrypting-api`](https://github.com/Kokoro-Fintech/demo-for-encrypting-api) repository.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kokoro-Fintech/metals-calculator.git
   cd metals-calculator
   ```

2. **Install required libraries:**
   ```bash
   pip install requests keyring
   ```

---

## 🚀 Usage

Run the main script from your terminal:

```bash
python metals_calculator.py
```

For each metal, you’ll be prompted to input:
- Weight (grams or ounces depending on metal)

---

## 🧪 Example Output
```
Live Gold Price: 3248.0 USD per ounce
Live Silver Price: 32.381 USD per ounce
Live Platinum Price: 952.083 USD per ounce

Enter the weight of your gold in grams: 10
Enter the weight of your silver in ounces: 5
Enter the weight of your platinum in grams: 5

The current value of 10.0g of gold is: $1044.26
The current value of 5.0 oz of silver is: $161.91
The current value of 5.0g of platinum is: $153.05

Total value of all metals: $1359.21
Resell for 15% markup: $1563.09
```
---

## 📁 Project Structure

```
metals-calculator/
├── get_prices.py           # Fetches real-time prices from OANDA
├── metals_calculator.py    # Main script for user interaction & calculation
├── README.md               # Project overview and instructions
├── .gitignore              # Python-specific ignores
└── LICENSE                 # MIT License
```

---

## 🪪 License

This project is licensed under the MIT License.  
Free to use, modify, and distribute — just credit the original author.
