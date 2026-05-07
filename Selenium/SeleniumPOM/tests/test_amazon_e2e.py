import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage



@pytest.mark.parametrize( ("search_product", "brandname", "mensize"),
[
    ("shoes", 'Nike', '9')
])
def test_product_ordering(driver, search_product, brandname, mensize):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    print(f"Search product - {search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load'
    print(f"Search results page loaded successfully = {search_product}")

    productlistingpage = ProductListingPage(driver)

    print(f"Applying Brand Filter - {brandname}")
    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), 'Brand filter did not apply'

    print(f"Applying Size Filter for men's shoes - {mensize}")
    productlistingpage.select_mensize_filter(mensize)

    assert  productlistingpage.check_size_in_title(mensize), 'Mensize filter not applied'