"""
    Util module.
"""


import cv2 as cv


def output_vid(output_file, vid_buffers, fps, frame_size):
    """ Save video as video file """
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    out = cv.VideoWriter(output_file, fourcc, fps, frame_size)

    for buf in vid_buffers:
        for frame in buf.next():
            out.write(frame)

    out.release()
