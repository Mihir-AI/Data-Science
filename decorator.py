def dec_fun(func):
     def wrap_func():
         print('******')
         func()
         print('*****')
     return wrap_func

@dec_fun

def hello():
    print('helloooooo')

print(hello())
from time import time
def performance(fn):
    def wrapper(*args,**kwargs):
        t1=time()
        result=fn(*args,**kwargs)
        t2=time()
        print(f"the time is{t2-t1}")
        return result
    return wrapper

@performance
def longtime():
    for i in range(10000000):
        i*5

longtime()
user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['name']:
        return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

