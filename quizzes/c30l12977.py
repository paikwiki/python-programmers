# https://school.programmers.co.kr/learn/courses/30/lessons/12977


def getPrimes(num):
    result = [1] * (num + 1)
    result[0:2] = [0, 0]

    for idx in range(2, num):
        mul = 2
        current = idx * mul
        while current <= num:
            if result[current] == 1:
                result[current] = 0
            mul = mul + 1
            current = idx * mul

    return result


def solution(nums):
    nums.sort(reverse=True)
    primes = getPrimes(nums[0] + nums[1] + +nums[2])

    count = 0
    for idx1, num1 in enumerate(nums[:-2]):
        for idx2, num2 in enumerate(nums[idx1 + 1 : -1]):
            for num3 in nums[idx1 + idx2 + 2 :]:
                if primes[num1 + num2 + num3] == 1:
                    count = count + 1

    return count


inputs_and_outputs = [
    # nums, result
    ([1, 2, 3, 4], 1),
    ([1, 2, 7, 6, 4], 4),
]
