"""
    Module for processing videos
"""

# pylint: disable=expression-not-assigned, too-many-locals, too-many-arguments


from datetime import datetime
from time import time
import sys

import cv2 as cv
#import face_recognition as fr
from security_webcam.video_buffer import VideoBuffer, TemporaryBuffer
from security_webcam.motion_detector import MotionDetector


class CameraControl:
    """ Camera control class """

    def __init__(self):
        self._md = MotionDetector(0.1)
        self._cap = None


    def start_cam(self, fps=30, webcam_code=0):
        """ Start webcam """
        self._cap = cv.VideoCapture(webcam_code)
        self._cap.set(cv.CAP_PROP_FPS, fps)


    def start_recording(self, fps=30, temp_buffer_len=5, vid_buffer_len=60,
                        max_len=5, show_time=False, show_cam=False, verbose=False):
        """ Start recording """
        _, frame = self._cap.read()   # read the first frame to get dimension of the frame

        # initialize buffer list
        temp_buffer = TemporaryBuffer(fps=fps, length=temp_buffer_len)
        buffers = [None] * (max_len + 1)
        buffers[0] = temp_buffer
        for i in range(1, len(buffers)):
            buffers[i] = VideoBuffer(fps=fps, length=vid_buffer_len)
        curr_i = 1

        # initialize some variables
        curr_time = prev_time = detected_time = time()
        motion_detected = False

        # start recording
        while True:
            _, frame = self._cap.read()

            detected_frame = self._md.detect(frame)

            # TODO use face recognition somewhere else?
            #small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
            #face_locations = fr.face_locations(small_frame)

            # switch mode once a face is detected
            if detected_frame:
                if not motion_detected:
                    print('>>> MOTION DETECTED!!!') if verbose else None
                    detected_time = time()

                motion_detected = True
                prev_time = time()

            frame = self._add_time(frame) if show_time else None
            self._show_cam(frame) if show_cam else None

            # decide which buffer to put in
            buffers[curr_i].load(frame) if motion_detected else temp_buffer.load(frame)

            curr_time = time()

            # use the next buffer once the current one is full
            if buffers[curr_i].is_full():
                curr_i += 1
                if curr_i == len(buffers):
                    curr_i -= 1
                    break
                else:
                    detected_time = time()

            # if wait time is reached, exit
            if motion_detected and (curr_time - prev_time) > temp_buffer_len:
                break

        real_fps = buffers[curr_i].num_frames / (curr_time - detected_time)
        return buffers, (frame.shape[1], frame.shape[0]), real_fps


    @staticmethod
    def _add_time(frame):
        """ Add time stamp to the frame """
        now = datetime.today().strftime("%m-%d-%Y %H:%M:%S")
        return cv.putText(frame, now, (25, 50), cv.FONT_HERSHEY_SIMPLEX,
                          1, (0, 0, 255), 2)


    @staticmethod
    def _show_cam(frame):
        """ Display the video feed """
        cv.imshow('Security Webcam', frame)
        key = cv.waitKey(1) & 0xFF
        if key == 27:
            sys.exit(0)


    def close_cam(self):
        """ Properly close webcam """
        self._cap.release()
        cv.destroyAllWindows()
