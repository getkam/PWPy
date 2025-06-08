from typing import Optional

from src.pom.pages.base_pom import PageObjectModelBase
from src.pom.components.header_component import Header

class CartPage(PageObjectModelBase):
    def __init__(self,page):
        super().__init__(page)
        self.header = Header(page)

        # CartPage Locators
        self.heading = self.page.get_by_role("heading", name="Products")
        self.total_price = self.page.locator("#totalp")
        self.place_order = self.get_by_role("button", name="Place Order")

    def table_cell(self, row_index, col_index):
        return self.page.locator(f"table tr:nth-child({row_index}) td:nth-child({col_index})")

    def product_picture(self, row_index):
        return self.table_cell(row_index,1)

    def product_title(self, row_index):
        return self.table_cell(row_index, 2)

    def product_price(self, row_index):
        return self.table_cell(row_index, 3)

    def product_delete(self, row_index):
        return self.table_cell(row_index, 4)

    def row_number(self, title:str) -> int:
        title_cells = self.page.locator("table tr td:nth-child(2)")
        row_count = title_cells.count()

        for i in range(row_count):
            cell_text =  title_cells.nth(i).inner_text()
            if cell_text and title in cell_text:
                return i + 1
        return 0

