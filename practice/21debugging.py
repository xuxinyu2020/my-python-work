"""调试"""
# assert
import logging



def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


if __name__ == '__main__':
    foo(2)

# logging
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
