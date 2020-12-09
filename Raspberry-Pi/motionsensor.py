from gpiozero import MotionSensor
from openalpr_ocr import ocr
from image import imagecapture
from time import sleep

def main():
    sleeptime = 5
    pir = MotionSensor(4)

    while True:
        pir.wait_for_motion()
        print("Car Motion Detected")
        imagecapture()
        print("Car Image Capture")
        ocr()
        sleep(sleeptime)


if __name__ == "__main__":
	main()
