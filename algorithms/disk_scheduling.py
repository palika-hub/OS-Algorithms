def first_come_first_serve(sequence , head_position):

    seek_count =0
    prev = head_position 
    for i in sequence:
        seek_count += abs(i-prev)
        prev = i
    sequence_track = [head_position] + sequence
    return sequence_track ,seek_count 

def sstf(sequence , head_position):

    curr_head = head_position 
    cnt = len(sequence)
    visited = [0]*cnt
    sequence_track = [head_position]
    total_seek_time = 0 
    for i in range(cnt):

        min_seek = 1e9
        idx = -1
        for i in range(len(sequence)):

            if visited[i] == 1 :
                continue
            else :
                seek_time = abs(curr_head - sequence[i])
                if seek_time < min_seek :
                    min_seek = seek_time 
                    idx = i 
        sequence_track.append(sequence[idx]) 
        total_seek_time += abs(sequence[idx] - curr_head)
        curr_head = sequence[idx]
        visited[idx] = 1
    
    return sequence_track , total_seek_time 

def scan(sequence , head , direction , disk_size):
    sequence_track = []
    left_track  = []
    right_track = []
    sequence.sort() 
    
    for i in sequence:
        if i <= head :
            left_track.append(i)
        else :
            right_track.append(i)
    if (direction == "LEFT"): 
        
        left_track.reverse()
        if (left_track == [] or left_track[-1] != 0):
            left_track.append(0)
        sequence_track = left_track + right_track
        total_seek_time = head 
        if (right_track != []):
            total_seek_time+= right_track[-1]
    
    else :
        # direction = RIGHT 
        if (right_track == [] or right_track[-1] != disk_size-1) :
            right_track.append(disk_size-1)
        left_track.reverse()
        sequence_track = right_track + left_track 
        total_seek_time = disk_size-1-head 
        
        if (left_track != []):
            total_seek_time += disk_size-1-left_track[-1]
    
    return sequence_track , total_seek_time 

def cscan(sequence , head , disk_size):
    sequence_track = []
    left_track  = []
    right_track = []
    sequence.sort() 
    
    for i in sequence:
        if i <= head :
            left_track.append(i)
        else :
            right_track.append(i)
    total_seek_distance = 0 
    if (right_track == [] or right_track[-1] != disk_size):
        right_track.append(disk_size)
    
    



queue = [176, 79, 34, 60,92, 11, 41, 114] 
head = 50
disk_size = 199 

# print(first_come_first_serve(queue,head))
# print(sstf(queue,head))
print(scan(queue,head,"LEFT",disk_size))



        


