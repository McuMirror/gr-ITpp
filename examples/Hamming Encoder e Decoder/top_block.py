#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Oct 31 21:54:58 2018
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import ITpp
import math
import numpy
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.const_type = const_type = 0
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = {0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[const_type] + " - Change const_type for different constellation types!"
        self.samp_rate_0 = samp_rate_0 = 100e3
        self.samp_rate = samp_rate = 32000
        self.const = const = (digital.constellation_bpsk(), digital.constellation_qpsk(), digital.constellation_8psk())
        self.EbN0 = EbN0 = 0

        ##################################################
        # Blocks
        ##################################################
        self._EbN0_range = Range(-10, 20, 0.1, 0, 200)
        self._EbN0_win = RangeWidget(self._EbN0_range, self.set_EbN0, 'Eb / N0 (dB)', "counter_slider", float)
        self.top_layout.addWidget(self._EbN0_win)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Constellation Type'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("")

        labels = ['BER (Com Hamming)', '', '', '', '',
                  '', '', '', '', '']
        units = ['x10^-6', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1e6, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(True)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(const[const_type].base())
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((const[const_type].points()), 1)
        self.blocks_throttle = blocks.throttle(gr.sizeof_char*1, samp_rate*10,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=int(1e7),
        	bits_per_symbol=const[const_type].bits_per_symbol(),
        )
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, const[const_type].arity(), 10000000)), True)
        self.analog_noise_source_x = analog.noise_source_c(analog.GR_GAUSSIAN, 1.0 / math.sqrt(const[const_type].bits_per_symbol() * 10**(float(EbN0-2.43)/10)), 42)
        self.ITpp_Hamming_Encoder_0 = ITpp.Hamming_Encoder(3)
        self.ITpp_Hamming_Decoder_0 = ITpp.Hamming_Decoder(3)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.ITpp_Hamming_Decoder_0, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_noise_source_x, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x, 0), (self.blocks_throttle, 0))
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.blocks_throttle, 0), (self.ITpp_Hamming_Encoder_0, 0))
        self.connect((self.blocks_throttle, 0), (self.blks2_error_rate_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.ITpp_Hamming_Decoder_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_const_type(self):
        return self.const_type

    def set_const_type(self, const_type):
        self.const_type = const_type
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter({0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[self.const_type] + " - Change const_type for different constellation types!"))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.const[self.const_type].points()))
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(self.const[self.const_type].bits_per_symbol() * 10**(float(self.EbN0-2.43)/10)))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle.set_sample_rate(self.samp_rate*10)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.const[self.const_type].points()))
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(self.const[self.const_type].bits_per_symbol() * 10**(float(self.EbN0-2.43)/10)))

    def get_EbN0(self):
        return self.EbN0

    def set_EbN0(self, EbN0):
        self.EbN0 = EbN0
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(self.const[self.const_type].bits_per_symbol() * 10**(float(self.EbN0-2.43)/10)))


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
