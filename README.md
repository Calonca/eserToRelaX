# eserToRelaX
##### Table of Contents  
[Example](#example)  
[Requirements](#requirements)  
[Usage](#usage)
    

## Example
This script generates a database usable in [RelaX](http://dbis-uibk.github.io/relax/landing) 

It transform input like:

```
  TableName1(num,name)
  TableName2(date,columnNameB)
```

into:

```
group: eserToRelax
description[[

This database was made with eserToRelaX,
you can find it here: https://github.com/Calonca/eserToRelaX

]]

TableName1 = {num, name
1, lo
1, a
0, b
2, lo
0, b}

TableName2 = {date, columnNameB
2004-05-15, lo
2004-05-15, lo
2004-05-15, b
1997-11-04, lo
2021-11-04, th}
```

## Requirements
You need Python 3 nad the module unidecode<br>
You can install unidecode using pip.


## Usage
1. Open a terminal window in the folder where the script is located and run

```
python3 eserToRelaX.py
```

2. Copy the input into the clipboard and press enter
3. Copy the output inside RelaX Group Editor
4. Click on preview
5. Click on "use Group in editor" (click multiple times if it doesn't work)
