1、缺失值



2、重复值
删除dataframe中的重复行：drop_duplicates(subset=["公司名","岗位名"],inplace=True)
#subset=["公司名","岗位名"]表示以列‘公司名’和'岗位名'为判断重复的标准
#inplace=True表示对原数据进行更改




3、异常值


4、数据变换
通过apply根据自定义函数对数据进行变换
df["岗位名"] = df["岗位名"].apply(lambda x:x.lower())，在不需要参数时，lambda非常方便

re.sub("数据专员","数据分析",x)：将字符串x中的“数据专员”替换成“数据分析”
re.match(r"Python", text)：在字符串text的开头匹配“Python”
re.search(r"programming", text)：在整个字符串text中匹配“programming”


5、数据结构变换




6、数据处理常用函数和属性
df["岗位名"].value_counts()：计算该列中各不同数值，以及出现的相应次数

count1 = text.str.count("Python", 10, 40)：#用于计算特定子字符串在原始字符串中出现的次数。该行为计算在字符串text中，索引10和40之间，"Python" 出现的次数.对于DataFrame或者Series对象，需要使用str属性。对一个标准的Python字符串对象，直接使用count()即可。

.shape：查看dataframe的形状

str.split(",", 3)：根据指定的符号","来拆分字符串，且最大的拆分次数为3.如不指定拆分的符号和次数，则默认为以空格为拆分符号，并且不限次数。对于DataFrame或者Series对象，需要使用str属性。对一个标准的Python字符串对象，直接使用split()即可。




7、常见操作
将列表转换成数组：数值的计算效率会更快；数组要求数据类型保持一致，利于数据分析；数组支持广播功能，可以在不同形状的数组间进行运算；数组可提供的数据处理更多。不过数组的内存开销会更大





