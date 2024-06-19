from datetime import datetime
def note(string, filename='note.log.txt'):
    string = str(string)
    with open(filename, 'a') as f:
        time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(time + ':\n')
        f.write(string + '\n')