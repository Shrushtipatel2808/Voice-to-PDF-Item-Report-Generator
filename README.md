# 🎙️ Voice to PDF Item Report Generator

A Python-based project that allows users to add item names and prices using voice commands and automatically generates a PDF report containing all the collected items.

## 📌 Project Overview

The Voice to PDF Item Report Generator uses speech recognition to capture item details through a microphone. It converts spoken input into text, extracts item names and numerical prices, stores the details, and generates a PDF report using the ReportLab library.

## ✨ Features

- Voice-based item entry
- Speech-to-text conversion
- Automatic item name extraction
- Numerical price extraction
- Stores multiple items in a Python list
- Generates a PDF report automatically
- Simple and easy-to-use interface through the terminal

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| SpeechRecognition | Converts speech into text |
| PyAudio | Captures audio through the microphone |
| ReportLab | Creates PDF reports |

## 📂 Project Structure

```text
Voice-to-PDF-Item-Report-Generator/
│
├── main.py
├── requirements.txt
├── README.md
└── Items_Report.pdf
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd Voice-to-PDF-Item-Report-Generator
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Run the project**

```bash
python main.py
```

## 🎤 How to Use

1. Run the Python program.
2. Allow microphone access if requested.
3. Speak an item name followed by its numerical price.
4. The program recognizes the spoken input.
5. The item name and price are stored in a list.
6. Say `exit` to stop adding items.
7. The program automatically generates `Items_Report.pdf`.

**Example Voice Commands:**

```text
Apple 50
Milk 60
Rice 100
Sugar 45
Exit
```

## 📄 Sample PDF Output

The generated PDF contains an item report with numbered entries and their respective prices.

Example:

```text
              Item Report

1. Apple  ---------> Rs 50
2. Milk   ---------> Rs 60
3. Rice   ---------> Rs 100
4. Sugar  ---------> Rs 45
```

## 📚 Python Concepts Used

- Functions
- While loops
- For loops
- Conditional statements
- Lists and tuples
- String operations
- Exception handling
- File generation

## 🚀 Future Improvements

- Add support for spoken number words.
- Add total price calculation.
- Add date and time to the PDF report.
- Improve PDF formatting and design.
- Add a graphical user interface (GUI).
- Support editing and deleting items.

## 👩‍💻 Author

**Shrushti Patel**

Computer Engineering Student | Python & AI/ML Learner

---

⭐ If you find this project useful, feel free to explore and improve it!