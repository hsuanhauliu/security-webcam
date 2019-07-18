""" Module for processing videos """


import cv2 as cv
from security_webcam.video_buffer import VideoBuffer


def start_webcam(fps=30, length=60, webcam_code=0, verbose=False):
    """ Start webcam capture """
    if verbose:
        print('Starting webcam capturing...')

    cap = cv.VideoCapture(webcam_code)
    cap.set(cv.CAP_PROP_FPS, fps)

    # read the first frame to get dimension of the frame
    _, frame = cap.read()
    height, width, _ = frame.shape
    vid_buffer = VideoBuffer((width, height), fps, length)
    while True:
        _, frame = cap.read()
        cv.imshow('Security Webcam', frame)

        key = cv.waitKey(1) & 0xFF
        vid_buffer.load(frame)
        if key == 27:
            break

    cap.release()
    return vid_buffer


def output_vid(output_file, video_clip, verbose=False):
    """ Save video as video file """
    if not isinstance(video_clip, VideoBuffer):
        raise TypeError('Video clip must be of type VideoBuffer')

    if video_clip.is_empty():
        raise ValueError('There are no frames to be saved')

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(output_file, fourcc, video_clip.fps, video_clip.frame_size)

    for frame in video_clip.read_frame():
        out.write(frame)

    out.release()

    if verbose:
        print('Finished saving video')
