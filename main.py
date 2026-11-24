
# Voice to PDF Item Report Generator

# --------------------------------------------------
# STEP 1: INSTALL REQUIRED LIBRARIES
# --------------------------------------------------

# pip install SpeechRecognition
# Used to convert spoken words into text.

# pip install pyaudio
# Used to capture the user's voice through the microphone.

# pip install reportlab
# Used to create PDF files.

# pip install word2number
# Used to convert number words into numeric values.
# Example: "five hundred" becomes 500.


# --------------------------------------------------
# PROJECT FLOW
# --------------------------------------------------

# 1. PyAudio captures the user's voice through the microphone.
# 2. SpeechRecognition converts the recorded voice into text.
# 3. The program extracts the item name and its price.
# 4. The item name and price are stored in a list.
# 5. ReportLab generates a PDF report using the stored items.


# --------------------------------------------------
# STEP 2: IMPORT REQUIRED LIBRARIES
# --------------------------------------------------

import speech_recognition as sr

# Imports the SpeechRecognition library.
# 'sr' is the short name used to access its functions.

from reportlab.pdfgen import canvas

# reportlab = Python library used to create PDF files.
# pdfgen = Module used for generating PDFs.
# canvas = Provides a drawing area where we can add text
# and other content to a PDF.

from word2number import w2n

# Imports the word-to-number conversion functionality.
# It converts spoken number words into numeric values.


# --------------------------------------------------
# STEP 3: CREATE RECOGNIZER AND ITEM STORAGE
# --------------------------------------------------

r = sr.Recognizer()
# recognizer is a class which provides methods to process audio.
# Creates a Recognizer object.
# It is responsible for processing and recognizing speech.

items = []

# Creates an empty list to store item names and prices.
# Each item will be stored as a tuple.
# Example: ("Apple", "500")


# --------------------------------------------------
# STEP 4: CREATE A FUNCTION TO CAPTURE VOICE
# --------------------------------------------------

def listen():

    # Opens the microphone to capture the user's voice.
    with sr.Microphone() as source:

        print("Adjusting noise...")

        # Adjusts the recognizer according to background noise.
        # Duration=2 means it listens to background noise for 2 seconds.
        r.adjust_for_ambient_noise(source, duration=2)

        print("🎙️ Speak (say 'exit' to finish)")

        # Records the user's voice through the microphone.
        # timeout=None means it waits until speech starts.
        # phrase_time_limit=10 limits recording to 10 seconds.
        audio = r.listen(source, timeout=None, phrase_time_limit=10)

    try:

        # Converts the recorded audio into text using Google Speech Recognition.
        text = r.recognize_google(audio)

        # Displays the recognized text.
        print("Recognized:", text)

        # Removes unnecessary spaces and returns the recognized text.
        return text.strip()     

    except sr.UnknownValueError:

        # Executes when the recognizer cannot understand the audio.
        print("Could not understand audio.")
        return ""

    except sr.RequestError:

        # Executes when the speech recognition service is unavailable.
        print("Speech recognition service unavailable.")
        return ""


# --------------------------------------------------
# STEP 5: TAKE INPUT AND PROCESS ITEMS
# --------------------------------------------------

# Runs continuously until the user says "exit".
while True:

    # Calls the listen() function to capture voice input.
    text = listen()

    print("Recognized Speech:", text)

    # If no text is recognized, the loop starts again.
    if not text:
        continue

    # Checks whether the user said "exit".
    # If yes, the loop stops.
    if text.lower() == "exit":
        break

    # Splits the recognized sentence into individual words.
    # Example: "Apple 500" becomes ["Apple", "500"].
    words = text.split()

    # Initially, price is an empty string.
    price = ""

    # Checks each word to find the numeric price.
    for w in words:

        # Checks whether the word contains a numeric value.
        # replace(".", "") also allows decimal values.
        if w.replace(".", "").isdigit():

            # Stores the numeric word as the price.
            price = w
            break

        # If no numeric price is found, tries converting
        # number words into numeric values.
        if not price:
            try:

                # Converts number words into a numeric value.
                # Example: "five hundred" becomes "500".
                price = str(w2n.word_to_num(text))

            except:

                # If conversion fails, keeps the price empty.
                price = ""

    # Extracts the item name by removing numeric words
    # and the word "rs" from the recognized sentence.
        item_name = " ".join(
            w for w in words
            if not w.replace(".", "").isdigit() and w.lower() != "rs"
        )

    # If a price is found, stores the item and price in the list.
    if price:

        # Appends the item name and price as a tuple.
        items.append((item_name, price))

        # Displays the successfully added item.
        print(f"ADDED: {item_name}   Rs. {price}")

    else:

        # Displays a message when the price is not recognized.
        print("Please repeat and say item with price")


# --------------------------------------------------
# STEP 6: GENERATE PDF REPORT
# --------------------------------------------------

#Total 
total=0


# Creates a new PDF file named Items_Report.pdf.
c = canvas.Canvas("Items_Report.pdf")

# Sets the font and font size for the PDF heading.
c.setFont("Helvetica", 12)

# Draws the report heading at the given X and Y coordinates.
c.drawString(200, 800, "Item Report")

# Sets bold font for the item details.
c.setFont("Helvetica-Bold", 12)

# Sets the initial vertical position for the first item.
y = 770

# Loops through all stored items.
# enumerate() provides a serial number along with each item.
for i, (name, price) in enumerate(items, 1):

    # Writes the item number, name and price into the PDF.
    # X coordinate = 50, Y coordinate = current y value.
    c.drawString(50, y, f"{i}. {name} --------->  Rs {price}")
    total=total+int(price)

    # Decreases the Y coordinate by 20 for the next item.
    # This prints each item on a new line.

    y -= 20

c.drawString(50,y,f"Grand Total: {total}")
# Saves the PDF file.
c.save()

# Displays a confirmation message after saving the PDF.
print("Report PDF Saved: Items_Report.pdf")
