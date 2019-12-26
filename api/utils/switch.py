from .decorators import stop_watch, log_entry_exit

class DecoratorSwitch(object):
    """decorator switch which allow you to turn it on and off"""
    def __init__(self,func):
        """disabled by default"""
        self._enabled = False
        self._func = func
    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, new_value):
        if not isinstance(new_value, bool):
            raise ValueError("enabled can only be set to a boolean value")
        self._enabled = new_value

    def __call__(self, target):
        """call the target if switch is disable. else, call the with teh decorator"""
        if self._enabled:
            return self._func(target)
        return target

"""disable or enable the time_it with a switch"""
time_it = DecoratorSwitch(stop_watch)
time_it.enabled = True

"""disable or enable the log entry and exit with a switch"""
log_around = DecoratorSwitch(log_entry_exit)
log_around.enabled = True

