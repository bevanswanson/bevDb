# BevDB

Start there, explore as you see fit using wiki/google etc. When you get bored let me know and I think building one is actually not that bad a shout as long as we do it in chunks.

If you fancy making a start:

1) find a big list of something (could be anything, names, products) on the internet that you can download as a text file.
2) Then write me an application (no front end needed if that's easier,  any language you like) that takes a search term, and finds me the position (row number) of that term in the text file.

Don't do anything clever about speed at this point or wildcard searches, just find it for me and output the row number(s) it appears on.
Should take no more than 1-2 hrs to do?

Here's maybe a nice data set. So for example we'll say : FInd me "Estany de les Abelletes" and the app will return "5"

- get a file
- take that file
- find a string in that file
- return what line it appears on

EXTRA:

- take a number and do that search that many times.

## Pseudo

- Select a file
for i in number: {
- Read file line by line
- create a results iterable
- if line contains string push that line number to the iterable
- return the iterable.
}

## Running
`pipenv run python main.py`