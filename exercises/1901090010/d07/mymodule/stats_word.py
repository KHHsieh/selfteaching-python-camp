import re
#(1)定义一个名为 stats_text_en 的函数
def stats_text_en(text):
    #(2)函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        return '请输入字符串'

    #(3)统计参数中每个英文单词出现的次数
    # 1.替换掉所有的符号
    word_str = text.replace(','," ").replace('.'," ").replace('!'," ").replace('*'," ").replace('--'," ")
    # 2.按照空格将所有的单词分割开

    word_str = re.sub(r'[^A-Za-z]',' ',word_str)
    word_list = word_str.split()


    # 3.对单词进行去重操作，作为字典的key
    word_one = set(word_list)
    # 4.构建一个词频字典
    dict = {}
    for word in word_one:
        dict[word] = word_list.count(word)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list



#(1)定义一个名为 stats_text_cn 的函数
def stats_text_cn(text):
    #(2)函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        return '请输入字符串'

    # 1.替换掉所有的符号
    d = text.replace(',','').replace('-',' ').replace('.','').replace(':','').replace('《','').replace('’','').replace(';','').replace('"','').replace('!','').replace('?','').replace('》',' ').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','').replace("'",'')
    # 2.将上文中的字符串，用正则运算剔除所有英文字母单词，数字
    d = re.sub("[A-Za-z0-9]", "", d)
    #print(d)

    # 3.将字符串中的汉字去重，作为字典的key  
    #d_list = list(d)
    #print(d_list)
    #d_index = set(d_list)
    # 4.构造词频字典
    dict = {}
    for i in d:
        dict[i] = d.count(i)
    # 5.对之前的词频字典按照value值进行排序
    d = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d 





def stats_text(text):
        '''
        
        合并 英文词频 和 中文词频 的结果
        
        '''
        return stats_text_en(text)+stats_text_cn(text)
        

if __name__ == "__main__":
    # 测试统计英文单词词频的函数
    text = '''
    How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two highmountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do ourbest to level these two mountains. We shall open a road that leads
to Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered his wife. “How on earth do you suppose you can level Mount Taixin
and Mount Wanwu? Moreover, where will all the earth and rubble go?”“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and remove the earth. They transported the earth and rubble to the Sea
of Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will neverunderstand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, mygrandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will notgrow any taler. We shall level them one day!” he declared with
confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugongand his crew were, they were struck with fear and reported the
incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens orderedtwo mighty gods to carry the mountains away.
'''
    # 测试不是字符串的情况
    test_num = 1
    # 测试正常情况
    array = stats_text_en(text)
    print(array)

 # 测试统计中文词频的函数
    text = '''
    愚公移山
太行，王屋二山的北面住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，擋住去路，使他
和家人往來極為不便。
一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，你們認為怎
樣？」
大家都異口同聲贊成，只有他的妻子表示懷疑，並說：「你連開鑿一個山丘的力量都沒有，怎
可能剷平太行、王屋二山呢？況且，鑿出的土石又丟到哪裏去呢？」
大家都熱烈地說：「把土石丟進渤海裏。」
於是愚公就和兒孫，一起開挖二山把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地过來幫忙。
寒來暑往，他們要一年才能往返渤海一次。
住在黄河河畔的智叟，看见他們這樣辛苦，取笑愚公說：「你不是很愚蠢嗎？你已经把年紀
了，就是用盡你的氣力，也不能挖去山的一⻆呢？」
愚公歎息道：「你有這樣的成见，是不會明白的。你比那寡婦的小兒还還不如呢！就算我死
了，還有我的兒子、我的孫子、我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有
一天，我們會把它們剷平。」
智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大力神揹走二山。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two highmountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do ourbest to level these two mountains. We shall open a road that leads
to Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered his wife. “How on earth do you suppose you can level Mount Taixin
and Mount Wanwu? Moreover, where will all the earth and rubble go?”“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and remove the earth. They transported the earth and rubble to the Sea
of Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will neverunderstand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, mygrandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will notgrow any taler. We shall level them one day!” he declared with
confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugongand his crew were, they were struck with fear and reported the
incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens orderedtwo mighty gods to carry the mountains away.
'''
    # 对统计中文词频函数进行测试
    array = stats_text_cn(text)

    print(array)

