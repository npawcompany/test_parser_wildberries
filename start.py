# -*- coding: utf-8 -*-

from playwright.async_api import async_playwright
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import asyncio
import nltk

class ParserWildberries:

	def __init__(self):
		nltk.download('punkt')
		nltk.download('punkt_tab')
		nltk.download('stopwords')

	async def startBrowser(self, headless: bool = True):
		self.playwright = await async_playwright().start()
		self.browser = await self.playwright.chromium.launch(headless=headless)
		self.context = await self.browser.new_context()

	async def closeBrowser(self):
		await self.browser.close()
		await self.playwright.stop()

	async def getPage(self, url:str, timeout:int=0):
		page = await self.context.new_page()
		await page.goto(url)
		await page.wait_for_timeout(timeout)
		return page

	async def getProduct(self, url:str) -> dict:
		page = await self.getPage(url,5000)

		title = page.locator('h1.product-page__title')
		title = await title.inner_text() if await title.count() else "Название не найдено"

		button_locator = page.locator("button.product-page__btn-detail")
		if await button_locator.count() > 0:
			await button_locator.click()
		else:
			print("Кнопка уточнения описания не найдена")
		await page.wait_for_timeout(500)
		description = page.locator("section.product-details__description p")
		description = await description.inner_text()

		keywords = await self.keywords(description)
		await page.close()
		return {
			"title": title,
			"description": description,
			"keywords": keywords
		}

	async def keywords(self, text:str, num_keywords:int=10) -> list:
		tokens = word_tokenize(text.lower())
		stop_words = set(stopwords.words('english') + stopwords.words('russian'))
		words = [word for word in tokens if word.isalnum() and word not in stop_words and len(word)>3]
		word_freq = Counter(words)
		return word_freq.most_common(num_keywords)

	async def getPosition(self, url: str, product_id: str) -> int:
		page = await self.getPage(url, 3000)
		products = page.locator('article')
		for i in range(await products.count()):
			art_id = await products.nth(i).get_attribute("data-nm-id")
			if art_id == product_id:
				await page.close()
				return i + 1
		await page.close()
		return 0

async def main():
	url = "https://www.wildberries.ru/catalog/6013953/detail.aspx"
	product_id = url.split('/')[-2]
	print(product_id)
	PW = ParserWildberries()
	await PW.startBrowser(False)
	product = await PW.getProduct(url)
	if not product:
		return
	print(f"Название товара: {product['title']}")
	print(f"Описание товара: {product['description']}")
	print(f"Ключевые слова: {product['keywords']}")

	for keyword, freq in product['keywords']:
		url = f"https://www.wildberries.ru/catalog/0/search.aspx?search={keyword}"
		position = await PW.getPosition(url, product_id)
		if position:
			print(f'По запросу "{keyword}", товар на {position} месте')
			continue
		print(f'По запросу "{keyword}", товара нет на первой странице')
	await PW.closeBrowser()

if __name__ == "__main__":
	asyncio.run(main())