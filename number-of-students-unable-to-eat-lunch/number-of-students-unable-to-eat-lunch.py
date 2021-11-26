class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_types = {}
        for val in students:            # Time: O(N)
            if val in student_types:
                student_types[val] += 1
            else:
                student_types[val] = 1
        # print(student_types)

        for sandwich_type in sandwiches:        # Time: O(N)
            if sandwich_type not in student_types.keys():
                break
            if student_types[sandwich_type] == 0:
                break
            student_types[sandwich_type] -= 1

        return (sum(student_types.values()))       # Time: O(1)

# Time: O(N)
# Space: O(1)