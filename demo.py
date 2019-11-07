"""
    A security camera on computer using webcam.

    Usage:
        python3 demo.py
"""


from datetime import datetime

import security_webcam as sw


def main():
    """ Main function """
    fps, buffer_length, verbose, show_cam = 30, 5, True, False

    cap = sw.start_cam(fps=fps)
    while True:
        frame_size, clips = sw.start_recording(cap, fps=fps, buffer_length=buffer_length,
                                               show_cam=show_cam, verbose=verbose)
        filename = str(datetime.today()) + '.mov'
        sw.output_vid(filename, clips, fps, frame_size, verbose=verbose)

    sw.close_cam(cap)


if __name__ == '__main__':
    main()
