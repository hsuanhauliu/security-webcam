"""
    A security camera on computer using webcam.

    Usage:
        python3 demo.py
"""


from datetime import datetime

import security_webcam as sw


def main():
    """ Main function """

    cc = sw.CameraControl()
    cc.start_cam(fps=30)
    input("Press Enter to start recording...")
    while True:
        print("Recording...")
        clips, frame_size, real_fps = cc.start_recording(fps=30,
                                                         temp_buffer_len=5,
                                                         vid_buffer_len=10,
                                                         max_len=5,
                                                         show_cam=False,
                                                         verbose=True,
                                                         show_time=True)
        print("Saving footage...")
        filename = str(datetime.today()) + '.mov'
        sw.output_vid(filename, clips, real_fps, frame_size)

    sw.close_cam()


if __name__ == '__main__':
    main()
