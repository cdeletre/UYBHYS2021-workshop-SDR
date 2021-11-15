#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Logitechex110 Dual Simu
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import qtgui

class logitechex110_dual_simu(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Logitechex110 Dual Simu")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Logitechex110 Dual Simu")
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

        self.settings = Qt.QSettings("GNU Radio", "logitechex110_dual_simu")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 240000
        self.decimation_nbfm = decimation_nbfm = 2
        self.decimation_fir = decimation_fir = 5
        self.baud_rate = baud_rate = 1200
        self.symbol_duration = symbol_duration = 1.0/baud_rate
        self.sps = sps = (samp_rate/baud_rate)/(decimation_nbfm*decimation_fir)
        self.output_rate = output_rate = int(samp_rate/(decimation_nbfm*decimation_fir))
        self.fs = fs = 27.120e6
        self.fc1 = fc1 = 27e6 + 143e3
        self.fc0 = fc0 = 27e6 + 93e3
        self.deviation = deviation = 2.5e3

        ##################################################
        # Blocks
        ##################################################
        self.wtab = Qt.QTabWidget()
        self.wtab_widget_0 = Qt.QWidget()
        self.wtab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.wtab_widget_0)
        self.wtab_grid_layout_0 = Qt.QGridLayout()
        self.wtab_layout_0.addLayout(self.wtab_grid_layout_0)
        self.wtab.addTab(self.wtab_widget_0, 'Waterfall')
        self.wtab_widget_1 = Qt.QWidget()
        self.wtab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.wtab_widget_1)
        self.wtab_grid_layout_1 = Qt.QGridLayout()
        self.wtab_layout_1.addLayout(self.wtab_grid_layout_1)
        self.wtab.addTab(self.wtab_widget_1, 'FFT')
        self.wtab_widget_2 = Qt.QWidget()
        self.wtab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.wtab_widget_2)
        self.wtab_grid_layout_2 = Qt.QGridLayout()
        self.wtab_layout_2.addLayout(self.wtab_grid_layout_2)
        self.wtab.addTab(self.wtab_widget_2, 'Demod channel 0')
        self.wtab_widget_3 = Qt.QWidget()
        self.wtab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.wtab_widget_3)
        self.wtab_grid_layout_3 = Qt.QGridLayout()
        self.wtab_layout_3.addLayout(self.wtab_grid_layout_3)
        self.wtab.addTab(self.wtab_widget_3, 'Demod channel 1')
        self.wtab_widget_4 = Qt.QWidget()
        self.wtab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.wtab_widget_4)
        self.wtab_grid_layout_4 = Qt.QGridLayout()
        self.wtab_layout_4.addLayout(self.wtab_grid_layout_4)
        self.wtab.addTab(self.wtab_widget_4, 'Logical channel 0')
        self.wtab_widget_5 = Qt.QWidget()
        self.wtab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.wtab_widget_5)
        self.wtab_grid_layout_5 = Qt.QGridLayout()
        self.wtab_layout_5.addLayout(self.wtab_grid_layout_5)
        self.wtab.addTab(self.wtab_widget_5, 'Logical channel 1')
        self.top_grid_layout.addWidget(self.wtab, 2, 1, 1, 3)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            512, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            fs, #fc
            samp_rate, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.2)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.wtab_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0_0_1_0 = qtgui.time_sink_f(
            1024, #size
            output_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_0.set_update_time(0.2)
        self.qtgui_time_sink_x_0_0_1_0.set_y_axis(0, 10)

        self.qtgui_time_sink_x_0_0_1_0.set_y_label('Channel 0', "")

        self.qtgui_time_sink_x_0_0_1_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 1.5, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_1_0.enable_stem_plot(False)

        self.qtgui_time_sink_x_0_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.wtab_layout_5.addWidget(self._qtgui_time_sink_x_0_0_1_0_win)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_f(
            1024, #size
            output_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.2)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(0, 10)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Channel 0', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 1.5, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_1.enable_stem_plot(False)

        self.qtgui_time_sink_x_0_0_1.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.wtab_layout_4.addWidget(self._qtgui_time_sink_x_0_0_1_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            1024, #size
            output_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.2)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-10, 10)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Channel 1', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.wtab_layout_3.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            output_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.2)
        self.qtgui_time_sink_x_0_0.set_y_axis(-10, 10)

        self.qtgui_time_sink_x_0_0.set_y_label('Channel 0', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 25, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.wtab_layout_2.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            512, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            fs, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.2)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        self.qtgui_freq_sink_x_0.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.wtab_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(decimation_fir, firdes.low_pass(1.0,samp_rate,deviation*1.5,deviation/2.0), fc1-fs, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decimation_fir, firdes.low_pass(1.0,samp_rate,deviation*1.5,deviation/2.0), fc0-fs, samp_rate)
        self.digital_correlate_access_code_bb_0_0 = digital.correlate_access_code_bb('0000000000111111111100000000001111111111', 1)
        self.digital_correlate_access_code_bb_0 = digital.correlate_access_code_bb('0000000000111111111100000000001111111111', 1)
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_char*1, '127.0.0.1', 9001, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, '127.0.0.1', 9000, 1472, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/user/gnuradio/logitechex110/gqrx_20180105_132052_27120000_240000_fc_password.raw', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_nbfm_rx_0_0 = analog.nbfm_rx(
        	audio_rate=output_rate,
        	quad_rate=int(samp_rate/decimation_fir),
        	tau=75e-6,
        	max_dev=deviation,
          )
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=output_rate,
        	quad_rate=int(samp_rate/decimation_fir),
        	tau=75e-6,
        	max_dev=deviation,
          )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.analog_nbfm_rx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_0_1, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0_1_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_correlate_access_code_bb_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.blocks_udp_sink_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_correlate_access_code_bb_0_0, 0))
        self.connect((self.digital_correlate_access_code_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_correlate_access_code_bb_0_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_nbfm_rx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "logitechex110_dual_simu")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_output_rate(int(self.samp_rate/(self.decimation_nbfm*self.decimation_fir)))
        self.set_sps((self.samp_rate/self.baud_rate)/(self.decimation_nbfm*self.decimation_fir))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1.0,self.samp_rate,self.deviation*1.5,self.deviation/2.0))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(firdes.low_pass(1.0,self.samp_rate,self.deviation*1.5,self.deviation/2.0))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.fs, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.fs, self.samp_rate)

    def get_decimation_nbfm(self):
        return self.decimation_nbfm

    def set_decimation_nbfm(self, decimation_nbfm):
        self.decimation_nbfm = decimation_nbfm
        self.set_output_rate(int(self.samp_rate/(self.decimation_nbfm*self.decimation_fir)))
        self.set_sps((self.samp_rate/self.baud_rate)/(self.decimation_nbfm*self.decimation_fir))

    def get_decimation_fir(self):
        return self.decimation_fir

    def set_decimation_fir(self, decimation_fir):
        self.decimation_fir = decimation_fir
        self.set_output_rate(int(self.samp_rate/(self.decimation_nbfm*self.decimation_fir)))
        self.set_sps((self.samp_rate/self.baud_rate)/(self.decimation_nbfm*self.decimation_fir))

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate
        self.set_sps((self.samp_rate/self.baud_rate)/(self.decimation_nbfm*self.decimation_fir))
        self.set_symbol_duration(1.0/self.baud_rate)

    def get_symbol_duration(self):
        return self.symbol_duration

    def set_symbol_duration(self, symbol_duration):
        self.symbol_duration = symbol_duration

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_output_rate(self):
        return self.output_rate

    def set_output_rate(self, output_rate):
        self.output_rate = output_rate
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.output_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.output_rate)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.output_rate)
        self.qtgui_time_sink_x_0_0_1_0.set_samp_rate(self.output_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.fc0-self.fs)
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.fc1-self.fs)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.fs, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.fs, self.samp_rate)

    def get_fc1(self):
        return self.fc1

    def set_fc1(self, fc1):
        self.fc1 = fc1
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.fc1-self.fs)

    def get_fc0(self):
        return self.fc0

    def set_fc0(self, fc0):
        self.fc0 = fc0
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.fc0-self.fs)

    def get_deviation(self):
        return self.deviation

    def set_deviation(self, deviation):
        self.deviation = deviation
        self.analog_nbfm_rx_0.set_max_deviation(self.deviation)
        self.analog_nbfm_rx_0_0.set_max_deviation(self.deviation)
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1.0,self.samp_rate,self.deviation*1.5,self.deviation/2.0))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(firdes.low_pass(1.0,self.samp_rate,self.deviation*1.5,self.deviation/2.0))



def main(top_block_cls=logitechex110_dual_simu, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
