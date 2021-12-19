class TimeMap:
    def __init__(self):
        self.dictionary = {} # to save data
        self.temp_array = [] # to search time stamp
        
    def binarySearch(self,timestamp):
        arr = self.temp_array
        low = 0
        high = len(arr) - 1
        while(low <= high):
            mid = (low + high) // 2
            if(arr[mid][1] == timestamp):
                return arr[mid][0]
            if(arr[mid][1] > timestamp):
                high = mid-1
            else:
                low = mid+1
        if(low == 0 and timestamp < arr[low][1]):
            return ''
        return arr[low-1][0]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key in self.dictionary.keys()):
            self.dictionary[key].append([value,timestamp])
        else:
            self.dictionary[key] = [[value,timestamp]]
        
    def get(self, key: str, timestamp: int) -> str:
        self.temp_array = self.dictionary[key]
        return self.binarySearch(timestamp)

#unit test        
timeMap = TimeMap()

timeMap.set("foo", "bar", 1)

output_1 = timeMap.get("foo", 1)
print("output 1 is " + output_1) # return "bar"

output_2 = timeMap.get("foo", 3)
print("output 2 is " + output_2) # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".

timeMap.set("foo", "bar2", 4)

output_3 = timeMap.get("foo", 4);
print("output 3 is " + output_3) # return "bar2"

output_4 = timeMap.get("foo", 5);
print("output 4 is " + output_4) # return "bar2"

