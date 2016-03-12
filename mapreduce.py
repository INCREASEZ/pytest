from functools import reduce
L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    return name[0].upper()+name[1:].lower()
L2 = list(map(normalize, L1))
print(L2)

#利用reduce求积
def prod(L):
    pass
    #return reduce(lambda x,y:x*y,L)
    fun=lambda x,y:x*y
    return reduce(fun,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


#利用map/reduce将字符串转换成浮点型
def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    l = s.split('.')
    return reduce(lambda x, y: x * 10 + y, map(char2num, l[0])) + reduce(lambda x, y: x / 10 + y, map(char2num, l[1][::-1])) / 10
print('str2float(\'123.456\') =', str2float('123.456'))