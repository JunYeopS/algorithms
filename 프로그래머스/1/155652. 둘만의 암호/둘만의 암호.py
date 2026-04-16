def solution(s, skip, index):
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    s = list(s.strip())
    skip = list(skip.strip())
    
    for i in skip:
        if i in alphabet:
            alphabet.remove(i)
            
    for i in range(len(s)):
        s[i] = alphabet[(alphabet.index(s[i]) + index) % len(alphabet)]

    answer = ("".join(s))
                
    return answer