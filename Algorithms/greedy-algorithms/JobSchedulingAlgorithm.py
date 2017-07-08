""""
implements greedy algorithm to compute weighted completion times of "jobs"
prioritization includes a (weight - length) implementation and a (weight/length) one.
"""


def create_difference_schedule(jobs):
    return jobs.sorted(key=lambda x: (x[0] - x[1], -x[0]))


def create_ratio_schedule(jobs):
    # tie breaker doesnt matter
    return jobs.sort(key=lambda x: int(x[0] / x[1]))


def compute_weighted_completion_time(schedule):
    # Todo: complete completion time calc routine
    print(schedule)
