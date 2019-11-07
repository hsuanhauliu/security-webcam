"""
    Module for processing videos
"""

# pylint: disable=expression-not-assigned, too-many-locals

from time import time
import sys

import cv2 as cv
import face_recognition as fr
from security_webcam.video_buffer import VideoBuffer, TemporaryBuffer


def start_cam(fps=30, webcam_code=0):
    """ Start webcam """
    cap = cv.VideoCapture(webcam_code)
    cap.set(cv.CAP_PROP_FPS, fps)
    return cap


def start_recording(cap, fps=30, buffer_length=5, show_cam=False, verbose=False):
    """ Start recording """
    _, frame = cap.read()   # read the first frame to get dimension of the frame

    # create two buffers
    temp_buffer = TemporaryBuffer(fps=fps, length=buffer_length)
    vid_buffer = VideoBuffer(fps=fps)
    buffers = []    # buffer list TODO set a maximum length for each buffer

    # initialize some variables
    prev_time = time()
    face_detected = False

    print('Starting webcam capturing...') if verbose else None
    while True:
        _, frame = cap.read()
        small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
        face_locations = fr.face_locations(small_frame)

        # switch mode once a face is detected
        if face_locations:
            print('>>> FACE DETECTED!!!') if verbose else None
            face_detected = True
            prev_time = time()

        # show the video feed
        if show_cam:
            cv.imshow('Security Webcam', frame)
            key = cv.waitKey(1) & 0xFF
            if key == 27:
                sys.exit(0)

        if face_detected:
            vid_buffer.load(frame)
        else:
            temp_buffer.load(frame)

        curr_time = time()

        # if wait time is reached, exit
        if face_detected and curr_time - prev_time > buffer_length:
            buffers.append(temp_buffer)
            buffers.append(vid_buffer)
            break

    return (frame.shape[1], frame.shape[0]), buffers


def close_cam(cap):
    """ Properly close webcam """
    cap.release()
    cv.destroyAllWindows()


def output_vid(output_file, video_clips, fps, frame_size, verbose=False):
    """ Save video as video file """
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(output_file, fourcc, fps, frame_size)

    for buf in video_clips:
        for frame in buf.next():
            out.write(frame)

    out.release()
    print('Finished saving video') if verbose else None
