from instapy import InstaPy
import schedule
import time

def job():
    session = InstaPy(username='akshaygupta_17', password='Akshay@1725', headless_browser=True)
    try:
        session = InstaPy(selenium_local_session=False) # Assuming running in Compose
        session.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
        session.login()
        session.set_do_comment(enabled=True, percentage=20)
        session.set_comments(['Well done!'])
        session.set_do_follow(enabled=True, percentage=5, times=2)
        session.like_by_tags(['love'], amount=100, media='Photo')
        session.end()
    except Exception as e:
        import traceback
        print(traceback.format_exc())

schedule.every().day.at("06:35").do(job)
schedule.every().day.at("16:22").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
