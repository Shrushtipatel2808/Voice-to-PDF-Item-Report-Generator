# 🎙️ Voice to PDF Item Report Generator

A Python-based project that converts voice input into an organized PDF item report using Speech Recognition.

The application allows users to speak item names and prices, automatically extracts the information, stores multiple items, calculates the grand total, and generates a PDF report.

## ✨ Features

- 🎤 **Voice Input:** Capture item details through a microphone.
- 🗣️ **Speech Recognition:** Convert spoken words into text using Google Speech Recognition.
- 📦 **Item Extraction:** Identify item names and prices from recognized speech.
- 🔢 **Number Conversion:** Convert number words into numeric values using Word2Number.
- 📝 **Multiple Items:** Store multiple item entries in a list.
- 📄 **PDF Generation:** Generate an organized PDF report.
- 💰 **Automatic Total Calculation:** Calculate the grand total of all added items.
- 🔊 **Error Handling:** Handle unclear speech and speech recognition service errors.

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- PyAudio
- ReportLab
- Word2Number

## 📁 Project Structure

```text
Voice_to_PDF_Item_Report_Generator/
│
├── main.py
├── requirements.txt
├── README.md
└── Items_Report.pdf
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/Shrushtipatel2808/Voice-to-PDF-Item-Report-Generator.git
```

**2. Navigate to the project folder**

```bash
cd Voice-to-PDF-Item-Report-Generator
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the project**

```bash
python main.py
```

## 🎤 How to Use

1. Run the Python application.
2. Allow microphone access.
3. Speak an item name followed by its price.
4. The application recognizes and extracts the item details.
5. Repeat for multiple items.
6. Say `exit` to finish adding items.
7. The application calculates the grand total.
8. A PDF report named `Items_Report.pdf` is generated.

### Example Voice Inputs

```text
Apple 500
Milk 50
Rice 100
exit
```

## 📄 Sample PDF Output

The generated PDF report contains:

- Item number
- Item name
- Item price
- Grand Total

Example:

| Item | Price |
|---|---:|
| Apple | ₹500 |
| Milk | ₹50 |
| Rice | ₹100 |
| **Grand Total** | **₹650** |

## 🧠 Concepts Learned

- Python Functions
- Loops (`for`, `while`)
- Conditional Statements (`if-else`)
- Lists and Tuples
- String Manipulation
- Exception Handling (`try-except`)
- Type Conversion
- Speech Recognition
- PDF Generation
- Automatic Calculations

## 🚀 Future Improvements

- Quantity Support
- Expense Summary
- Better PDF Formatting
- Edit and Delete Items
- Multilingual Voice Recognition

## 👩‍💻 Author

**Shrushti Patel**

GitHub: [@Shrushtipatel2808](https://github.com/Shrushtipatel2808)

---

⭐ If you find this project interesting, feel free to explore the repository!