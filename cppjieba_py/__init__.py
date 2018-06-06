from libcppjieba import cut_for_search_internal as _cut_for_search_internal,\
    tag_internal as _tag_internal,\
    cut_internal as _cut_internal
from libcppjieba import Tokenizer
from libcppjieba import lcut,lcut_for_search,initialize

def _iter_wraps_doc(origin):
    return origin.__doc__.replace(origin.__name__,"Iterator wraps %s" % origin.__name__,1)  
    
def cut(*args,**kvargs):
    it = _cut_internal(*args,**kvargs)
    return iter(it)

cut.__doc__ = _iter_wraps_doc(_cut_internal)

def cut_for_search(*args,**kvargs):
    it = _cut_for_search_internal(*args,**kvargs)
    return iter(it)
    
cut_for_search.__doc__ = _iter_wraps_doc(_cut_for_search_internal)

def _c_cut(ins,*args,**kvargs):
    it = ins.cut_internal(*args,**kvargs)
    return iter(it)

def _c_cut_for_search(ins,*args,**kvargs):
    it = ins.cut_for_search_internal(*args,**kvargs)
    return iter(it)

_c_cut.__doc__ = _iter_wraps_doc(Tokenizer.cut_internal)

_c_cut_for_search.__doc__ = _iter_wraps_doc(Tokenizer.cut_for_search_internal)

setattr(Tokenizer,"cut",_c_cut)
setattr(Tokenizer,"cut_for_search",_c_cut_for_search)

from libcppjieba import get_default_analyse

analyse = get_default_analyse()