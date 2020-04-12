"""
    Util module.
"""

from datetime import datetime
from pathlib import Path

import cv2 as cv


EVENT = {
    'start': 'Program started',
    'recording': 'Start recording',
    'save': 'Saving footage',
    'exit': 'Program exited'
}


def create_vid_dir(dir_path="recordings/"):
    """ Create a folder to storing recorded videos """
    Path(dir_path).mkdir(exist_ok=True)


def output_vid(output_file, vid_buffers, fps, frame_size):
    """ Save video as video file """
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    out = cv.VideoWriter(output_file, fourcc, fps, frame_size)

    for buf in vid_buffers:
        for frame in buf.next():
            out.write(frame)

    out.release()


def log_event(event_name, filename="logs.txt"):
    """ Log important events """
    with open(filename, "a") as rfile:
        curr_time = str(datetime.today())
        rfile.write(f"{curr_time}: {EVENT[event_name]}\n")
