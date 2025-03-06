import pytesseract
from PIL import Image
import re

# 🔹 Set the Tesseract OCR Path (Change this based on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 🔹 Load the image containing the chat
image_path = "chat_screenshot.png"  # Replace with your image filename
image = Image.open(image_path)

# 🔹 Extract text from the image using OCR
extracted_text = pytesseract.image_to_string(image)
print("Extracted Text:\n", extracted_text)  # Print extracted text for debugging

# 🔹 Define a regular expression pattern to extract usernames and messages
chat_pattern = r"([\w\d]+): (.+)"  # Pattern: "Username: Message"
matches = re.findall(chat_pattern, extracted_text)

# 🔹 Define toxic words for bullying detection
toxic_words = ["dumb", "loser", "stupid", "idiot", "ugly", "fool"]

# 🔹 Analyze messages for bullying content
for username, message in matches:
    is_bullying = any(word in message.lower() for word in toxic_words)  # Case insensitive check
    
    if is_bullying:
        print(f"🚨 Warning! {username} might be bullying: {message}")
    else:
        print(f"✅ Safe Message from {username}: {message}")
