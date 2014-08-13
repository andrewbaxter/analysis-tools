analysis-tools
==============

Python scripts for analyzing and comparing various human readable data files.

## cvs_x.py

```bash
cvs_x.py CSVFILE COLUMNS...
```

Prints COLUMNS separated by spaces for every row in CVSFILE.  CVSFILE must have a header.

## json_x.py

```bash
json_x.py JSONFILE FIELDS...
```

Prints FIELDS separated by spaces for every row in JSONFILE.

## subsediff.py

```bash
subsediff.py FILE
```

Highlights characters that are different from the character on the previous line at the same position.  Requires a terminal that supports standard color escape sequences.

## yank.py

```bash
yank.py REGEXES... FILE
```

Uses regexes to pull information from lines in FILE to the beginning of the line.  

Given a line in FILE, for each REGEX: 

1. REGEX is searched against the line.  
2. If there's a match, the first group (if it exists, otherwise the whole match) is printed, followed by a space.  The whole match is erased from the line.  
4. When all regexes have been processed, the remainder of the line is printed.

## disjoin.py

```bash
disjoin.py join|disjoin FILE1 FILE2
```

#### In "join" mode:

Combines lines in FILE1 and FILE2 that match on a key.  The key is always the first space-delimited word.  The key is only printed once per line, at the beginning of the line.

#### In "disjoin" mode:

Prints lines in FILE2 that do not match any lines in FILE1 by the same matching criteria as "join" mode.
