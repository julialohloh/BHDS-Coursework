#Sequence 1
f = open("gbbct1_truncated.seq.txt","r")
seq = f.read()
beginning = "ctgcagc"
end = "//"
beginning_index = seq.find(beginning)
end_index = seq.find(end)
sequence = seq[beginning_index:end_index]

result = ''.join([i for i in sequence if not i.isdigit()])
result_split = result.replace(" ","")
result_split = ''.join(result_split.splitlines())
wordlist = list(result_split.upper())
print(wordlist)

Table_1_A = [1.00, 0.25, 0.00, 0.25, 0.00, 0.25]
Table_1_C = [0.00, 0.00, 0.00, 0.25, 0.25, 0.25]
Table_1_G = [0.00, 0.75, 0.75, 0.00, 0.50, 0.25]
Table_1_T = [0.00, 0.00, 0.25, 0.50, 0.25, 0.25]

i=0
total_list = []
for i in range(len(wordlist)-4):
    score_1 = 0
    score_2 = 0
    score_3 = 0
    score_4 = 0     
    score_5 = 0  
    for char in wordlist[i]:
        if char =='A':
            score_1 = Table_1_A[0]
        elif char =='C':
            score_1 = Table_1_C[0]
        elif char =='G':
            score_1 = Table_1_G[0]  
        elif char=='T':
            score_1 = Table_1_T[0]   
    
    for char in wordlist[i+1]:
        if char =='A':
            score_2 = Table_1_A[1]
        elif char =='C':
            score_2 = Table_1_C[1]
        elif char =='G':
            score_2 = Table_1_G[1]  
        elif char =='T':
            score_2 = Table_1_T[1]   
    
    for char in wordlist[i+2]:
        if char=='A':
            score_3 = Table_1_A[2]
        elif char == 'C':
            score_3 = Table_1_C[2]
        elif char =='G':
            score_3 = Table_1_G[2]  
        elif char =='T':
            score_3 = Table_1_T[2]   
    
    for char in wordlist[i+3]:
        if char =='A':
            score_4 = Table_1_A[3]
        elif char =='C':
            score_4 = Table_1_C[3]
        elif char =='G':
            score_4 = Table_1_G[3]  
        elif char =='T':
            score_4 = Table_1_T[3]   
    
    for char in wordlist[i+4]:
        if char =='A':
            score_5 = Table_1_A[4]
        elif char =='C':
            score_5 = Table_1_C[4]
        elif char =='G':
            score_5 = Table_1_G[4]  
        elif char =='T':
            score_5 = Table_1_T[4]   
            
        total_score = score_1 + score_2 + score_3 + score_4 + score_5
        total_list.append(total_score)     
        
print(total_list)

thresholdlist = []
for values in total_list:
    threshold = round(((values/3.5)*100),2)
    thresholdlist.append(threshold)

print(thresholdlist)
    
for index, x in enumerate(total_list):
    if round(((x/3.5)*100),2) >= 70.0:
        print("The sequence weight for bases in sequence 1 that falls within 70% threshold is " + str(x) +  " and corresponding location is : " + str(index+1))
    else:
        continue

for i, x in enumerate(thresholdlist):
    previous_element = thresholdlist[i-1] if i > 0 else None 
    previous_element2 = thresholdlist[i-2] if i > 0 else None 
    next_element = thresholdlist[i+1] if i < len(thresholdlist)-1 else None  
    if x <=70.0:
        continue   
    elif x >= 70.0 and previous_element < x >= next_element and previous_element2 < x:
        print("The location of match found in Sequence 1 is " + str(i+1) + " with threshold of " + str(x))
        continue

i=0
for i in range(i,len(thresholdlist),5):
    newlist = thresholdlist[i:i+5]
    print(newlist)
    print("Consolidated value of " + str(max(newlist)) + " for Position " + str(i+1) + " to Position " + str(i+5) + " in Sequence 1 ")
