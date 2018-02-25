from random import randint
import time

def generateRandomArray(min, max, length):
    array = []
    for x in range(0, length):
        array.append(randint(min, max))
    return array
    
def bubbleSort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) -i - 1):
            if(array[j+1] < array[j]):
                next = array[j+1]
                current = array[j]
                array[j+1] = current
                array[j] = next
    return array

def measure(sortingMethod, array):
    start = time.time()
    print(sortingMethod(array))
    end = time.time()
    elapsed = end - start
    print(str(elapsed * 1000) + "ms")

def main():
    array = generateRandomArray(0, 300, 10)
    print(array)
    
    measure(bubbleSort, array)

if __name__ == "__main__":
    main()