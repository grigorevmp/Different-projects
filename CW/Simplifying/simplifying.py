# When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually
# bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!
#
# Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in
# integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been
# simplified in the following way ( -> means application of simplify):
#
# All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
# "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"
#
# All monomials appears in order of increasing number of variables, e.g.:
# "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"
#
# If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
# "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"
#
# There is no leading + sign if the first coefficient is positive, e.g.:
# "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

import re
import collections
import functools

PART_REGEX = re.compile(r'([+-])?(\d+)?(\w+)')


class Poly:
    def __init__(self, sign, cof, polys):
        self.cof = int(f'{sign}1') * (int(cof or 1) if isinstance(cof, str) else cof)
        self.polys = ''.join(sorted(polys))

    def __add__(self, other):
        return Poly('', self.cof + other.cof, self.polys)

    def __lt__(self, other):
        return self.polys < other.polys if len(self.polys) == len(other.polys) else len(self.polys) < len(other.polys)

    def to_str(self, pos=0):
        if self.cof == 0:
            return ''

        prefix = f'{"+" if self.cof > 0 and pos != 0 else ""}{"-" if self.cof == -1 else ""}' \
                 f'{self.cof if abs(self.cof) != 1 else ""}'
        return f'{prefix}{self.polys}'


def simplify(poly):
    all_polys = collections.defaultdict(list)
    for sign, cof, polys in PART_REGEX.findall(poly):
        p = Poly(sign, cof, polys)
        all_polys[p.polys] = [functools.reduce(lambda a, b: a + b, all_polys[p.polys], p)]

    return ''.join(p.to_str(i) for i, (p, *_) in enumerate(sorted(all_polys.values())))


print(simplify("2xy-yx"))
