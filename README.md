# django-signals-mixin

Use Django signals (almost) like JavaScript events.

## Why?

Because I like JavaScript's event triggering and listening, so I thought, "Why
not tune Django signals to use them in a same way?"

## How do I use them?

Simply add the `SignalsMixin` to your model's base classes, and then attach
receivers using the class' `on_signal` method, like so:

```
from django.db import models
from django_signals_mixin import SignalsMixin

class MyModel(models.Model, SignalsMixin):
    ...

MyModel.on_signal('saved', alert_mymodel_saved)
```

## Wait, you attached the receiver to the class!

Yes, because in Python (unlike JavaScript) we have classes, so we can! So we
attach signal listeners only once (to the class), instead of attaching it to
every single instance.

## What data do receivers get?

All signals send to receivers the following parameters:

* sender: model of the instance that sent the signal
* instance: instance that sent the signal

Default signals also send some extra data, depending on the signal (check the Django
documentation). Custom signals also send a *name* parameter, which is their key
in the dictionary that defines them.

## Did you say custom signals?

Yes, if you need custom signals simply override the `CUSTOM_SIGNALS` attribute
in the model (which is empty by default) and then signal it:

```
...

class MyModel(models.Model, SignalsMixin):

    CUSTOM_SIGNALS = {
        'played': Signal()
    }

    def play(self):
        ...
        self.signal('played)'
```

That's it. Now all receivers that have registered to that signal will execute
when it's sent.
