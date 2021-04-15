import json
from difflib import SequenceMatcher, get_close_matches
import tkinter
from tkinter import messagebox
def importdata(x):

    data = json.load(open('/Users/gmacdabeast/Python/Thesaurus/data.json', 'r'))
   # seq = SequenceMatcher(None, data[x])
    match = get_close_matches(x, data.keys(), n=1)
    print(match)
    while True:
        if x in data:
            return data[x]
            break
        elif len(match) > 0:
            ask = input(f'Did you mean: {match}?')
            if ask in ['Y','N']:
                if ask in 'Y':
                    x = match
                    return data[x]
                    break
                elif ask in 'N':
                    print('Word not found, try again.')
                    main()
                    break
                    
            else:
                print('Not a valid input! Try again!')
        else:
            return "Word not found, try again."




def main():
    input1 = input("Enter a word you would like to search: ").lower()

    answer = importdata(input1)
    thecount = len(answer)
    print(thecount)
    if type(answer) is list:
        for i in answer:
            print(i+'\n')
    else:
        print(answer)
        
    #print(translate(answer))
    #messagebox.showinfo('Title', f'There are {thecount} definitions found!\n\n' + '\n'.join(answer))


if __name__ == '__main__':
    main()