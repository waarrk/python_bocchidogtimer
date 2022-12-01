import random
import time

import cv2
from bocchidog import Bocchidog, BocchidogBark

img = cv2.imread('jimihei.jpg')


def main():

    print('ぼっちどっぐたいま Start！')
    bocchidog = Bocchidog(2)
    bocchidog.start()

    try:
        while True:
            sleep = random.random() * 3
            print("ぼっちちゃんが戻るまで{:.1f}秒...".format(sleep))

            time.sleep(sleep)
            bocchidog.check()
    except BocchidogBark:
        print('ぼっち・ざ・どっぐ！')
        cv2.imshow('BocchiDog!', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    finally:
        bocchidog.stop()


if __name__ == '__main__':
    main()
