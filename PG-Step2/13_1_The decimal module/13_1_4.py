from decimal import Decimal as D
from decimal import *

num = D(input())
res = num.exp() + num.ln() + num.log10() + num.sqrt()

print(res)


# from decimal import Decimal as D
# d = D(input())
# print(sum(func() for func in (d.exp, d.ln, d.log10, d.sqrt)))

# from decimal import Decimal
#
# d = Decimal(input())
# print(sum(getattr(d, f)() for f in ('exp', 'ln', 'log10', 'sqrt')))

