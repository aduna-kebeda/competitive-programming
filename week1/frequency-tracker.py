class FrequencyTracker:
    def __init__(self):
        self.data = {}
        self.freq = {}

    def add(self, number):
        count = self.data.get(number, 0)
        if self.freq.get(count, 0) > 0:
            self.freq[count] -= 1
        self.data[number] = self.data.get(number, 0) + 1
        self.freq[count + 1] = self.freq.get(count + 1, 0) + 1

    def deleteOne(self, number):
        count = self.data.get(number, 0)
        if count == 0:
            return
        self.freq[count] -= 1
        self.data[number] -= 1
        self.freq[count - 1] = self.freq.get(count - 1, 0) + 1

    def hasFrequency(self, frequency):
        return self.freq.get(frequency, 0) > 0
