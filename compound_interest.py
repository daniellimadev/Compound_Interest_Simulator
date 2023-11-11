##################################################
##### DEVELOPED BY: DANIEL PEREIRA DE LIMA #####
##################################################


def ppv(x):
    nx = x.replace(',', '.')
    if nx.count('.') == 0:
        fx = int(nx)
    else:
        fx = float(nx)
    return fx


def msv(k):
    mf = '{:.2f}'.format(k)
    dec = mf[-2:]
    intf = '{:,}'.format(int(k))
    before = str(intf).replace(',', '.')
    fn = '{}{}{}'.format(before, ',', dec)
    return fn


def cycle(m):
    while True:
        try:
            v = ppv(str(input(m)))
            return v
        except ValueError:
            print('\nYou entered one or more invalid characters. '
                  'Only enter numbers, separating decimal places with a period or comma!\n')
            continue


div = ('=' * 85)

print()
print(div)
print('{:^85}'.format('COMPOUND INTEREST SIMULATOR'))
print(div)
print()

ii = cycle('Enter the initial investment (enter 0 for none): $ ')
mv = cycle('Enter the fixed amount you want to deposit every month (enter 0 for none)? $ ')
fees = cycle('Enter the monthly compound interest yield percentage: ')
years = cycle('Enter the number of years you want to pay: ')
months = int(years * 12)
total = ii
dep = 0

for times in range(1, (months + 1)):
    dep += mv
    total += (total * fees / 100)
    total += mv

dep = dep + ii
compound_interest = total - dep

ii = msv(ii)
mv = msv(mv)
fees = msv(fees)
total = msv(total)
dep = msv(dep)
compound_interest = msv(compound_interest)

if years == 1:
    man = 'YEAR'
else:
    man = 'YEARS'

print()
print(div)
print()

print('''INITIAL INVESTMENT: R$ {}
MONTHLY DEPOSIT: R$ {}
COMPOUND INTEREST RATE: {}%
TOTAL OF months: {}

ADDED VALUE OF MONEY ITSELF: {}
VALUE ADDED IN COMPOUND INTEREST: {}
FINAL VALUE AFTER {} {} INCOME: R$ {}'''.format(ii, mv, fees, months, dep, compound_interest, years, man, total))

print()
print(div)

input()