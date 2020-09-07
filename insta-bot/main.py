from instapy import InstaPy

session = InstaPy(username='d_coders_hub', password='technopass@crat', headless_browser=True)
session.login()

# session.set_smart_hashtags(['coding', 'programming','hacking'], limit=3, sort='top', log_tags=True)
# session.like_by_tags(['pythonprogramming','coding','c++','c','javaprogramming'], amount=5)
# session.set_dont_like(['nsfw','naked','snake'])
# session.set_smart_location_hashtags(['204517928/chicago-illinois', '213570652/nagoya-shi-aichi-japan'], radius=20, limit=10)
# session.like_by_locations(locations=['delhi','haryana'], amount=5, skip_top_posts=False)
# session.set_do_follow(True, percentage=30)
# session.set_do_comment(True, percentage=50)
# session.set_comments(['Nice post',"you're doing great job",'follow my page','wow'])
# session.set_relationship_bounds(enabled=True, max_followers=4000, min_following=1000)
# session.set_quota_supervisor(enabled=True, peak_comments_daily=200, peak_comments_hourly=70, peak_follows_daily=60, peak_follows_hourly=10,
# peak_likes_hourly=40, peak_likes_daily=400)

session.set_smart_hashtags(['cycling', 'roadbike'], limit=3, sort='top', log_tags=True)
# session.set_smart_location_hashtags(['204517928/chicago-illinois', '213570652/nagoya-shi-aichi-japan'], radius=20, limit=10)
session.like_by_tags(amount=10, use_smart_hashtags=True)


session.end()