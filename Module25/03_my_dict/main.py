class MyDict(dict):
    def get(self, __key, default=0):
        return super().get(__key, default)


mydict = MyDict({'a': 1, 'b': 2})
print(mydict.get('c'))
