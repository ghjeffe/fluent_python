#===============================================================================
# def deco(func):
#     def inner():
#         print('running inner()')
#     return inner
#  
# @deco
# def target():
#     print('running target()')
#          
# target()
# print(target)
#===============================================================================


#===============================================================================
# import datetime
# registry = []
# 
# 
# def register(func):
#     print('running register{}@{}'.format(func, datetime.datetime.now()))
#     registry.append(func)
#     return func
# 
# @register
# def f1():
#     print('running f1()@{}'.format(datetime.datetime.now()))
# 
# @register
# def f2():
#     print('running f2()@{}'.format(datetime.datetime.now()))
# 
# def f3():
#     print('running f3()@{}'.format(datetime.datetime.now()))
# 
# def main():
#     print('running main()@{}'.format(datetime.datetime.now()))
#     print('registry ->', registry)
#     f1()
#     f2()
#     f3()
# 
# if __name__ == '__main__':
#     main()
#===============================================================================


from chap6_design_patterns import ecomm
promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    '''5% discount for customer with >= 1000 fidelity points'''
    return order.total() * .05

@promotion
def bulk_item(order):
    '''10% discount for each LineItem with >= 20 units'''
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    '''7% discount for orders with >= 10 distinct items'''
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    '''Select best discount available'''
    return max(promo(order) for promo in promos)