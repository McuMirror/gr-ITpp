/* -*- c++ -*- */

#define ITPP_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "ITpp_swig_doc.i"

%{
#include "ITpp/Hamming_Encoder.h"
#include "ITpp/Hamming_Decoder.h"
%}

%include "ITpp/Hamming_Encoder.h"
GR_SWIG_BLOCK_MAGIC2(ITpp, Hamming_Encoder);
%include "ITpp/Hamming_Decoder.h"
GR_SWIG_BLOCK_MAGIC2(ITpp, Hamming_Decoder);
