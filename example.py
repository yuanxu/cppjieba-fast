from cppjieba_py import Tokenizer ,cut

def main():

    jieba_instance = Tokenizer()
    seg_list = jieba_instance.cut("我来到北京清华大学")
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式


    seg_list = jieba_instance.cut("他来到了网易杭研大厦")  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba_instance.cut_for_search(
        "小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))
    
    print(cut("我来到北京清华大学"))

if __name__ == '__main__':
    main()
