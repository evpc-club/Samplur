import numpy as np
import matplotlib.pyplot as plt
import random, math
plt.rcdefaults()

#Return new rounded dictionary
def round_dict(dict, round_value):
    result={}
    for key in dict:
        temp = means[key]
        new_key = round(key, round_value)
        result[new_key] = temp
    return result

def add_labels(rects, max_frequency):
    smallest_x = 0
    for rect in rects:
        height = rect.get_height()
        if height == max_frequency:
            if (rect.get_x() - smallest_x) > 20:
                smallest_x = rect.get_x()
                ax.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(rect.get_x()),ha='center', va='bottom')
            elif (rect.get_x() - smallest_x) > 10:
                ax.text(rect.get_x() + rect.get_width()/2., 1.03 * height,'%d' % int(rect.get_x()),ha='center', va='bottom')
file = []
f = open("data.txt", "r")
for x in f:
    file.append(int(x))

sample_size = 10 #Hard-coded value for testing purposes
# sample_size = int(input("Please enter the sample size: ")) #Take the sample
while sample_size > len(file):
    sample_size = int(input("\nPlease try again. Your sample size is larger than the amount of data: "))

repetitions = 100 #Hard-coded value for testing purposes
# repetitions = int(input("\nPlease enter the number of times you want this to repeat: "))

means = {} #Dictionary. Key = mean, value = amount

for i in range(repetitions): #Record the means and add to aggregate list
    temp_mean = sum(random.sample(file, sample_size))/sample_size
    temp_mean = round(temp_mean, 0)
    if temp_mean in means.keys(): #Check if the pre-existing mean exists in dictionary
        means[temp_mean] += 1
    else:
        means[temp_mean] = 1 #Initialize dict[temp_mean] to have frequency 1

max_mean = int(max(means.keys()))
min_mean = int(min(means.keys()))

round_value=round(int(math.log(max_mean/min_mean) - 1), 1) #Constant equation to round. Defined by Yashika.
means = round_dict(means,round_value)

x_axis = means.keys()
y_axis = [means[key] for key in means] #Y-axis is the dictionary value (frequency) of every value in x

x_ticks = range(min_mean,max_mean,(max_mean-min_mean)//10)

plt.rcParams.update({'font.size': 8})
fig, ax = plt.subplots()
bar1 = ax.bar(x_axis, y_axis, width=3,  align='center', alpha=0.5)
plt.xticks(x_ticks)
plt.ylabel('Occurrences')
# plt.title('Statistics')

add_labels(bar1, max(y_axis))

plt.show()
