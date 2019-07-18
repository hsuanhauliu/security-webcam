class VideoBuffer:
    """ Video Buffer class """

    def __init__(self, frame_size, fps=30, length=60):
        self.frame_size = frame_size
        self.fps = fps
        self.length = length
        self._limit = fps * length
        self._buffer = []
        self.num_frames = 0


    def load(self, new_frame):
        """ Load new frame to video buffer """
        if self.num_frames < self._limit:
            self._buffer.append(new_frame)
            self.num_frames += 1
            return

        # discard the oldest frame
        self._buffer.pop(0)
        self._buffer.append(new_frame)


    def is_empty(self):
        """ Check if the buffer is empty """
        return self.num_frames == 0


    def read_frame(self):
        """ Generator for reading frame from buffer """
        for frame in self._buffer:
            yield frame
