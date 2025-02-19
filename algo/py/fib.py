# test save a file
def fib_recursive(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib_recursive(n-1)+fib_recursive(n-2)
def fib_loop(n):
    n_2=0
    n_1=1
    res=0
    for i in range(2, n+1):
        res = n_1+n_2
        n_2 = n_1
        n_1 = res
    return res
def power_set(input_set):
    if len(input_set)==0:
        return [[]]
    final = []
    first = input_set[0]
    rest_subset = power_set(input_set[1:])
    for subset in rest_subset:
        print("--------------------------------------------------------------")
        print(subset)
        print([first]+subset)
        final.append([first]+subset)
        final.append(subset)

    return final
def exponential_growth(n, factor, days):
    var = n
    res = []
    res.append(n)
    for i in range(days):
        var = var * factor
        res.append(var)
    return res
def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1
    while True:
        time_left -= time_in_country
        time_in_country *= factor
        if not time_left>0:
            return count
        count += 1
if __name__ == "__main__":
    print(fib_recursive(9))
    print(fib_loop(9))
    print(power_set([1, 2, 3]))
    print(exponential_growth(10, 2, 4))
    print(num_countries_in_days(3, 1.2))
