import bisect

class IntervalMerger:
    def __init__(self):
        self.intervals = []

    def addInterval(self, start, end):
        # Find position to insert new interval
        bisect.insort(self.intervals, (start, end))
        
        # Merge intervals if they overlap
        merged = []
        for interval in self.intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        self.intervals = merged

    def getIntervals(self):
        return self.intervals

# Example Usage
merger = IntervalMerger()
merger.addInterval(1, 5)
merger.addInterval(6, 8)
merger.addInterval(4, 7)
print(merger.getIntervals())  # Output: [[1, 8]]
