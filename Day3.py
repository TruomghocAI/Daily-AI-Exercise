def find_squared_root(a):
    e = 0.001
    x0 = a
    
    while (1):
        fx = x0**2 - a
        fdx = 2*x0        
        x1 = x0 - (fx/fdx)        
        if abs(x1 - x0) < e:
            return x1
        x0 = x1
        

if __name__ == "__main__":
    print(find_squared_root(3))
    