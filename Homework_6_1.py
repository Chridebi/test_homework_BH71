#TODO 6_1 Написать функцию перевода числа в двоичное и обратно, без использования функции int

print('Vvedite number:')
number = int(input())
spisok_data_2=[]
while number >= 1:
     spisok_data_2.append( number % 2)
     number = number // 2
data_2 = ("").join([str(i) for i in spisok_data_2[::-1]    ] )

data_10=list(data_2)
data_sum_10 = 0
n = len(data_10)
for i in range(0, n ):
     data_sum_10 += int(data_10[i]) * 2**(n-i-1)

print( data_2 )
print (data_sum_10)
