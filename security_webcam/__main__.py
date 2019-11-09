"""
    A security camera on computer using webcam.
"""


from argparse import ArgumentParser
from datetime import datetime
import os

import security_webcam as sw


def main():
    """ Main function """
    verbose, show_cam, show_time, output_path, top_fps, buffer_len = parse_inputs()
    print(f"Settings >>> top fps: {top_fps}, buffer length: {buffer_len} seconds")

    if not os.path.isdir(output_path):
        raise ValueError('Not a directory')

    cc = sw.CameraControl()
    cc.start_cam(fps=top_fps)
    input(">>> Press Enter to start recording...")
    while True:
        print("Recording...") if verbose else None
        clips, frame_size, real_fps = cc.start_recording(fps=top_fps,
                                                         buffer_length=buffer_len,
                                                         show_cam=show_cam,
                                                         verbose=verbose,
                                                         show_time=show_time)

        filename = os.path.join(output_path, str(datetime.today()) + '.mov')
        sw.output_vid(filename, clips, real_fps, frame_size)

    cc.close_cam()


def parse_inputs():
    """ Helper method for parsing user input """
    parser = ArgumentParser(description='Input FPS and buffer length')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    parser.add_argument('-t', '--time', action='store_true', help='place timestamp on recording')
    parser.add_argument('-s', '--show', action='store_true', help='show cam while recording')
    parser.add_argument('-o', '--output', default='./', help='specify output folder')
    parser.add_argument('fps', type=int, help='Enter top FPS of the recording')
    parser.add_argument('buffer_length', type=int, help='Enter buffer length of the recording')
    args = parser.parse_args()

    return args.verbose, args.show, args.time, args.output, args.fps, args.buffer_length


if __name__ == "__main__":
    main()
