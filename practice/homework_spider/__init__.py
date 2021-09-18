import json
from collections import Counter

import jieba

jieba.setLogLevel(jieba.logging.INFO)

most = open('jd_good_comments.csv', 'r',encoding='utf-8').read()
most_words = [x for x in jieba.cut(most) if len(x) >= 3]  # 将全文分割，并将大于三个字的词语放入列表
c = Counter(most_words).most_common(10)  # 取最多的10组
row=json.dumps(c, ensure_ascii=False)
with open("result.txt", "w") as f:
    f.write(row)
