import random

class FourthSem:
    def __init__(self):
        self.RollNum = [f"Roll{str(i+1).zfill(2)}" for i in range(20)]
        self.Test1Marks = [random.randint(40, 100) for _ in range(20)]
        self.Test2Marks = [random.randint(40, 100) for _ in range(20)]
        self.Test3Marks = [random.randint(40, 100) for _ in range(20)]

    def calculateClassAverage(self):
        avg1 = sum(self.Test1Marks) / 20
        avg2 = sum(self.Test2Marks) / 20
        avg3 = sum(self.Test3Marks) / 20
        print(f"\nClass Average for Test 1: {avg1:.2f}")
        print(f"Class Average for Test 2: {avg2:.2f}")
        print(f"Class Average for Test 3: {avg3:.2f}")

    def calculateStudentAverages(self):
        print("\n--- Student Averages ---")
        for i in range(20):
            avg = (self.Test1Marks[i] + self.Test2Marks[i] + self.Test3Marks[i]) / 3
            print(f"{self.RollNum[i]} - Avg: {avg:.2f}")

    def displayTopAndBottomScores(self):
        for test_num, marks in enumerate([self.Test1Marks, self.Test2Marks, self.Test3Marks], start=1):
            sorted_scores = sorted(zip(self.RollNum, marks), key=lambda x: x[1], reverse=True)
            print(f"\nTest {test_num} - Top 5 Scores:")
            for roll, score in sorted_scores[:5]:
                print(f"{roll}: {score}")

            print(f"Test {test_num} - Bottom 5 Scores:")
            for roll, score in sorted_scores[-5:]:
                print(f"{roll}: {score}")

    def displayAllMarks(self):
        print("\n--- All Students' Marks ---")
        for i in range(20):
            print(f"{self.RollNum[i]} - T1: {self.Test1Marks[i]}, T2: {self.Test2Marks[i]}, T3: {self.Test3Marks[i]}")

fourth_sem_class = FourthSem()
fourth_sem_class.displayAllMarks()
fourth_sem_class.calculateClassAverage()
fourth_sem_class.calculateStudentAverages()
fourth_sem_class.displayTopAndBottomScores()



