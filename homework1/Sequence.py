class ArrayList:

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values
            if not isinstance(values, (list, tuple, set, str)):
                print("неверный тип")
                return
            if len(values) == 0:
                return
            else:
                t = type(values[0])
                for value in values:
                    if t!= type(value):
                        print("неверная запись")
                        return


    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __contains__(self, item):
        if item in self.values:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return ArrayList(list(reversed(self.values)))


    def count(self, item):
        coun = 0
        for it in self.values:
            if (it == item):
                coun += 1
        return coun

    def index(self, item):
        for i, it in enumerate(self.values):
            if (it == item):
                ite = i
        return ite
