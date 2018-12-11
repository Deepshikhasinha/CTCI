# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:16:41 2018

@author: dsinha1
"""
# LeetCode
#950. Reveal Cards In Increasing Order
###
#In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

#Initially, all the cards start face down (unrevealed) in one deck.

#Now, you do the following steps repeatedly, until all cards are revealed:

#Take the top card of the deck, reveal it, and take it out of the deck.
#If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
#If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
#Return an ordering of the deck that would reveal the cards in increasing order.

#The first entry in the answer is considered to be the top of the deck.
###
list1 = [17,13,11,2,3,5,7]
sorted_list = sorted(list1)
undonelist = []
done = []
count = 0;
done.append(sorted_list[0])
size = len(sorted_list)
i = 1
j = 1
while i <= size-1:
    if i % 2 != 0:
        undonelist.append(str(j))
    else:
        undonelist.append(sorted_list[j])
        j += 1
    i += 1
#print(undonelist)
values = {}
new_list = undonelist.copy()
i = 0
while len(undonelist) > 0:
    if i % 2 == 0:
        undonelist.append(undonelist[0])
    else:
        if isinstance(undonelist[0],str):
            done.append(sorted_list[len(done)])
            values.update({undonelist[0] : sorted_list[len(done)-1]})
        else:
            done.append(undonelist[0])
    del(undonelist[0])
    i += 1

print(new_list)
print(values)
final_list = []
final_list.append(sorted_list[0])
for i in new_list:
    if i in values:
        final_list.append(values[i])
    else:
        final_list.append(i)

print(final_list)
