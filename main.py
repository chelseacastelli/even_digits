
def findNumbers(nums) -> int:
    total_even = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            total_even += 1

    return total_even


if __name__ == '__main__':
    arr = [12,345,2,6,7896]
    print(findNumbers(arr))

    arr2 = [555,901,482,1771]
    print(findNumbers(arr2))

