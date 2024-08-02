
class FirstFit:
    def __init__(self,m=10,blockSize=[100,50,70,90,200,110,150,80,100,50]):
        self.blockSize = blockSize
        self.processSize = []
        self.m = m
        self.n = 0
        self.allocation = []
        self.process = 0
        self.target = 0
        for i in range(m):
            self.allocation.append([])
    def FirstFit(self,blockSize, m, processSize, n): 

        allocation = [-1] * n 

        for i in range(n): 
            for j in range(m): 
                if blockSize[j] >= processSize[i]: 
                    allocation[i] = j + 1
                    blockSize[j] -= processSize[i] 
                    break
                
        return allocation 
    def __addnew__(self,processSize):
        progress = []
        issuccessful = False
        for target in range(self.m):
            if self.blockSize[target] >= processSize:
                self.allocation[target].append((self.process,processSize))
                self.blockSize[target] -= processSize
                issuccessful = True
                progress.append((target,processSize,issuccessful))
                break
            else:
                progress.append((target,processSize,issuccessful))
          
        if not issuccessful:
            progress.append(-1)
        return progress
    def reset(self):
        self.blockSize = [100,50,70,90,200,110,150,80,100,50]
        self.allocation = []
        self.process = 0
        self.target = 0
        self.m = 10
        for i in range(self.m):
            self.allocation.append([])
    
class NextFit:
    def __init__(self, m=10, blockSize=[100,50,70,90,200,110,150,80,100,50]):
        self.blockSize = blockSize
        self.processSize = []
        self.m = m
        self.n = 0
        self.allocation = []
        self.process = 0
        self.target = 0
        self.fromnext = 0
        for i in range(m):
            self.allocation.append([])

    def next_fit(self, processSize):
        allocation = [-1] * self.n
        issuccessful = False
        j = self.target

        for i in range(self.n):
            while j < self.m:
                if self.blockSize[j] >= processSize[i]:
                    allocation[i] = j + 1
                    self.allocation[j].append((self.process, processSize[i]))
                    self.blockSize[j] -= processSize[i]
                    issuccessful = True
                    break
                j = (j + 1) % self.m

            if not issuccessful:
                j = 0
                self.target = 0
                allocation[i] = -1
            else:
                self.target = j

        return allocation
    def __addnew__(self,processSize):
        progress = []
        issuccessful = False
        j = self.target
        count = 0
        while j < self.m:
            if self.blockSize[j] >= processSize:
                self.allocation[j].append((self.process,processSize))
                self.blockSize[j] -= processSize
                issuccessful = True
                progress.append((j,processSize,issuccessful))
                count+=1
                break
            else:
                count+=1
                if (count==self.m):
                    progress.append(-1)
                    break
                else:
                    progress.append((j,processSize,issuccessful))
            

            
            j = (j + 1) % self.m
        if not issuccessful:
            j = 0
            self.target = 0
            progress.append(-1)
        else:
            self.target = j
        return progress
    def reset(self):
        self.blockSize = [100,50,70,90,200,110,150,80,100,50]
        self.allocation = []
        self.process = 0
        self.target = 0
        self.m = 10
        for i in range(self.m):
            self.allocation.append([])

class BestFit:
    def __init__(self, m=10, blockSize=[100,50,70,90,200,110,150,80,100,50]):
        self.blockSize = blockSize
        self.processSize = []
        self.m = m
        self.n = 0
        self.allocation = []
        self.process = 0
        self.target = 0
        for i in range(m):
            self.allocation.append([])

    def best_fit(self, processSize):
        allocation = [-1] * self.n
        issuccessful = False

        for i in range(self.n):
            bestIdx = -1
            for j in range(self.m):
                if self.blockSize[j] >= processSize[i]:
                    if bestIdx == -1 or self.blockSize[bestIdx] > self.blockSize[j]:
                        bestIdx = j

            if bestIdx != -1:
                allocation[i] = bestIdx + 1
                self.allocation[bestIdx].append((self.process, processSize[i]))
                self.blockSize[bestIdx] -= processSize[i]
                issuccessful = True

            if not issuccessful:
                allocation[i] = -1

        return allocation

    def __addnew__(self, processSize):
        progress = []
        issuccessful = False

        bestIdx = -1
        for j in range(self.m):
            if self.blockSize[j] >= processSize:
                if bestIdx == -1 or self.blockSize[bestIdx] > self.blockSize[j]:
                    bestIdx = j
            progress.append((j, processSize, issuccessful)) 

        if bestIdx != -1:
            self.allocation[bestIdx].append((self.process, processSize))
            self.blockSize[bestIdx] -= processSize
            issuccessful = True
            progress.append((bestIdx, processSize, issuccessful))
        else:
            progress.append(-1)

        return progress
    def reset(self):
        self.blockSize = [100,50,70,90,200,110,150,80,100,50]
        self.allocation = []
        self.process = 0
        self.target = 0
        self.m = 10
        for i in range(self.m):
            self.allocation.append([])

class WorstFit:
    def __init__(self, m=10, blockSize=[100,50,70,90,200,110,150,80,100,50]):
        self.blockSize = blockSize
        self.processSize = []
        self.m = m
        self.n = 0
        self.allocation = []
        self.process = 0
        self.target = 0
        for i in range(m):
            self.allocation.append([])

    def worst_fit(self, processSize):
        allocation = [-1] * self.n
        issuccessful = False

        for i in range(self.n):
            wstIdx = -1
            for j in range(self.m):
                if self.blockSize[j] >= processSize[i]:
                    if wstIdx == -1 or self.blockSize[wstIdx] < self.blockSize[j]:
                        wstIdx = j

            if wstIdx != -1:
                allocation[i] = wstIdx + 1
                self.allocation[wstIdx].append((self.process, processSize[i]))
                self.blockSize[wstIdx] -= processSize[i]
                issuccessful = True

            if not issuccessful:
                allocation[i] = -1

        return allocation

    def __addnew__(self, processSize):
        progress = []
        issuccessful = False

        wstIdx = -1
        for j in range(self.m):
            if self.blockSize[j] >= processSize:
                if wstIdx == -1 or self.blockSize[wstIdx] < self.blockSize[j]:
                    wstIdx = j
            progress.append((j, processSize, issuccessful))

        if wstIdx != -1:
            self.allocation[wstIdx].append((self.process, processSize))
            self.blockSize[wstIdx] -= processSize
            issuccessful = True
            progress.append((wstIdx, processSize, issuccessful))
        else:
            progress.append(-1)

        return progress
    def reset(self):
        self.blockSize = [100,50,70,90,200,110,150,80,100,50]
        self.allocation = []
        self.process = 0
        self.target = 0
        self.m = 10
        for i in range(self.m):
            self.allocation.append([])


# 
# 
# def NextFit(blockSize, m, processSize, n):

#     allocation = [-1] * n
#     j = 0
#     t = m-1
#     for i in range(n):
#         while j < m:
#             if blockSize[j] >= processSize[i]:

#                 allocation[i] = j + 1

#                 blockSize[j] -= processSize[i]

#                 t = (j - 1) % m
#                 break
#             if t == j:
#                 t = (j - 1) % m
#                 break
#             j = (j + 1) % m
			
#     return allocation

# def BestFit(blockSize, m, processSize, n): 

#     allocation = [-1] * n  

#     for i in range(n): 

#         bestIdx = -1
#         for j in range(m): 
#             if blockSize[j] >= processSize[i]: 
#                 if bestIdx == -1:  
#                     bestIdx = j  
#                 elif blockSize[bestIdx] > blockSize[j]:  
#                     bestIdx = j 

#         if bestIdx != -1: 

#             allocation[i] = bestIdx + 1

#             blockSize[bestIdx] -= processSize[i]

#     return allocation

# def WorstFit(blockSize, m, processSize, n): 
 
#     allocation = [-1] * n 

#     for i in range(n): 
 
#         wstIdx = -1
#         for j in range(m): 
#             if blockSize[j] >= processSize[i]: 
#                 if wstIdx == -1:  
#                     wstIdx = j  
#                 elif blockSize[wstIdx] < blockSize[j]:  
#                     wstIdx = j 
 
#         if wstIdx != -1: 

#             allocation[i] = wstIdx + 1
    
#             blockSize[wstIdx] -= processSize[i] 

#     return allocation


# # blockSize = [100, 500, 200, 300, 600] 
# # processSize = [212, 417, 112, 426] 
# # m = len(blockSize) 
# # n = len(processSize) 

# # # allocation = firstFit(blockSize, m, processSize, n) 
# # # allocation = NextFit(blockSize, m, processSize, n) 
# # # allocation = BestFit(blockSize, m, processSize, n) 
# # allocation = WorstFit(blockSize, m, processSize, n) 

# # print(" Process No. Process Size	 Block no.") 
# # for i in range(n): 
# # 	print(" ", i + 1, "		 ", processSize[i], 
# # 					"		 ", end = " ") 
# # 	if allocation[i] != -1: 
# # 			print(allocation[i]) 
# # 	else: 
# # 		print("Not Allocated")
	
