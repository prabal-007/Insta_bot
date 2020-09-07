from instapy import InstaPy
import schedule
import time

def job():
    session = InstaPy(username=user, password=passw, headless_browser=True)
    try:
        session = InstaPy(selenium_local_session=False) 
        session.set_selenium_remote_session(selenium_url=r'http://selenium:4444//wd//hub')
        session.login()
        session.set_do_comment(enabled=True, percentage=20)
        session.set_comments(['Well done!'])
        session.set_do_follow(enabled=True, percentage=5, times=2)
        session.like_by_tags(['love'], amount=100, media='Photo')
        session.end()
    except Exception as e:
        import traceback
        print(traceback.format_exc())

def basic():
    global user, passw
    user=input('Username  - ')
    passw=input('Password - ')
    print(f'searching https://www.instagram/{user}.......')
    print('/..........')
    time.sleep(3)
    print('/..................')
    time.sleep(5)
    print('/.............................Working')
    time.sleep(3)
    print('..\nIn progress')

user = ''
passw = ''
basic()
schedule.every().day.at("06:35").do(job)
schedule.every().day.at("16:22").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
