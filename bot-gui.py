from tkinter import Label,Button,Text,Frame,LEFT,RIGHT,DISABLED,BOTTOM,TRUE,X,Entry,Tk,StringVar,IntVar,Spinbox,Checkbutton,SUNKEN,FLAT,PhotoImage

import tkinter.messagebox as tms
from instapy import InstaPy

tag=None
list1 = ['business','akshaykumar','profit','dreams']
list2=[]
def advance():
    root.geometry('415x440')
    global tag
    global list2,  list1
    f5 = Frame(root,bg='orange')

    Label(f5,text='Add special Tags',font='arial 9 bold',padx='5',pady='5',bg='orange').pack(side=LEFT)
    tag = Text(f5,font='arial 9',width='30',height='2')
    tag.pack(side=RIGHT,pady=5)
    f5.pack()
    f6 = Frame(root,bg='orange')

    Label(f6,text='Add Locations',font='arial 9 bold',padx='5',pady='5',bg='orange').pack(side=LEFT,padx=9)
    loc = Text(f6,font='arial 9',width='30',height='2')
    loc.pack(side=RIGHT,pady=5)
    f6.pack()
    adv.config(state=DISABLED)
    
    str1 = tag.get('1.0','end')
    list2 = str1.split(',')
    list1.extend(list2)

def exi():
    value = (tms.askyesno('Exit','Are you sure, ou want to exit?'))
    if value == True:
        exit()
def hel():
    root2=Tk()
    def exi():
        root2.destroy()
    root2.geometry('500x400')
    root2.configure(background='orange')
    Label(root2, text='by Prabal Gupta', anchor='e', fg='white', bg='black').pack(side=BOTTOM, fil=X)
    root2.title("Insta BOT- Help")
    head=Label(root2, text=' HELP BOX ',bg='orange', font='arial 18 bold',underline=True)
    head.pack(pady='15')
    cont=Label(root2, text='Execute this instagram bot by following these\nsimple steps.\nStep-0. Enter your instagram username\nStep-1. Enter your instagram account password.\nstep-2. Select the actions(like, comment or shere) \nand thier quentity.\nStep-3. Click the advance options button to get advance\noptions like adding specail tags.\n\tstep-3.0. You an add special tags (to intract with\nspecifi community)\nstep-4. Click the start button to execute your insta bot.\nNOTE - Step-3 is optional.',
    font='arial 12 bold',padx='5',pady='10')
    cont.pack(pady='5',fill=X)
    Button(root2,text='Exit',bg='gray',font='Arial 10 bold',command=exi).pack()
    root2.mainloop()
def About():
    root3=Tk()
    def exi():
        root3.destroy()
    root3.geometry('400x400')
    Label(root3, text='by Prabal Gupta', anchor='e', fg='white', bg='black').pack(side=BOTTOM, fil=X)
    root3.configure(background='orange')
    root3.title('Insta BOT- About')
    head=Label(root3, text='About',bg='orange', font='arial 18 bold')
    head.pack(pady='20')
    cont=Label(root3, text='Name - Insta BOT\nVersion - str.IB.0.2\nDeveloper - Prabal Gupta\ngithub - https://github.com/prabal-007', font='arial 12 bold',padx='5',pady='5')
    cont.pack(pady='20')
    Button(root3,text='Exit',bg='gray',font='Arial 10 bold',command=exi).pack()
    root3.mainloop()

def start():
    u=user.get()
    p=passw.get()
    session = InstaPy(username=u, password=p, headless_browser=True)
    session.login()
    
    session.set_relationship_bounds(enabled=True, max_followers=1000, min_following=100)
    session.set_quota_supervisor(enabled=True, peak_comments_daily=250, peak_comments_hourly=20, peak_follows_daily=60, peak_follows_hourly=10,
    peak_likes_hourly=40, peak_likes_daily=500)

    if like.get() == 1:
        session.set_dont_like(['nsfw','naked','snake'])
        session.like_by_tags(list1, amount=int(amt_like.get()), use_smart_hashtags=True)
        
    if comment.get() == 1:
        session.set_comments(comments=['Work from home - dm for more details',"Earn easily from home - dm to know more",'follw to get earning opportunties','wow'],
        media='Photo')
        
    if follow.get() == 1:
        flo = int(amt_follow.get())
        session.follow_by_tags(tags=list1, amount=flo, use_smart_hashtags=True, interact=False)

def vis():
    v = (password['show']=='*')
    if v == TRUE:
        password.config(show='')
    else:
        password.config(show='*')

if __name__ == "__main__":
    root = Tk()
    root.title('Insta Bot')
    root.geometry('415x390')
    root.config(bg='orange')

    Label(text='Instagram Bot',font='arial 20 bold',padx=10).pack(pady=20)
    f1 = Frame(root,bg='orange')
    Label(f1,text='Username', font='Arial 10 bold',padx='5',pady='5',bg='orange',width='9').pack(side=LEFT)
    user=StringVar()
    username = Entry(f1, textvariable=user, font='arial 10')
    username.pack(side=RIGHT,padx=10)
    f1.pack(pady=5)

    f2 = Frame(root,bg='orange')
    Label(f2, text='Password',font='Arial 10 bold',padx='5',pady='5',bg='orange').pack(side=LEFT,padx=13)
    passw = StringVar()
    password = Entry(f2, textvariable=passw, show='*',width=24)
    password.pack(side=LEFT)
    vi=PhotoImage(file='vis1.png')
    vis = Button(f2,image=vi,command=vis,font='bold',width='10',height='11',relief=FLAT)
    vis.pack(side=LEFT)
    f2.pack(pady=5)

    Label(root,text='Select Actions & Quantity',font='arial 10 bold',padx=5).pack()
    f3 = Frame(root,bg='orange')
    like=IntVar()
    comment=IntVar()
    follow=IntVar()
    Checkbutton(f3,text='LIKE',variable=like,bg='orange').pack(side=LEFT,padx=5)
    Checkbutton(f3,text='COMMENT',variable=comment,bg='orange').pack(side=LEFT,padx=10)
    Checkbutton(f3,text='FOLLOW',variable=follow,bg='orange').pack(side=RIGHT,padx=10)
    f3.pack()

    f4 = Frame(root,bg='orange')
    amt_like = Spinbox(f4, from_=1, to_=450, width=5, relief=SUNKEN)
    amt_like.pack(side=LEFT,padx=5)
    amt_comment = Spinbox(f4, from_=1, to_=150, width=5, relief=SUNKEN)
    amt_comment.pack(side=LEFT,padx=50)
    amt_follow = Spinbox(f4, from_=1, to_=50, width=5, relief=SUNKEN)
    amt_follow.pack(side=LEFT)
    f4.pack()

    adv = Button(root,text='Advance Options',font='arial 5 bold',activebackground='red',command=advance)
    adv.pack(pady=5)
    
    endfrm = Frame(root)
    Label(endfrm,text="By Starkk's", bg='gold').pack(side=RIGHT)
    Label(endfrm,text='©sta.IB.0.2').pack(side=LEFT)
    endfrm.pack(side=BOTTOM, fill=X)
    frm4 = Frame(root,bg='orange')
    Button(frm4,text='About us',bg='gray', command=About).pack(side=LEFT,padx=5,pady=2)
    b1 = Button(frm4,text='Exit',bg='gray',command=exi,activebackground='red').pack(side=LEFT,padx=5,pady=2)
    Button(frm4,text='Help',bg='gray', command=hel).pack(side=LEFT,padx=5,pady=2)
    frm4.pack(side=BOTTOM,fill=X,padx=120)
    Button(root,text='START',font='arial 10 bold',pady='5',activeforeground='green',command=start).pack(pady=5,side=BOTTOM)

    root.mainloop()
