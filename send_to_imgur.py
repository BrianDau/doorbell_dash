#from twilio.rest import TwilioRestClient
import pyimgur
from creds import *

TXT_MSG = "Door Bell Pressed!"
IMAGE_DIR = "/home/pi/Desktop/"

IMG = "snap.jpg"

def UploadToImgur():
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(IMAGE_DIR + IMG, title=TXT_MSG)
    media_url = uploaded_image.link
    return media_url
