0、基础知识
#创建Dataframe
data = {'m':[[1,2], [2,3],[3,4]]}
data = pd.DataFrame(data)

#创建Series
data = [[1,2], [2,3],[3,4]]
data3 = pd.Series(data,name='m')


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
df['平均值'] = df[['a', 'b']].mean(axis=1)：添加一列，该列为'a'列和'b'列的平均值。df[['a', 'b']]表示同时选择'a'列和'b'列。

df["岗位名"].value_counts()：计算该列中各不同数值，以及出现的相应次数.

count1 = text.str.count("Python", 10, 40)：#用于计算特定子字符串在原始字符串中出现的次数。该行为计算在字符串text中，索引10和40之间，"Python" 出现的次数.对于DataFrame或者Series对象，需要使用str属性。对一个标准的Python字符串对象，直接使用count()即可。
#target_job = ['算法', '开发', '分析', '工程师', '数据', '运营', '运维']
#job_han = [job_info1["岗位名"].str.count(i) for i in target_job]
#job_han = np.array(job_han).sum(axis=0)>0
#job_info1 = job_info1[job_han]
#print(job_info1.shape)

.shape：查看dataframe的形状

contains_result = df['text'].str.contains('an', case=True, na=False)：表示判断text列中，数据是否包含"an"，case表示是否区分大小写。na=False表示如果数据值为空值，则为不包含。

str.split(",", 3)：根据指定的符号","来拆分字符串，且最大的拆分次数为3.如不指定拆分的符号和次数，则默认为以空格为拆分符号，并且不限次数。对于DataFrame或者Series对象，需要使用str属性。对一个标准的Python字符串对象，直接使用split()即可。

zip(gs.index.tolist(), gs.values.tolist())：将两个列表一一配对，连接在一起，变成一个个连接好的元祖。zip()函数产生的是一个迭代器对象，需通过for循环将元素输出。

job_info.loc[job_info["行业"].apply(lambda x:len(x)<6),"行业"] = np.nan：通过loc[]以及布尔值数组，筛选出满足条件的行。

job_info["行业"] = job_info["行业"].str[2:-2].str.split("/").str[0]：根据特定的符号对数据进行分割，并只取分割后的第一个元素

index1 = job_info1['工资'].str[-1].isin(['月','年']):判断“工资列”数值的最后一个字符是否属于['月','年']中

try...except语句中，可以同时内嵌多个平行的if...elif语句：
#定义标准化的函数
def get_max_min(x):
    try:
        if x[-3] == '万':
            z = [float(i)*10000 for i in re.findall("[0-9]+\.?[0-9]*",x)]
        elif x[-3] == '千':
            z = [float(i)*1000 for i in re.findall("[0-9]+\.?[0-9]*",x)]
        if x[-1] == '年':
            z = [m/12 for m in z]
        return z
    except:
        return x







7、常见操作
将列表转换成数组：数值的计算效率会更快；数组要求数据类型保持一致，利于数据分析；数组支持广播功能，可以在不同形状的数组间进行运算；数组可提供的数据处理更多。不过数组的内存开销会更大。

将数值数据，根据数值大小，转换成分类数据：结合if语句使用。




8、正则表达式："[0-9]+\.?[0-9]*"，用来匹配整数或小数。
普通字符：普通字符（例如字母、数字、标点符号等）通常表示它们自己。例如，正则表达式中的字母 "a" 匹配字符串中的 "a" 字符。
元字符：元字符是正则表达式中具有特殊含义的字符，例如：
.：匹配除换行符外的任何字符。
*：匹配前一个字符的零次或多次重复。
+：匹配前一个字符的一次或多次重复。
?：匹配前一个字符的零次或一次重复。
|：用于分隔多个选择，例如 A|B 匹配 "A" 或 "B"。
字符类：字符类用方括号 [] 括起来，表示匹配其中的任何一个字符。例如，[aeiou] 匹配任何一个元音字母。
范围：字符类中可以使用短划线 - 来表示范围。例如，[0-9] 匹配任何一个数字。
反向字符类：在字符类前加上 ^ 表示匹配字符类中未列出的字符。例如，[^0-9] 匹配任何一个非数字字符。
转义字符：使用反斜杠 \ 来转义具有特殊含义的字符。例如，\. 匹配句点字符，而不是任何字符。
位置锚定：位置锚定字符用于指定匹配发生的位置：
^：匹配字符串的开头。
$：匹配字符串的结尾。
\b：匹配单词边界。
\B：匹配非单词边界。
分组：使用圆括号 () 创建分组，用于将一组字符视为单个单元，并对其应用重复操作符。







