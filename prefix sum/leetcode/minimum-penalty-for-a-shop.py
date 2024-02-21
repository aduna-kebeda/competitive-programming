class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total = 0
        pre = [0]
        for customer in customers:
            if customer == "Y":
                total += 1
            pre.append(total)
        penalty = total
        time = 0
        N = 0
        print(pre)
        for i in range(len(customers)):
            if customers[i] == "N":
                N += 1
            if total-pre[i+1]+N < penalty:
                time = i+1
                penalty = total-pre[i+1]+N

        return time