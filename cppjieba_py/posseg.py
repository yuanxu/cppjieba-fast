from libcppjieba import tag_internal

def cut(sentence):
       it = tag_internal(sentence)
       return iter(it)

def lcut(sentence):
    return tag_internal(sentence)