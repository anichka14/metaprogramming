import numpy as np
import re


class Meta(type):

    def __new__(mcs, name, bases, class_dict):
        def save(self, file_name="Value"):
            with open(f"{file_name}.txt", 'w+') as f:
                f.write("\n".join(str(key) + ": " + str(item) for key, item in self.__dict__.items()))

        def load(self, file_name="Value"):
            try:
                with open(f"{file_name}.txt", 'r') as f:
                    for line in f:
                        lst = re.split(r"\s*:\s*|\s*=\s*| ", line)
                        new_dict = {lst[0]: float(lst[1].replace("\n", ""))}
                        self.__dict__.update(new_dict)
                    print(self.__dict__)
                    return self.__class__()
            except OSError:
                print("File is not exist!")

        new_class = super(Meta, mcs).__new__(mcs, name, bases, class_dict)  # при створенні нового класу
        # виклик функції __new__ з класу Meta
        setattr(new_class, save.__name__, save)  # додаємо методи до new_class
        setattr(new_class, load.__name__, load)
        return new_class


class Vector(metaclass=Meta):

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def get_vector(self):
        return np.array([self.x, self.y, self.z])


if __name__ == "__main__":
    v = Vector(1, 6, 9)
    v.save()
    with open("Value.txt", "r") as f:
        print(f.read())
    v.load("Value2")
    print(v.get_vector)