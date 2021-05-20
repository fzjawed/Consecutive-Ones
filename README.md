# Consecutive-Ones
>20th May 2021 09:22 PM

Pfahahhaaha I'm on a roll with these I guess! My initial plan was to do one a day but the easy level ones I'm actually enjoying a bit. 

***Question: You are given a list of integers nums which contains at least one 1. Return whether all the 1s appear consecutively.***

I think when it comes to my code - I am not super efficient with it but I still get ecstatic upong getting the solution :) 

Whatever solution it may be.

For this question I started off a little confused because the hints didn't do much to help me. I was traversing through the list and locating "1" in the list. After finding it I was gonna compare the value before and after it - but I didn't know what to do after that. Roadblock.

The solution I've come up with is to find the indexes of each of the 1s and put them in a new list. I will then compare to see if the difference between each element in this list is greater than 1. If it is greater than 1, that means the indexes are far apart thus the 1s are not consecutive. 

A little long I guess!
