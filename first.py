from playwright.sync_api import Page, expect
def test_highlight_search(page:Page):
    page.goto("https://playwright.dev/python/")
    search_icon = page.locator('.DocSearch-Search-Icon')
    search_icon.highlight();
    search_icon.click();

def test_highlight_getstarted(page :Page):
    page.goto("https://playwright.dev/python/")
    page.get_by_role("link",name="Get started").click()
    
def test_highlight_github_star(page: Page):
    page.goto("https://playwright.dev/python/")
    star_button = page.locator('[aria-label="Star microsoft/playwright-python on GitHub"]')
    star_button.highlight()
    star_button.click()  
    page.wait_for_timeout(5000)
    
def test_highlight_star2(page: Page ):
    page.goto("https://playwright.dev/python/")
    page.locator('[aria-label="78k+ stargazers on GitHub"]').highlight()
    
