import matplotlib.pyplot as plt
import random, math, os
plt.rcdefaults()


#Return buckets based on frequency
def generate_axes(data, buckets):
    max_mean = int(max(data))
    min_mean = int(min(data))
    round_value = round(int(math.log(max_mean/min_mean) - 1), 1) #Constant equation to round. Defined by Yashika.
    bucket_size = math.ceil((max_mean-min_mean)/buckets)
    bucket_number = 0
    leftover_count = 0

    x_axis = []
    y_axis = []

    data.sort()

    i = 0
    for b in range(buckets):
        start = b * bucket_size + min_mean
        end = (b+1) * bucket_size + min_mean
        x_axis.append(str(start) + "-" + str(end))
        y_axis.append(0)

        while i < len(data) and data[i] < end:
            y_axis[b] += 1
            i += 1

    return x_axis, y_axis

data = []
path = os.path.dirname(os.path.realpath(__file__)) + "\\"
f = open(path+"data2.txt", "r")
for x in f:
    data.append(int(x))

sample_size = 10 #Hard-coded value for testing purposes
# sample_size = int(input("Please enter the sample size: ")) #Take the sample
while sample_size > len(data):
    sample_size = int(input("\nPlease try again. Your sample size is larger than the amount of data: "))

repetitions = 10000 #Hard-coded value for testing purposes
# repetitions = int(input("\nPlease enter the number of times you want this to repeat: "))

buckets = 20 #Hard-coded value for testing purposes
# buckets = int(input("\nPlease enter the amount of buckets (note than going above 50 may result in performance issues): "))

means = [] #List of all means
means.extend([round(sum(random.sample(data, sample_size))/sample_size, 0) for i in range(repetitions)])
x_axis, y_axis = generate_axes(means, buckets)

plt.rcParams.update({'font.size': 8})
fig, ax = plt.subplots()
graph = ax.bar(x_axis, y_axis, width=0.5,  align='center')
plt.ylabel('Occurrences')
plt.xlabel('Mean Ranges')
plt.title('Statistics')

if buckets < 30:
    ax.set_xticklabels(x_axis, rotation=60)
else:
    ax.set_xticklabels([])

plt.show()
