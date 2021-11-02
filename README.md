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

2. Copy the input into the clipboard![image](https://user-images.githubusercontent.com/36551215/139943273-d9b62693-bb3e-48cc-93d8-fda60d602514.png)
3. Press Enter
4. Copy the output inside RelaX Group Editor
5. Click on preview
6. Click on "use Group in editor" (click multiple times if it doesn't work)
