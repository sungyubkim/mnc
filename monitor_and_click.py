import time
import pyautogui
import easyocr
import numpy as np

def find_and_click_text(target_text, first_only=True):
    # Take a screenshot using pyautogui
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to an array
    screen_array = np.array(screenshot)
    
    # Convert RGB to BGR (OpenCV format)
    screen_open_cv = screen_array[:, :, ::-1]

    # Initialize the easyocr Reader with English language
    reader = easyocr.Reader(['en'])
    
    # Perform OCR on the image
    results = reader.readtext(screen_open_cv)
    # from pprint import pprint;pprint(results)
    
    original_position = pyautogui.position()  # Save original mouse position
    # Iterate through the results
    for (bbox, text, prob) in results:
        if target_text in text:
            # Calculate the center of the bounding box
            # print(bbox, type(bbox), len(bbox));input()
            top_left = bbox[0]
            bottom_right = bbox[2]
            x = int((top_left[0] + bottom_right[0]) / 2)
            y = int((top_left[1] + bottom_right[1]) / 2)
            
            # Click the center of the bounding box
            pyautogui.click(x, y)
            print(f"Clicked on '{text}' at ({x}, {y})")
            if first_only:
                pyautogui.moveTo(original_position)  # Return the mouse to its original position
                return None
    pyautogui.moveTo(original_position)  # Return the mouse to its original position

if __name__ == '__main__':
    while True:
        find_and_click_text("NEXT", first_only=True)
        time.sleep(3)  # Wait for 10 seconds before taking another screenshot
