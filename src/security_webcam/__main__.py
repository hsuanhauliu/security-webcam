"""
    A security camera on computer using webcam.
"""


from datetime import datetime
from multiprocessing import Process, cpu_count
import os

import security_webcam as sw


def main():
    """ Main Loop """
    args = sw.parse_inputs()
    print(f"Settings >>> top fps: {args.fps}, recording length: {args.max_len} minutes")
    sw.utils.log_event('start')

    sw.utils.create_vid_dir(args.output)
    cc = sw.CameraControl(fps=args.fps, temp_buffer_len=args.temp_buffer_len,
                          vid_buffer_len=args.vid_buffer_len, max_len=args.max_len,
                          show_cam=args.show, show_time=args.time)
    cc.start_cam()
    input(">>> Press Enter to start recording...")
    while True:
        if args.verbose: print("Recording...") 
        sw.utils.log_event('recording')
        bufs, frame_size, real_fps = cc.start_recording(verbose=args.verbose)

        if args.verbose: print("Saving footage...") 
        sw.utils.log_event('save')
        filename = os.path.join(args.output, str(datetime.today()) + '.mov')
        p = Process(target=sw.utils.output_vid, args=(filename, bufs, real_fps, frame_size))
        p.start()

    sw.utils.log_event('exit')
    cc.close_cam()


if __name__ == "__main__":
    main()
