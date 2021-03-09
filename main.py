emojiList = ["😋", "🌈","🦋", "🧁", "🎧", "🌉", "💜"]

#1. Using a for loop, print out each emoji in your list
#2. Print out the lenght of your list
#3. Print out the 4th item in your list

for index in emojiList:
  print(index)

print(" ")

print(len(emojiList))

print(' ')

print(emojiList[3])

#create a favoriteEmoji variable and set that equal to your favorite emoji in the list
favoriteEmoji = emojiList[1]

#using a for loop, ake a pyramid with your favorite emoji 

print(' ') 

for index in range (1,11):
  print((favoriteEmoji + " ")*index)
  index += 1

#upside down pyramid

print(" ")

for index in range(10,0,-1):
  print((favoriteEmoji + ' ')*index)
  index += 1

#make the pyramid right aligned 
for index in range (11,0,-1):
  print((" " * index) + favoriteEmoji * (11 - index))