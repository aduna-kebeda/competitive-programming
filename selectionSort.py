class Solution:
    def select(self, arr, i):
        # code here 
        min_idx = i
        for j in range(i + 1, n):
           if arr[j] < arr[min_idx]:
              min_idx = j
        return min_idx

    def selectionSort(self, arr, n):
        # code here
        for i in range(n):
            min_idx = self.select(arr, i)  # Added self. to call the select method
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
