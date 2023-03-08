from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://all.uddataplus.dk/opgave/?id=id_menu_opgaver")
    page.click("a.select2-choice")
    page.click("text=College360")
    page.click("button#btnUnilogin")
    page.fill("input#username", "osca1939")
    page.click("button[type=submit]")
    page.fill("input#form-error", "Rzp53qpw2005")
    page.click("button[type=submit]")
    with page.expect_navigation(url="https://all.uddataplus.dk/opgave/"):
        print(page.inner_html("body"))