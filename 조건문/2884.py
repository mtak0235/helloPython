hour, min = map(int, input().split())

if (min < 45) :	
    if (hour == 0) :	
        hour = 23
        min += 60
    else :	
        hour -= 1	
        min += 60
        
print(hour, min-45)	
