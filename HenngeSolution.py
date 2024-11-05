def process_numbers(numbers_str):
    numbers = list(map(int, numbers_str.split()))
    return sum(map(lambda x: x*x if x > 0 else 0, numbers))

def recursive_process_cases(n, results=[]):
    if n == 0:
        return results
    
    count = int(input())
    numbers = input()
    result = process_numbers(numbers)
    return recursive_process_cases(n-1, results + [result])


n = int(input())
results = recursive_process_cases(n)
print(*results, sep='\n')


