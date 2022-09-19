import cv2
from PIL import ImageGrab
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

class Capture:
    def __init__(self, x1 = 0, y1 = 0, x2 = 400, y2 = 400):
        self.custom_config = r'-c tessedit_char_whitelist=1234567890 --psm 6'    # only number

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def imageToString(self):
        image = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(self.x1, self.y1, self.x2, self.y2))), cv2.COLOR_BGR2GRAY)
        result = pytesseract.image_to_string(image, config=self.custom_config)
        print(result)

        cv2.imshow("image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return result
