import pyimgur
from creds import *
import requests
from send_to_imgur import UploadToImgur

TXT_MSG = "Door Bell Pressed!"
IMAGE_DIR = "/home/pi/Desktop/"

IMG = "snap.jpg"

def UploadAndSendNotification():
    media_url = UploadToImgur()
    print(media_url)
    ifttt_url = IFTTT_URL % (IFTTT_EVENT, IFTTT_KEY)#'https://maker.ifttt.com/trigger/button_pressed/with/key/yaQw9rPudVgRqoiTMEg5u'
    report = {}
    report["value1"] = media_url
    r = requests.post(ifttt_url, data=report)
    print(r)
