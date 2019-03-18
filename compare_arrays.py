# Complete the compareTriplets function below.
class Triplets:

    def __init__(self):
        self.result = [0,0]


    def compareTriplets(self, a, b):
        if self.problem_clarity(a, b) and self.originality(a, b):
            return self.difficulty(a, b)
        return None

    def problem_clarity(self, a, b):
        if a[0] < b[0] and a[0] != b[0]:
            self.result[1] = 1
        if a[0] > b[0] and a[0] != b[0]:
            self.result[0] = 1
        return self.result

    def originality(self, a, b):
        if a[1] < b[1] and a[1] != b[1]:
            self.result[1] += 1
        if a[1] > b[1] and a[1] != b[1]:
            self.result[0] += 1
        return self.result

    def difficulty(self, a, b):
        if a[2] < b[2] and a[2] != b[2]:
            self.result[1] += 1
        if a[2] > b[2] and a[2] != b[2]:
            self.result[0] += 1
        return self.result


a = [17, 28, 30]
b = [99, 16, 8]
print(Triplets().compareTriplets(a, b))
