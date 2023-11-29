# OURsql
OURsql was one of the most interesting challenge in this CTF. It seems it was a binary that read a `database` ~~a text file~~ and used it for some queries. <br>
Upon analysis, I noticed that when the maximum number of users was reached, the program began to overwrite users at the beginning of the list. This allowed me to overwriting the password of the user with the flag. The exploit in fact involved spamming registrations until the user with the flag was overwritten. Afterward, logging in would have solved the challenge.

### Challenge Description
> Check out OUR new database!