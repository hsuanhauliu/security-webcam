"""
    Argument Parser for the main script.
"""


from argparse import ArgumentParser
import json


def parse_inputs():
    """ Helper method for parsing user input """

    parser = ArgumentParser(description='Input FPS and buffer length')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')
    parser.add_argument('-j', '--json', action='store_true',
                        help='use the config.json file for configurations')
    parser.add_argument('-t', '--time', action='store_true', default=True,
                        help='place time on footage')
    parser.add_argument('-s', '--show', action='store_true',
                        help='show video steam while recording')
    parser.add_argument('-o', '--output', default='recordings/',
                        help='specify output folder path')
    parser.add_argument('--temp_buffer_len', type=int, default=5,
                        help='video temporary buffer length (in seconds)')
    parser.add_argument('--vid_buffer_len', type=int, default=60,
                        help='video footage buffer length (in seconds)')
    parser.add_argument('--fps', type=int, default=30,
                        help='Top FPS of the recording')
    parser.add_argument('--max_len', type=int, default=5,
                        help='maximum number of minutes for the recordings')
    args = parser.parse_args()

    if args.json:
        filename = "config.json"
        args = ArgHandler(filename)

    return args


class ArgHandler:
    """ Argument handler class """

    def __init__(self, filename):
        self.dict = self._load_config(filename)
        self.verbose = self.dict["verbose"]
        self.time = self.dict["time"]
        self.show = self.dict["show_vid"]
        self.output = self.dict["output_path"]
        self.temp_buffer_len = self.dict["temp_buffer_len"]
        self.vid_buffer_len = self.dict["vid_buffer_len"]
        self.fps = self.dict["fps"]
        self.max_len = self.dict["max_len"]


    @staticmethod
    def _load_config(filename):
        """ Load the JSON configuration file """

        content = None
        with open(filename, "r") as rfile:
            content = json.load(rfile)

        return content
