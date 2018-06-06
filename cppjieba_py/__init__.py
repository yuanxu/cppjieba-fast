from libcppjieba import cut_for_search_internal,tag_internal,cut_internal
from libcppjieba import Tokenizer
from libcppjieba import lcut,lcut_for_search,initialize

def cut(*args,**kvargs):
    it = cut_internal(*args,**kvargs)
    return iter(it)

def cut_for_search(*args,**kvargs):
    it = cut_for_search_internal(*args,**kvargs)
    return iter(it)

def c_cut(ins,*args,**kvargs):
    it = ins.cut_internal(*args,**kvargs)
    return iter(it)

def c_cut_for_search(ins,*args,**kvargs):
    it = ins.cut_for_search_internal(*args,**kvargs)
    return iter(it)

setattr(Tokenizer,"cut",c_cut)
setattr(Tokenizer,"cut_for_search",c_cut_for_search)

__version__ = '0.0.3'
