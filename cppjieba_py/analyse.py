from libcppjieba import get_default_keywordExtractor as _get_default_keywordExtractor,\
    get_default_textrank_extractor as _get_default_textrank_extractor

keywordExtractor = _get_default_keywordExtractor()
textrankExtractor = _get_default_textrank_extractor()

def extract_tags(sentence,topK = 20):
    return keywordExtractor.extract_tags(sentence,topK)

def textrank(sentence, topK=20, withWeight=False):
    if not withWeight:
        return textrankExtractor.textrank(sentence,topK)
    else:
        return textrankExtractor.textrank_with_weight(sentence,topK)