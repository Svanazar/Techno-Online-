# Assignment 1 Submissions
##Problem 3 Solution Explanation

First if x>y, then we just need to use the x-1 spell repeatedly and we can reach y.
***If x>=y, we can always reach y***

This means that if x happens to be < y, what we need to check is whether it is possible to make x > y, because as soon that happens, we can readily reach y.

Now, for even values of x, spell 1 can be used directly to increase it. However, because of the division by 2, it might be possible that x becomes odd before crossing y. For odd values of x, the only option is to decrease them by 1 to make them even(spell 2), and then apply spell 1. Essentially, this is what the actual process of reaching y from x would look like:

if x is even: apply spell 1
if x is odd: apply spell 2

Now, this process would work for large enough values of x, however for smaller values, we might run into a problem: The increase offered by spell 1 is just not great enough. To see that, let's first consider an even x and apply spell 1 to it. The increase gained is : 3x/2 - x= x/2.

For values of x >=4, the increase is >=2, which means we can get to a greater even number. (eg. if x=6, we get an increase of 3, i.e. now x=9. Since it is odd, we apply spell 2 to make it even, getting 8. This can be repeated to reach greater and greater values as we like.)

***Hence, if x>=4 or equivalently, x>3, we can reach any value of y.***

However, for x<4 i.e. for x=2, the increase is of 1. i.e. we reach x=3. since it is odd, we apply spell 2 to make it even, getting back at 2 again. Hence, the maximum value we can reach is 3.

***If x=2, the maximum y is 3***

The three inferences are what we need to solve the problem.
