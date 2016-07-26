def get_likes_button():
    child = subprocess.Popen(['python', '-u', 'getLikes.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    #--- This part must be placed into V2.py ---
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    #--------------END---------------------
    child.stdout.close()
    child.wait()
