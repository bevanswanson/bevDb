# BevDB

Start there, explore as you see fit using wiki/google etc. When you get bored let me know and I think building one is actually not that bad a shout as long as we do it in chunks.

If you fancy making a start:

1) find a big list of something (could be anything, names, products) on the internet that you can download as a text file.
2) Then write me an application (no front end needed if that's easier,  any language you like) that takes a search term, and finds me the position (row number) of that term in the text file.

Don't do anything clever about speed at this point or wildcard searches, just find it for me and output the row number(s) it appears on.
Should take no more than 1-2 hrs to do?

Here's maybe a nice data set. So for example we'll say : Find me "Estany de les Abelletes" and the app will return "5"

- get a file
- take that file
- find a string in that file
- return what line it appears on

EXTRA:

- take a number and do that search that many times.

## Running

`pipenv run python bevdb [term, times]`

## Further tasks

Find a suitable text file where you can search for multiple things e.g. https://download.geonames.org/export/dump/

Write an application that searches through the first word of the first column  of that file for a search term exact match, then returns all the rows with that text

Run 1000 times to get a baseline time

What determines the speed?

Make the file shorter, how long does it take now?

Create another file, this one contains the possible search terms in the first column, and a list of the row numbers you find it on. Then use this file to return the same result as (3) above.
The file will look something like:


Is it any faster?

Now I want the search to return the latitude value for each search term - this is the 6th field in the file. So I search for e.g."Font" and get back "42.52342, 42.5557…"
Do the search without using your index from (11)
Do it with the index - look up the row numbers for "Font" and then use the full file to get the latitudes
How do the times compare? How do you explain it?

Write an additional search mode for your app. It's pretty much the same, except instead of writing the index as Pic -> line numbers, write is as term ->Offset at the start of the line.
e.g. Pic -> 0, 272, 414…
You'll also have to add another type of search, that doesn’t go through line by line, and instead can go straight to an offset in file.
Using this mode, repeat the latitude search - how does the speed compare? Why?

Now you'll write a new index, this time go through the whole file line by line and write another file that contains term, latitude -> offsets of lines
e.g.


Repeat the search from 17 using this new index i.e. give me all the latitudes for "Roc"
How do the speeds compare?

Write a new index, like (27) but this time it will be sorted by search term i.e. all the Pics are together, all the Rocs are together
Do the same latitude search - which is faster, this one or the one from 27?
This one CAN be faster, but you will have to change the search method too - look up "binary search" or "binary chop" and mplement it for this index search
Why does this speed improvement require sorting?

From now on, use the index & search method from 34-37

Write a function so I can say "Give me all the data for 'Pic's that have a latitude between X and Y"
Compare it to what it would have to do if you didn't use the index.

Write a wildcard search e.g. "Find me the latitudes for places that end with 'ic'" or "Start with 'Ro'"
What slows this down even though you have a nice index?

CHANGING DATA

Ignoring indexes now, change your app so I can say "update the first field to be x where the row number is y" - this should change the actual file to have the new value(s) e.g. update row 4, set the road name to be "Roc de les Abelettes"

Similarly, add the ability to say "insert a road at x row number" i.e. so I can say, at row number 10, insert a new row "11111, Pic De Bevan, Pic De Bevan, etc….."
What is the most costly part of this operation?
Where's the cheapest place to actually insert this row, and why is it the cheapest? Cheapest = least time, least hardware resource etc

Add the ability to delete row X.
Is this expensive, can you see any potential future drawbacks with deleting rows?
Is it better, when deleting, to leave a blank row in its place, or to really delete it?

Now, let's index this table again - with the index you last used from step 24-37
How do you have to change your update function now?
What do you think about the cost of unindexed table update vs indexed table update?

Add a row again, do you need to update the function to do anything with the index?
What's the cheapest way to insert a row to an indexed table?
Can you do this and somehow still retain the sorting?

Make a copy of your data file.
Write some code to rearrange the file so that you have 10 rows of data followed by 10 blank rows - so you have the same data but it takes up 2x the space
Ignoring the index, how does this change inserts/updates/deletes, if at all? NB you're allowed to overwrite a blank row if you want to, without shifting everything else downwards

What if you made the same blank row padding in the index file? Change your app to work for inserts/updates/deletes with the padding in the index file and the data file
What happens if I tell you to insert 11 rows at the same position, one after the other?
Has your thinking about deletes changed at all? What if you deleted half the data in your dataset, what impact might this have on your SELECTs?


Congratulations! You now know pretty much everything you need to know to be a data engineer!
These next bits you should just have a quick 30 min read about, and maybe implement in BevanDB if you're having fun! It should all fall into place!
Joining two or more tables
Clustered indexes
Column store/parquet
Execution plans
NoSQL