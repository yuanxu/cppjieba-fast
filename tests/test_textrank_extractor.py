# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# pylint: disable=E1101
from spec import Spec
import sys
if sys.version_info[0] >=3:
    from pathlib import Path
else:
    from pathlib2 import Path

DICT_DIR = Path("../cppjieba/libcppjieba/dict")
DICT = str(DICT_DIR / "jieba.dict.utf8")
IDF = str(DICT_DIR / "idf.utf8")
STOP_WORD = str(DICT_DIR / "stop_words.utf8")

from cppjieba import Tokenizer
from cppjieba.analyse import TextRankExtractor


class TextRankExtractorTest(Spec):
    @classmethod
    def setUpClass(cls):
        cls.dt = Tokenizer(DICT)
        cls.sentence = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
        cls.extractor = TextRankExtractor(cls.dt)

    class init:
        "__init__"

        def takes_arg1_as_tokenizer(self):
            pass

        def takes_arg2_as_STOP_WORD_PATH(self):
            TextRankExtractor(self.dt, STOP_WORD)

    class textrank_no_weight:

        def takes_arg1_as_sentence(self):
            self.extractor.textrank_no_weight(self.sentence)

        def takes_arg2_as_topK(self):
            self.extractor.textrank_no_weight(self.sentence, topK=5)

        def returns_list(self):
            r = self.extractor.textrank_no_weight(self.sentence, topK=5)
            assert isinstance(r, list)
