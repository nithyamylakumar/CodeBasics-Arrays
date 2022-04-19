#codebasics- youtube - ARRAY exercise-1

#monthly expenses
expense = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?

extra = expense[0] - expense[1]
print(abs(extra))

# 2. Find out your total expense in first quarter (first three months) of the year.

quarter_1 = expense[0] + expense[1] + expense[2]
print(abs(quarter_1))

#3. Find out if you spent exactly 2000 dollars in any month

a = 2000 in expense
print(a)

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.append(1980)
print(expense)

#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

expense[3]= expense[3] - 200
print(expense)


# exercise 2

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list

length = len(heros)
print("length of the list is",length)

# 2. Add 'black panther' at the end of this list

heros.append('black panther')
print("updated list is", heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'

heros.remove('black panther')
heros.insert(3, 'black panther')
print('Updated:',heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.

heros[1:3]=['doctor strange']
print(heros)

#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros.sort()
print(heros)


# exercise 3:
# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

max = int(input('enter max no.: '))

odd = []

for i in range(max):
    if i%2 != 0:
        odd.append(i)

print('Odd numbers:',odd)

