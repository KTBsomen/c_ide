import asyncio
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile 
from time import sleep
import tkinter
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os,sys
import fast_autocomplete
from fast_autocomplete import AutoComplete
#import re
from tkinter import *
import subprocess

#==========================================================================================


file=None
head_text='''/* ctrl+s for saving \n ctrl+o for open file \n ctrl+r for compile and run \n ============================================\n*/\n#include <stdio.h>\n#include <conio.h>
void main()
{
\tprintf( "I am Somen ! Beware.");

\tgetch();

}'''
#======================================================================
d='''auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while

#define
#error
#if
#ifdef
#ifndef
#else
#elif
#endif
#include
#line
#pragma
#undef
abort
abs
acos
asctime
asin
assert
atan
atan2
atexit
atof
atoi
atol
bsearch
calloc
ceil
clearerr
clock
cos
cosh
ctime
difftime
div
exit
exp
fabs
fclose
feof
ferror
fflush
fgetc
fgetpos
fgets
floor
fmod
fopen
fprintf
fputc
fputs
fread
free
freopen
frexp
fscanf
fseek
fsetpos
ftell
fwrite
getch
getchar
getenv
gets
gmtime
isalnum
isalpha
iscntrl
isdigit
isgraph
islower
isprint
ispunct
isspace
isupper
isxdigit
labs
ldexp
ldiv
localtime
log
log10
longjmp
malloc
memchr
memcmp
memcpy
memmove
memset
mktime
modf
perror
pow
printf
putc
putchar
puts
qsort
raise
rand
realloc
remove
rename
rewind
scanf
setbuf
setjmp
setlocale
setvbuf
signal
sin
sinh
sprintf
sqrt
srand
sscanf
strcat
strchr
strcmp
strcoll
strcpy
strcspn
strerror
strftime
strlen
strncat
strncmp
strncpy
strpbrk
strrchr
strspn
strstr
strtod
strtok
strtol
strtoul
strxfrm
system
system("cls")
tan
tanh
time
tmpfile
tmpnam
tolower
toupper
ungetc
va_arg
vprintf
vfprintf
vsprintf


'''



pr=d.replace('\n',' ').split(' ')


res = dict(zip(pr, [{}]*len(pr))) 


#print(res)


#lista = ['a', 'actions', 'additional', 'also', 'an', 'and', 'angle', 'are', 'as', 'be', 'bind', 'bracket', 'brackets', 'button', 'can', 'cases', 'configure', 'course', 'detail', 'enter', 'event', 'events', 'example', 'field', 'fields', 'for', 'give', 'important', 'in', 'information', 'is', 'it', 'just', 'key', 'keyboard', 'kind', 'leave', 'left', 'like', 'manager', 'many', 'match', 'modifier', 'most', 'of', 'or', 'others', 'out', 'part', 'simplify', 'space', 'specifier', 'specifies', 'string;', 'that', 'the', 'there', 'to', 'type', 'unless', 'use', 'used', 'user', 'various', 'ways', 'we', 'window', 'wish', 'you']

async def autoc():
    ls=[]
    fg=[]
            



    
    echo="====================================\npress ENTER to stop and go back to Editor\n===================================="
    print(echo)

    def ac(x):
        lb.delete(0,'end')
        words = res
        autocomplete=AutoComplete(words=words)
        k=autocomplete.search(word=x, max_cost=2, size=15)
        #print(len(k))
        for i in range(len(k)):
            #print(k[i])
            lb.insert(i,'%s'%k[i][0])
	
		
	

    print('To run a C program you mast save it first BY ctrl+s \nand then click compile&run(ctrl+r)\nctrl+o for open file')
    text=Text(win,height=25,width=90,fg='green2',bg='black',font=("Times", 12, "bold")
,bd=2,insertbackground='white',undo=True)
    
    text.grid(row = 1, column = 0, sticky = W, pady = 2,columnspan=5)
    def openh():
       pass
    tn=Button(win,text="new file",command=openh())#root is the first windowname
    tn.grid(row = 0, column = 7, sticky = W, pady = 2,columnspan=5)
    
    textt = Text(win,height=10,width=127,bd=2,fg='red')
    textt.grid(row = 2, column = 0, sticky = W, pady = 2,columnspan=10)
    textt.insert("1.0",'if you have any error in code then\nthe last saved error-free code will run\nyou will see all of your Errors here\n=======================================================================\n')
    text.tk_focusFollowsMouse()       
    def my_upd(my_widget):
        try:
            my_w = my_widget.widget
            index = int(my_w.curselection()[0])
            text.focus_set()
            value = my_w.get(index)
            text.focus_set()
            #print ("You selected item ",index, value)
            if ls[-1]=="2":
                abcd=text.delete('insert-%sc'%ls[-2],'insert')
            elif ls[-1]>=eval("4"):
                abcd=text.delete('insert-%sc'%ls[-2],'insert')
            else:
                abcd=text.delete('insert-%sc'%ls[-2],'insert')
            #print(abcd)
            text.insert("insert",value)
            coloring()
            lb.selection_clear('insert')
            text.focus_set()
            fg.clear()
            
        except IndexError:pass
        except:pass
        
    def color(tex,color):
        text.tag_remove("tagname","1.0",END)
        first = "1.0"
        while(True):
            first = text.search(tex, first, nocase=False, stopindex=END)
            if not first:
                break
            last = first+"+"+str(len(tex))+"c"
            text.tag_add("tagname_%s"%tex, first, last)
            first = last
            text.tag_config("tagname_%s"%tex, foreground=color)


    def coloring():
        
    
        color('printf','blue')
        color('main()','blue')
        color('clrscr()','red')
        color('type','blue')
        color('def','orange')
        color('void','pink')
        color('#include','orange')
        color('<','orange')
        color('>','orange')
        color('for','orange')
        color('while ','orange')
        color('int ','orange')
        color('char ','orange')
        color('True','orange')
        color('break','orange')
        color('if','orange')
        color('else','orange')
        color('do','orange')
        color('float','orange')
        color('return','orange')
        color('scanf','blue')
        color(';','yellow')
        color('[','yellow')
        color(']','yellow')
        color('{','yellow')
        color('}','yellow')
        color('1','yellow')
        color('2','yellow')
        color('3','yellow')
        color('4','yellow')
        color('5','yellow')
        color('6','yellow')

        color('7','yellow')
        color('8','yellow')
        color('9','yellow')
        color('0','yellow')
        color('(','yellow')
        color(')','yellow')
        color('*','yellow')
        color('!','yellow')
        color('@','yellow')
        color('#','yellow')
        color('$','yellow')
        color('%','yellow')
        color('^','yellow')
        color('&','yellow')
        color('_','yellow')
        color('-','yellow')
        color('+','yellow')
        color('=','yellow')
        color('/','yellow')
        color(r'\\','yellow')
        color('"','#78D9F7')
        color("'",'red')
        color("/*",'gray')
        color("*/",'gray')
        color("//",'gray')
        color('|','yellow')
        color("auto","orange")
        color("break","orange")
        color("case","orange")
        
        color("const","orange")
        color("continue","orange")
        color("default","orange")
        
        color("double","orange")
        color("else","orange")
        color("enum","orange")
        color("extern","orange")
        color("float","orange")
        color("for","orange")
        color("goto","orange")
        color("if","orange")
        
        color("long","orange")
        color("register","orange")
        color("return","orange")
        color("short","orange")
        color("signed","orange")
        color("sizeof","orange")
        color("static","orange")
        color("struct","orange")
        color("switch","orange")
        color("typedef","orange")
        color("union","orange")
        color("unsigned","orange")
        
        color("volatile","orange")
        color("#define","orange")
        color("#error","orange")
        color("#if","orange")
        color("#ifdef","orange")
        color("#ifndef","orange")
        color("#else","orange")
        color("#elif","orange")
        color("#endif","orange")
        
        color("#line","orange")
        color("#pragma","orange")
        color("#undef","orange")
        color("abort","orange")
        color("abs","orange")
        color("acos","orange")
        color("asctime","orange")
        color("asin","orange")
        color("assert","orange")
        color("atan","orange")
        color("atan2","orange")
        color("atexit","orange")
        color("atof","orange")
        color("atoi","orange")
        color("atol","orange")
        color("bsearch","orange")
        color("calloc","orange")
        color("ceil","orange")
        color("clearerr","orange")
        color("clock","orange")
        color("cos","orange")
        color("cosh","orange")
        color("ctime","orange")
        color("difftime","orange")
        color("div","orange")
        color("exit","orange")
        color("exp","orange")
        color("fabs","orange")
        color("fclose","orange")
        color("feof","orange")
        color("ferror","orange")
        color("fflush","orange")
        color("fgetc","orange")
        color("fgetpos","orange")
        color("fgets","orange")
        color("floor","orange")
        color("fmod","orange")
        color("fopen","orange")
        color("fprintf","orange")
        color("fputc","orange")
        color("fputs","orange")
        color("fread","orange")
        color("free","orange")
        color("freopen","orange")
        color("frexp","orange")
        color("fscanf","orange")
        color("fseek","orange")
        color("fsetpos","orange")
        color("ftell","orange")
        color("fwrite","orange")
        color("getch","orange")
        color("getchar","orange")
        color("getenv","orange")
        color("gets","orange")
        color("gmtime","orange")
        color("isalnum","orange")
        color("isalpha","orange")
        color("iscntrl","orange")
        color("isdigit","orange")
        color("isgraph","orange")
        color("islower","orange")
        color("isprint","orange")
        color("ispunct","orange")
        color("isspace","orange")
        color("isupper","orange")
        color("isxdigit","orange")
        color("labs","orange")
        color("ldexp","orange")
        color("ldiv","orange")
        color("localtime","orange")
        color("log","orange")
        color("log10","orange")
        color("longjmp","orange")
        color("malloc","orange")
        color("memchr","orange")
        color("memcmp","orange")
        color("memcpy","orange")
        color("memmove","orange")
        color("memset","orange")
        color("mktime","orange")
        color("modf","orange")
        color("perror","orange")
        color("pow","orange")
        
        color("putc","orange")
        color("putchar","orange")
        color("puts","orange")
        color("qsort","orange")
        color("raise","orange")
        color("rand","orange")
        color("realloc","orange")
        color("remove","orange")
        color("rename","orange")
        color("rewind","orange")
        
        color("setbuf","orange")
        color("setjmp","orange")
        color("setlocale","orange")
        color("setvbuf","orange")
        color("signal","orange")
        color("sin","orange")
        color("sinh","orange")
        color("sprintf","orange")
        color("sqrt","orange")
        color("srand","orange")
        color("sscanf","orange")
        color("strcat","orange")
        color("strchr","orange")
        color("strcmp","orange")
        color("strcoll","orange")
        color("strcpy","orange")
        color("strcspn","orange")
        color("strerror","orange")
        color("strftime","orange")
        color("strlen","orange")
        color("strncat","orange")
        color("strncmp","orange")
        color("strncpy","orange")
        color("strpbrk","orange")
        color("strrchr","orange")
        color("strspn","orange")
        color("strstr","orange")
        color("strtod","orange")
        color("strtok","orange")
        color("strtol","orange")
        color("strtoul","orange")
        color("strxfrm","orange")
        color("system","orange")
        color("tan","orange")
        color("tanh","orange")
        color("time","orange")
        color("tmpfile","orange")
        color("tmpnam","orange")
        color("tolower","orange")
        color("toupper","orange")
        color("ungetc","orange")
        color("va_arg","orange")
        color("vprintf","orange")
        color("vfprintf","orange")
        color("vsprintf","orange")
        
        
            



    lb = Listbox(win,height=25 ,width=50,bg = "grey",activestyle = 'dotbox',  font = ("Helvetica",12),fg = "yellow") 
    lb.grid(row = 1, column = 6, sticky = W, pady = 2)
    lb.bind('<<ListboxSelect>>', my_upd)
    text.focus_set()

    def save_it(x):
        
        try:
            if file is not None:
                try:
                    filee=open(file.name,'w')
                    print(text.get('1.0', 'end-1c'),file=filee)                       
                    abcd=text.get('insert-1c')
                    fg.append(abcd)
                    gh=open('auto.txt','w')
                    for i in range(len(fg)):
                    	
                        #print(fg[i].replace("}","\n").replace(" ","\n").replace("}","\n").replace("(","\n").replace(")","\n").replace(":","\n").replace(";","\n"),end='')
                    	print(fg[i].replace("}","\n").replace(" ","\n").replace("}","\n").replace("(","\n").replace(")","\n").replace(":","\n").replace(";","\n"),end='',file=gh)
                        
                    
                    gh.close()
                    sd=open('auto.txt','r').readlines()
                    
                
                    
                    ls.append(len(sd[-1]))
                    print(ls)
                    
                    ac(sd[-1])
                    
                    coloring()
                    
                
                except:print("else block runns")
            else: 
                try:
                    
                    
                    filee=open(save_text_as.name,'w')
                    print(text.get('1.0', 'end-1c'),file=filee)
                    abcd=text.get('insert-1c')
                    #print(abcd)
                    fg.append(abcd)
                    gh=open('auto.txt','w')
                    for i in range(len(fg)):
                        
                        
                        
                        print(fg[i].replace("1","\n").replace("2","\n").replace("3","\n").replace("4","\n").replace("5","\n").replace("6","\n").replace("7","\n").replace("8","\n").replace("9","\n").replace("0","\n").replace("-","\n").replace("=","\n").replace("!","\n").replace("@","\n").replace("#","\n").replace("$","\n").replace("%","\n").replace("^","\n").replace("&","\n").replace("*","\n").replace("(","\n").replace(")","\n").replace("_","\n").replace("+","\n").replace("{","\n").replace("}","\n").replace("[","\n").replace("]","\n").replace(":","\n").replace(";","\n").replace("|","\n").replace("<","\n").replace(">","\n").replace("?","\n").replace("/","\n").replace(",","\n").replace(".","\n"),end='',file=gh)
                        
                       

                    gh.close()
                    sd=open('auto.txt','r').readlines()
                    #print(sd[-1])
                    ls.append(sd[-1])
                    print(ls)
                    ac(sd[-1])
                    
                    coloring()
            
                except NameError:
                    messagebox.showinfo("Error", "First save the file click on( save as c file)button.")
                except AttributeError:
                    messagebox.showinfo("Error", "First save the file click on( save as c file)button.")
        
        except NameError:pass   
    text.insert('1.0',head_text)
    text.focus_set()
    #text.bind("<KeyPress>",get_text)
    
    text.bind("<Control-S>",lambda x:asyncio.run(save()))
    text.bind("<Control-s>",lambda y:asyncio.run(save()))
    text.bind("<Control-o>",lambda z:asyncio.run(open_file()))
    text.bind("<Control-O>",lambda a:asyncio.run(open_file()))
    text.bind("<Control-r>",lambda z:asyncio.run(runing()))
    text.bind("<Control-R>",lambda a:asyncio.run(runing()))
    text.bind("<F5>",lambda a:asyncio.run(runing()))
    btn = ttk.Button(win, text = 'Save as C file', command = lambda:asyncio.run(save())) 
    btn.grid(row = 0, column = 1, sticky = W, pady = 2) 

    text.bind("<KeyRelease>",save_it)
    btnn = ttk.Button(win, text = 'Compile & Run(F5)', command = lambda:asyncio.run(runing())) 
    btnn.grid(row = 0, column = 2, sticky = W, pady = 2) 

    
    btnnn = ttk.Button(win, text = 'Open File', command = lambda:asyncio.run(open_file())) 
    btnnn.grid(row = 0, column = 3, sticky = W, pady = 2) 


        
    
    async def save():
        

        
        btn.configure(text='save as C file')
        global save_text_as
        save_text_as = asksaveasfile(mode='w',defaultextension='.c')
        if save_text_as:
                
            text_to_save = text.get('1.0', 'end-1c')
            save_text_as.write (text_to_save)
            coloring()
            btn.configure(text='Auto saving started')
            

            #print(save_text_as.name)
            win.title(save_text_as.name)
            
        else :
            messagebox.showinfo("Error", "Cancelled")
            btn.configure(text='save as C file')

            #win.config(title='C IDE(made by somen)')
        try:
            save_text_as.close()
        except AttributeError:pass
    def run(x):
        
        
        try:
            
            p=subprocess.run('gcc -o %s %s'%((x.name).split('.')[0],x.name),shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            #print(p.stderr.strip())
            
            #ffg=subprocess.run('%s'%((save_text_as.name).split('.')[0]),capture_output=True,shell=False,text=True)
            #print(ffg.stdout)
            os.system('%s'%(x.name).split('.')[0])  
            # store the return code of the c program(return 0) 
            # and display the output
            #print('gcc -o %s %s'%((save_text_as.name).split('.')[0],save_text_as.name))
            #h = subprocess.check_output('gcc -o %s %s'%((save_text_as.name).split('.')[0],save_text_as.name,), shell = True)

            #s=subprocess.getoutput('python')
            
            #print(s.decode("utf-8"))
            


        
            
            
            textt.delete('1.0',END)
            textt.insert(END,p.stderr.strip())
            
            
            
            #print('gcc -o %s %s'%((save_text_as.name).split('.')[0],save_text_as.name))
           # print('%s'%(save_text_as.name).split('.')[0])
        except NameError: messagebox.showinfo("Error", "First save the file (ctrl+s)")
    async def runing():
        try:
            if file is not None:
                run(file)
            else:run(save_text_as)
        except NameError:messagebox.showinfo("Error", "First save the file (ctrl+s)")
        except AttributeError:messagebox.showinfo("Error", "You have to save the file again")
    async def open_file():
        global file
        
        #print(save_text_as.name)
        file = askopenfile(mode ='r', filetypes =[('C Files', '*.c')]) 
        if file is not None: 
            content= file.read()
            
            if content:
                
                text_to_save = text.get('1.0', 'end-1c')
                #save_text_as.write (text_to_save)
                coloring()
                
                btn.configure(text='Auto saving started')
                

                #print(file.name)
                win.title(file.name)
                                    
                try:
                    text.delete('1.0',END)
                    text.insert('end-1c',content)
                    coloring()
                    text.focus_set()
                except:pass
                try:
                    file.close()
                except:pass
                    
            else :
                messagebox.showinfo("Error", "Cancelled You have to save the file again")
                btn.configure(text='save as C file')

                #win.config(title='C IDE(made by somen)')
            try:
                content.close()
            except AttributeError:
                pass
    

        
    




#856ff8
win=tkinter.Tk()
win['background']='black'
win.title('C IDE(made by somen)')

asyncio.run(autoc())



win.mainloop()
