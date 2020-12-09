from picamera import PiCamera
from time import sleep
from openalpr_ocr import ocr

def imagecapture():
	sleeptime = 0
	camera = PiCamera()
	camera.resolution = (1920, 1080)
	camera.start_preview()
	sleep(sleeptime)
	camera.capture('picture.jpg')
	camera.stop_preview()
	camera.close()
