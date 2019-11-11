"""
    A security camera on computer using webcam.

    Usage:
        python3 demo.py
"""


from datetime import datetime

import security_webcam as sw


def main():
    """ Main function """

    cc = sw.CameraControl(fps=30, temp_buffer_len=5, vid_buffer_len=10,
                          max_len=5, show_cam=False, show_time=True)
    cc.start_cam()
    input("Press Enter to start recording...")
    while True:
        print("Recording...")
        clips, frame_size, real_fps = cc.start_recording(verbose=True)

        print("Saving footage...")
        filename = str(datetime.today()) + '.mov'
        sw.output_vid(filename, clips, real_fps, frame_size)

    sw.close_cam()


if __name__ == '__main__':
    main()
