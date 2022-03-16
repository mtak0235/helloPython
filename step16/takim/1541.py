expression=list(input())

word=''
chunks=[]
words=[]


for j in range(len(expression)):
    
        
    if expression[j] in '0123456789':
        word+=expression[j]
        
    elif expression[j]=='+':
        words.append(int(word))
        word=''
    elif expression[j]=='-' :
       
        words.append(int(word))
        chunks.append(sum(words))
        word=''
        words=[]
    if j== len(expression)-1:
       
        words.append(int(word))
    
        chunks.append(sum(words))
        word=''
        words=[]
result=chunks[0]
for i in range(1,len(chunks)):
    result-=chunks[i]
print(result)
    
        
    
