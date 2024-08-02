def FirstFit(blockSize, m, processSize, n): 
    visited = [0] * m
    allocation = [-1] * n 
    for i in range(n): 
        for j in range(m): 
             if blockSize[j] >= processSize[i] and visited[j] == 0: 
                allocation[i] = j + 1
                visited[j] = 1
                break		
    return allocation 

def NextFit(blockSize, m, processSize, n):

    allocation = [-1] * n
    visited = [0] * m
    j = 0
    t = m-1
    for i in range(n):
        while j < m:
            if blockSize[j] >= processSize[i] and visited[j] == 0:

                allocation[i] = j + 1

                visited[j] = 1

                t = (j - 1) % m
                break
            if t == j:
                t = (j - 1) % m
                break
            j = (j + 1) % m
			
    return allocation

def BestFit(blockSize, m, processSize, n): 

    allocation = [-1] * n  
    visited = [0] * m
    for i in range(n): 

        bestIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i] and visited[j] == 0: 
                if bestIdx == -1:  
                    bestIdx = j  
                elif blockSize[bestIdx] > blockSize[j]:  
                    bestIdx = j 

        if bestIdx != -1: 

            allocation[i] = bestIdx + 1
            visited[bestIdx] = 1

    return allocation

def WorstFit(blockSize, m, processSize, n): 
 
    allocation = [-1] * n 
    visited = [0] * m
    for i in range(n): 
 
        wstIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i] and visited[j] == 0: 
                if wstIdx == -1:  
                    wstIdx = j  
                elif blockSize[wstIdx] < blockSize[j]:  
                    wstIdx = j 
 
        if wstIdx != -1: 

            allocation[i] = wstIdx + 1
            visited[wstIdx] = 1

    return allocation


blockSize = [100, 500, 200, 300, 600] 
processSize = [212, 417, 112, 426] 
m = len(blockSize) 
n = len(processSize) 

# allocation = FirstFit(blockSize, m, processSize, n) 
# allocation = NextFit(blockSize, m, processSize, n) 
# allocation = BestFit(blockSize, m, processSize, n) 
allocation = WorstFit(blockSize, m, processSize, n) 

print(" Process No. Process Size	 Block no.") 
for i in range(n): 
	print(" ", i + 1, "		 ", processSize[i], 
					"		 ", end = " ") 
	if allocation[i] != -1: 
			print(allocation[i]) 
	else: 
		print("Not Allocated")
	
