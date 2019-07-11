"""
    A security camera on computer using webcam.
"""

import cv2 as cv
import numpy as np


def main():
    """ Main function """
    cap = cv.VideoCapture(0)


    while True:
        _, frame = cap.read()
        cv.imshow('smile', frame)

        key = cv.waitKey(1) & 0xFF

        if key == 27:
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
