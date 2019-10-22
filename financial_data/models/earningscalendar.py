from datetime import datetime


class Structure:
    # Class vafriable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments, if any
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(', '.join(kwargs)))

    def __repr__(self):
        return '\n'.join(['{}: {}'.format(name, getattr(self, name)) for name in self._fields])


class EarningsCalendar(Structure):

    _fields = ['q1', 'q2', 'q3', 'q4', 'period', 'time', 'etype', 'date', 'timestamp']

    @property
    def is_up_to_date(self):
        if self.date > datetime.now():
            return True
        return False
