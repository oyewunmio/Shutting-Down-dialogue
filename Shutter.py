# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:05:35 2019

@author: oyewunmi oluwaseyi
"""
import os
import platform
import tkinter as tk
class ShutDown(tk.Tk):
    '''This is the base class for shutting down the system'''
    def __init__(self, *args, **kwargs):
        '''default constructor for class Shutdown'''
        tk.Tk.__init__(self, *args, **kwargs)
        #self.About()
        self.panel()
    def panel(self):
        '''panel method for the creation of the tkinter panel'''
        Var=tk.IntVar()
        Var2=tk.IntVar()

        def Panel2():
            Frame1=tk.Toplevel(self)
            Frame2=tk.LabelFrame(Frame1,text='ShutDown Timer')
            Frame2.pack(side='top')
            tk.Label(Frame2,text='Hours').pack(side='top')
            #tk.Label(Frame2,text='Time to shut down').pack()
            tk.Spinbox(Frame2,from_=0 , to=1000,textvariable=Var2).pack()
            tk.Scale(Frame2,label='Minutes',from_=0, to=60,orient='horizontal',length=200,variable = Var,tickinterval=10).pack()
            tk.Button(Frame2,text='Shutdown',command=Reader,bg='red').pack()
        def Reader():
            Min = Var2.get()
            Sec = Var.get()
            callback(Min,Sec)
        def callback(Min,Sec):
            '''callback for the Button labeled Yes'''

            #print (Min,':',Sec)
            if (platform.system()=='Linux'):
                if Min==0:
                    os.system('shutdown +{}'.format(Sec))
                else:
                    os.system('shutdown {}:{}'.format(Min,Sec))
            else:
               os.system('shutdown -s -t {}'.format(Min))
            self.destroy()
        def callback2():
            '''callback for the Button labeled No'''
            self.destroy()
        def Msg():
            Frame=tk.Toplevel(self)
            tk.Label(Frame,text='This application was created by \n Oyewunmi Oluwaseyi for his sole use only.\nContact:\noluwaseyioyewunmi99@gmail.com').pack(side='top')
        def Source():
            SrcFrame=tk.Toplevel(self)
            tk.Label(SrcFrame, text= 'The source code is:\n',relief='groove').pack(side='top')
            Codes = open('Print.txt', 'r+')
            for lines in Codes:
                line = lines
                #print(line)
        Name = platform.system()
        Abt=tk.Menubutton(self,text='Info',bg='yellow',fg='brown',font='arial 9 bold italic', width=28,borderwidth=3,relief='groove')
        Abt.pack(side='top')
        Abt.menu=tk.Menu(Abt)
        Abt.menu.add_command(label='Print Source Code',command=Source)
        Abt.menu.add_command(label='About',command=Msg)
        Abt.menu.add_command(label='Exit',command=callback2)
        Abt['menu']=Abt.menu
        frame = tk.LabelFrame(self, text='Dialogue', bg='black',fg='green')
        frame.pack(side='bottom')
        tk.Label(frame, text='Do you want to shut your {} system down'.format(Name), bg='Black', fg='yellow' ,wraplength=200, justify='center').pack(side='top')
        tk.Button(frame, text='Yes', borderwidth=4, bg='blue',  command=Panel2).pack(side='left', padx=25)
        tk.Button(frame, text='No', borderwidth=4, relief='raised', bg='purple', command=callback2).pack(side='right', padx=25)
ShutDown(className='Shutdown system').mainloop()
