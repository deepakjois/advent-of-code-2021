import sys

report = [s.strip() for s in sys.stdin.readlines()]
length = len(report)
size = len(report[0])


def one_counts(inputs):
    return [sum(int(r[i]) for r in inputs) for i in range(size)]


def filter_by_criteria(inputs, criteria):
    curr_pos = 0
    while len(inputs) > 1:
        num_ones_at_pos = one_counts(inputs)[curr_pos]
        num_zeros_at_pos = len(inputs) - num_ones_at_pos
        result = criteria(num_ones_at_pos, num_zeros_at_pos)
        inputs = set(filter(lambda x: x[curr_pos] == result, inputs))
        curr_pos = curr_pos + 1

    return next(iter(inputs))


def part1():
    gamma = "".join(('1' if x > (length - x) else '0') for x in one_counts(report))
    epsilon = "".join('0' if x == '1' else '1' for x in gamma)
    print(int(gamma,2)* int(epsilon,2))


def part2():
    most_common = lambda num_ones, num_zeros: '1' if num_ones >= num_zeros else '0'
    o2_rating = int(filter_by_criteria(set(report), most_common), 2)

    least_common = lambda num_ones, num_zeros: '0' if num_zeros <= num_ones else '1'
    co2_rating = int(filter_by_criteria(set(report), least_common), 2)

    print(o2_rating * co2_rating)


part1()
part2()