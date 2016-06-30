# coding: utf-8
'''
	-python是动态类型语言,变量不用声明直接使用,而且变量
	 可以的值可以赋予不同的类型.

'''


#整数(python的整数可以任意大,没有上下限)
#------------------------------------------------
a = 100
b = -200
c = a * b
d = pow(9,90)

#十六进制数
e = 0x123efc
f = -0xabcdef


#浮点数
#------------------------------------------------
g = 1.234
f = -2.345
g = pow(1.23,50)


#布尔
#------------------------------------------------
h = True 	#True实际上是1的别名
i = False 	#False实际上是0的别名

#空值
#------------------------------------------------
j = None

#字符串
#------------------------------------------------
k = "haha"
l = 'hehe'
m = "hihi" + k + l
n = "ab" * 3	#n = "ababab"


# 格式化字符串
str0 = "hi %s" % "wll"

str1 = "hi my name is %s, I am %d years old" % ("wll", 20)




#运算符
#------------------------------------------------
#算术
o = 1 + 2 -3 * 4 / 5

#bool
p = True and False or True
q = (2 == 3) and (2<=3) or (not (32>=10))
qq = 2 != 4

#位运算
r = 2&3
s = 3|4
t = ~12


#list
#------------------------------------------------
u = []
v = [1,2,3]
w = [1,2,True,"hehe"]
x = [1,2,3] + [4,5,6]

x[0]	#1
x[5]	#6
# x[6]:error

#倒序访问
#下标从－1开始
x[-1]	#6
x[-6]	#1
# x[-7]	error

x.append('a')	#在x最后追加一个'a'
x.insert(0,'b')	#在x的下标为0的地方插入一个'b'

x.pop()			#将x的最后一个元素删除
x.pop(3)		#将x的第3个元素删除

x[3] = True		#list中的元素可以被赋值


#tuple
#-----------------------------------------------
#tuple除了不支持修改类的操作外，其它的与list一样
#python的tuple与函数式程序语言中的list比较像
u = ()
v = (1,2,3)
w = (1,2,True,"hehe")
x = (1,2,3) + (4,5,6)

x[0]	#1
x[5]	#6
# x(6):error

#倒序访问
#下标从－1开始
x[-1]	#6
x[-6]	#1
# x[-7]	error

#单元素tuple
y = (23,)	#后面加一个",",因为(23)语义不明，与优先级使用的括号重复


#dict
#------------------------------------------------
z = {}
z = {2:3, "sw":True, 1.56:"hehe"}

z[2] 	# = 3
z["sw"]	# = True
z[1.56]	# = "hehe"

# z["blabla"] error

z[2] = 5	#update



#判断是否有某个key
#way1:
"blabla" in z #返回True/False，这里为False

#way2:
z.get("blabla")	#返回None
z.get(2)		#返回3



#遍历
for key in z:
	#处理key
	print(z[key])



#将dict转化为list
li = a.items()

#li = [(2, 3), ('sw', True), (1.56, 'hehe')]


#set
#-----------------------------------------------
#set只能用list或tuple创建
ss = set([1,2,3,4,5])
ss = set([1,2,False,"hehe"])
ss = set((1,2,"haha"))

#set会过滤掉相同的元素
set([1,2,2,2]) == set([1,2])

#也用in判断是否有某元素
5 in ss
"hehe" in ss

#遍历
for val in ss:
	print(val)

#插入删除

#插入已有的不会报错
ss.add(4)
ss.add("haha")

#删除没有的元素会报错
ss.remove(4)
# ss.remove("hi")	error


#内建函数
#-----------------------------------------------
aa = len([1,2,3])
bb = len((1,2,3,4))
cc = len({2:3, "sw":True, 1.45:"hehe"})
dd = len(set([1,2,3]))

type(123)
type("eded")
type([1,2,3])
type((1,2,3,4))

#cmp 返回1表示第一个大，返回0表示一样大，返回－1表示第二个大
cmp(1,2)
cmp(True,True)
cmp("abc","de")	#字符串按字典序比
cmp([1,2,3],[4,5])	#list与字符串比较规则一样


#转换函数
str(123)
str(12.34)
str(False)


int(1.234)
int("123")

float("1.23")
float(12)









