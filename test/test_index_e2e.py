import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class E2ETests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(service=Service('./driver/chromedriver'))
		self.driver.get('http://localhost:5000')
	
	def tearDown(self):
		self.driver.quit()

	def test_broser_title_contains_app_name(self):
		self.assertIn('Named Entity', self.driver.title)

	def test_page_heading_is_named_entity_finder(self):
		heading = self._find('heading')
		self.assertEqual('Named Entity Finder', heading.text)

	def test_page_has_input_for_text(self):
		input_element = self._find('input-text')
		self.assertIsNotNone(input_element)

	def test_page_has_button_for_submitting_text(self):
		submit_button = self._find('find-button')
		self.assertIsNotNone(submit_button)

	def test_page_has_table(self):
		input_element = self._find('input-text')
		submit_button = self._find('find-button')
		input_element.send_keys("France and Germany share a border in Europe")
		submit_button.click()
		table = self._find('ner-table')
		self.assertIsNotNone(table)

	def _find(self, val):
		return self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{val}"]')