

def snake_case(string): 
    return ''.join(['_' + i.lower() if i.isupper()  
               else i for i in string]).lstrip('_')