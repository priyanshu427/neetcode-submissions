# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        fetch = self.store.get(key, [])
        vprev = ""
        l, r = 0, len(fetch) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if fetch[mid][1] <= timestamp:
                vprev = fetch[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return vprev


# Pattern: Hash Map of Sorted Lists + Upper-Bound Binary Search (track best valid <= timestamp)
# Time: O(1) set, O(log n) get | Space: O(total entries)
