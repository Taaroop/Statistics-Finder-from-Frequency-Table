# Statistics finder
# Coded by Taaroop

n = int(input("Enter the number of columns: "))

li_value = []
li_freq = []

for i in range(n):
    value = float(input("Enter class value: "))
    freq = int(input("Enter class frequency: "))
    if freq != 0:
        li_value.append(value)
        li_freq.append(freq)

def mean(li_value, li_freq):
    summation = 0
    for j in range(len(li_value)):
        summation += li_value[j]*li_freq[j]

    mean = summation/sum(li_freq)
    return mean

def median(li_value, li_freq_ini):
    li_super = []
    for a in range(len(li_value)):
        li_super.append([li_value[a], li_freq_ini[a]])

    li_value.sort()
    li_freq = []

    for b in range(len(li_value)):
        val = li_value[b]
        for c in li_super:
            if c[0] == val:
                li_freq.append(c[1])

    mid_freq = (sum(li_freq) + 1) / 2

    if int(mid_freq) != float(mid_freq):
        mid_freq_1 = int(mid_freq)
        mid_freq_2 = int(mid_freq) + 1
    else:
        mid_freq_1 = int(mid_freq)
        mid_freq_2 = int(mid_freq)

    cum_freq = 0
    count = 0

    while cum_freq < mid_freq_1:
        cum_freq += li_freq[count]
        count += 1

    val_1 = li_value[count - 1]

    cum_freq = 0
    count = 0

    while cum_freq < mid_freq_2:
        cum_freq += li_freq[count]
        count += 1

    val_2 = li_value[count - 1]

    median = (val_1 + val_2) / 2
    
    return median

def mode(li_value, li_freq):
    f = max(li_freq)
    li_mode = []
    for i in range(len(li_freq)):
        if li_freq[i] == f:
            li_mode.append(li_value[i])

    return li_mode

def my_range(li_value, li_freq):
    range_val = max(li_value) - min(li_value)
    return range_val

print("Mean:", mean(li_value, li_freq))
print("Mode:", mode(li_value, li_freq))
print("Range:", my_range(li_value, li_freq))
print("Median:", median(li_value, li_freq)) # Please keep the median at the end, as it sorts the li_value, which may affect outputs from other functions
