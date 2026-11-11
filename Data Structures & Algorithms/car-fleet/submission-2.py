class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        last = cars.pop()
        ans = 1
        while cars:
            car = cars.pop()
            if ((target - car[0]) / car[1]) > ((target - last[0]) / last[1]):
                ans += 1
                last = car
        return ans