# histogrammer

Tune histogramm of dark pictures with multi-process paralel processing and EXIF support

## Fork me on Github

https://github.com/KAMI911/histogrammer

## Donation

If you find this useful, please consider a donation:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RLQZ58B26XSLA)

numpy - https://pypi.python.org/pypi/numpy/

OpenCV - https://pypi.python.org/pypi/opencv/

py3exiv2 - https://pypi.org/project/py3exiv2/

## Installation

### Linux (Debian/Ubuntu/Linux Mint)

**Install Python 3.5 (3.0 or newer), Numpy, OpenCV**

```
sudo apt-get install python3.3 python-numpy python-opencv python-all-dev libexiv2-dev libboost-python-dev g++
```

**Install required modules**

```
pip install -r requirements.txt
```

### Windows (using rather new Python 3.x)

**Install Python 3.5**

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

numpy-1.14.3+mkl-cp35-cp35m-win_amd64.whl for 64 bit version

https://download.lfd.uci.edu/pythonlibs/t5yhk4lc/numpy-1.14.3+mkl-cp35-cp35m-win_amd64.whl

numpy-1.14.3+mkl-cp35-cp35m-win32.whl for 32 bit version

https://download.lfd.uci.edu/pythonlibs/t5yhk4lc/numpy-1.14.3+mkl-cp35-cp35m-win32.whl

And install it:

```
C:\Python27\Scripts\pip.exe install "numpy-1.14.3+mkl-cp35-cp35m-win_amd64.whl"
```

**Install OpenCV**

Download:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

One of these files:

opencv_python-3.4.1-cp35-cp35m-win_amd64.whl for 64 bit version

https://download.lfd.uci.edu/pythonlibs/t5yhk4lc/opencv_python-3.4.1-cp35-cp35m-win_amd64.whl

opencv_python-3.4.1-cp35-cp35m-win32.whl for 32 bit version

https://download.lfd.uci.edu/pythonlibs/t5yhk4lc/opencv_python-3.4.1-cp35-cp35m-win32.whl

And install it:

```
C:\Python27\Scripts\pip.exe install "opencv_python-3.4.1-cp35-cp35m-win_amd64.whl"
```

### Windows (using rather old Python 2.7)

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

### One folder with picture files

Correct jpg pictures using 8 CPU cores:

```
histogrammer.py -i /home/hopp/directory/ -o /home/hopp/anotherdir/ -input_format jpg -cores 8
```
