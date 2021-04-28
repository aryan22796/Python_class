import multiprocessing 
output=[] #create global variale in this ouput list
def square_number(num):
    for i in num:
        print('output',str(i*i))
        output.append(i*i)
        print(' the result'+str(output))