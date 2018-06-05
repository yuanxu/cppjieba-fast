#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "cppjieba/Jieba.hpp"
#include <iostream>

namespace py = pybind11;

const std::string DICT_PATH = "cppjieba/dict/jieba.dict.utf8";
const std::string HMM_PATH = "cppjieba/dict/hmm_model.utf8";
const std::string IDF_PATH = "cppjieba/dict/idf.utf8";
const std::string STOP_WORD_PATH = "cppjieba/dict/stop_words.utf8";
using namespace std;

struct Tokenizer
{
    cppjieba::Jieba jieba;

  public:
    Tokenizer(const string &USER_DICT_PATH ) : jieba(DICT_PATH, HMM_PATH, USER_DICT_PATH, IDF_PATH, STOP_WORD_PATH){};
    Tokenizer() : jieba(DICT_PATH, HMM_PATH, "", IDF_PATH, STOP_WORD_PATH){};

    vector<string> cut(const string &sentence, bool hmm = true)
    {
        vector<string> words;
        jieba.Cut(sentence, words, hmm);
        return words;
    }

    vector<string> cut_all(const string &sentence)
    {
        vector<string> words;
        jieba.CutAll(sentence, words);
        return words;
    }

    vector<string> cut_for_search(const string &sentence, bool hmm = true)
    {
        vector<string> words;
        jieba.CutForSearch(sentence, words, hmm);
        return words;
    }

};


namespace Jieba
{
     Tokenizer* dt;

     void initlize(){
        dt = new Tokenizer();
    };

     void init_check(){
        if(!dt){
            initlize();
        }
    };

     vector<string> cut(const string &sentence, bool hmm = true)
    {
        init_check();
        return dt->cut(sentence,hmm);
    };

     vector<string> cut_all(const string &sentence)
    {
        init_check();
        return dt->cut_all(sentence);
    };

     vector<string> cut_for_search(const string &sentence, bool hmm = true)
    {
        init_check();
        return dt->cut_for_search(sentence,hmm);
    };

};

PYBIND11_MODULE(cppjieba_py, m)
{
    m.doc() = "python extension for cppjieba"; // optional module docstring
    m.def("cut", &Jieba::cut,py::arg("sentence"),py::arg("hmm") = true);
    m.def("cut_all", &Jieba::cut_all);
    m.def("cut_for_search", &Jieba::cut_for_search,py::arg("sentence"),py::arg("hmm") = true);
    py::class_<Tokenizer>(m, "Tokenizer")
        .def(py::init<>())
        .def(py::init<const string &>())
        .def("cut", &Tokenizer::cut,py::arg("sentence"),py::arg("hmm") = true)
        .def("cut_all", &Tokenizer::cut_all)
        .def("cut_for_search", &Tokenizer::cut_for_search,py::arg("sentence"),py::arg("hmm") = true);
}