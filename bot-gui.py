from tkinter import *
from instapy import InstaPy
tag=None
list1 = []
def advance():
    global tag
    global list1
    f5 = Frame(root,bg='orange')

    Label(f5,text='Add special Tags',font='arial 10 bold',padx='5',pady='5',bg='orange').pack(side=LEFT)
    # tagVar=StringVar()
    tag = Text(f5,font='arial 10',width='30',height='2')
    tag.pack(side=RIGHT,pady=5)
    f5.pack()
    f6 = Frame(root,bg='orange')

    Label(f6,text='Add Locations',font='arial 10 bold',padx='5',pady='5',bg='orange').pack(side=LEFT,padx=9)
    loc = Text(f6,font='arial 10',width='30',height='2')
    loc.pack(side=RIGHT,pady=5)
    f6.pack()

    adv.config(state=DISABLED)
    str = tag.get('1.0','end')
    list1 = str.split(',')

def start():
    # ur = user.get()
    # pas = passw.get()
    session = InstaPy(username='d_coders_hub', password='technopass@crat', headless_browser=True)
    session.login()
    if like.get() == 1:
        session.like_by_tags(list1, amount=int(amt_like.get()))
        session.set_dont_like(['nsfw','naked','snake'])
    if comment.get() == 1:
        # com = int(amt_comment.get())*10
        session.set_do_comment(enabled=True, percentage=25)
        commen = ['Work from home - dm for more details',"Earn easily from home - dm to know more",'follw to get earning opportunties','wow']
        session.set_comments(comments=commen)
 
    if follow.get() == 1:
        # flo = int(amt_follow.get())*10
        # session.set_do_follow(True, percentage=flo)
        session.follow_by_tags(list1, amount=int(amt_follow.get()))
    # username.delete('1.0','end')
    # username.update()
    # password.delete('1.0','end')
    # password.update()
    session.set_relationship_bounds(enabled=True, max_followers=1000, min_following=100)
    session.set_quota_supervisor(enabled=True, peak_comments_daily=250, peak_comments_hourly=50, peak_follows_daily=60, peak_follows_hourly=10,
    peak_likes_hourly=40, peak_likes_daily=500)

    # x = tag.index('end')
    # if x == 0:
    #     print('ok working')
    # else:
    #     print(x)
    # session.set_do_like(enabled=True, percentage=70)

if __name__ == "__main__":
    root = Tk()
    root.title('Insta Bot')
    root.geometry('400x400')
    root.config(bg='orange')

    Label(text='Instagram Bot',font='arial 20 bold',padx=10).pack(pady=20)
    f1 = Frame(root,bg='orange')
    Label(f1,text='Username', font='arial 10 bold',padx='5',pady='5',bg='orange').pack(side=LEFT)
    user=StringVar()
    username = Entry(f1, textvariable=user, font='arial 10')
    username.pack(side=RIGHT,padx=10)
    f1.pack(pady=5)

    f2 = Frame(root,bg='orange')
    Label(f2, text='Password',font='arial 10 bold',padx='5',pady='5',bg='orange').pack(side=LEFT)
    passw = StringVar()
    password = Entry(f2, textvariable=passw, show='*',width=24)
    password.pack(side=RIGHT,padx=18)
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
    amt_like = Spinbox(f4, from_=10, to_=450, width=5, relief=SUNKEN)
    amt_like.pack(side=LEFT,padx=5)
    amt_comment = Spinbox(f4, from_=5, to_=150, width=5, relief=SUNKEN)
    amt_comment.pack(side=LEFT,padx=50)
    amt_follow = Spinbox(f4, from_=1, to_=50, width=5, relief=SUNKEN)
    amt_follow.pack(side=LEFT)
    f4.pack()

    adv = Button(root,text='Advance Options',font='arial 5 bold',activebackground='red',command=advance)
    adv.pack(pady=5)
    Button(root,text='START',font='arial 10 bold',pady='5',activeforeground='green',command=start).pack(pady=5,side=BOTTOM)

    root.mainloop()
