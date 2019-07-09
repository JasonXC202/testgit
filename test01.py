# -*- coding:utf-8 -*-
#print("this is one")
def testarg(*args):
    return sum(args)


#print('__name__的值为:',__name__)
if __name__ == '__main__':
    a= testarg(10,2,-3)
    print(a)
