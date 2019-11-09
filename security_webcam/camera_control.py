"""
    Module for processing videos
"""

# pylint: disable=expression-not-assigned, too-many-locals


from datetime import datetime
from time import time
import sys

import cv2 as cv
#import face_recognition as fr
from security_webcam.video_buffer import VideoBuffer, TemporaryBuffer
from security_webcam.motion_detector import MotionDetector


def start_cam(fps=30, webcam_code=0):
    """ Start webcam """
    cap = cv.VideoCapture(webcam_code)
    cap.set(cv.CAP_PROP_FPS, fps)
    return cap


def start_recording(cap, fps=30, buffer_length=5, show_time=False, show_cam=False, verbose=False):
    """ Start recording """
    _, frame = cap.read()   # read the first frame to get dimension of the frame
    md = MotionDetector(0.1)

    # create two buffers
    temp_buffer = TemporaryBuffer(fps=fps, length=buffer_length)
    vid_buffer = VideoBuffer(fps=fps)
    buffers = []    # buffer list TODO set a maximum length for each buffer

    # initialize some variables
    curr_time = prev_time = detected_time = time()
    motion_detected = False

    print('Starting webcam capturing...') if verbose else None
    while True:
        _, frame = cap.read()

        # motion detection
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.resize(gray, (0, 0), fx=0.25, fy=0.25)
        gray = cv.GaussianBlur(gray, (7, 7), 0)

        detected_frame = md.detect(gray)

        # detect face

        # TODO use face recognition somewhere else?
        #small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
        #face_locations = fr.face_locations(small_frame)

        # switch mode once a face is detected
        if detected_frame:
            print('>>> MOTION DETECTED!!!') if verbose else None
            if not motion_detected:
                detected_time = time()

            motion_detected = True
            prev_time = time()

        # Add time stamp to the frame
        if show_time:
            now = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
            frame = cv.putText(frame, now, (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                               1, (0, 0, 255), 2)

        # show the video feed
        if show_cam:
            cv.imshow('Security Webcam', frame)
            key = cv.waitKey(1) & 0xFF
            if key == 27:
                sys.exit(0)

        # decide which buffer to put in
        if motion_detected:
            vid_buffer.load(frame)
        else:
            temp_buffer.load(frame)

        curr_time = time()
        md.update(gray)

        # if wait time is reached, exit
        if motion_detected and curr_time - prev_time > buffer_length:
            buffers.append(temp_buffer)
            buffers.append(vid_buffer)
            break

    real_fps = vid_buffer.num_frames / (curr_time - detected_time)
    return buffers, (frame.shape[1], frame.shape[0]), real_fps


def close_cam(cap):
    """ Properly close webcam """
    cap.release()
    cv.destroyAllWindows()
