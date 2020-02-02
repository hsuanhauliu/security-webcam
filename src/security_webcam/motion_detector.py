"""
    Motion detection module.
"""

import cv2 as cv
import numpy as np


class MotionDetector:
    """ Motion detection class. """

    def __init__(self, weight=0.5):
        self.weight = weight
        self.bg = None
        self._counter = 0


    @staticmethod
    def _process_frame(frame, ratio):
        """ Process frame for motion detection """
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.resize(gray, (0, 0), fx=ratio, fy=ratio)
        return cv.GaussianBlur(gray, (7, 7), 0)


    def _update(self, im):
        """ Compute average weight of the input image """
        if self.bg is None:
            self.bg = im.copy().astype("float")
            return

        cv.accumulateWeighted(im, self.bg, self.weight)


    def detect(self, im, threshold=25):
        """ Detect motion from the image """
        im = self._process_frame(im, 0.25)

        if self.bg is None or self._counter < 10:
            self._counter += 1
            self._update(im)
            return None

        # calculate absolute difference first
        delta = cv.absdiff(self.bg.astype("uint8"), im)

        # use binary thresholding method to make pixel values 0 or 255
        th = cv.threshold(delta, threshold, 255, cv.THRESH_BINARY)[1]

        # apply erosion and dilation to remove small blobs
        th = cv.erode(th, None, iterations=2)
        th = cv.dilate(th, None, iterations=2)

        cnts = cv.findContours(th.copy(), cv.RETR_EXTERNAL,
                               cv.CHAIN_APPROX_SIMPLE)[0]
        rect = self._find_boundary(cnts)

        self._update(im)
        return rect


    @staticmethod
    def _find_boundary(contours):
        """ Find boundary coordinates based on contours """
        if not contours:
            return None

        min_x, min_y, max_x, max_y = np.inf, np.inf, -np.inf, -np.inf
        for c in contours:
            x, y, w, h = cv.boundingRect(c)
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_x, max_y = max(max_x, x + w), max(max_y, y + h)

        return (min_x, min_y, max_x, max_y)
