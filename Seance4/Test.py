def main():
    s= 'A'
    get_middle(s)




def get_middle(s):
    c = 0
    
    for i in s :
    
        if len(s)%2 != 0 :
            L = len(s) + 0.5
            
        if c == len(s)/2 : 
            return i
        
        elif c == L :
            return i
        
        c += 1




if __name__=="__main__":
    main()