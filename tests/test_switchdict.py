import mock
import pytest
from switchdict import SwitchDict


def test_function_switchdict():

    switch = SwitchDict()

    @switch('first')
    def switch_first():
        return mock.sentinel.first

    @switch('second')
    def switch_second():
        return mock.sentinel.second

    assert switch['first']() is mock.sentinel.first
    assert switch['second']() is mock.sentinel.second

    with pytest.raises(KeyError):
        switch['third']

    @switch.default
    def switch_default():
        return mock.sentinel.default

    assert switch['unknown']() is mock.sentinel.default

def test_method_switchdict():

    class Test(object):

        switch = SwitchDict()
        state = None

        @switch('first')
        def first(self):
            return mock.sentinel.first

        @switch('second')
        def second(self):
            return mock.sentinel.second

        @switch.default
        def test_default(self):
            return mock.sentinel.default

        def test(self):
            return self.switch[self.state]()

    t = Test()
    assert t.test() is mock.sentinel.default

    t.state = 'first'
    assert t.test() is mock.sentinel.first
