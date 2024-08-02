import random

NumFrames = int(input("Enter the number of frames you want in the memory: "))
FrameSize = int(input("Enter the frame size: "))

MemManager = [-1] * NumFrames
NumProcess = int(input("Enter the number of processes you want to store: "))
PageTables = list()

processID = 0

while processID < NumProcess:

    pSize = int(input("Enter your process size: "))
    NumPages = int(pSize/FrameSize)
    PageTable = [-1] * NumPages

    for i in range(NumPages):
        flag = 0
        while flag == 0:
            frame = random.randint(0, NumFrames - 1)
            if MemManager[frame] == -1:
                flag = 1
                MemManager[frame] = [processID, i]
                PageTable[i] = frame

    PageTables.append(PageTable)
    processID += 1

def findPage(processID, byte):
    Pages = PageTables[processID]
    page = int(byte / FrameSize)
    offSet = byte % FrameSize
    frame = Pages[page]
    return frame, frame+offSet


print(MemManager)
print(PageTables)

processID = int(input("Enter the process id you want to search: "))
byte = int(input("Enter the byte which CPU wants from process: "))
frame, loc = findPage(processID, byte)
print(frame)
print(frame + loc)
