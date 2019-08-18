from store.database import store

class cat(store):
  pass

if __name__ == "__main__":
    cat = cat(provider='sqlite')
    cat.zoe = {
        'gender': 'female',
        'age': 1,
        'feature': ['lovely', 'beautiful']
    }
    cat.meng = {
        'gender': 'female',
        'age': 1,
        'feature': ['lovely', 'soft']
    }
    cat.mimi = {
        'gender': 'female',
        'age': 0.5,
        'feature': ['lovely']
    }
    cat.orz = {
        'gender': 'male',
        'age': 1.5,
        'feature': ['leadership', 'speed']

    }
    cat.neo = {
        'gender': 'male',
        'age': 0.3,
        'feature': ['cute']
    }