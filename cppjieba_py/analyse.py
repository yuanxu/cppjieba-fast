from libcppjieba import get_default_keywordExtractor as _get_default_keywordExtractor,\
    get_default_textrank_extractor as _get_default_textrank_extractor

from libcppjieba import KeywordExtractor ,\
      TextRankExtractor as TextRank

TFIDF = KeywordExtractor

def _textrank(self,sentence, topK=20, withWeight=False):
    if not withWeight:
        return self.textrank_no_weight(sentence,topK)
    else:
        return self.textrank_with_weight(sentence,topK)

setattr(TextRank,"textrank",_textrank)

keywordExtractor = _get_default_keywordExtractor()
textrankExtractor = _get_default_textrank_extractor()

extract_tags = keywordExtractor.extract_tags
textrank = textrankExtractor.textrank

