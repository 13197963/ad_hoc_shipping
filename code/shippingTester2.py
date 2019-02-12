#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: shippingUDPTester2
# Author: Daniel Osmond
# Generated: Tue Feb 12 13:43:58 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gnuShipping
import sys
from gnuradio import qtgui


class shippingTester2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "shippingUDPTester2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("shippingUDPTester2")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "shippingTester2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10000
        self.msg_str = msg_str = 'BBB111111'

        self.QPSK = QPSK = digital.constellation_calcdist(([1+1j, -1+1j, 1-1j, -1-1j]), ([0, 1, 3, 2]), 4, 1).base()


        ##################################################
        # Blocks
        ##################################################
        self._msg_str_tool_bar = Qt.QToolBar(self)
        self._msg_str_tool_bar.addWidget(Qt.QLabel("msg_str"+": "))
        self._msg_str_line_edit = Qt.QLineEdit(str(self.msg_str))
        self._msg_str_tool_bar.addWidget(self._msg_str_line_edit)
        self._msg_str_line_edit.returnPressed.connect(
        	lambda: self.set_msg_str(str(str(self._msg_str_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._msg_str_tool_bar)
        self.gnuShipping_shippingSender_0 = gnuShipping.shippingSender(5)
        self.gnuShipping_shippingReciever_0 = gnuShipping.shippingReciever(msg_str)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(False)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(True)
        self.blocks_socket_pdu_1 = blocks.socket_pdu("UDP_CLIENT", 'localhost', '10000', 10000, False)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_1, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.gnuShipping_shippingReciever_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_socket_pdu_1, 'pdus'))
        self.msg_connect((self.gnuShipping_shippingSender_0, 'out'), (self.digital_crc32_async_bb_1, 'in'))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "shippingTester2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_msg_str(self):
        return self.msg_str

    def set_msg_str(self, msg_str):
        self.msg_str = msg_str
        Qt.QMetaObject.invokeMethod(self._msg_str_line_edit, "setText", Qt.Q_ARG("QString", str(self.msg_str)))
        self.gnuShipping_shippingSender_0.post_message(self.msg_str)

    def get_QPSK(self):
        return self.QPSK

    def set_QPSK(self, QPSK):
        self.QPSK = QPSK


def main(top_block_cls=shippingTester2, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
