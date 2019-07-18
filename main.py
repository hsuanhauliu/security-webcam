"""
    A security camera on computer using webcam.
"""


import cv2 as cv
#import matplotlib.pyplot as plt
#import numpy as np

import security_webcam as sw


def main():
    """ Main function """
    fps = 30
    length = 5
    verbose=True
    output_file = 'temp.mov'

    clip = sw.start_webcam(fps=fps, length=length, verbose=verbose)
    sw.output_vid(output_file, clip, verbose=verbose)

    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
