from math import ceil
import urllib.request
import json


def currencyExchange(con_from, con_to, value):
    result = 0
    curr_page = urllib.request.urlopen(
        'http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62')
    obj = curr_page.read().decode(encoding='UTF-8')
    content = json.loads(obj)
    try:
        _from = content['rates'][con_from]
        _to = content['rates'][con_to]
        convert_amt = _to / _from
        result = convert_amt * value
    except:
        raise NameError
    return result


class Converter:
    _temps = {'cf': lambda c: c * (9 / 5) + 32,
              'fc': lambda f: (f - 32) * (5 / 9),
              'ck': lambda c: c + 273.15,
              'kc': lambda k: k - 273.15,
              'fk': lambda f: (f + 459.67) * 5 / 9,
              'kf': lambda k: k * (9 / 5) - 459.67
              }

    def tempConvert(self, msr_from, msr_to, amt):
        try:
            return self._temps[msr_from[0] + msr_to[0]](amt)
        except KeyError:
            "Cannot convert from {0} to {1}".format(msr_from, msr_to)

    pass
