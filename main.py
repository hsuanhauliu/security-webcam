"""
    A security camera on computer using webcam.
"""


import cv2 as cv
import face_recognition as fr
#import matplotlib.pyplot as plt
#import numpy as np

import security_webcam as sw


def main():
    """ Main function """

    top_fps = 30
    length = 5
    verbose = True
    output_file = 'temp.mov'

    clip = sw.start_webcam(fps=top_fps, buffer_length=length, show_cam=False, verbose=verbose)
    print('FPS:', clip.fps)
    sw.output_vid(output_file, clip, verbose=verbose)

    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
