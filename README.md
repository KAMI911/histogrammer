# histogrammer

Tune histogramm of dark pictures

## Fork me on Github

https://github.com/KAMI911/histogrammer

## Donation

If you find this useful, please consider a donation:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RLQZ58B26XSLA)

numpy - https://pypi.python.org/pypi/numpy/

OpenCV - https://pypi.python.org/pypi/opencv/

## Installation

### Linux (Debian/Ubuntu/Linux Mint)

**Install Python 2.7, Numpy, OpenCV

```
sudo apt-get install python2.7 python-numpy python-opencv
```

### Windows

**Install Python 2.7**

We prefer 64 bit AMD64 version.

https://www.python.org/downloads/

**Install pip**

Installation manual: https://pip.pypa.io/en/latest/installing.html

Download: https://bootstrap.pypa.io/get-pip.py

```
python get-pip.py
```

**Install Numpy**

Download:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

One of these files:

numpy-1.9.2+mkl-cp27-none-win_amd64.whl for 64 bit version

http://www.lfd.uci.edu/~gohlke/pythonlibs/3i673h27/numpy-1.9.2+mkl-cp27-none-win_amd64.whl

numpy-1.9.2+mkl-cp27-none-win32.whl for 32 bit version

http://www.lfd.uci.edu/~gohlke/pythonlibs/3i673h27/numpy-1.9.2+mkl-cp27-none-win32.whl

And install it:

```
C:\Python27\Scripts\pip.exe install "numpy-1.9.2+mkl-cp27-none-win_amd64.whl"
```

**Install OpenCV**

Download:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

One of these files:

opencv_python-2.4.12-cp27-none-win_amd64.whl for 64 bit version

http://www.lfd.uci.edu/~gohlke/pythonlibs/wkvprmqy/opencv_python-2.4.12-cp27-none-win_amd64.whl

opencv_python-2.4.12-cp27-none-win32.whl for 32 bit version

http://www.lfd.uci.edu/~gohlke/pythonlibs/wkvprmqy/opencv_python-2.4.12-cp27-none-win32.whl

And install it:

```
C:\Python27\Scripts\pip.exe install "opencv_python-2.4.12-cp27-none-win_amd64.whl"
```

## Usage

### One LAS file

Correct pictures:

```
histogrammer.py -i /home/hopp/directory/ -o /home/hopp/anotherdir/ -input_format jpg
```

