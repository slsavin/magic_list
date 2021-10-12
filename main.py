from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


class MagicList(list):
    def __init__(self, cls_type=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if len(self) == 0:
            self.append(value)
        else:
            super().__setitem__(key, value)


if __name__ == '__main__':
    b = MagicList(cls_type=Person)

    a = MagicList()
    a[0] = 5
    print(a)


