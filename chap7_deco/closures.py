#===============================================================================
# from dis import disassemble
# 
# def f1(a):
#     print(a)
#     print(b)
# 
# b = 6
# f1(3)
# 
# b = 6
# def f2(a):
#     global b
#     print(globals().get('b'))
#     print(a)
#     print(b)
# #     b = 9
# 
# f2(3)
# 
# disassemble(f1)
# disassemble(f2)
#===============================================================================

#===============================================================================
# class Averager():
#     def __init__(self):
#         self.series = []
#     
#     def __call__(self, new_value):
#         self.series.append(new_value)
#         total = sum(self.series)
#         return total/len(self.series)
# 
# avg = Averager()
# print([avg(num) for num in range(0,10000,100)])
#===============================================================================

def make_averager(): #p. 196
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
        
    return averager

avg = make_averager()
for i in range(5):
    print(avg(i))