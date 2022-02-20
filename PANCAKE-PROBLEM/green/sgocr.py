# import easyocr
# reader = easyocr.Reader(['ch_sim'],gpu=False) # this needs to run only once to load the model into memory
# result = reader.readtext('shot.jpg')
# print(result)

import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open("./shot.jpg"))
print(text)