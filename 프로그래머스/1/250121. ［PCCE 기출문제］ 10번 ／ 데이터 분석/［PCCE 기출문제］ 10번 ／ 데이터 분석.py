def solution(data, ext, val_ext, sort_by):
    answer = []
    
    ext_option = ["code", "date", "maximum", "remain"]
    ext_offset = ext_option.index(ext)
     
    for i in range(len(data)):
        if data[i][ext_offset] < val_ext:
            answer.append(data[i])
    
    sort_offset = ext_option.index(sort_by)
    answer.sort(key=lambda x: x[sort_offset])
    
    return answer