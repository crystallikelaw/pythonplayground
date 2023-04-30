'''
random walk, where every step is randomly jumping between current position and the end.
'''

import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

# parameters
end_pos = 500
max_reps = 100


# Here, we do max_reps of a river of length end_pos

# container for results
count = []

# loop
for x in range(max_reps):
    current_pos = 0
    steps = 0
    while current_pos < end_pos:
        current_pos = random.randint(current_pos + 1, end_pos + 1)
        steps = steps + 1
    count.append(steps)
print('Average of', len(count), 'jumps is', sum(count) / len(count))
# print(count)


# Here, we fix the length of the river at end_pos, and increase
# repetitions upto max_reps

# containers for graphs
n = []
mean1 = []

temp_1 = 1

while temp_1 < max_reps:

    # container for results
    count = []

    # loop
    for temp_2 in range(temp_1):
        current_pos = 0
        steps = 0
        while current_pos < end_pos:
            current_pos = random.randint(current_pos + 1, end_pos + 1)
            steps = steps + 1
        count.append(steps)
    mean1.append(sum(count) / len(count))
    n.append(temp_1)
    temp_1 = temp_1 + 1


plt.figure()
plt.legend(
    plt.plot(n, mean1),
    ['Increasing repetitions']
)
# plt.show()

# Here, we do max_reps of rivers of increasing width, upto end_pos

# containers for graphs
length = []
mean2 = []

temp_1 = 1

for temp_1 in range(end_pos):

    # container for results
    count = []

    # loop
    for temp_2 in range(max_reps):
        current_pos = 0
        steps = 0
        while current_pos < temp_1:
            current_pos = random.randint(current_pos + 1, temp_1 + 1)
            steps = steps + 1
        count.append(steps)
    mean2.append(sum(count) / len(count))
    length.append(temp_1)


plt.figure()
plt.legend(
    plt.plot(length, mean2),
    ['Increasing n']
)
# plt.show()
