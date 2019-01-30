# Installation guide


1. cd to gr-gnuShipping
2. `mkdir build`
3. `cd build`
4. `cmake ../`
5. `make`
6. `sudo make install`
7. `sudo ldconfig`

The blocks should now be available in Gnuradio Companion under **gnuShipping**.

It is necessary to keep the *addressControl.py* and *shippingControl.py* files with the automatically generated *gnuShipping.py* file.

Installation of the [BitArray](https://github.com/ilanschnell/bitarray) library may be necessary if it is not already installed.