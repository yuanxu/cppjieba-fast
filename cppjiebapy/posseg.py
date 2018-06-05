from cppjieba_py import tag_internal

def cut(sentence):
       it = tag_internal(sentence)
       for word,tag in it:
           yield (word,tag)

def lcut(sentence):
    return list(tag_internal(sentence))