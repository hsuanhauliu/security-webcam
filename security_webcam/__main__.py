"""
    A security camera on computer using webcam.
"""


from argparse import ArgumentParser
from datetime import datetime
import os

import security_webcam as sw


def main():
    """ Main function """
    args = parse_inputs()
    print(f"Settings >>> top fps: {args.fps}, recording length: {args.max_len} minutes")

    if not os.path.isdir(args.output):
        raise ValueError('Not a directory')

    cc = sw.CameraControl(fps=args.fps, temp_buffer_len=args.temp_buffer_len,
                          vid_buffer_len=args.vid_buffer_len, max_len=args.max_len,
                          show_cam=args.show, show_time=args.time)
    cc.start_cam()
    input(">>> Press Enter to start recording...")
    while True:
        print("Recording...") if args.verbose else None
        bufs, frame_size, real_fps = cc.start_recording(verbose=args.verbose)

        print("Saving footage...") if args.verbose else None
        filename = os.path.join(args.output, str(datetime.today()) + '.mov')
        sw.output_vid(filename, bufs, real_fps, frame_size)

    cc.close_cam()


def parse_inputs():
    """ Helper method for parsing user input """
    parser = ArgumentParser(description='Input FPS and buffer length')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')
    parser.add_argument('-t', '--time', action='store_true', default=True,
                        help='place time on footage')
    parser.add_argument('-s', '--show', action='store_true',
                        help='show video steam while recording')
    parser.add_argument('-o', '--output', default='./',
                        help='specify output folder path')
    parser.add_argument('--temp_buffer_len', type=int, default=5,
                        help='video temporary buffer length (in seconds)')
    parser.add_argument('--vid_buffer_len', type=int, default=60,
                        help='video footage buffer length (in seconds)')
    parser.add_argument('--fps', type=int, default=30,
                        help='Top FPS of the recording')
    parser.add_argument('--max_len', type=int, default=5,
                        help='maximum number of minutes for the recordings')
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
