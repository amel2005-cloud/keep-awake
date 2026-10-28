import sys
from playwright.sync_api import sync_playwright

URL = "https://layanan-ojk-jember.streamlit.app/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    # Kalau app tidur, klik tombol bangunkan
    try:
        btn = page.get_by_role("button", name="Yes, get this app back up!")
        btn.wait_for(timeout=15000)
        btn.click()
        print("Tombol wake-up diklik")
    except Exception:
        print("Tidak ada tombol wake-up, app kemungkinan sudah hidup")

    # Beri waktu app boot dan buka WebSocket
    page.wait_for_timeout(90000)
    browser.close()
    print("Selesai")
