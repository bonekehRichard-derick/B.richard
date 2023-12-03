import numpy as np

def branch_and_bound(cost_matrix):
    N = len(cost_matrix)
    min_val = 0
    for i in range(N):
        min_val += min(cost_matrix[i])
    jobs = [-1]*N
    visited = [False]*N
    state = (-min_val, 0, jobs, visited)
    states = [state]
    while len(states) > 0:
        states.sort(reverse=True)
        _, person, jobs, visited = states.pop(0)
        if person == N:
            return jobs
        for job in range(N):
            if not visited[job]:
                new_jobs = jobs.copy()
                new_jobs[person] = job
                new_visited = visited.copy()
                new_visited[job] = True
                new_val = sum(cost_matrix[i][new_jobs[i]] for i in range(person+1))
                if person < N-1:
                    new_val += sum(min(cost_matrix[i][j] for j in range(N) if not new_visited[j]) for i in range(person+1, N))
                new_state = (-new_val, person+1, new_jobs, new_visited)
                states.append(new_state)

# Test the function
cost_matrix = np.array([[7, 5, 2], [1, 8, 3], [3, 2, 4]])
print(branch_and_bound(cost_matrix))
