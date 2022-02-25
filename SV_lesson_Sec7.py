# # class Person(object):
# #     #コンストラクター
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def say_somthing(self):
# #          print('I am {}.hello'.format(self.name))
# #          self.run(10)
# #
# #     def run(self, num):
# #         print('run' * num)
# #     # オブジェクトが無くなるときに呼び出される
# #     def __del__(self):
# #         print('good bye')
# #
# # person= Person('Mike')
# # person.say_somthing()
# #
# # del person # 明示的にdelを呼ぶとき
# # print('###########################')
# # # 継承
#
# class Person(object):
#     #コンストラクター
#     def __init__(self, age = 1):
#         self.age = age
#     def drive(self):
#         if self.age >= 18:
#             print('OK')
#         else:
#             raise Exception('No drive')
#
# class Baby(Person):
#     def __init__(self, age = 1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
# class Adult(Person):
#     def __init__(self, age = 18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
# baby = Baby()
# adult=Adult()
#
# class Car(object):
#     def __init__(self, model = None):
#         self.model = model
#     def run(self):
#         print('run')
#     def ride(self,person):
#         person.drive()
#
# car =Car()
# car.ride(baby)
#
#
# print('###########################')
#
# class ToyotaCar(Car): #Carを継承している
#     def run(self):
#         print('run')
#
# class TeslaCar(Car):
#     def __init__(self, model='Model S',
#                         enable_auto_run =False,
#                         passwd='123'):
#         #self.model=model
#         super().__init__(model) # 親の変数を呼び出す
#         self._enable_auto_run = enable_auto_run
#         self.passwd = passwd
#
#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run
#
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.passwd == '456':
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError
#
#     def auto_run(self):
#         print('auto run')
#
# tesla_car = TeslaCar('Model_S', passwd='456')
# tesla_car._enable_auto_run = True
# print(tesla_car.enable_auto_run)
#
#
# # car =Car()
# # car.run()
# # print('#Toyota#')
# # toyota_car = ToyotaCar('Lexus')
# # print(toyota_car.model)
# # toyota_car.run()
# # print('#TeslaCar#')
# # tesla_car = TeslaCar('Model_S')
# # print(tesla_car.model)
# # tesla_car.run()
# # tesla_car.auto_run()
#
# class T(object):
#     pass
# t =T()
# t.name= 'Mike'
# t.age=20
# print(t.name, t.age)
#
#
class Person(object):
    def talk(self):
        print('talk')
    def run

class Car(object):
    def run(self):
        print('run')

class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()