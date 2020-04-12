"""
    Buffer classes for storing incoming video frames.
"""


class VideoBuffer:
    """ Video Buffer class """

    def __init__(self, fps=30, length=60):
        self._fps = fps
        self._buffer = [0] * (fps * length)
        self._curr_i = 0

    @property
    def num_frames(self):
        """ Number of frames in the buffer """
        return self._curr_i

    @property
    def fps(self):
        """ Frame per second of the video buffer """
        return self._fps

    @fps.setter
    def fps(self, fps):
        self._fps = fps

    def load(self, new_frame):
        """ Load new frame to video buffer """
        if self.is_full():
            raise AttributeError("Buffer is full")

        self._buffer[self._curr_i] = new_frame
        self._curr_i += 1

    def is_empty(self):
        """ Check if the buffer is empty """
        return not self._num_frames

    def is_full(self):
        """ Check if the buffer is full """
        return len(self._buffer) == self._curr_i

    def next(self):
        """ Generator for reading frame from buffer """
        for frame in self._buffer[: self._curr_i]:
            yield frame


class TemporaryBuffer(VideoBuffer):
    """ Fixed-size video buffer """

    def __init__(self, fps=30, length=5):
        super().__init__(fps=fps)
        self._num_frames = 0
        self._length = length
        self._limit = fps * length
        self._buffer = [None] * self._limit

    @property
    def num_frames(self):
        """ Number of frames in the buffer """
        return self._limit if self.is_full() else self._curr_i

    @property
    def length(self):
        """ Length of the video buffer in seconds """
        return self._length

    def load(self, new_frame):
        """ Load new frame to video buffer """
        self._buffer[self._curr_i] = new_frame
        self._curr_i = (self._curr_i + 1) % self._limit

    def is_full(self):
        """ Check if the buffer is full """
        return self._buffer[self._curr_i] is not None

    def next(self):
        """ Generator for reading frame from buffer """
        if self.is_full():
            for frame in self._buffer[self._curr_i :]:
                yield frame

            for frame in self._buffer[: self._curr_i]:
                yield frame
            return

        for frame in self._buffer[: self._curr_i]:
            yield frame
