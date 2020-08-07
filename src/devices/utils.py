import random


class Field:
    def __init__(self, name, type, min, max, default):
        self.name = name
        self.min = type(min)
        self.max = type(max)
        self.type = type
        self.default = default

    def get_default_value(self):
        return type(self.default)

    def get_random_value(self):
        if self.type is int:
            return random.randint(self.min, self.max)
        else:
            return round(random.uniform(self.min, self.max), 1)


class RangeField:
    # Min and Max are supposed to be tuples
    def __init__(self, name, type, min, max, default):
        self.name = name
        self.type = type
        self.min = min
        self.max = max
        self.default = default

    def get_default_value(self):
        return ','.join([str(i) for i in self.default])

    def get_random_value(self):
        while True:
            if self.type is int:
                min_val = random.randint(*self.min)
                max_val = random.randint(*self.max)
            else:
                min_val = round(random.uniform(*self.min), 1)
                max_val = round(random.uniform(*self.max), 1)
            if min_val < max_val:
                return ','.join([str(min_val), str(max_val)])


class MultiField:
    pass


def get_random_data(obj):
    data = {}
    if obj.__dict__:
        for var in obj.__dict__.keys():
            if isinstance(obj.__getattribute__(var), MultiField):
                field = obj.__getattribute__(var)
                data[field.name] = get_random_data(field)
            elif isinstance(obj.__getattribute__(var), (Field, RangeField)):
                field = obj.__getattribute__(var)
                data[field.name] = field.get_random_value()
    return data


def get_default_data(obj):
    data = {}
    if obj.__dict__:
        for var in obj.__dict__.keys():
            obj = obj.__getattribute__(var)
            if isinstance(var, (Field, RangeField)):
                data[obj.name] = obj.get_default_value()
    return data
