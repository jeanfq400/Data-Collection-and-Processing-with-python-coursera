#The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.


nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

output = nested[1][2]


#Below, a list of lists is provided. Use in and not in tests to create variables
#with Boolean values. See comments for further instructions.


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = False
for ch in lst[2]:
    if 'yellow' in ch:
        yellow = True



#Test to see if 4 is in the second list of lst. Save to variable ``four``
for num in lst:
    if 4 in num:
        four = True
    else:
        four = False




#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = False
for char in lst[0]:
    if 'orange' in char:
        orange = True


#Below, we’ve provided a list of lists. Use in statements to create variables with
#Boolean values - see the ActiveCode window for further directions.


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for wrd in L:
        if 'hola' in wrd:
            test1 = True
        else:
            test1 = False

# Test if [5, 8, 7] is in the list L. Save to variable name test2
numero = L[0]
for num in L:
    if numero == num:
        test2 = True




# Test if 6.6 is in the third element of list L. Save to variable name test3

for fl in L:
    if 6.6 in fl:
        test3 = True

#Provided is a nested data structure. Follow the instructions in the comments below.
#Do not hard code.


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = False
for ch in nested.keys():
    if "data" in ch:
        data = True

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = False
for num in nested.values():
    if 24 in num:
        twentyfour = True
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = False
for w in nested.keys():
    if 'whole' in w:
        whole = True

    else:
        False

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = False
for k in nested:
    if 'physics' in k:
        physics = True

    else:
        False

#The variable nested_d contains a nested dictionary with the gold medal counts for
#the top four countries in the past three Olympics. Assign the value of Great
#Britain’s gold medal count from the London Olympics to the variable london_gold.
#Use indexing. Do not hardcode.


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

london_gold = nested_d['London']['Great Britain']

#Below, we have provided a nested dictionary. Index into the dictionary to create
#variables that we have listed in the ActiveCode window.


sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]

# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women'][:]

# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]


#Given the dictionary, nested_d, save the medal count for the USA from all three
#Olympics in the dictionary to the list US_count.


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
US_count = []

US_count.append(nested_d['Beijing']['USA'])
US_count.append(nested_d['London']['USA'])
US_count.append(nested_d['Rio']['USA'])


#Iterate through the contents of l_of_l and assign the third element of sublist
#to a new list called third.


l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []
for ch in l_of_l:
    third.append(ch[2])


#Given below is a list of lists of athletes. Create a list, t, that saves only the
#athlete’s name if it contains the letter “t”. If it does not contain the letter “t”,
#save the athlete name into list other.


athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []
for ch in athletes:
    for wrd in ch:
        if "t" in wrd:
            t.append(wrd)
        else:
            other.append(wrd)
            
