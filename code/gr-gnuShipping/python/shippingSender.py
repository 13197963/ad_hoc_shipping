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
import time
from bitstring import *
from addressControl import *
from shippingControl import *
from gnuradio import gr
from gnuradio import digital


class shippingSender(gr.basic_block):
    def __init__(self,msg_per,buffer=""):
        #the buffer only exists to capture a null char that was getting randomly generated
        gr.basic_block.__init__(self,
            name="shippingSender",
            in_sig=[],
            out_sig=[])
        self.message_port_register_out(pmt.intern('out'))
        self.msg_per = msg_per

        


       
        



    def post_message(self, msg_str):

        send_str = (lowFreqMessage(1,0,0,0,0,4, BitArray("0b10000000"), BitArray("0b10000000"), 0, 0, 0, 0, BROADCAST_ADDRESS, msg_str).bin)
        
        

        send_pmt = pmt.make_u8vector(len(send_str), ord(' '))
        for i in range(len(send_str)):
            pmt.u8vector_set(send_pmt, i, ord(send_str[i]))

        while 1:
            self.message_port_pub(pmt.intern('out'), pmt.cons(pmt.make_dict(), send_pmt))
            time.sleep(self.msg_per)




            