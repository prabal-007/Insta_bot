from instapy import InstaPy

session = InstaPy(username='<your username>', password='<your password>', headless_browser=True)
session.login()

session.like_by_tags(['pythonprogramming','coding'], amount=2)
session.set_do_like(['nsfw','naked','snake'])
session.set_do_follow(True, percentage=30)
session.set_do_comment(True, percentage=50)
session.set_comments(['Nice post',"you're doing great job",'follow my page','wow'])
session.end()
