""" Module for processing videos """


from time import time

import cv2 as cv
import face_recognition as fr
from security_webcam.video_buffer import VideoBuffer


def start_webcam(fps=30, buffer_length=10, webcam_code=0, show_cam=False, verbose=False):
    """ Start webcam capture """
    cap = cv.VideoCapture(webcam_code)
    cap.set(cv.CAP_PROP_FPS, fps)

    # initialize some variables
    _, frame = cap.read()   # read the first frame to get dimension of the frame
    vid_buffer = VideoBuffer((frame.shape[1], frame.shape[0]), buffer_length)
    prev_time = time()
    num_frames, face_detected = 0, False

    if verbose:
        print('Starting webcam capturing...')

    while True:
        _, frame = cap.read()
        small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
        face_locations = fr.face_locations(small_frame)

        # switch mode once a face is detected
        if face_locations:
            if verbose:
                print('FACE DETECTED!!!')
            face_detected = vid_buffer.recording = True

            # reset time and num of frames every time a face is detected
            prev_time = time()
            num_frames = 0

        if show_cam:
            cv.imshow('Security Webcam', frame)

        vid_buffer.load(frame)
        num_frames += 1
        curr_time = time()
        if face_detected and curr_time - prev_time > buffer_length:
            vid_buffer.fps = num_frames // (curr_time - prev_time)
            break

    cap.release()
    return vid_buffer


def output_vid(output_file, video_clip, verbose=False):
    """ Save video as video file """
    if not isinstance(video_clip, VideoBuffer):
        raise TypeError('Video clip must be of type VideoBuffer')

    if not video_clip:
        raise ValueError('There are no frames to be saved')

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(output_file, fourcc, video_clip.fps, video_clip.frame_size)

    for frame in video_clip.next():
        out.write(frame)

    out.release()

    if verbose:
        print('Finished saving video')
