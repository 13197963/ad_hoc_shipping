#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Shipping Passing App
# Author: Daniel Osmond
# Generated: Wed Jan 30 11:51:00 2019
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gnuShipping
import sys
import tutorial
from gnuradio import qtgui


class audioTxRx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Shipping Passing App")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Shipping Passing App")
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

        self.settings = Qt.QSettings("GNU Radio", "audioTxRx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.msg_str = msg_str = "CSQ305438"

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
        self.tutorial_my_qpsk_demod_cb_0 = tutorial.my_qpsk_demod_cb(True)
        self.gnuShipping_shippingSender_0 = gnuShipping.shippingSender(5)
        self.gnuShipping_shippingReciever_0 = gnuShipping.shippingReciever(msg_str)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(False)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(True)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((QPSK.points()), 1)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, "tsb_tag")
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(2, 8, "tsb_tag", True, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 2, "tsb_tag", False, gr.GR_LSB_FIRST)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, "tsb_tag")
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(False, False)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_complex_to_interleaved_short_0 = blocks.complex_to_interleaved_short(False)
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.gnuShipping_shippingReciever_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.gnuShipping_shippingSender_0, 'out'), (self.digital_crc32_async_bb_1, 'in'))
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_complex_to_interleaved_short_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.tutorial_my_qpsk_demod_cb_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.audio_sink_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_complex_to_interleaved_short_0, 0))
        self.connect((self.tutorial_my_qpsk_demod_cb_0, 0), (self.blocks_repack_bits_bb_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "audioTxRx")
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


def main(top_block_cls=audioTxRx, options=None):

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
