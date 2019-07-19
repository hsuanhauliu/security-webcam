"""
    A security camera on computer using webcam.
"""


from argparse import ArgumentParser
from datetime import datetime

import security_webcam as sw


def main():
    """ Main function """
    verbose, top_fps, buffer_length = parse_inputs()
    cap = sw.start_cam(fps=top_fps)

    while True:
        clip = sw.start_recording(cap, fps=top_fps, buffer_length=buffer_length, show_cam=False, verbose=verbose)
        sw.output_vid(str(datetime.today()) + '.mov', clip, verbose=verbose)

    sw.close_cam(cap)


def parse_inputs():
    """ Helper method for parsing user input """
    parser = ArgumentParser(description='Input FPS and buffer length')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    parser.add_argument('fps', type=int, help='Enter top FPS of the recording')
    parser.add_argument('buffer_length', type=int, help='Enter buffer length of the recording')
    args = parser.parse_args()

    return args.verbose, args.fps, args.buffer_length


if __name__ == '__main__':
    main()
