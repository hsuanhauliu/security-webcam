"""
    A security camera on computer using webcam.
"""


from argparse import ArgumentParser
from datetime import datetime
import os

import security_webcam as sw


def main():
    """ Main function """
    verbose, show_cam, show_time, output_path, top_fps, temp_buffer_len, vid_buffer_len, max_len = parse_inputs()
    print(f"Settings >>> top fps: {top_fps}, recording length: {max_len} minutes")

    if not os.path.isdir(output_path):
        raise ValueError('Not a directory')

    cc = sw.CameraControl()
    cc.start_cam(fps=top_fps)
    input(">>> Press Enter to start recording...")
    while True:
        print("Recording...") if verbose else None
        clips, frame_size, real_fps = cc.start_recording(fps=top_fps,
                                                         temp_buffer_len=temp_buffer_len,
                                                         vid_buffer_len=vid_buffer_len,
                                                         max_len=max_len,
                                                         show_cam=show_cam,
                                                         verbose=verbose,
                                                         show_time=show_time)

        print("Saving footage...") if verbose else None
        filename = os.path.join(output_path, str(datetime.today()) + '.mov')
        sw.output_vid(filename, clips, real_fps, frame_size)

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

    return args.verbose, args.show, args.time, args.output, args.fps, args.temp_buffer_len, args.vid_buffer_len, args.max_len


if __name__ == "__main__":
    main()
