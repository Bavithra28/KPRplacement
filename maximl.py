CHARS = 256
def max_dis(str, z): 
    cnt = [0] * CHARS 
    for a in range(z): 
        cnt[ord(str[a])] += 1
    max_dist = 0
    for a in range(CHARS): 
        if (cnt[a] != 0): 
            max_dist += 1    
    return max_dist 
def smallestSubstr_maxDistictChar(str): 
    z = len(str)    
    max_dist = max_dis(str, z) 
    minl = z    
    for a in range(z): 
        for b in range(z): 
            subs = str[a:b] 
            subs_lenght = len(subs) 
            sub_dis = max_dis(subs,subs_lenght) 
            if (subs_lenght < minl and 
                max_dist == sub_dis): 
                minl = subs_lenght 
    return minl 
if __name__ == "__main__": 
    str = "AABBBCBB"
    q = smallestSubstr_maxDistictChar(str); 
    print( "Len of small substr", 
           "consisting of max distinct", 
           "chars :", q) 
  
