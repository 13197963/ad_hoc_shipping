#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 Daniel Osmond.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
import string
import numpy
import pmt
from bitstring import *
from addressControl import *
from shippingControl import *
from gnuradio import gr
from gnuradio import digital


class shippingReciever(gr.basic_block):

    def __init__(self, my_address):
        gr.basic_block.__init__(self,
            name="shippingReciever",
            in_sig=[],
            out_sig=[])
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
        self.my_address = my_address

    def handle_msg(self, msg_pmt):
        meta = pmt.to_python(pmt.car(msg_pmt))
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print "[ERROR] Recieved invalid message type.\n"
            return
        msg_str = "".join([chr(x) for x in pmt.u8vector_elements(msg)])
        
        parseMessage(msg_str, deviceList, self.my_address)

