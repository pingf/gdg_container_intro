

from store.database import Store

class Cat(Store):
  pass

if __name__ == "__main__":
    cat = Cat(provider='sqlite')
    cat.miaomiao.age = cat.miaomiao.age + 1