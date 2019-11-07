"""
    A security camera on computer using webcam.
"""


from argparse import ArgumentParser
from datetime import datetime
import os

from security_webcam.processing import *


def main():
    """ Main function """
    verbose, show_cam, output_path, top_fps, buffer_length = parse_inputs()

    if not os.path.isdir(output_path):
        raise ValueError('Not a directory')

    cap = start_cam(fps=top_fps)
    while True:
        # return clips only when the whole footage is captured
        frame_size, clips = start_recording(cap, fps=top_fps, buffer_length=buffer_length,
                                            show_cam=show_cam, verbose=verbose)

        # combine all clips into one video and store it in the current directory
        file_path = os.path.join(output_path, str(datetime.today()) + '.mov')
        output_vid(file_path, clips, top_fps, frame_size, verbose=verbose)

    close_cam(cap)


def parse_inputs():
    """ Helper method for parsing user input """
    parser = ArgumentParser(description='Input FPS and buffer length')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    parser.add_argument('-s', '--show', action='store_true', help='show cam while recording')
    parser.add_argument('-o', '--output', default='./', help='specify output folder')
    parser.add_argument('fps', type=int, help='Enter top FPS of the recording')
    parser.add_argument('buffer_length', type=int, help='Enter buffer length of the recording')
    args = parser.parse_args()

    return args.verbose, args.show, args.output, args.fps, args.buffer_length


if __name__ == "__main__":
    main()
