"""使用元类"""

def fn(self,name = 'word'):
    print(f'Hello,{name}')

Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
