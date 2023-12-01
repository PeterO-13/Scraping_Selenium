from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://techstepachedemy.com/trial-of-the-stones")

# Riddle of stone
stone_input = browser.find_element_by_css_selector('input[id="r1Input"]')
stone_answer_butn = browser.find_element_by_css_selector("button[id='r1Btn']")
stone_result = browser.find_element_by_css_selector('div[id="passwordBanner"] > h4')

# Riddle of secrets
secrets_input = browser.find_element_by_css_selector(
   "input[id='r2input']"
)
secret_answer_butn = browser.find_element_by_css_selector(
    "button#r2Butn"
)
# Two Merchants
richest_merchants_name = browser.find_element_by_xpath(
    "//p[text()='3000']"
).text
merchants_input = browser.find_element_by_css_selector("input[id='r3Input']")
merchants_answer_butn = browser.find_element_by_css_selector(
    "button[name='checkButn']"
)
check_butn = browser.find_element_by_css_selector(
    "button[name='checkButn']"
)
complete_msg = browser.find_element_by_css_selector("div[id='trialCompleteBanner h4']")



