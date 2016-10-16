switchdict
===============================

version number: 0.0.1
author: Adam Kaliński

Overview
--------

This package is an experiment to try to improve usability of typical
`switch-case` statement which does not exist in Python. As an alternative we
can use `if-elif-else` or, what I personally prefer, `dict`s.

Idea is to provide convenient decorators that will add keys to our switch-dict

Installation / Usage
--------------------

Clone the repo:

    $ git clone https://github.com/adamkal/switchdict.git
    $ python setup.py install

For now I'm not putting this to PIP as it serves only my educational purposes. If you
find this useful, let me know and I'll publish it on pip

Contributing
------------

If you have any ideas how we could improve this project feel free to add issues
or pull requests.

Example
-------

```python
import switchdict

notifier = switchdict.SwitchDict()

@notifier('email')
def email_notifier(recopient, msg):
  …

@notifier('chat')
def chat_notifier(recopient, msg):
  …

@notifier('snailmail')
def snailmail_notifier(recopient, msg):
  …

@notifier.default
def default_notifier(recopient, msg):
  …


class User(object):

  def __init__(name, notify_by=''):
    self.name = name
    self.notify_by = notify_by

  def notify(self, message):
    notifier[self.notify_by](self.name, message)

u = User('John', 'email')
u.notify('Hello world')

```
