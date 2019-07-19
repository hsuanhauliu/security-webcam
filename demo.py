"""
    A security camera on computer using webcam.
"""


from datetime import datetime

import security_webcam as sw


def main():
    """ Main function """
    top_fps = 30
    buffer_length = 5
    verbose = True
    cap = sw.start_cam(fps=top_fps)

    while True:
        clip= sw.start_recording(cap, fps=top_fps, buffer_length=buffer_length, show_cam=False, verbose=verbose)
        sw.output_vid(str(datetime.today()) + '.mov', clip, verbose=verbose)

    sw.close_cam(cap)


if __name__ == '__main__':
    main()
