from cppjiebapy import Tokenizer ,cut,cut_for_search,lcut,lcut_for_search
import cppjiebapy.posseg as pseg

def main():

    jieba_instance = Tokenizer()
    seg_list = jieba_instance.cut("我来到北京清华大学")
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式


    seg_list = jieba_instance.lcut("他来到了网易杭研大厦")  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba_instance.cut_for_search(
        "小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))
    
    print(lcut("我来到北京清华大学"))
    print(list(cut("我来到北京清华大学")))

    print(lcut_for_search("我来到北京清华大学"))
    print(list(cut_for_search("我来到北京清华大学")))

    print(pseg.lcut("我来到北京清华大学"))
    print(list(pseg.cut("我来到北京清华大学")))

if __name__ == '__main__':
    main()
