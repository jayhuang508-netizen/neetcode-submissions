class TimeMap:

    def __init__(self):
        self.store: dict[str, list[tuple[int, str]]]={}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store.keys():
            self.store[key] = []
        self.store[key].append((timestamp, value))
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys():
            return ""
        if len(self.store[key]) == 0:
            return ""
        value_list = self.store[key]
        if value_list[0][0] > timestamp:
            # all values are after timestamp
            return ""
        res = ""
        l, r = 0, len(value_list) - 1
        while l <= r:
            m = l+(r-l)//2
            if value_list[m][0] > timestamp:
                r = m-1
            elif value_list[m][0] < timestamp:
                res = value_list[m][1]
                l = m + 1
            else:
                return value_list[m][1]
        return res
        
