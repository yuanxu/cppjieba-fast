from spec import Spec
from pathlib import Path

DICT_DIR = Path("../cppjieba/dict")
DICT = str(DICT_DIR / "jieba.dict.utf8")
USER_DICT = str(DICT_DIR / "user.dict.utf8")
STOP_WORD = str(DICT_DIR / "stop_words.utf8")

import cppjieba_py as jieba

class JiebaTest(Spec):

    class cut:

        def takes_arg1_as_sentence(self):
            jieba.cut("")

        def takes_arg2_as_cut_all(self):
            jieba.cut("", True)

        def takes_arg3_as_HMM(self):
            jieba.cut("", True, True)

        def returns_iterator(self):
            from collections import Iterable, Sequence
            r = jieba.cut("", True, True)
            iterable = isinstance(r, Iterable)
            sequence = isinstance(r, Sequence)
            assert iterable and not sequence

    class lcut:
        def takes_arg1_as_sentence(self):
            jieba.cut("")

        def takes_arg2_as_cut_all(self):
            jieba.cut("", True)

        def takes_arg3_as_HMM(self):
            jieba.cut("", True, True)

        def returns_list(self):
            r = jieba.lcut("", True, True)
            assert isinstance(r, list)

    class load_userdict:
        def accept_string_as_arg(self):
            jieba.load_userdict("")

        def accept_list_as_arg(self):
            jieba.load_userdict([])

        def accept_set_as_arg(self):
            jieba.load_userdict(set([]))
