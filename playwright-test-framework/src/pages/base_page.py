class BasePage:
    def __init__(self, page):
        self.page = page

    async def navigate_to(self, url):
        await self.page.goto(url)

    async def find_element(self, selector):
        return await self.page.query_selector(selector)

    async def click(self, selector):
        element = await self.find_element(selector)
        if element:
            await element.click()

    async def fill(self, selector, value):
        element = await self.find_element(selector)
        if element:
            await element.fill(value)

    async def get_text(self, selector):
        element = await self.find_element(selector)
        if element:
            return await element.inner_text()
        return None