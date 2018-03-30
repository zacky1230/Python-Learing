import math
import operator
import copy

# 基本数据类型
print(id(3))  # 内建函数id()可以查看每个对象的内存地址，即身份
print(id(3.0))

# 了解身份后 了解类型
print(type(3))
print(type(3.0))

# 变量
x = 5
print(x)

# 四则运算
print(2 + 5)
print(5 - 2)
print(5 * 2)
print(5 / 2 + 1)

# 整数除以整数
print(7 / 3)
print(type(print(7 / 3)))

# 浮点数除以整数
print(9.0 / 4)

# 浮点数精确问题可以用 decimal 模块去解决

# 余数
print(5 % 2)
print(6 % 4)

# 四舍五入
print(round(1.234567))
print(round(1.234567, 2))
print(round(1.234567, 3))

# 使用math模块
print(math.pi)

# 使用dir查看模块功能
print(dir(math))

# 使用help查看具体方法使用
print(help(math.pow))

# 字符串
a = 123
b = "free"
print(repr(a) + b)

# input()方法,python3 中没有 raw_input()函数
# content = input("please input something you want:")
# print(content)

# 索引和切片
lang = "study python"
print(lang[0])
print("study python"[1])
print(lang.index("y"))
print(lang[:])  # 得到所有的
print(lang[1:5])  # 得到一部分
c = lang
print(id(c) == id(lang))

# 字符串基本操作
str1 = "abc"
str2 = "efg"
print(str1 + str2)
print("a" in str1)
print(max(str2))
print(max(str1))
print(operator.eq(str1, str2))  # python3中不支持cmp()函数
print(len(str1 + str2))

# 字符串格式化输出
print("%d years" % 15)
print("%c" % 'c')

# format方式格式化
s1 = "I like {0}".format("python")
print(s1)
age = 25
print('{0} and {1}'.format('Kobe', 'James'))

# split函数
a = "I LOVE PYTHON"
print(a.split(" "))

# 去掉字符两头的空格
b = " hello "
print(b.strip())

# join拼接字符串
print(" ".join(a))

# 字符编码
print("中国")

# 列表反转
alist = [1, 2, 3, 4, 5]
print(alist[::-1])  # 不推荐
print(list(reversed(alist)))  # 推荐

# list函数
la = [1, 2, 3]
lb = ["zacky", "python"]
la.extend(lb)
print(len(la))
la.append(lb)

# list insert
all_users = ['zacky', 'python', 'learning']
all_users.insert(0, "io")

# list remove
all_users.remove("io")
print(len(all_users))

# dict
citys = ["suzhou", "tangshan", "beijing", "shanghai"]
city_codes = ["0512", "0315", "011", "012"]
print("{} : {}".format(citys[0], city_codes[0]))

person = {"name": "qiwsir", "site": "qiwsir.github.io", "language": "python"}
print(person)

# 元组构建法
name = (["first", "Google"], ["second", "Yahoo"])
website = dict(name)
print(website)

# 基本操作
print(len(city_codes))
print(website["first"])
website["third"] = "Microsoft"
print(website)
del website["second"]
print(website)

# copy
ad = {"name": "qiwsir", "lang": "python"}
bd = ad
print(bd)
print(id(ad))
print(id(bd))

# python在所执行的复制动作中，如果是基本类型的数据，就在内存中重新建个窝，如果不是基本类型的，就不新建窝了，而是用标签引用原来的窝
x = {"name": "qiwsir", "lang": ["python", "java", "c"]}
y = x.copy()
print(y)
print(id(x))
print(id(y))

z = copy.deepcopy(x)
print(id(x["lang"]))
print(id(z["lang"]))
x["lang"].remove("java")
print(x)
print(z)

# dict clear
z.clear()
print(z)

# dict del
del z
# print(z)

# dict.get('key') dict['key']
d = {"name": "zacky"}
print(d.get("age"), 12)
# print(d["age"])

# 创建set
s1 = set("qiwsir")
print(s1)
s2 = set([123, "google", "face", "book", "facebook", "book"])
print(s2)
s3 = {"facebook", 123}
print(type(s3))
