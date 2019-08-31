# A command line
fruits = ['apples', 'oranges', 'pears', 'bananas']
for fruit in fruits:
    print (fruit + ' for sale')
fruitPrices = {'apples': 2.00, 'oranges' : 1.50, 'pears' : 1.75}
for fruit, price in fruitPrices.items():
    if price < 2.00:
        print ('%s cost %f a pound' % (fruit, price))
    else:
        print (fruit + ' are too expensive')

#Writing Scripts    
nums = [1,2,3,4,5,6]
plusOneNums = [x+1 for x in nums]
print (plusOneNums)

#List Comprehensions
strings =['Vietnam', 'HaNoi', 'NgheAn', 'CaMau', 'This', 'That']
lowercase = [x.lower() for x in strings if len(x) > 5]
print (lowercase)

