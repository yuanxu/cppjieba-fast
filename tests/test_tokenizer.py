# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# pylint: disable=E1101
from spec import Spec
import sys
if sys.version_info[0] >= 3:
    from pathlib import Path
else:
    from pathlib2 import Path

DICT_DIR = Path("../cppjieba/libcppjieba/dict")
DICT = str(DICT_DIR / "jieba.dict.utf8")
USER_DICT = str(DICT_DIR / "user.dict.utf8")
STOP_WORD = str(DICT_DIR / "stop_words.utf8")

from cppjieba import Tokenizer


class TokenizerTest(Spec):
    @classmethod
    def setUpClass(cls):
        cls.dt = Tokenizer(DICT)
        cls.dt.add_word("区块链", 10, "nz")

    class init_0:
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

    class add_word:
        def takes_arg1_as_word(self):
            self.dt.add_word("区块链")

        def takes_arg2_as_freq(self):
            self.dt.add_word("区块链", 10)

        def takes_arg3_as_tag(self):
            pass

    class find:
        def takes_arg1_as_word(self):
            self.dt.find("区块链")

        def can_find_added_word(self):
            r = self.dt.find("区块链")
            assert r == True

    class lookup_tag:
        def takes_arg1_as_word(self):
            self.dt.lookup_tag("区块链")

        def can_find_added_word(self):
            self.dt.add_word("区块链", 10, "nz") # because of random test order
            # from nose.plugins.skip import Skip
            r = self.dt.lookup_tag("区块链")
            # try:
            assert r == "nz"
            # except AssertionError:
            #     raise Skip()
