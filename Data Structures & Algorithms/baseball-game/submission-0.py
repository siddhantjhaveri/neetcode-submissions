class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        l=0
        for i in range(len(operations)):
            if operations[i] == 'C':
                record.pop()
                l-=1
            elif operations[i] == '+':
                record.append(record[l-1] + record[l-2])
                l+=1
            elif operations[i] == 'D':
                record.append(2*record[l-1])
                l+=1
            else:
                record.append(int(operations[i]))
                l+=1
            print(record)
        return sum(record)