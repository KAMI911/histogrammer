__author__ = 'kszalai'

try:
    import traceback
    import argparse
    import textwrap
    import glob
    import logging
    import datetime
    from libs import Logging, Timing, HistogrammerCommandline, HistogrammerWorkflow
    from datetime import date
except Exception as err:
    traceback.print_exc()
    exit(128)

script_path = __file__
__version__ = '20151123'

header = textwrap.dedent('''Histogrammer''')


def main():
    timer = Timing.Timing()
    logfilename = 'histogrammer_' + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + '.log'
    Logging.SetLogging(logfilename)

    logging.info(header)
    logging.info('Version: %s' % (__version__))

    histogrammer_commandline = HistogrammerCommandline.HistogrammerCommandline()
    histogrammer_commandline.parse()

    histogrammer_workflow = HistogrammerWorkflow.HistogrammerWorkflow(histogrammer_commandline.get_input(),
                                                                      histogrammer_commandline.get_output(),
                                                                      histogrammer_commandline.get_input_format(),
                                                                      histogrammer_commandline.get_output_format(),
                                                                      histogrammer_commandline.get_cores(),
                                                                      histogrammer_commandline.get_recursive(),
                                                                      histogrammer_commandline.get_image_contrast_limit())
    histogrammer_workflow.process()
    logging.info('Total duration of process: %s. Finished, exiting and go home ...' % timer.end())


if __name__ == '__main__':
    main()