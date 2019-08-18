

from store.database import Store

class Cat(Store):
  pass

if __name__ == "__main__":
    cat = Cat(provider='sqlite')
    print(cat['age>1'])