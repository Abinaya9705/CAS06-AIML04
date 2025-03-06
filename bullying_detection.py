import pytesseract
from PIL import Image
import re
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = "chat_screenshot.png"  
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)
print("Extracted Text:\n", extracted_text)
chat_pattern = r"([\w\d]+): (.+)"  
matches = re.findall(chat_pattern, extracted_text)
toxic_words = ["dumb", "loser", "stupid", "idiot", "ugly", "fool"]
for username, message in matches:
    is_bullying = any(word in message.lower() for word in toxic_words) 
    if is_bullying:
        print(f"🚨 Warning! {username} might be bullying: {message}")
    else:
        print(f"✅ Safe Message from {username}: {message}")
