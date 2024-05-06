import time
import pyautogui
from PIL import Image
import pytesseract

# Configure tesseract to the location where it is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path according to your installation

def find_next_button():
    """Takes a screenshot, detects 'NEXT', and clicks on it if found."""
    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Use pytesseract to convert image to string
    text = pytesseract.image_to_string(screenshot)
    
    # Check if 'NEXT' is in the screenshot
    if 'NEXT' in text:
        print("Found 'NEXT'. Attempting to click...")
        # Attempt to find the button position using image analysis
        for word in pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)['text']:
            if word.lower() == 'next':
                index = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)['text'].index(word)
                # Get bounding box coordinates
                x, y, w, h = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)['left'][index], \
                             pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)['top'][index], \
                             pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)['width'][index], \
                             pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)['height'][index]
                
                # Calculate the center of the bounding box
                x_center = x + w / 2
                y_center = y + h / 2
                
                # Click the center of the 'NEXT' button
                pyautogui.click(x_center, y_center)
                print("Clicked on 'NEXT'.")
                return

        print("'NEXT' was detected but no clickable area found.")
    else:
        print("No 'NEXT' detected on screen.")

if __name__ == '__main__':
    while True:
        find_next_button()
        time.sleep(10)  # Wait for 10 seconds before taking another screenshot