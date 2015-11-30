# import re
# from jinja2 import attr
#
# __author__ = 'luis'
#
# class FilterModule(object):
#     def filters(self):
#         return {
#             'luis': self.luis,
#         }
#
#     def luis(self, check, at, checkin):
#         if check.attr(at) in checkin:
#             return True
#         else:
#             return False



# from jinja2 import Environment
# def luis(value, list):
#     if value in list:
#         return True
#     else:
#         return False
# environment.tests['luis'] = luis