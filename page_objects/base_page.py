from playwright.sync_api import Page, Playwright
from page_objects.client_search import ClientSearch


class BasePage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def click_adviser_workplace(self):
        self.page.locator(BasePage.Locators.ADVISER_WORKPLACE).click()
        self.page.locator(BasePage.Locators.BASE_SEARCH).click()
        return self

    def add_template_category(self):
        self.page.locator(BasePage.Locators.ADMINISTRATION).click()
        self.page.locator(BasePage.Locators.DOCDESIGNER).click()
        self.page.locator(BasePage.Locators.TEMPLATES).click()
        self.page.locator(BasePage.Locators.TEMPLATE_CATEGORIES).click()
        self.page.locator(BasePage.Locators.CATEGORY_NAME).fill(BasePage.Values.CATEGORY_NAME_VALUE)
        self.page.locator(BasePage.Locators.CATEGORY_DESC).fill(BasePage.Values.CATEGORY_DESC_VALUE)
        self.page.locator(BasePage.Locators.CREATE_CATEGORY).click()
        return self

    def add_dd_template_and_promote(self, template, category):
        self.page.locator(BasePage.Locators.ADMINISTRATION).click()
        self.page.locator(BasePage.Locators.DOCDESIGNER).click()
        self.page.locator(BasePage.Locators.TEMPLATE_TAB).click()
        self.page.locator(BasePage.Locators.TEMPLATE_ACTIONS).click()
        self.page.locator(BasePage.Locators.CREATE_TEMPLATE).click()
        self.page.frame_locator(BasePage.Locators.TEMPLATE_IFRAME).locator(BasePage.Locators.TEMPLATE_NAME).\
            fill(template)
        self.page.frame_locator(BasePage.Locators.TEMPLATE_IFRAME).\
            locator(BasePage.Locators.Choose_Available_Categories_CheckBox).click()
        self.page.frame_locator(BasePage.Locators.TEMPLATE_IFRAME).\
            locator(BasePage.Locators.CATEGORY_LIST).select_option(label=category)
        self.page.frame_locator(BasePage.Locators.TEMPLATE_IFRAME).\
            locator(BasePage.Locators.CREATE_TEMPLATE_BUTTON).click()
        # Promote
        tn = template
        self.page.wait_for_timeout(1000)
        self.page.locator(BasePage.Locators.DOCDESIGNER).click()
        self.page.locator(BasePage.Locators.TEMPLATE_TAB).click()
        self.page.locator(BasePage.Locators.FILTER_NAME).fill(tn)
        self.page.locator('xpath=//a[text()="Filter"]').click()
        self.page.wait_for_timeout(1000)
        self.page.locator("tbody > tr:nth-of-type(2) [title='Open']").click()
        self.page.locator('xpath=//a[text()="Promote"]').click()
        self.page.wait_for_timeout(1000)
        self.page.locator(BasePage.Locators.TEMPLATE_TAB).click()

    def promote_template(self, template_name):
        self.page.locator(BasePage.Locators.ADMINISTRATION).click()
        self.page.locator(BasePage.Locators.DOCDESIGNER).click()
        # self.page.locator(BasePage.Locators.TEMPLATE_TAB).click()
        tn = template_name
        self.page.locator(BasePage.Locators.FILTER_NAME).fill(tn)
        self.page.locator('xpath=//a[text()="Filter"]').click()
        self.page.wait_for_timeout(1000)
        self.page.locator("tbody > tr:nth-of-type(2) [title='Open']").click()
        self.page.locator('xpath=//a[text()="Promote"]').click()

    class Locators:
        ADVISER_WORKPLACE = "a[title = \"Adviser Workplace\"]"
        BASE_SEARCH = "text=Clients By Name"
        ADMINISTRATION = "a[id = menu_node_administration]"
        DOCDESIGNER = "a[title = \"Document Designer\"]"
        TEMPLATES = "a[ui_test_id = \"nav-link6\"]"
        TEMPLATE_CATEGORIES = "a[title = \"Template Categories\"]"
        CATEGORY_NAME = "input[id = \"id_Name\"]"
        CATEGORY_DESC = "input[id = \"id_Description\"]"
        CREATE_CATEGORY = "[ui_test_id = \"btn25\"]"
        TEMPLATE_TAB = "a[ui_test_id = \"nav-link11\"]"
        TEMPLATE_ACTIONS = "button[ui_test_id = \"template-actions\"]"
        CREATE_TEMPLATE = "a[ui_test_id = \"dropdown-menu-item10\"]"
        TEMPLATE_NAME = "input[id = \"id_TemplateName\"]"
        TEMPLATE_IFRAME = "iframe[id=\'frame1\']"
        Choose_Available_Categories_CheckBox = "input[id = \"OptionsList_2\"]"
        CATEGORY_LIST = "select[id = \"CategoryList\"]"
        CREATE_TEMPLATE_BUTTON = "a[ui_test_id = \"btn1\"]"
        FILTER_NAME = "input[id = \"id___filterName\"]"

    class Values:
        CATEGORY_NAME_VALUE = "dn_temp_cat_002"
        TEMPLATE_NAME_VALUE = "template_name_1"
        CATEGORY_DESC_VALUE = "ddddd"


