# Logs Manager
### Gui app useful to concatenete or execute a key based merge (database like) on your csv/xlsx/xls files<br>
<p align="center">
  <img src="images/logsmanager_image.png">
</p>

### Index

1. [**What is Logs Manager?**](#what-is-logs-manager)
2. [**System Dependencies**](#requirements-and-dependencies)
3. [**Quick Start**](#quick-start)
6. [**Instructions**](#instructions)
7. [**Credits**](#credits)

<ul>


## What is Logs Manager?

**Logs Manager** is an application developed for a "Networks and distributed systems security" exam 
at **Univeristy Aldo Moro** of Taranto Italy. <br>
its goal is to manage log files released from different apps. 
It can be used to concatenete a large ammount of data logs spreads in different CSV/XLS/XLSX files, 
in addiction, it can allow merge two log files using a key (column name) at the same way a databases would do.

### Functionalities
<ul>

<li>
    Concatenete two or more log files : Useful to unify different files into a single one.
</li>
<li>
    Key based merge of two log files : Useful to filter records between two log files.
</li>

</ul>


<li>

## Requirements and Dependencies
```
Python 3.4 or higher (tested on 3.7)
pandas~=1.0.3
PyQt5~=5.15.1
 ```  
	
**Resources for dependencies required** <br>
Panadas: [**pandas.pydata.org/**](https://pandas.pydata.org/) <br>
PyQt5: [**pypi.org/project/PyQt5**](https://pypi.org/project/PyQt5/) <br>

</li>
<li>

## Quick Start

1 - Clone this repository <br> 
2 - Install all dependencies with "pip3 install -r requirements.txt" <br> 
3 - Execute "main.py" <br>
4 - Good work with **Logs Manager** <br>

</li>
<li>


## Instructions

### Prerequisites and notes
- For CSV files, they must have first row with headers separeted by "," and all record attributes must be separeted by ","
- For XLS/XLSX files, they must have first row with headers
- All input files must have the same extension but the output file could be choose as differet one : (CSV->XLSX | XLSX->CSV)

### Concatenete Function <br> 
1 - Click on "Open" button and select 2 or more log files (CSV/XLS/XLSX)<br>
2 - Click on "Save" button and select name and directory of the output file (CSV/XLS/XLSX)<br>
3 - Click on "CONCAT NOW" to execute concatenation of log files<br> 

### Merge Function <br>
1 - Click on "Open" button and select 2 log files (CSV/XLS/XLSX)<br>
2 - Click on "Save" button and select name and directory of the output file (CSV/XLS/XLSX)<br>
3 - Click on "MERGE NOW" to execute concatenation of log files<br>

![](images/XXXX.png)
<p align="center">
  <img src="images/XXXX.png">
</p>

</li>
<li>

### Credits

**Developed and Designed by:**

[**Chrism1c**](https://github.com/Chrism1c)

</li>
</ul>

