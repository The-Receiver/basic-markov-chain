import random

file = open('hamlet.txt').read()

def tokenize(str):
   return str.split()

#todo: allow phrase lengths of more than one
def build_dict(strray):
    dict = {}
    i = 0
    while i < len(strray) - 1:
        str = strray[i]
        next = strray[i+1]
        if str in dict.keys():
            dict[str].append(next)
        else:
            dict[str] = [next]
        i += 1  
    return dict
    
def random_driver(dict, n):
    sample_list = random.sample(list(dict), 1)
    string = strbuilder = random.sample(sample_list, 1)[0]
    for i in range(n): 
      sample_list = dict.get(string)
      if(sample_list == None):
          sample_list = random.sample(list(dict), 1)
      string = random.sample(sample_list, 1)[0]
      strbuilder = strbuilder + ' ' + string 
    return(strbuilder)

dict = build_dict(tokenize(file))
print(random_driver(dict,100))
