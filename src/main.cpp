#include <pybind11/pybind11.h>
#include <pybind11/complex.h>
#include <pybind11/stl.h>
#include "cppjieba/Jieba.hpp"
#include "cppjieba/TextRankExtractor.hpp"
#include <iostream>

namespace py = pybind11;

const std::string DICT_PATH = "cppjieba/dict/jieba.dict.utf8";
const std::string HMM_PATH = "cppjieba/dict/hmm_model.utf8";
const std::string IDF_PATH = "cppjieba/dict/idf.utf8";
const std::string STOP_WORD_PATH = "cppjieba/dict/stop_words.utf8";
using namespace std;

// PYBIND11_MAKE_OPAQUE(std::vector<cppjieba::Word>);

using Word = cppjieba::Word;

using WordVector = std::vector<string>;

using WordsTaged = vector<pair<string, string>>;

struct Tokenizer
{
    cppjieba::Jieba jieba;

  public:
    Tokenizer(const string &USER_DICT_PATH) : jieba(DICT_PATH, HMM_PATH, USER_DICT_PATH, IDF_PATH, STOP_WORD_PATH){};
    Tokenizer() : jieba(DICT_PATH, HMM_PATH, "", IDF_PATH, STOP_WORD_PATH){};

    WordVector cut_internal(const string &sentence, bool cut_all = false, bool HMM = true)
    {
        WordVector words;
        if (cut_all)
        {
            jieba.Cut(sentence, words, HMM);
        }
        else
        {
            jieba.CutAll(sentence, words);
        }
        return words;
    };

    vector<string> lcut(const string &sentence, bool cut_all = false, bool HMM = true)
    {
        vector<string> words;
        if (cut_all)
        {
            jieba.Cut(sentence, words, HMM);
        }
        else
        {
            jieba.CutAll(sentence, words);
        }

        return words;
    };

    vector<string> cut_all(const string &sentence)
    {
        vector<string> words;
        jieba.CutAll(sentence, words);
        return words;
    };

    vector<string> lcut_all(const string &sentence)
    {
        vector<string> words;
        jieba.CutAll(sentence, words);
        return words;
    };

    WordVector cut_for_search_internal(const string &sentence, bool HMM = true)
    {
        WordVector words;
        jieba.CutForSearch(sentence, words, HMM);
        return words;
    };

    vector<string> lcut_for_search(const string &sentence, bool HMM = true)
    {
        vector<string> words;
        jieba.CutForSearch(sentence, words, HMM);
        return words;
    };

    WordsTaged tag_internal(const string &sentence)
    {
        WordsTaged words;
        jieba.Tag(sentence, words);
        return words;
    };
};

namespace Jieba
{
struct KeyowrdExtractor
{
  private:
    Tokenizer *tokenizer;
    cppjieba::KeywordExtractor *keywordExtractor;

  public:
    KeyowrdExtractor(Tokenizer *t) : tokenizer(t)
    {
        initKeyowrdExtractor();
    };

    vector<string> extract_tags(const string &sentence, size_t topK = 20)
    {
        vector<string> keywords;
        keywordExtractor->Extract(sentence, keywords, topK);
        return keywords;
    };

    void initKeyowrdExtractor(const string &idfPath = IDF_PATH,
                              const string &stopWordPath = STOP_WORD_PATH)
    {
        keywordExtractor = new cppjieba::KeywordExtractor(tokenizer->jieba.GetDictTrie(), tokenizer->jieba.GetHMMModel(), idfPath, stopWordPath);
    };
};

struct TextRankExtractor
{
  private:
    Tokenizer *tokenizer;
    cppjieba::TextRankExtractor *textRankExtractor;

  public:
    TextRankExtractor(Tokenizer *t) : tokenizer(t)
    {
        initTextRankExtractor();
    };

    vector<string> textrank(const string &sentence, size_t topK = 20)
    {
        vector<string> keywords;
        textRankExtractor->Extract(sentence, keywords, topK);
        return keywords;
    };

    vector<pair<string, double>> textrank_with_weight(const string &sentence, size_t topK = 20)
    {
        vector<pair<string, double>> keywords;
        textRankExtractor->Extract(sentence, keywords, topK);
        return keywords;
    };

    void initTextRankExtractor(const string &stopWordPath = STOP_WORD_PATH)

    {
        textRankExtractor = new cppjieba::TextRankExtractor(tokenizer->jieba.GetDictTrie(), tokenizer->jieba.GetHMMModel(), stopWordPath);
    };
};

Tokenizer *dt;
KeyowrdExtractor *keywordExtractor;
TextRankExtractor *textRankExtractor;

void initialize()
{

    dt = new Tokenizer();
};

void init_check()
{
    if (!dt)
    {
        initialize();
    }
};

Tokenizer *get_default_tokenizer()
{
    init_check();
    return dt;
};

void init_check_textrank_extractor()
{
    if (!textRankExtractor)
    {
        textRankExtractor = new TextRankExtractor(get_default_tokenizer());
    }
};

TextRankExtractor *get_default_textrank_extractor()
{
    init_check_textrank_extractor();
    return textRankExtractor;
};

void init_check_keywordExtractor()
{
    if (!keywordExtractor)
    {
        keywordExtractor = new KeyowrdExtractor(get_default_tokenizer());
    }
};

KeyowrdExtractor *get_default_keywordExtractor()
{
    init_check_keywordExtractor();
    return keywordExtractor;
};

WordsTaged tag_internal(const string &sentence)
{
    init_check();
    return dt->tag_internal(sentence);
};

WordVector cut_internal(const string &sentence, bool cut_all = false, bool HMM = true)
{
    init_check();
    return dt->cut_internal(sentence, cut_all, HMM);
};

vector<string> lcut(const string &sentence, bool cut_all = false, bool HMM = true)
{
    init_check();
    return dt->lcut(sentence, cut_all, HMM);
};

vector<string> lcut_all(const string &sentence)
{
    init_check();
    return dt->lcut_all(sentence);
};

WordVector cut_for_search_internal(const string &sentence, bool HMM = true)
{
    init_check();
    return dt->cut_for_search_internal(sentence, HMM);
};

vector<string> cut_all(const string &sentence)
{
    init_check();
    return dt->cut_all(sentence);
};

vector<string> lcut_for_search(const string &sentence, bool HMM = true)
{
    init_check();
    return dt->lcut_for_search(sentence, HMM);
};

}; // namespace Jieba

PYBIND11_MODULE(libcppjieba, m)
{
    m.doc() = "python extension for cppjieba"; // optional module docstring

    m.def("cut_internal", &Jieba::cut_internal, py::arg("sentence"), py::arg("cut_all") = false, py::arg("HMM") = true);
    m.def("lcut", &Jieba::lcut, py::arg("sentence"), py::arg("cut_all") = false, py::arg("HMM") = true);
    m.def("cut_all", &Jieba::cut_all);
    m.def("lcut_all", &Jieba::lcut_all);
    m.def("lcut_for_search", &Jieba::lcut_for_search, py::arg("sentence"), py::arg("HMM") = true);
    m.def("cut_for_search_internal", &Jieba::cut_for_search_internal, py::arg("sentence"), py::arg("HMM") = true);
    m.def("tag_internal", &Jieba::tag_internal, py::arg("sentence"));
    m.def("initialize", &Jieba::initialize);
    m.def("get_default_keywordExtractor", &Jieba::get_default_keywordExtractor);
    m.def("get_default_textrank_extractor", &Jieba::get_default_textrank_extractor);

    py::class_<Jieba::KeyowrdExtractor>(m, "KeyowrdExtractor")
        .def(py::init<Tokenizer *>())
        .def("extract_tags", &Jieba::KeyowrdExtractor::extract_tags, py::arg("sentence"), py::arg("topK") = 20);

    py::class_<Jieba::TextRankExtractor>(m, "TextRankExtractor")
        .def(py::init<Tokenizer *>())
        .def("textrank_with_weight", &Jieba::TextRankExtractor::textrank_with_weight, py::arg("sentence"), py::arg("topK") = 20)
        .def("textrank", &Jieba::TextRankExtractor::textrank, py::arg("sentence"), py::arg("topK") = 20);

    py::class_<Tokenizer>(m, "Tokenizer")
        .def(py::init<>())
        .def(py::init<const string &>())
        .def("cut_internal", &Tokenizer::cut_internal, py::arg("sentence"), py::arg("cut_all") = false, py::arg("HMM") = true)
        .def("lcut", &Tokenizer::lcut, py::arg("sentence"), py::arg("cut_all") = false, py::arg("HMM") = true)
        .def("lcut_all", &Tokenizer::lcut_all)
        .def("cut_all", &Tokenizer::cut_all)
        .def("lcut_for_search", &Tokenizer::lcut_for_search, py::arg("sentence"), py::arg("HMM") = true)
        .def("cut_for_search_internal", &Tokenizer::cut_for_search_internal, py::arg("sentence"), py::arg("HMM") = true)
        .def("tag_internal", &Tokenizer::tag_internal, py::arg("sentence"));
}