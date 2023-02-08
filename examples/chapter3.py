import collections


class StrKeyDict0(dict):
    """
    При поиске по нестроковому ключу объект преобразует
    его в тип str в случае отсутствия
    """
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


class StrKeyDict(collections.UserDict):
    """
    Всегда преобразует нестроковые ключи в тип str —
    при вставке, обновлении и поиске
    """
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item
