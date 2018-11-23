import random


class Effect:
    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value

    @property
    def Name(self):
        return self._name

    @property
    def Value(self):
        return self._value

    @staticmethod
    def get_effect(effects: list, name: str = None, bitmask: int = None):
        if name is not None:
            for e in effects:
                if e.Name == name:
                    return e
        elif bitmask is not None:
            for e in effects:
                if e.Value == bitmask:
                    return e

    @staticmethod
    def get_random_effect(effects: list):
        return random.sample(effects, 1)[0]

    @staticmethod
    def combine_effects(effects: list):
        bitmask = 0
        for e in effects:
            bitmask += e.Value

        return bitmask
