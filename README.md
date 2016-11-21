SpellX – by Unimatrix0

(Current version is hardcoded and static. Designed to test the functionality.)

Summary: The SpellX will be a multi-lingual spellchecking tool with possible profanity filter and US – UK English comparing functions.

Currently the program support 4 languages:
•	en_GB: British English
•	en_US: American English
•	de_DE: German
•	fr_FR: French

However based on the documentation of the PyEnchant it can use dictionaries from the OpenOffice.org project so the number of supported language are almost unlimited.

Currently the core of the program is functioning correctly and effectively with an Approx.: 1Mb+/min data processing performance. The performance was tested on Mix plain text and HTML/XML content. (The program ignore the HTML/XML content as required – no error).

Every part of the program is free to use and distribute based on the GNU General Public License.

As a good practice the program will be documented at the time of further development.

The solution I use here is very light weight and do not require serious processing power. However an Intel I7 CPU with 8GB Memory perfect, (Tested on my Own PC).

Implementation plan and tools:
-	Dynamic input options / interactivity – https://www.python.org/
-	Graphical user interface (GUI) -- http://ironpython.net/
-	Possible security option. -- http://www.pythonsecurity.org/
-	Transform the code into an executable windows file. -- http://www.py2exe.org/
-	(Maybe) Extract the core modules and libraries and design it as an autonomic program with an install shield. -- http://www.py2exe.org/ and http://www.pyinstaller.org/

The Goal: This program is dedicated to simplify and speed up some of the very time consuming Generic tests applied by Sony. The main reason to help the Functional Test team to do more accurate tests. 

Key words: Scalable, User Friendly, Accurate, Fast and Simple.

Python enviroment:

https://sourceforge.net/projects/winpython/files/WinPython_3.4/3.4.3.7/
