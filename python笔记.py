'''----------------------第一章：变量和简单数据类型-------------------------'''
#变量和简单数据类型
# message = "hello world"
# print(message)
# 变量名只能以字母或下划线开头，且只能包含字母、数字、下划线

#字符串大小写
# 首字母大写title,全部大写upper，全部小写lower
# name = 'ada'
# print(name.title())
# print(name.upper())
# print(name.lower())
#字符串中使用变量
# print(f"my name is {name}")
#制表符\t，换行符\n

#rstrip()，lstrip()，strip()分别删除字符串末尾、开头、两边空白
# a = " kkk "
# print(a.strip())

# 整数可以用加减乘除运算：+-*/
# 所有带小数点都是浮点数，任意两个数相除结果都是浮点数
# 书写较大数字可以用下划线分组便于阅读，如 14_555_66666
#python支持同时给多个变量赋值，如 x,y,z=1,2,3

'''----------------------第二章：列表-------------------------'''
#列表用方括号表示[]
# name = ['kk','jj','qq']
#索引访问列表元素，左边从0开始，右边从-1开始
# print(name[0])

# 修改列表元素
# name[0] = 'tt'
# print(name[0])
# append()列表末尾添加元素，insert（）列表中插入元素，列表中删除元素del
# name.append('pp')
# name.insert(1,'uu')
# del name[0]
# print(name)

#pop()根据下标值弹出元素，remove()根据元素值删除元素
#name = ['kk','hh','gg']
# name1 = name.pop() #不填则弹出最后一位，填索引则弹出对应元素
# print(name1)
# print(name)
# a = 'kk'
# name.remove(a)
# print(a)
# print(name)

#sort()对列表永久排序，sorted()对列表临时排序,reverse()倒序排序
# cars = ['bmw','audi','toyota','xiaomi']
# print(sorted(cars))
# cars.sort()
# cars.sort(reverse=True) #反向排序
# cars.reverse()
# print(cars)

'''----------------------第三章：操作列表-------------------------'''
# for循环遍历列表
# ladys = ['da','fasd','jjj']
# for lady in ladys:
#     print(lady)
#print('循环结束')

#range()函数,range(a,b,c) a为初始值，b为末值但不包含b，c为步长，步长不填则默认为1，如输出从10以内的偶数：
# for value in range(0,11,2):
#     print(value)

#数字列表可以用函数min() max() sum()求最小值 最大值 和，但没平均值函数
# num = [1,2,3,4,5]
# print(min(num))
# print(max(num))
# print(sum(num))

# 列表切片
# players = ['qq','ww','ee','rr','tt']
# print(players[1:3])  #打印列表第2、3位，若[:3]从第一个元素到第3个元素，[1:]从第二个元素到最后一个元素
# for player in players[:3]:
#     print(player.title())   #遍历切片，首字母大写打印列表前三个元素
# players_copy = players  #复制列表
# print(players_copy)

# 不可变的列表称为元组，元组的值是不可变的，用圆括号标识
# nums = (200,5,99)
# print(nums[0])  #同样可以根据索引打印对应元素值
# for num in nums:   #同样可以遍历元组
#     print(num)
# nums = (100,2)  #元组元素不能改，但可以重新定义整个元组，前面的元组失效
# print(nums)

'''----------------------第四章：if语句-------------------------'''
# if,if-else,if-elif-else结构
# 条件测试，相等==，不相等!=，数值比较< > =< >=,多个条件and且 or或，是否包含in / not in
# age = int(input('请输入你的年龄：'))
# if age < 2:
#     print('婴儿')
# elif age < 10:
#     print('儿童')
# elif age < 18:
#     print('青少年')
# elif age < 60:
#     print('成年人')
# else:
#     print('老年人')

'''----------------------第五章：字典-------------------------'''
# 字典是一系列键值对，花括号表示
# alien = {'color':'green','age':11,'adr':'local'}
# print(alien['color'])  #输出值green
# alien['num'] = 123   #字典alien末添加键值对'num':123
# print(alien)
# alien['color'] = 'yellow'  #修改字典中color值为yellow
# print(alien)
# del alien['color']  #删除字典alien中color的键值对
# print(alien)
# age1 = alien.get('age2','没这个键')  #get访问值，如果有指定的键，则返回对应的值，如果没有则返回指定的默认值，如果没有填默认值则返回none
# print(age1)

# 遍历字典
# user = {'username':'hui','kk':'hui','first':'enrico','last':'fermi',}
# for k,v in user.items():   #items()方法返回键值对列表，示例为遍历所有键值对
#     print(f'\nkey:{k}')
#     print(f'value:{v}')
# for k in user.keys():   #keys()方法遍历字典所有键，返还一个列表包含字典中所有键
#     print(k)
# for v in user.values():   #values()方法遍历字典所有键，返还一个列表包含字典中所有键
#     print(v)
# for unique in set(user.values()):   #集合set()方法去重，集合中的元素都是唯一的
#     print(unique)
# name = {'a','b'}   #集合可以用花括号创建，集合没有键值对

#字典嵌套
#字典列表
# name1 = {'kkhh','iui'}
# name2 = {'kkuy','iji'}
# name3 = {'kjfghf','ijgi'}
# name = [name1,name2,name3]
# print(name)

# #字典中存储列表
# favorite_languages = {
#     'jen':['python','c'],
#     'saraj':['c'],
#     'lady':['go','haskell']
# }
# for name,languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

#字典中存储字典
# users = {
#     'zengzhihui':{
#         'first':'zeng',
#         'last':'zhihui',
#         'location':'conghua',
#     },
#     'lijianting':{
#         'first':'li',
#         'last':'jianting',
#         'location':'henan',
#     }
#
# }
# for username,user_info in users.items():
#     print(f"\nUsername:{username}")
#     full_name = f"{user_info['first']}{user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name:{full_name.title()}")
#     print(f"\tlocation:{location.title()}")

'''----------------------第六章：用户输入和while循环-------------------------'''
#input()函数输出提示并等待用户输入
# a = int(input("请输入数字："))    #input()默认是字符串，需要用int()等定义返还的类型
# print(f"你输入的数字为 {a}")

# b = 4 % 3  #求模运算符%，它将两个数相除并返回余值
# print(b)

#while循环，不断运行代码，直到指定条件不满足为止
# num = 1
# while num <= 5:
#     print(num)
#     num += 1

# message = ""    #让用户选择何时退出
# while message != 'quit':
#     message = input("请输入内容，若为quit则退出程序：")
#     if message != 'quit':
#         print(f"你输入的内容为{message}")

#使用标志（flag）：当多个条件满足程序才能运行时，可以定义一个变量判断程序是否处于活动状态
# active = True  #定义标志
# message = ""    #让用户选择何时退出
# while active:
#     message = input("请输入内容，若为quit则退出程序：")
#     if message == "quit":
#         active = False
#     else:
#         print(f"你输入的内容为{message}")

#使用break退出循环
# while True:
#     city = input('请输入城市名字：')
#     if city == 'quit':
#         break
#     else:
#         print(f'你输入的城市名为：{city}')

#continue返回循环开头，并根据条件测试结果决定是否继续执行循环
# num = 0   #输出1-10之间的奇数
# while num <10:
#     num += 1
#     if num % 2 ==0:
#         continue
#     print(num)

#使用while循环处理列表和字典
#在列表之间移动元素
# name = ['hh','kk','pp']
# name_1 = []
# while name:
#     name_2 = name.pop()
#     name_1.append(name_2)
# print(name_1)
#删除为特定值的所有列表元素
# pets = ['cat','dog','cat','fish']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
#使用用户输入来填充字典
# responses = {}
# active = True
# while active:
#     name = input('请输入你的名字：')
#     response = input('你认为世界和平吗？')
#     responses[name] = response      #将名字和对应的回答存储在自动中
#     repeat = input('你还要指定其他人回答这个问题吗：')
#     if repeat == 'no':
#         active = False
# print('----------------调查结束----------------')
# for name,response in responses.items():
#     print(f"{name}的回答是世界{response}")

'''----------------------第七章：函数-------------------------'''
#定义函数
# def greet_user():
#     print('hello')
# greet_user()

#向函数传递信息
# def greet_user(username):    #username是形参，zengzhihui是实参
#     print(f"hello,{username.title()}")
# greet_user('zengzhihui')

#传递实参
#位置实参
# def pet(animal_type,pet_name):
#     print(f'I have a {animal_type},name is {pet_name}!')
# pet('dog','xiaohei')   #根据参数顺序输出结果：我有一只狗，名字叫小黑
# pet('xiaohei','dog')   #函数可以重复调用，根据参数顺序输出结果就很奇怪：我有一只小黑，名字叫狗
#关键字实参,写明形参对应的实参是什么，这时候顺序就无所谓了
# pet(pet_name='xiaohei',animal_type='dog')

#默认值
# def pet(pet_name,animal_type='dog'):
#     print(f'I have a {animal_type},name is {pet_name}!')
# pet('xiaohei')  #animal_type不传递参数，就取默认值dog
# pet('xiaohei','cat')  #animal_type传递参数，就取传递进去的参数cat

#返回值
# def name(first_name,last_name):
#     full_name = f"{first_name} {last_name}"
#     return f"my name is {full_name}"
#     return full_name.title()   #return 返回一个或者一组值
# people_name = name('zeng','zhihui')
# print(people_name)

#让实参变成可选的，可以定义默认值为空
# def name(first_name,last_name,middle_name=''):   #注意，若使用位置传递实参形式最好把有默认值的参数放在最后
#     if middle_name:
#         full_name = f"{first_name} {middle_name}{last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return f"my name is {full_name}"
# name_1 = name('zeng','hui','zhi')   #my name is zeng zhihui
# print(name_1)
# name_2 = name('zeng','hui')    #my name is zeng hui
# print(name_2)

#返回字典
# def build_persion(first_name,last_name,age=None):   #可选形参age，将其默认值设置为特殊值None（表示变量没有值），可将None视为占位符
#     persion = {'first':first_name,'last':last_name}
#     if age:
#         persion['age'] = age
#     return persion
# persion_1 = build_persion('zeng','zhihui')
# print(persion_1)    #{'first': 'zeng', 'last': 'zhihui'}
# persion_2 = build_persion('zeng','zhihui',30)
# print(persion_2)    #{'first': 'zeng', 'last': 'zhihui', 'age': 30}

#结合使用函数和while循环
# def name(first_name,last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name
# while True:
#     print("\nplease tell me your name")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("first name:")
#     if f_name == "q":
#         break
#     l_name = input("last name:")
#     if l_name == "q":
#         break
#     name_1 = name(f_name,l_name)
#     print(f"\nhello,{name_1}!")

#传递列表
# def greet_users(names):
#     for name in names:
#         msg = f"hello,{name}"
#         print(msg)
# usernames = ['jj','kk','ll']
# greet_users(usernames)

#在函数中修改列表
# def print_models(unprinted_designs,complete_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"printing model:{current_design}")
#         complete_models.append(current_design)
# def show_completed_models(completed_models):
#     print("\nthe folowing models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models = []
# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)

#禁止函数修改列表，切片表示法[:]创建列表副本，例如接上面的程序
# def print_models(unprinted_designs,complete_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"printing model:{current_design}")
#         complete_models.append(current_design)
# def show_completed_models(completed_models):
#     print("\nthe folowing models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['phone case','robot pendant','dodecahedron']   #修改之前这个列表运行程序后为空，创建副本后该列表不受影响
# completed_models = []
# print_models(unprinted_designs[:],completed_models)    #使用unprinted_designs的副本进行操作
# show_completed_models(completed_models)
# print(unprinted_designs)   #验证原始列表不受影响

#传递任意数量的实参
# def make_pizza(*toppings):   #形参中的*让python创建一个名为toppings的空元组，并将收到的所有值封装到这个元组中
#     print('\nmakking pizza with the following toppings:')
#     for topping in toppings:
#         print(topping)
# make_pizza('mushrooms')
# make_pizza('mushrooms','green peppers','extra cheese')

#使用位置实参和任意数量实参时，要将任意数量实参放在最后，例如
# def make_pizza(size,*toppings):
#     print(f'\nmakking a {size}-inch pizza with the following toppings:')
#     for topping in toppings:
#         print(topping)
# make_pizza('5','mushrooms')
# make_pizza('5','mushrooms', 'green peppers', 'extra cheese')

#使用任意数量的关键字实参
# def people(first,last,**user_info):         #形参**让python创建一个名为user_info的空字典，并将所有接收到的键值对存储在这个字典中
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info
# people_1 = people('aa','bb',location='conghua',laguage='chinese')
# print(people_1)  #结果为{'location': 'conghua', 'laguage': 'chinese', 'first_name': 'aa', 'last_name': 'bb'}

#将函数存储在模块中，后续可供导入到程序使用
# import time  导入时间模块
# from time import *    导入时间模块所有函数
# from time import sleep    导入时间模块的sleep函数
# from  time import sleep,strptime,clock_settime   导入时间模块的sleep,strptime,clock_settime三个函数
# from time import sleep as sl  导入时间模块的sleep函数并赋予别名sl，通常用于程序中已有同名变量，作区分避免冲突
# import time as tm  导入时间模块并赋予别名tm

'''----------------------第八章：类-------------------------'''
# class Dog:
#     def __init__(self,name,age):   #初始化属性name和age，形参self必不可少且要位于其他形参前面
#         self.name = name   #以self为前缀的变量可以供类中所有方法使用，可以通过类的任何实例来访问
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is now sitting")
#     def roll_over(self):
#         print(f"{self.name} rolled voer!")
# 类中的函数称为方法。方法__int__()是一个特殊方法，每当你根据Dog类创建新实例时，python都会自动运行它
# My_Dog = Dog('xiaohei',6)   #创建实例
# print(f"my dog name is {My_Dog.name}")   #访问属性
# My_Dog.sit()    #调用方法
# My_Dog.roll_over()

# your_dog = Dog('dabai',5)   #创建多个实例
# my_little_dog = Dog('shagou',1)
# print(f"your dog name is {your_dog.name}")
# your_dog.sit()
# your_dog.roll_over()
# print(f"my little dog name is {my_little_dog.name}")
# my_little_dog.sit()
# my_little_dog.roll_over()

#给属性指定默认值，可在方法__init__()中为其指定默认值
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 100  #指定默认值
#     def read_odometer(self):
#         print(f"this car has {self.odometer_reading} miles on it")
# my_car = Car("bmw","325","2024")
# my_car.read_odometer()   #打印默认值

#修改属性值得
#直接修改属性的值
# my_car.odometer_reading = 200
# my_car.read_odometer()
#通过方法修改属性的值
#     def update_odometer(self,mileage):
#         self.odometer_reading = mileage
# my_car = Car("bmw","325","2024")
# my_car.update_odometer(125)
# my_car.read_odometer()
#通过方法对属性的值进行递增
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles
# my_car = Car("bmw","325","2024")
# my_car.increment_odometer(22)
# my_car.read_odometer()

#继承
# class Car():    #父类
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#     def fill_gas_tank(self):
#         print('this car need a gas tank')
# class ElectricCarf(Car):   #子类，继承自Car类。子类继承了父类的所有方法和属性，同时还可以定义自己的属性和方法
#     def __init__(self,make,model,year):   #初始化父类属性
#         super().__init__(make,model,year)   #super()是一个特殊函数，可以让你调用父类方法
#         self.battery_size = 75  #添加新属性
#     def describe_battery(self):    #添加新方法
#         print(f"This car has a {self.battery_size}-KWh battery.")
#     def fill_gas_tank(self):   #重写父类方法
#         print("electriccar doesn't need a gas tank")
# my_tesla = ElectricCarf('tesla','model s',2024)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()

#将实例用作属性
# class Name_1:
#     def __init__(self,a = 55):
#         self.a = a
#     def send_name(self):
#         print(self.a)
# class Name_2:
#     def __init__(self):
#         self.b = Name_1()   #创建一个新的Name_1实例，并将实例赋值给属性b，每当方法__init__()被调用时都执行该操作
# name = Name_2()
# name.b.send_name()   #输出55

#导入类。将Car类、ElectricCarf类保存为car.py文件
# from car import Car   #导入单个类
# from car import Car,ElectricCarf   #导入多个类
# import car    #导入整个模块
# from car import *    #导入模块中所有类
# from car import ElectricCarf as El   #使用别名

#python标准库
# from random import randint,choice
# a = randint(1,6)   #随机返回一个1到6之间的整数
# print(a)
# players = ['aa','bb','cc']
# first_up = choice(players)   #choice()将一个列表或者元组作为参数，并随机返回其中一个元素
# print(first_up)

'''----------------------第九章：文件和异常-------------------------'''
#从文件中读取数据
#测试111