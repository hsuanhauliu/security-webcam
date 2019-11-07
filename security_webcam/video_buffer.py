class VideoBuffer:
    """ Video Buffer class """

    def __init__(self, frame_size, fps=30, length=60):
        self.frame_size = frame_size
        self.num_frames = 0
        self._fps = fps
        self._length = length
        self._limit = fps * length
        self._buffer = [None] * self._limit
        self.recording = False  # lock for the buffer
        self.curr_i = 0


    @property
    def fps(self):
        """ Frame per second of the video buffer """
        return self._fps

    @fps.setter
    def fps(self, fps):
        self._fps = fps
        self._limit = fps * self.length


    @property
    def length(self):
        """ Length of the video buffer in seconds """
        return self._length


    def load(self, new_frame):
        """ Load new frame to video buffer """
        self._buffer[self.curr_i] = new_frame
        self.curr_i = (self.curr_i + 1) % self._limit
        self.num_frames = min(self.num_frames + 1, self._limit)


    def is_empty(self):
        """ Check if the buffer is empty """
        return self.num_frames == 0


    def is_full(self):
        """ Check if the buffer is full """
        return self._buffer[self.curr_i] is not None


    def next(self):
        """ Generator for reading frame from buffer """
        if self.is_full():
            for frame in self._buffer[self.curr_i:]:
                yield frame

            for frame in self._buffer[:self.curr_i]:
                yield frame
            return

        for frame in self._buffer[:self.curr_i]:
            yield frame
