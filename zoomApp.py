from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import face_recognition
from PIL import Image, ImageDraw

chrome_options = Options()
chrome_options.add_argument("use-fake-ui-for-media-stream")
#chrome_options.add_argument("allow-file-access-from-files")
#chrome_options.add_argument("use-fake-device-for-media-stream")



driver = webdriver.Chrome(chrome_options=chrome_options)
baseUrl = "localhost:3000/2b1a7e68-93ac-490e-89ef-237febbdb6a7"

driver.get(baseUrl)

for x in range(2):
    divGrid = driver.find_element_by_id("video-grid")
    divChildren = divGrid.find_elements_by_css_selector("*")
    print(str(divChildren))
    try:
        print(divChildren[0].screenshot('./Screenshots/'+str(x)+'.png'))
        image = face_recognition.load_image_file('./Screenshots/'+str(x)+'.png')
        face_landmarks_list = face_recognition.face_landmarks(image)
        print(face_landmarks_list)
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)
        for face_landmarks in face_landmarks_list:

            # Print the location of each facial feature in this image
            for facial_feature in face_landmarks.keys():
                print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

            # Let's trace out each facial feature in the image with a line!
            for facial_feature in face_landmarks.keys():
                d.line(face_landmarks[facial_feature], width=5)

        pil_image.show()
    except Exception as e:
        print(str(e))
    time.sleep(1)



