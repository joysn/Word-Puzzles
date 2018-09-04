from builtins import type
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD

def spellathon(comp_char,other_char_list):
    
    fh = open('dictionary.txt','r')
    op_list = list()

    max_word_len = len(other_char_list) + len(comp_char)
    min_word_len = 4
            
    for words in fh:
        #print(type(words))
        
        temp_other_char_list = other_char_list+list(comp_char) # add compulsory char in temp list
        if((words.find(comp_char) != -1) and (len(words.strip()) <= int(max_word_len)) and (len(words.strip()) >= int(min_word_len))): 
        # contains the compulsory character, The size of word is between minimum and max
            is_pres = 1
            word_list = list(words.strip())
            #print(word_list)
            for wc in word_list:
                try:
                    if(temp_other_char_list.index(wc) != -1):
                        #print('is present ',wc,temp_other_char_list,word_list)
                        is_pres = 1
                        temp_other_char_list.remove(wc) # remove it so that it is not considered for comparison next time                        
                    else :
                        print('in else - should not come here',wc,temp_other_char_list,word_list,temp_other_char_list.index(wc))
                except:
                    #print("in except",wc,words)
                    is_pres = 0;
                    break
            if is_pres == 1:
                op_list.append(words)
                #print(words)
                
    sp_op = ''
    for i in op_list:
        sp_op += str(i.strip()+' ')
    #print()
    #print()
    fh.close()
    return sp_op

def scramble(scramble_text):
    fh = open('dictionary.txt','r')
    list_stext = list(scramble_text)
    list_stext.sort(key=None, reverse=False)
     
    op_list = list()
     
    for lines in fh:
        if lines.strip() == scramble_text:
            op_list.append(lines.strip())
            continue
        if len(lines.strip()) == len(scramble_text):
            list_lines = list(lines.strip())
            list_lines.sort(key=None, reverse=False)
            if list_lines == list_stext:
                op_list.append(lines.strip())
    fh.close()
    print('Scrambled Word:',scramble_text.ljust(8),' Unscrambled Word(s): ',end='')
    for ow in op_list:
        print(ow,end=' ')
    print()
    return op_list

def spellathon_find_to_main():
    e1.delete(0, END)
    e2.delete(0,END)
    spellathon_find_window.destroy()
    
    
def spellathon_find_win():
    sp_op = spellathon(es1.get(),list(es2.get()))
    
    global spellathon_find_window
    spellathon_find_window = Toplevel(root)
    spellathon_find_window.title('Spellathon results')
    sp_label = ttk.Label(spellathon_find_window,text = sp_op)
    sp_label.grid(row=0,columnspan=2)
     
    spellathon_back_button = ttk.Button(spellathon_find_window ,text = "Back",
                                        command = spellathon_find_to_main).grid(row=1,column = 0,ipadx=7,ipady=7,padx=5,pady=10,stick = 'nsew')     
    spellathon_exit_button = ttk.Button(spellathon_find_window ,text = "Exit",
                                        command = spellathon_find_window.quit).grid(row=1,column = 1,ipadx=7,ipady=7,padx=5,pady=10,stick = 'nsew')

    
def validate_es1(comp_str):
    if(len(comp_str) == 1):
        return True
    else:
        return False
    


def spellathon_main_win():
 
    global sp_label, e1,e2,spellathon_main_window,es1,es2
    spellathon_main_window = Toplevel(root)
    spellathon_main_window.title('Spellathon')
    #spellathon_main_window.geometry("300x100")

    validate_es1_command = spellathon_main_window.register(validate_es1)
     
    ttk.Label(spellathon_main_window, text="Compulsory Character").grid(row=1,column = 0,ipadx=7,ipady=7,padx=5,pady=10)
    ttk.Label(spellathon_main_window, text="Other Characters").grid(row=2,column = 0,ipadx=7,ipady=7,padx=5,pady=10)
 
    es1 = StringVar()
    es2 = StringVar()
    e1 = ttk.Entry(spellathon_main_window,textvariable = es1)
    e1.config(width = 1,font=('Helvetica', 16,BOLD))
    e1.grid(row=1, column=1,columnspan=2)
    e2 = ttk.Entry(spellathon_main_window,textvariable = es2)
    e2.config(width = 6,font=('Helvetica', 16))
    e2.grid(row=2, column=1,columnspan=2)
 
     
    spellathon_find_button = ttk.Button(spellathon_main_window ,text = "Spellathon",
                                        command = spellathon_find_win).grid(row=3,column= 0,ipadx=7,ipady=7,padx=5,pady=10,stick = 'nsew')
    spellathon_back_button = ttk.Button(spellathon_main_window ,text = "Back",
                                        command = spellathon_main_window.destroy).grid(row=3,column=1,ipadx=7,ipady=7,padx=5,pady=10)
    spellathon_exit_button = ttk.Button(spellathon_main_window ,text = "Exit",
                                        command = spellathon_main_window.quit).grid(row=3,column=2,ipadx=7,ipady=7,padx=5,pady=10)
    
 

def spellathon_find_to_main():
    e1.delete(0, END)
    scramble_find_window.destroy()

def scramble_find_win():
    sp_op = scramble(es1.get())
    
    global scramble_find_window
    scramble_find_window = Toplevel(root)
    scramble_find_window.title('Scramble results')
    sp_label = ttk.Label(scramble_find_window,text = sp_op)
    sp_label.grid(row=0,columnspan=2)
     
    spellathon_back_button = ttk.Button(scramble_find_window ,text = "Back",
                                        command = spellathon_find_to_main).grid(row=1,column = 0,ipadx=7,ipady=7,padx=5,pady=10,stick = 'nsew')     
    spellathon_exit_button = ttk.Button(scramble_find_window ,text = "Exit",
                                        command = scramble_find_window.quit).grid(row=1,column = 1,ipadx=7,ipady=7,padx=5,pady=10,stick = 'nsew')

										
def scramble_main_win():
 
    global sp_label, e1,scramble_main_window,es1
    scramble_main_window = Toplevel(root)
    scramble_main_window.title('Scramble')
    
    validate_es1_command = scramble_main_window.register(validate_es1)
     
    ttk.Label(scramble_main_window, text="Scrambled Words").grid(row=1,column = 0,ipadx=7,ipady=7,padx=5,pady=10)
    
    es1 = StringVar()
    e1 = ttk.Entry(scramble_main_window,textvariable = es1)
    e1.config(width = 6,font=('Helvetica', 16,BOLD))
    e1.grid(row=1, column=1,columnspan=2)
    
     
    spellathon_find_button = ttk.Button(scramble_main_window ,text = "UnScramble",
                                        command = scramble_find_win).grid(row=3,column= 0,ipadx=7,ipady=7,padx=5,pady=10,stick = 'nsew')
    spellathon_back_button = ttk.Button(scramble_main_window ,text = "Back",
                                        command = scramble_main_window.destroy).grid(row=3,column=1,ipadx=7,ipady=7,padx=5,pady=10)
    spellathon_exit_button = ttk.Button(scramble_main_window ,text = "Exit",
                                        command = scramble_main_window.quit).grid(row=3,column=2,ipadx=7,ipady=7,padx=5,pady=10)
										
def main():
    
    # Global variables
    global  comp_char,other_char_list, f, root

    root = Tk()
    root.title('Puzzles')
    #root.geometry('320x240+200+200')
    
    # No need for Another frame inside it as of now
    main_frame = LabelFrame(root)
    main_frame.pack()
    #main_frame.config(height =320, width = 200,padx=5, pady=5)
    main_frame.config(padx=5, pady=5)
    #main_frame.grid_propagate(0)
    
    
    
    #comp_char = 'w'
    #other_char_list = ['t','a','y','r','s','h']
    #comp_char = 'd'
    #other_char_list = ['e','s','k']
    #print("********** SPELLATHON **************")
    #spellathon(comp_char, other_char_list)

    # Make them expandable
    main_frame.rowconfigure(0,weight = 1)
    main_frame.rowconfigure(1,weight = 1)
    main_frame.rowconfigure(2,weight = 1)
    
    main_frame.columnconfigure(0,weight = 1)
    main_frame.columnconfigure(1,weight = 1)
    main_frame.columnconfigure(2,weight = 1)
    
    main_spellathon_button = ttk.Button(main_frame,text = "Spellathon",width=50)
    main_spellathon_button.config(command = spellathon_main_win)
    main_spellathon_button.grid(row=0,ipadx=7,ipady=7,padx=5,pady=10)

    main_scambled_button = ttk.Button(main_frame,text = "Scrambled Words",width=50)
    main_scambled_button.config(command = scramble_main_win)
    main_scambled_button.grid(row=1,ipadx=7,ipady=7,padx=5,pady=10)
    
    main_exit_button = ttk.Button(main_frame ,text = "Exit", command = root.quit,width=50)
    main_exit_button.grid(row=2,ipadx=7,ipady=7,padx=5,pady=10)
    
    
    for widget in root.grid_slaves():
        print(widget.grid_info())
        #widget.pack_configure(fill=BOTH, expand=True)
       

	   
    # Testing
    #scramble_text_list = ('naaer','cosst','bdinnu','hosddy')
    #print("********** SCRAMBLE ****************")
    #for scramble_text in scramble_text_list:
    #    scramble(scramble_text) 
    
    
    #print()
    print()
    
    root.mainloop()

if __name__ == "__main__":
    main()
