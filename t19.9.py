import numpy as np
import re  # регулярні вирази для пошуку фрагмента тексту


def file_worker(cls):

    def save(self, file_name="Value"):
        with open(f"{file_name}.txt", 'w+') as f:
            f.write("\n".join(str(key) + ": " + str(item) for key, item in self.__dict__.items()))

    def load(self, file_name="Value"):
        try:
            with open(f"{file_name}.txt", 'r') as f:
                for line in f:
                    try:
                        lst = re.split(r"\s*:\s*|\s*=\s*| ", line)  # ділить рядок за заданим шаблоном
                        new_dict = {lst[0]: float(lst[1].replace("\n", ""))}
                        self.__dict__.update(new_dict)
                    except ValueError:
                        raise ValueError(f"Error in {lst[0]} value: {lst[1]}")
                print(self.__dict__)
                return self.__class__()
        except OSError:
            print("File is not exist!")

    setattr(cls, "save", save)
    setattr(cls, "load", load)
    return cls


@file_worker
class Vector:

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

# load повинен зчитувати з файлу і створювати новий об`єкт за тими полями, які було збережено в цей файл
# файл зчитуємо і створюємо по його даним відповідні поля
# зчитати поля і записати у self.__dict__()
