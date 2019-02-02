import picamera
import datetime
from ifttt import UploadAndSendNotification

IMG_WIDTH = 800
IMG_HEIGHT = 600

IMAGE_DIR_DB = "/home/pi/doorbell_dash/doorbell_dash_project/photos/photos/"
IMAGE_DIR = "/home/pi/Desktop/"

IMG = "snap.jpg"

suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S.jpg")
file = "".join([IMAGE_DIR_DB, suffix])


def pic():
    camera = picamera.PiCamera()
    # YMMV, adjust these depending on the orientation of your camera
    camera.vflip = False
    camera.hflip = False
    camera.rotation=270
    camera.brightness = 60
    camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
    camera.capture(IMAGE_DIR + IMG)
    camera.close()
    pic_to_db()


def pic_to_db():
    # YMMV, adjust these depending on the orientation of your camera
    camera = picamera.PiCamera()
    camera.vflip = False
    camera.hflip = False
    camera.rotation=270
    camera.brightness = 60
    camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
    camera.capture(file)
    camera.close()
    UploadAndSendNotification()
