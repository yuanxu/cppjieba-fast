#encoding=utf-8
import sys
import os
import random
import datetime

#wget https://raw.githubusercontent.com/yanyiwu/practice/master/nodejs/nodejieba/performance/weicheng.utf8 -O performace_test/weicheng.utf8

if __name__ == "__main__":
    if sys.argv[1] == "cppjiebapy":# 0:00:03.861202
        import cppjiebapy as jieba
    elif sys.argv[1] == "jieba": # 0:01:24.703040
        import jieba
    lines = []
    weicheng = os.path.join(os.path.dirname(__file__),"weicheng.utf8")
    for line in open(weicheng):
        lines.append(line.strip());


    result = [""] * 10;
    result[random.randint(0, 9)] = '/'.join(jieba.cut("南京长江大桥"))
    starttime = datetime.datetime.now()
    
    for i in range(50):
        for line in lines:
            r = '/'.join(jieba.cut(line))
            # print(r)
            result[random.randint(0, 9)] = r
            #result[random.randint(0, 9)] = jieba.cut(line)
    endtime = datetime.datetime.now()
    print (endtime - starttime)