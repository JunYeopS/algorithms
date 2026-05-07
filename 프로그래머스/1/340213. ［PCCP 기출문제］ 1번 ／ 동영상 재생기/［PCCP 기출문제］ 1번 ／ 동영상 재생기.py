def solution(video_len, pos, op_start, op_end, commands):
    
    def to_sec(time):
        time = list(map(int,time.split(":")))
        m_to_s = time[0] * 60 
        return m_to_s + time[1]
    
    video_len= to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    
    # command loop 
    for i in commands:
        # opening check
        if op_start <= pos < op_end:
            pos = op_end
        if i == "next":
            pos += 10
        else:
            pos -= 10
        if pos > video_len:
            pos = video_len
        if pos < 0:
            pos = 0
    
    if op_start <= pos < op_end:
        pos = op_end 
    
    pos_m = pos // 60
    pos_s = pos % 60
    
    if pos_m < 10:
        pos_m = f"0{pos_m}"
    if pos_s < 10:
        pos_s = f"0{pos_s}"
    
    return f"{pos_m}:{pos_s}"