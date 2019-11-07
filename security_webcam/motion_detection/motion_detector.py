"""
    Motion detection module.
"""

import numpy as np
import cv2 as cv
import imutils


class MotionDetector:
    """ Motion detection class. """
    def __init__(self, weight=0.5):
        self.weight = weight
        self.bg = None


    def update(self, im):
        """ Compute average weight of the input image """
        if self.bg is None:
            self.bg = im.copy().astype("float")
            return

        cv.accumulateWeighted(im, self.bg, self.weight)


    def detect(self, im, threshold=25):
        """ Detect motion from the image """
        # calculate absolute difference first
        delta = cv.absdiff(self.bg.astype("uint8"), im)

        # use binary thresholding method to make pixel values 0 or 255
        th = cv.threshold(delta, threshold, 255, cv.THRESH_BINARY)[1]

        # apply erosion and dilation to remove small blobs
        th = cv.erode(th, None, iterations=2)
        th = cv.dilate(th, None, iterations=2)

        cnts = cv.findContours(th.copy(), cv.RETR_EXTERNAL,
                               cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        if not cnts:
            return None

        minX, minY = np.inf, np.inf
        maxX, maxY = -np.inf, -np.inf
        for c in cnts:
            x, y, w, h = cv.boundingRect(c)
            minX, minY = min(minX, x), min(minY, y)
            maxX, maxY = max(maxX, x + w), max(maxY, y + h)

        return th, (minX, minY, maxX, maxY)
