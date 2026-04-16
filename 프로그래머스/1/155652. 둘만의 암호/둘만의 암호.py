def solution(s, skip, index):
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    s = list(s.strip())
    skip = list(skip.strip())
    
    for i in skip:
        if i in alphabet:
            alphabet.remove(i)
            
    print(alphabet)
    
    if len(alphabet)>1:
        for i in range(len(s)):
            offset = alphabet.index(s[i])
            print(offset)
            if offset + index >= len(alphabet):
                pos =  (offset + index) % len(alphabet) 
                s[i] = alphabet[pos]
            else:
                s[i] = alphabet[offset+index]
        answer = ("".join(s))
    else:
        answer = ""
                
    return answer