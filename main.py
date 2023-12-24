import pyttsx3
from PyPDF2 import PdfReader

# Open the PDF file in binary mode
with open('oop.pdf', 'rb') as book:
    # Create a PdfReader object
    pdfReader = PdfReader(book)

    # Get the total number of pages in the PDF
    pages = len(pdfReader.pages)
    print(f'Total number of pages: {pages}')

    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Adjust voice and volume properties for a more natural sound
    speaker.setProperty('voice', 'english_us')  # Choose a suitable voice
    speaker.setProperty('rate', 150)  # Adjust the speech rate
    speaker.setProperty('volume', 1.0)  # Adjust the volume (1.0 is the default)

    # Loop through each page (starting from page 0)
    for num in range(pages):
        # Get the specific page
        page = pdfReader.pages[num]

        # Extract text from the page
        text = page.extract_text()

        # Speak the text
        speaker.say(text)

    # Ensure all the text is spoken before exiting
    speaker.runAndWait()
