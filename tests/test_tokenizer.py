# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# pylint: disable=E1101
from spec import Spec
import sys
if sys.version_info[0] >=3:
    from pathlib import Path
else:
    from pathlib2 import Path

DICT_DIR = Path("../cppjieba/dict")
DICT = str(DICT_DIR / "jieba.dict.utf8")
USER_DICT = str(DICT_DIR / "user.dict.utf8")
STOP_WORD = str(DICT_DIR / "stop_words.utf8")

from cppjieba_py import Tokenizer


class TokenizerTest(Spec):
    @classmethod
    def setUpClass(cls):
        cls.dt = Tokenizer(DICT)

    class init:
        "__init__"

        def takes_arg1_as_main_dict_path(self):
            pass

        def takes_arg2_as_user_dict_path(self):
            Tokenizer(DICT, USER_DICT)

        def takes_arg3_as_stopword_path(self):
            Tokenizer(DICT, USER_DICT, STOP_WORD)

    class cut:

        def takes_arg1_as_sentence(self):
            self.dt.cut("")

        def takes_arg2_as_cut_all(self):
            self.dt.cut("", True)

        def takes_arg3_as_HMM(self):
            self.dt.cut("", True, True)

        def returns_iterator(self):
            from collections import Iterable, Sequence
            r = self.dt.cut("", True, True)
            iterable = isinstance(r, Iterable)
            sequence = isinstance(r, Sequence)
            assert iterable and not sequence

    class lcut:
        def takes_arg1_as_sentence(self):
            self.dt.cut("")

        def takes_arg2_as_cut_all(self):
            self.dt.cut("", True)

        def takes_arg3_as_HMM(self):
            self.dt.cut("", True, True)

        def returns_list(self):
            r = self.dt.lcut("", True, True)
            assert isinstance(r, list)

    class load_userdict:
        def accept_string_as_arg(self):
            self.dt.load_userdict("")

        def accept_list_as_arg(self):
            self.dt.load_userdict([])

        def accept_set_as_arg(self):
            self.dt.load_userdict(set([]))
