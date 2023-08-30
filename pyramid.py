import random
count=0
def generate_random_array(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]

def sum_adjacent_pairs(arr):
    new_arr = []
    blnk_arr=[]
    
    c=0
    
    
    while c <= count:
        blnk_arr.append(" ")
        c=c+1
       
    
    for i in range(len(arr) - 1):
        
        new_arr.append(arr[i] + arr[i + 1])
    return new_arr

def print_pyramid(arr):
    blnk_arr =[]
    for row in arr:
        global count
        count=count+1
        print(blnk_arr+row)
        if count%2 != 0:
            blnk_arr.append(" ")
            
            
        

def main():
    pyramid = []
    original_array = generate_random_array(10, 1, 100)
    pyramid.append(original_array)

    while len(pyramid[-1]) > 1:
        new_row = sum_adjacent_pairs(pyramid[-1])
        pyramid.append(new_row)

    print("Pirámide generada:")
    print_pyramid(pyramid)

if __name__ == "__main__":
    main()