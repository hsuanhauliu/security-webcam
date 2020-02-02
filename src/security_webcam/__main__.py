"""
    A security camera on computer using webcam.
"""


from datetime import datetime
import os

import security_webcam as sw


def main():
    """ Main function """

    args = sw.parse_inputs()
    print(f"Settings >>> top fps: {args.fps}, recording length: {args.max_len} minutes")

    args.output = check_output_path(args.output)
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


def check_output_path(path):
    """ Check given output directory path """
    if not path:
        path = sw.create_vid_folder()

    if not os.path.isdir(path):
        raise ValueError('Not a directory')

    return path


if __name__ == "__main__":
    main()
