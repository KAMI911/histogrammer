__author__ = 'kszalai'

try:
    import traceback
    import argparse
    import textwrap
except Exception as err:
    traceback.print_exc()
    exit(128)


class HistogrammerCommandline:
    def __init__(self):
        # predefinied paths
        self.parser = argparse.ArgumentParser(prog="histogrammer",
                                              formatter_class=argparse.RawDescriptionHelpFormatter,
                                              description='',
                                              epilog=textwrap.dedent('''
        example:
            '''))
        # reguired parameters
        self.parser.add_argument('-i', type=str, dest='input', required=True,
                                 help='required:  input file or folder')
        self.parser.add_argument('-o', type=str, dest='output', required=True,
                                 help='required:  output file or folder (d:\pictures\processed)')

        # optional parameters
        self.parser.add_argument('-r', dest='recursive', required=False,
                                 help='optional:  recursive directory processing', action='store_true')
        self.parser.add_argument('-cores', type=int, dest='cores', required=False, default=2,
                                 help='optional:  cores (default=2)')
        self.parser.add_argument('-input_format', type=str, dest='input_format', required=False,
                                 choices=['pgm', 'jpg', 'png'],
                                 help='optional:  input format (default=pgm)')
        self.parser.add_argument('-output_format', type=str, dest='output_format', required=False,
                                 choices=['png', 'jpg', 'pgm'],
                                 help='optional:  output format (default=png)')
        self.parser.add_argument('-image_contrast_limit', type=float, dest='image_contrast_limit', required=False,
                                 default=3,
                                 help='optional:  cores (default=3)')
        self.parser.add_argument('-v', dest='verbose', required=False,
                                 help='optional:  verbose toggle (-v=on, nothing=off)', action='store_true')
        self.parser.add_argument('-version', action='version', version=self.parser.prog)

    def parse(self):
        self.args = self.parser.parse_args()

        if not self.args.input_format:
            self.args.input_format = 'pgm'

        if not self.args.output_format:
            self.args.output_format = 'jpg'

        ##defaults
        if self.args.verbose:
            self.args.verbose = ' -v'
        else:
            self.args.verbose = ''

        if self.args.cores == None:
            self.args.cores = 1

    # ---------PUBLIC METHODS--------------------
    def get_output(self):
        return self.args.output

    def get_input(self):
        return self.args.input

    def get_input_format(self):
        return self.args.input_format

    def get_output_format(self):
        return self.args.output_format

    def get_image_contrast_limit(self):
        return self.args.image_contrast_limit

    def get_recursive(self):
        return self.args.recursive

    def get_verbose(self):
        return self.args.verbose

    def get_cores(self):
        return self.args.cores
