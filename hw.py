import random
import timeit
from prettytable import PrettyTable

coins = [50,25,10,5,2,1]

def find_coins_greedy(sum):
    result = {}
    for coin in coins:
        if sum >= coin:
            result[coin] = sum // coin
            sum = sum % coin
    return result


def find_min_coins(sum_val):
    table = [float('inf')] * (sum_val + 1)
    table[0] = 0
    used_coins = [0] * (sum_val + 1)

    for coin in coins:
        for i in range(coin, sum_val + 1):
            if table[i - coin] + 1 < table[i]:
                table[i] = table[i - coin] + 1
                used_coins[i] = coin
    result = {}
    current_sum = sum_val
    while current_sum > 0:
        coin = used_coins[current_sum]
        result[coin] = result.get(coin, 0) + 1
        current_sum -= coin

    return result   


print(find_coins_greedy(113)) #{50: 2, 10: 1, 2: 1, 1: 1}
print(find_min_coins(113)) #{1:1,2:1,5:1,10:1,25:1,50:2}


ammounts = [random.randint(1,1000) for _ in range(5)]
print(ammounts)

result = []
for ammount in ammounts:
    res = [ ammount,
           timeit.timeit(lambda:find_coins_greedy(ammount), number=100),
            timeit.timeit(lambda:find_min_coins(ammount), number=100)]
    result.append(res)

table = PrettyTable()
table.field_names = ['Sum', 'Greedy', 'Dynamic']
table.add_rows(result)
print(table)