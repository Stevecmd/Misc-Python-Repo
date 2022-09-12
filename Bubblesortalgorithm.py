# Bubble sort algorithm
arr = [7,6,4,5,7,9,2,1,4,5]

def bubbleSort(sequence):
    q = len(sequence)
    for i in range(q - 1):
        for j in range(q - 1 - i):
            if(sequence)[j] > sequence[j + 1]:
                temp = sequence[j]
                sequence[j] = sequence[j + 1]
                sequence[j + 1] = temp
    return sequence

print(bubbleSort(arr))