"""Create a list. Get user input on DNA sequences and append it to the list.
Start from i = 1 since DNA seq counts starts from 1 and ends at 5 (becoz first qns is to read 4 dna sequences) and then increment by 1 
in i +=1. """

dna_list=[]
i=0
for i in range(1,5):
    dna_list.append(input("DNA seq" + str(i) + " : "))
    i += 1
print(dna_list)

#Separate each individual bases in dna_list if not the bases are conjoined
dna_list = [list(sub) for sub in dna_list]
print(dna_list)

"""create a dictionary with all the bases and iterate through the length of 
dna_list, starting from [0] thru i incrementing the count of each respective 
bases. Enumerate in order to separate the dna list via the indices"""
n = len(dna_list[0])
dictionary = {'A':[0]*n,'G':[0]*n,'C':[0]*n,'T':[0]*n}
for dna in dna_list:

    for i, dna in enumerate(dna):
        dictionary[dna][i] += 1
        
"""calculate consensus. Iterate through len of dna_list and set max_count to 
start from 0 in order to increment when looping through bases. set max base as 
'X' in order to spot bases 'ACGT' which is expressed as a string and count them.
A if-else loop also sets the criteria such that if the iteration reaches 
max_count, it will print the base with the max_count (max_base) and that 
max-base is equivalent to consensus."""
consensus = ""
for i in range(n):
    max_count = 0
    max_base = 'X'
    for base in "ACGT":
        if dictionary[base][i] == max_count:
            max_base = '-' # more than one base as max
        elif dictionary[base][i] > max_count:
            max_count = dictionary[base][i]
            max_base = base
    consensus += max_base
print("The consensus sequence is " + str(consensus))

"""print out the results of number of bases in a matrix format (tabulated table)
where base is the ACGT as expressed in the dictionary whereas values will be the 
number of ACGT in the dna sequences. .join is to convert the integers into 
string for printing"""
for base, value in dictionary.items():
    print(base,':', " ".join([str(x) for x in value] ))

"""append the values in tabulated table as list so that the list can be multiplied by another
list (multipliers)."""
tabulated = []
for i in dictionary.values():
    tabulated.append(i)
print("The tabulated table is : " + str(tabulated))

"""multiplier list is set at 0.25 (score 1 / 4 sequences) and then * 5 (len of 
dna seq. Multiply the list with the new_list in a for loop and enumerate the 
tabulated list such that the values in the list can be access. i is the index and x in len of tabulated table """
multipliers = [0.25]*5
weighted = [[multipliers[i] * j for j in x]
      for i, x in enumerate(tabulated)]
print("The weighted table is : " + str(weighted))

"""use in-built max function to get the max index in weighted table. Weighted table is zip to return iterables as tuples. Consensus/base score is the sum of all the max index. Remove 0.25 because its means for that column each base has the same count"""
consensus_score = [max(value) for value in zip(*weighted)]
for value in consensus_score:
    if value == 0.25:
        consensus_score.remove(0.25)
    else:
        consensus_score
base_score = float(sum(consensus_score))
print("Consensus score is: " + str(base_score))

Table_1_A = weighted[0]
Table_1_C = weighted[1]
Table_1_T = weighted[2]
Table_1_G = weighted[3]

total_list = []
i = 0
for i in range(len(dna_list)):
    print(dna_list[i])
    for base in dna_list[i][0]:      
        if base =='A':
            score_1 = Table_1_A[0]
        elif base =='C':
            score_1 = Table_1_C[0]
        elif base =='G':
            score_1 = Table_1_G[0]  
        elif base =='T':
            score_1 = Table_1_T[0]   
 
    for base in dna_list[i][1]:
        if base =='A':
            score_2 = Table_1_A[1]
        elif base =='C':
            score_2 = Table_1_C[1]
        elif base =='G':
            score_2 = Table_1_G[1]
        elif base =='T':
            score_2 = Table_1_T[1]  
          
    for base in dna_list[i][2]:
        if base=='A':
            score_3 = Table_1_A[2]
        elif base == 'C':
            score_3 = Table_1_C[2]
        elif base =='G':
            score_3 = Table_1_G[2] 
        elif base =='T':
            score_3 = Table_1_T[2]  
           
    for base in dna_list[i][3]:
        if base =='A':
            score_4 = Table_1_A[3]
        elif base =='C':
            score_4 = Table_1_C[3]
        elif base =='G':
            score_4 = Table_1_G[3] 
        elif base =='T':
            score_4 = Table_1_T[3]   
          
    for base in dna_list[i][4]:
        if base=='A':
            score_5 = Table_1_A[4]
        elif base=='C':
            score_5 = Table_1_C[4]
        elif base =='G':
            score_5 = Table_1_G[4] 
        elif base =='T':
            score_5 = Table_1_T[4]   
    
        total_score = score_1 + score_2 + score_3 + score_4 + score_5
        total_list.append(total_score)        

for index, x in enumerate(total_list):
    print("The weighted score of DNA sequence " + str(index+1) + " is " + str(x))
    
matchlist = []
for values in total_list:
    match = round(((float(values)/ float(base_score))*100),2)
    matchlist.append(match)

for index, x in enumerate(matchlist):
    print("The match probability of sequence " + str(index+1) + " is " + str(x))

i = 0
new_dna_list = []
new_dna_list.append(input("New DNA seq: "))
new_dna_list = [list(sub) for sub in new_dna_list]
print(new_dna_list)

for base in new_dna_list[0][0]:
    if base =='A':
        score_1 = Table_1_A[0]
    elif base =='C':
        score_1 = Table_1_C[0]
    elif base =='G':
        score_1 = Table_1_G[0]  
    elif base =='T':
        score_1 = Table_1_T[0]        
            
for base in new_dna_list[0][1]:
    if base =='A':
        score_2 = Table_1_A[1]
    elif base =='C':
        score_2 = Table_1_C[1]
    elif base =='G':
        score_2 = Table_1_G[1]  
    elif base =='T':
        score_2 = Table_1_T[1]   
            
for base in new_dna_list[0][2]:
    if base=='A':
        score_3 = Table_1_A[2]
    elif base == 'C':
        score_3 = Table_1_C[2]
    elif base =='G':
        score_3 = Table_1_G[2]  
    elif base =='T':
        score_3 = Table_1_T[2]  

for base in new_dna_list[0][3]:
    if base =='A':
        score_4 = Table_1_A[3]
    elif base =='C':
        score_4 = Table_1_C[3]
    elif base =='G':
        score_4 = Table_1_G[3]  
    elif base =='T':
        score_4 = Table_1_T[3] 

for base in new_dna_list[0][4]:
    if base=='A':
        score_5 = Table_1_A[4]
    elif base=='C':
        score_5 = Table_1_C[4]
    elif base =='G':
        score_5 = Table_1_G[4]  
    elif base =='T':
        score_5 = Table_1_T[4]  
    Total_score_new_seq = float(score_1 + score_2 + score_3 + score_4 + score_5)
    match_new_seq = round(((float(Total_score_new_seq)/ float(base_score))*100),2)
                
print("Total score for new DNA seq is " + str(Total_score_new_seq))       
new_threshold = float(input("What is the new threshold(%): "))
if match_new_seq >= new_threshold:
    print("Match probability for new DNA seq: " + str(match_new_seq) + " and it matches")
else:
    print("Match probability for new DNA seq: " + str(match_new_seq) + " and it does not match")
