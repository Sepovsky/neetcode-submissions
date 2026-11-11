class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        num_set = set(numbers)

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in seen:
                return list([seen[diff], i + 1])
            seen[numbers[i]] = i + 1