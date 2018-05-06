__author__ = 'kszalai'

try:
    import traceback
    import textwrap
    import glob
    import os
    import logging
    import datetime
    import numpy as np
    import cv2
    import multiprocessing
    import pyexiv2
    from datetime import date
except ImportError as err:
    traceback.print_exc()
    exit(128)


def ProcessImageHistogram(paramterers):
    # Get process realted informations
    current = multiprocessing.current_process()
    proc_name = current.name
    # We are starting
    logging.info('[%s] Starting ...' % (proc_name))
    # Parameters
    input_file = paramterers[0]
    output_file = paramterers[1]
    contrast_limit = paramterers[2]
    # Opening file
    logging.info('[%s] Opening: %s file ...' % (proc_name, input_file))
    img = cv2.imread(input_file, cv2.IMREAD_COLOR)
    # We got problem with the opened file
    if img is None:
        logging.error('[%s] Error opening: %s file!' % (proc_name, input_file))
        return -1
    else:
        # Color image should be splitted to BGR color channels
        logging.info('[%s] Split BGR image color channels of: %s file ...' % (proc_name, input_file))
        b, g, r = cv2.split(img)
        logging.info('[%s] Processing file: %s ... Contrast limit is: %s.' % (proc_name, input_file, contrast_limit))
        # create a CLAHE object - Contrast Limited Adaptive Histogram Equalization an apply on every channel
        clahe = cv2.createCLAHE(clipLimit=contrast_limit, tileGridSize=(8, 8))
        b = clahe.apply(b)
        g = clahe.apply(g)
        r = clahe.apply(r)
        # Merge image color channels
        logging.info('[%s] Merge BGR image color channels of: %s file ...' % (proc_name, input_file))
        cl1 = cv2.merge((b, g, r))
        logging.info('[%s] File has been processed: %s.' % (proc_name, input_file))
        # Write image, file type decided based on its extension
        cv2.imwrite(output_file, cl1)
        logging.info('[%s] File has been written: %s.' % (proc_name, output_file))
        # Copy EXIF data from original image
        try:
            source_image = pyexiv2.metadata.ImageMetadata(input_file)
            source_image.read()
            destination_image = pyexiv2.metadata.ImageMetadata(output_file)
            destination_image.read()
            source_image.copy(destination_image, exif=True, iptc=True, xmp=True, comment=True)
            destination_image.write(preserve_timestamps=True    )
        except Exception as err:
            logging.warning('[{}] Error occured during EXIF manipulation ({})'.format(proc_name, err))
            raise(err)
        else:
            logging.info('[%s] File EXIF has set: %s.' % (proc_name, output_file))
    return 0


class HistogrammerWorkflow:
    def __init__(self, inputfiles, outputfiles, inputformat, outputformat, cores, recursive, image_contrast_limit):
        self.inputfiles = inputfiles
        self.outputfiles = outputfiles
        self.inputformat = inputformat
        self.outputformat = outputformat
        self.cores = cores
        self.recursive = recursive
        self.image_contrast_limit = image_contrast_limit
        self.inputpath = os.path.normpath(self.inputfiles)
        self.outputpath = os.path.normpath(self.outputfiles)
        self.inputisdir = False

    def process(self):
        doing = []
        results = []
        # User specified a directory
        if os.path.isdir(self.inputfiles):
            self.inputisdir = True
            files_list = []
            if self.recursive:
                for root, subdirs, files in os.walk(self.inputfiles):
                    temp_files_list = glob.glob(os.path.join(root, '*.' + self.inputformat))
                    if temp_files_list:
                        files_list = files_list + temp_files_list
            else:
                files_list = glob.glob(os.path.join(self.inputfiles, '*.' + self.inputformat.lower()))
                files_list += glob.glob(os.path.join(self.inputfiles, '*.' + self.inputformat.upper()))
            for workfile in files_list:
                logging.info('Adding %s to the queue.' % (workfile))
                image_input_file = workfile
                filename = os.path.relpath(workfile, self.inputpath)
                filename_name = os.path.splitext(filename)[0]
                image_output_file = os.path.join(self.outputpath, filename_name + '.' + self.outputformat)
                if not os.path.exists(os.path.dirname(image_output_file)):
                    os.makedirs(os.path.dirname(image_output_file))
                doing.append([image_input_file, image_output_file, self.image_contrast_limit])
        # User specified a file
        elif os.path.isfile(self.inputfiles):
            self.inputisdir = False
            workfile = self.inputfiles
            if os.path.basename(self.outputfiles) is not "":
                image_output_file = os.path.join(self.outputpath, os.path.basename(workfile))
                doing.append([workfile, image_output_file, self.image_contrast_limit])
            else:
                image_output_file = os.path.join(self.outputpath,
                                                 os.path.basename(workfile.replace('.' + self.inputformat,
                                                                                   '') + '_opt.' + self.outputformat))
                doing.append([workfile, image_output_file, self.image_contrast_limit])
            logging.info('Adding {} to the queue.'.format(workfile))
        else:
            # Not a file, not a dir
            logging.error('Cannot found input file: {}!'.format(self.inputfiles))
            exit(1)

        # If we got one file, start only one process
        if self.inputisdir is False:
            self.cores = 1

        if self.cores != 1:
            pool = multiprocessing.Pool(processes=self.cores)
            results = pool.map_async(ProcessImageHistogram, doing)
            pool.close()
            pool.join()
        else:
            for d in doing:
                ProcessImageHistogram(d)
