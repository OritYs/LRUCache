class Validation(object):

    @staticmethod
    def positive_validation(field):
        if field > 0:
            return True
        return False

    @staticmethod
    def range_validation(field, min_value, max_value):
        if min_value <= field <= max_value:
            return True
        return False
