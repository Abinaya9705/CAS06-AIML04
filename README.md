PROBLEM STATEMENT CLARITY : Cyberbullying on social media is a growing concern, affecting mental health and online safety. Many users face harassment, offensive language, and repeated bullying from specific accounts. However, there is no automated system that monitors the screen in real-time, detects harmful messages, and alerts users about potential cyberbullies.
INNOVATION : Real time screen monitoring on social media
             Harmful Text Detection
             Multi Level Severiety Detection(Safe Mild Insult Severe Cyberbullying)
             Avoiding bullying people
             Avoid False Positives
FEASIBILITY : 
Screen Monitoring: Feasible via Flutter UI overlay, continuously capturing screenshots.
OCR Integration: Extract text using Tesseract OCR  (Python).
Cyberbullying Detection: Deep learning models (BERT) classify extracted text.
Real-time Response: The Flutter app communicates with a local Python Flask API, processing and displaying alerts immediately.

TECHNICAL STACK SELECTION :
Front-end (Real-time Monitoring & UI): Flutter
OCR for Text Extraction: Tesseract OCR 
Cyberbullying Detection Model: BERT (fine-tuned for social media text)
Deployment: Runs locally on the device

SCALIBILITY: 
