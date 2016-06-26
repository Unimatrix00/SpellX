# --- SpellX version 1.0.2 --- 
# --- Made by Attila_Kardos aka Unimatrix0---


# I support GNU General Public License so this program snippet is free to use and modify. 

# This program use Python version 3.5.
# This program use PyEnchant version 1.6.6.

# Please make sure the above mentioned tools are installed before run the program!

# The first 2 lines import the necessary modules from the PyEnchant libraries.
# PyEnchant documentation -> http://pythonhosted.org/pyenchant/tutorial.html


from enchant.tokenize import get_tokenizer, HTMLChunker
from enchant.checker import SpellChecker
import codecs

# By default PyEnchant support

 # en_GB: British English
 # en_US: American English
 # de_DE: German
 # fr_FR: French


chkr = SpellChecker("en_GB")
tknzr = get_tokenizer("en_GB",chunkers=(HTMLChunker,))

# HTMLChunker able to deal with XML perfectly. (same syntax)

file = codecs.open("SpellX_test.txt", 'r',encoding='latin-1')
resu = open("test-result.txt", "w")
for f in file.readlines():
    a = [w for w in tknzr(f)]
    chkr.set_text(f)
    for err in chkr:
        resu.writelines(err.word + "\n")
        print("ERROR:", err.word)
        
resu.close()
    
