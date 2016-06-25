
class RangeValidator(object):

    def __init__(self, min_val=None, max_val=None):
        """
        Validator for a value inside a specific range.

        The boundaries specified for this validator are inclusive, this means
        that the validator is satisfied when ``min < value < max``

        :param min_val: Lower limit. If None, no limit is applied.
        :param max_val: Upper limit. If None, no limit is applied.
        """
        self.min = min_val
        self.max = max_val

    def validate(self, value):
        if ((self.min is None or value >= self.min) and
                (self.max is None or value <= self.max)):
            return True
        raise ValueError("%s is out of [%s, %s]" % (value, self.min, self.max))