__author__ = 'luis@escala.io'

class FilterModule(object):
    def filters(self):
        return {
            'attrinlist': self.attr_in_list,
        }

    # Returns a new seq of items whose attributes matched any of the elements in the match_list.
    def attr_in_list(self, seq, path, match_list):
        try:
            path = str(path) # Path must be a string.
        except UnicodeError:
            raise
        else:
            for item in seq:
                if self.matches_any_in_list(path, item, match_list):
                    yield item

    def matches_any_in_list(self, path, mapping, match_list):
        try:
            value = self.getattrd(mapping, path) 
        except AttributeError:
            raise
        else:
            if value in match_list:
                return True
            else:
                return False

    # Uses reduce to get to attributes separated by a "." in a nested dictionary.
    def getattrd(self, obj, name):
        try:
            return reduce(dict.get, name.split('.'), obj)
        except AttributeError, e:
            raise
