# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541018393_2Unit

def fruits_in_baskets(fruits_arr):
    window_start = 0
    max_fruits = 0
    fruits_freq = {}

    for window_end in range(len(fruits_arr)):
        end_fruit = fruits_arr[window_end]
        if end_fruit not in fruits_freq:
            fruits_freq[end_fruit] = 0
        fruits_freq[end_fruit] += 1

        while len(fruits_freq) > 2:
            start_fruit = fruits_arr[window_start]
            fruits_freq[start_fruit] -= 1
            if fruits_freq[start_fruit] == 0:
                del fruits_freq[start_fruit]
            window_start += 1
        
        max_fruits = max(max_fruits, window_end - window_start + 1)
        # similarly, could've written res = max(res, sum(baskets.values()))

    return max_fruits

Fruit = ['A', 'B', 'C', 'A', 'C']
print(fruits_in_baskets(Fruit))
Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
print(fruits_in_baskets(Fruit))