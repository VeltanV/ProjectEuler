fibo_list=[1,2]
even_sumList=[]
last_entry=0
even_sum=0
threshold=4000000



while last_entry<threshold:

        
        if fibo_list[len(fibo_list)-1]%2==0:   #check if they have remainder

            even_sumList.append(fibo_list[len(fibo_list)-1])
        fibo_list.append(fibo_list[len(fibo_list)-1]+fibo_list[len(fibo_list)-2]) #add the sum of the previous 2
        whole_sum=sum(fibo_list) 
        even_sum=sum(even_sumList)
        last_entry=fibo_list[len(fibo_list)-1]

print even_sum
print even_sumList
print whole_sum





