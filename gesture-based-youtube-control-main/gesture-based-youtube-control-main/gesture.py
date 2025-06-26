import cv2
import mediapipe as mp
from func import recognizeHandGesture, getStructuredLandmarks
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Path to your ChromeDriver
chrome_driver_path =r'D:\Projects\Youtube Video controller\chromedriver-win32\chromedriver-win32\chromedriver.exe'

  # Ensure this path is correct

# Configure Selenium to use the correct driver
chrome_service = Service(chrome_driver_path)
chrome_options = Options()

def gest():
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get('https://www.youtube.com/watch?v=09R8_2nJtjg')
    driver.execute_script('document.getElementsByTagName("video")[0].play()')
    
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(0)
    i = 0
    c = 0
    try:
        while cap.isOpened():
            l = []
            i += 1
            success, image = cap.read()
            if not success:
                break
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    c += 1
                    for lp in hand_landmarks.landmark:
                        l.append(lp.x)
                        l.append(lp.y)
            cv2.imshow('MediaPipe Hands', image)

            # Check if 'l' has the expected number of elements before processing
            if len(l) == 42:
                recognizedHandGesture = recognizeHandGesture(getStructuredLandmarks(l))
                print(recognizedHandGesture)
                if recognizedHandGesture == 5:
                    driver.execute_script('document.getElementsByTagName("video")[0].pause()')
                elif recognizedHandGesture == 4:
                    driver.execute_script('document.getElementsByTagName("video")[0].play()')
                elif recognizedHandGesture == 3:
                    driver.execute_script('document.getElementsByTagName("video")[0].playbackRate = 2')
                elif recognizedHandGesture == 2:
                    driver.execute_script('document.getElementsByTagName("video")[0].playbackRate = 1')
                elif recognizedHandGesture == 6:
                    driver.execute_script('document.getElementsByTagName("video")[0].volume = 0')
                elif recognizedHandGesture == 7:
                    driver.execute_script('document.getElementsByTagName("video")[0].volume = 1')
                elif recognizedHandGesture == 8:
                    # Fast Forward (All fingers open except the ring finger)
                    driver.execute_script('document.getElementsByTagName("video")[0].currentTime += 5')
                elif recognizedHandGesture == 9:
                    # Rewind (All fingers open except the little finger)
                    driver.execute_script('document.getElementsByTagName("video")[0].currentTime -= 5')
            else:
                print("Insufficient landmarks detected")

            if cv2.waitKey(5) & 0xFF == 27:
                break
    except Exception as e:
        print('Not Recognized:', e)
    finally:
        hands.close()
        cap.release()
        driver.quit()
        cv2.destroyAllWindows()

gest()
