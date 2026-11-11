class TimeMap:

    def __init__(self):
        self.maps = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.maps:
            self.maps[key] = {}
        self.maps[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maps:
            return ""
        if timestamp in self.maps[key]:
            return self.maps[key].get(timestamp)
        ts = list(self.maps[key].keys())
        
        l, r = 0, len(ts) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if ts[m] <= timestamp:
                res = self.maps[key][ts[m]]
                l = m + 1
            else:
                r = m - 1
        
        return res
        
