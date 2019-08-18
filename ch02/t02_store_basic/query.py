
from store.database import Store

class Cat(Store):
  pass

if __name__ == "__main__":
    cat = Cat(provider='sqlite')
    print('.'*40)
    print(cat.miaomiao)
    print(cat.mimi)
    print('.'*40)
    print(cat.orz.feature)
    print('.'*40)
    print(cat['feature:cute'])
    print('.'*40)
    print(cat['gender=male'])
    print('.'*40)
    print(cat['^m'])