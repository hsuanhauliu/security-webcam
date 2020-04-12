"""
    Argument Parser for the main script.
"""


from argparse import ArgumentParser
import json


def parse_inputs():
    """ Helper method for parsing user input """
    parser = ArgumentParser(description='Input FPS and buffer length')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Increase output verbosity.')
    parser.add_argument('-j', '--json', type=str,
                        help='Read settings from a json file.')
    parser.add_argument('-t', '--time', action='store_true', default=True,
                        help='Show time on footage if set true.')
    parser.add_argument('-s', '--show', action='store_true',
                        help='Show video steam while recording if set true.')
    parser.add_argument('-o', '--output', default='recordings/',
                        help='Specify output folder path. By defaul, the program will create a \
                            "recording" folder in the current directory.')
    parser.add_argument('--temp_buffer_len', type=int, default=5,
                        help='Video temporary buffer length (in seconds). Default is set to 5 seconds.')
    parser.add_argument('--vid_buffer_len', type=int, default=60,
                        help='Video footage buffer length (in seconds). Default is set to 60 seconds.')
    parser.add_argument('--fps', type=int, default=30,
                        help='Top FPS of the recording.')
    parser.add_argument('--max_len', type=int, default=5,
                        help='Maximum number of minutes for the recordings.')
    args = parser.parse_args()

    if args.json:
        args = ArgHandler(args.json)

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
