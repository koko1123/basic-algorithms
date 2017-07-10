""""
implements greedy algorithm to compute weighted completion times of "jobs"
prioritization includes a (weight - length) implementation and a (weight/length) one.
"""


def create_difference_schedule(jobs):
    sorted(jobs, key=lambda x: (x[0] - x[1], -x[0]))
    return jobs


def create_ratio_schedule(jobs):
    sorted(jobs, key=lambda x: int((-x[0] / x[1]) * 100))
    return jobs


def compute_weighted_completion_time(schedule):
    completion_time = 0
    completion_time_scores = []
    for job in schedule:
        completion_time += job[1]
        completion_time *= job[0]
        completion_time_scores.append(completion_time)
    return sum(completion_time_scores)


job_list = [(1, 2), (3, 5)]
print(compute_weighted_completion_time(create_difference_schedule(job_list)))
print(compute_weighted_completion_time(create_ratio_schedule(job_list)))
