def get_likes_button():
    child = subprocess.Popen(['python', '-u', 'getLikes.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()
