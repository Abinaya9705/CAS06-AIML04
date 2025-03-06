import pytesseract
from PIL import Image
import re
import json
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = "chat_screenshot.png"  
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)
print(" Extracted Text:\n", extracted_text)  
chat_pattern = r"([\w\d\s_]+):\s*(.+)"  
matches = re.findall(chat_pattern, extracted_text)
toxic_words = ["dumb", "loser", "stupid", "idiot", "ugly", "fool", "hate", "kill", "worthless"]
user_behavior = {}
for username, message in matches:
    is_bullying = any(re.search(rf"\b{word}\b", message, re.IGNORECASE) for word in toxic_words)
    if username not in user_behavior:
        user_behavior[username] = {"safe": 0, "warning": 0, "bully": 0}
    if is_bullying:
        user_behavior[username]["bully"] += 1
        print(f" WARNING! {username} might be bullying: \"{message}\"")
    else:
        user_behavior[username]["safe"] += 1
        print(f"Safe Message from {username}: \"{message}\"")
flagged_users = {}
for username, stats in user_behavior.items():
    total_messages = stats["safe"] + stats["bully"]
    if stats["bully"] > 0:
        flagged_users[username] = " Bully"
    elif total_messages >= 5 and stats["safe"] / total_messages > 0.9:
        flagged_users[username] = " Trusted User"
    else:
        flagged_users[username] = " Warning User"
with open("flagged_users.json", "w") as file:
    json.dump(flagged_users, file, indent=4)
print("\n Final User Categorization Report:")
print(json.dumps(flagged_users, indent=4))