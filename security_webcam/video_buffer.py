class VideoBuffer:
    """ Video Buffer class """

    def __init__(self, frame_size, fps=30, length=60):
        self.frame_size = frame_size
        self._fps = fps
        self._length = length
        self._limit = fps * length
        self._buffer = []
        self.num_frames = 0
        self.recording = False


    @property
    def fps(self):
        return self._fps


    @fps.setter
    def fps(self, new_fps):
        self._fps = new_fps
        self._limit = new_fps * self._length


    @property
    def length(self):
        return self._length


    @length.setter
    def length(self, new_length):
        self._length = new_length
        self._limit = new_length * self._fps


    def load(self, new_frame):
        """ Load new frame to video buffer """
        if self.recording or self.num_frames < self._limit:
            self._buffer.append(new_frame)
            self.num_frames += 1
            return

        # discard the oldest frame
        self._buffer.pop(0)
        self._buffer.append(new_frame)


    def is_empty(self):
        """ Check if the buffer is empty """
        return self.num_frames == 0


    def next(self):
        """ Generator for reading frame from buffer """
        for frame in self._buffer:
            yield frame
