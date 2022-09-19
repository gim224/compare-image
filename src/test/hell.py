from PIL import ImageGrab
import time
import cv2
import keyboard
import mouse
import numpy as np
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# def set_roi():
#     global ROI_SET, x1, y1, x2, y2
#     ROI_SET = False
#     print("Select your ROI using mouse drag.")
#     while(mouse.is_pressed() == False):
#         x1, y1 = mouse.get_position()
#         while(mouse.is_pressed() == True):
#             x2, y2 = mouse.get_position()
#             while(mouse.is_pressed() == False):
#                 print("Your ROI : {0}, {1}, {2}, {3}".format(x1, y1, x2, y2))
#                 ROI_SET = True
#                 return

# keyboard.add_hotkey("ctrl+1", lambda: set_roi())

# ROI_SET = False
# x1, y1, x2, y2 = 0, 0, 0, 0
# while True:
#     if ROI_SET == True:
#         image = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2))), cv2.COLOR_BGR2RGB)
#         cv2.imshow("image", image)
#         key = cv2.waitKey(100)

#         print(pytesseract.image_to_string(image))

#         if key == ord("q"):
#             print("Quit")
#             break

# cv2.destroyAllWindows()

intervalSeconds = 2
endSeconds = 60 * 60 * 2

def compareImg(): 
    global prevImg, curImg

    for i in range(endSeconds):
        curImg = ImageGrab.grab()
    
        if prevImg is None:
            prevImg = curImg;
        time.sleep(intervalSeconds)