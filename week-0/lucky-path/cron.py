import schedule
import time

def run_crawler():
    print(">> 크롤링 작업 시작")
    # 여기에 크롤러 실행 코드를 추가하세요
    print(">> 크롤링 작업 완료")

schedule.every(5).seconds.do(run_crawler) # 5초마다 실행

while True:
    schedule.run_pending()
    time.sleep(1)