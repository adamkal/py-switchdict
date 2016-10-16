import inspect
from functools import partial
from collections import defaultdict


class SwitchDict(dict):

    def __init__(self, *args, **kwargs):
        super(SwitchDict, self).__init__(*args, **kwargs)
        self.instance = None

    def __call__(self, key):
        def inner(func):
            self[key] = func
            return func
        return inner

    def default(self, func):
        self._default = func
        return func

    def __missing__(self, key):
        try:
            return self._default
        except AttributeError:
            raise KeyError('Unknown key "{}"'.format(key))

    def __get__(self, instance=None, owner=None):
        self.instance = instance
        return self

    def __getitem__(self, item):
        func = super(SwitchDict, self).__getitem__(item)
        if self.instance:
            func = func.__get__(self.instance, self.owner)
        return func
