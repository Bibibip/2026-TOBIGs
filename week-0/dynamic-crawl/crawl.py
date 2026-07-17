from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import getpass

# --- 1. 로그인 정보 ---
my_id = input("네이버 아이디를 입력하세요: ")
my_pw = getpass.getpass("네이버 비밀번호를 입력하세요: ")

# --- 2. Selenium 드라이버 설정 ---
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

# --- 3. 네이버 로그인 페이지로 이동 및 로그인 실행 ---
try:
    driver.get("https://nid.naver.com/nidlogin.login")
    time.sleep(1) # 페이지 로딩 대기

    # --- ★★★ 여기가 바뀐 부분 ★★★ ---
    # 아이디와 비밀번호 입력창 요소를 찾아서 타이핑하듯이 값을 입력합니다.
    id_input = driver.find_element(By.ID, "id")
    id_input.send_keys(my_id)
    time.sleep(1) # 로봇으로 인식되지 않도록 약간의 딜레이를 줍니다.

    pw_input = driver.find_element(By.ID, "pw")
    pw_input.send_keys(my_pw)
    
    time.sleep(1)
    # --------------------------------

    # 로그인 버튼 클릭
    driver.find_element(By.ID, "log.login").click()
    input("2단계 인증 또는 자동입력 방지문자를 해결한 후, 터미널로 돌아와 Enter 키를 눌러주세요...")

    # --- 4. 네이버 메일 페이지로 이동 ---
    print("네이버 메일 페이지로 이동합니다...")
    driver.get("https://mail.naver.com/v2/folders/0")
    time.sleep(5)

    # --- 5. 메일 제목 파싱 (BeautifulSoup) ---
    print("메일 제목을 파싱합니다...")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.mail_list.font_small')
    mail_titles = ul.select('li > div > div > div > a')

    if not mail_titles:
        print("메일 제목을 찾을 수 없습니다. 로그인이 실패했거나 페이지 구조가 변경되었을 수 있습니다.")
    else:
        print("\n--- [최신 메일 제목 목록] ---")
        for i, title in enumerate(mail_titles, 1):
            print(f"{i}. {title.get_text(strip=True)}")
        print("--------------------------\n")

except Exception as e:
    print(f"오류가 발생했습니다: {e}")

finally:
    # --- 6. 드라이버 종료 ---
    print("5초 뒤에 브라우저를 종료합니다.")
    time.sleep(5)
    driver.quit()
