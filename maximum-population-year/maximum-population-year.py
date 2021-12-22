class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        def get_first_year(log):

            return log[0]

        logs.sort(key=get_first_year)

        res = -1
        max_population = 0
        population = []
        for log in logs:
            for date in population:
                if date <= log[0]:
                    population.remove(date)

            population.append(log[1])
            if len(population) > max_population:
                max_population = len(population)
                res = log[0]
        return res

#Time: O(N Log N) + O(N * N) => O(N)=len(logs) 
#Space: O(N)