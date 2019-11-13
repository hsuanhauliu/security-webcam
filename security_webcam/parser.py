"""
    Argument Parser for the main script.
"""


from argparse import ArgumentParser


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
    parser.add_argument('-o', '--output', default='./',
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

    return args
