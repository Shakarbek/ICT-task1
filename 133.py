numbers1 = {
    1:"one", 2:"two", 3:"three" , 4:"four", 5:"five" , 6:"six", 7:"seven", 8:"eight", \
    9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", \
    15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"
}
numbers2 = {
    20:"twenty", 30:"thirty", 40:"forty", 50:"fifty",\
    60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"
}

def function(number):
    if number == 0:
        return ""
    if number<20:
        return (numbers1[number])
    elif number < 100:
        a = divmod(number, 10)
        return (numbers2[a[0] * 10] + " " + function(a[1]))
    elif number < 1000:
        a  = divmod(number, 100)
        if a[1] == 0:
            b = "hundred"
        else:
            b = " hundred and "
        return(numbers1[a[0]] + b + function(a[1]))


n = int(input())
print(function(n))