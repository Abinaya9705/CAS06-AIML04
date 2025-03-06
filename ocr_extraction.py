from PIL import Image
import pytesseract

# 🔹 Set the path to Tesseract-OCR manually
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# 🔹 Load the image
image_path = "image.png"  # Ensure the image is in the same folder
image = Image.open(image_path)

# 🔹 Extract text
extracted_text = pytesseract.image_to_string(image)

# 🔹 Print the extracted text
print("Extracted Text:\n", extracted_text)
