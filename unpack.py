def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts
'''
coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "Knuts")
# unpack a list
print(total(*coins), "Knuts")
'''
'''
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# unpack a dictinonary
print(total(**coins), "Knuts")
'''

def f(*args, **kwargs):
#    print("Positional:", args)
    print("Named:", kwargs)


#f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)