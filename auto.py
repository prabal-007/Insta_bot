from instapy import InstaPy

session = InstaPy(username='d_coders_hub', password='technopass@crat', headless_browser=True)
session.login()

session.like_by_tags(['pythonprogramming','coding'], amount=2)
session.set_do_like(['nsfw','naked','snake'])
session.set_do_follow(True, percentage=30)
session.set_do_comment(True, percentage=50)
session.set_comments(['Nice post',"you're doing great job",'follow my page','wow'])
session.set_relationship_bounds(enabled=True, max_followers=4000, min_following=1000)
session.set_quota_supervisor(enabled=True, peak_comments_daily=200, peak_comments_hourly=70, peak_follows_daily=60, peak_follows_hourly=10,
peak_likes_hourly=40, peak_likes_daily=400)
session.end()
