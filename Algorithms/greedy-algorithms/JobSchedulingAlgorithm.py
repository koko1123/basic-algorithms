""""
implements greedy algorithm to compute weighted completion times of "jobs"
prioritization includes a (weight - length) implementation and a (weight/length) one.
"""


def create_difference_schedule(jobs):
    return jobs.sort(cmp=diff_comparator)


# I know using a cmp is slow, but can't find a better way to ensure the tie breaker (higher weight first)
def diff_comparator(x, y):
    x_diff = x[0] - x[1]
    y_diff = y[0] - y[1]
    if x_diff == y_diff:
        return y[0] - x[0]
    return x_diff - y_diff


def create_ratio_schedule(jobs):
    # tie breaker doesnt matter
    return jobs.sort(key=lambda x: int(x[0] / x[1]))


def compute_weighted_completion_time(schedule):
    # Todo: complete completion time calc routine
    print(schedule)
