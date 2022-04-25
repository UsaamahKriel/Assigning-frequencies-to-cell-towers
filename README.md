# Assigning-frequencies-to-cell-towers
You are given a data frame with the location of various towers and you have to assign six unique frequencies to each tower so that towers with the same frequency are far apart and towers with different frequencies are close. This is my attempt at a solution.
This is a good attempt at the problem but it needs some tidying up and comments. One glaring issue with this algorthm is that when it assigns a new frequency to a tower it assigns the lowest value first. This leads to there being more towers with a lower frequency than at a higher frequency.
