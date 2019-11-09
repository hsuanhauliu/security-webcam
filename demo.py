"""
    A security camera on computer using webcam.

    Usage:
        python3 demo.py
"""


from datetime import datetime

import security_webcam as sw


def main():
    """ Main function """
    fps, buffer_length, verbose, show_cam, show_time = 30, 5, True, True, True
    print(f"Settings >>>> top fps: {fps}, buffer length: {buffer_length} seconds")

    cc = sw.CameraControl()
    cc.start_cam(fps=fps)
    input("Press Enter to start recording...")
    while True:
        print("Recording...") if verbose else None
        clips, frame_size, real_fps = cc.start_recording(fps=fps,
                                                         buffer_length=buffer_length,
                                                         show_cam=show_cam,
                                                         verbose=verbose,
                                                         show_time=show_time)
        filename = str(datetime.today()) + '.mov'
        sw.output_vid(filename, clips, real_fps, frame_size)

    sw.close_cam()


if __name__ == '__main__':
    main()
