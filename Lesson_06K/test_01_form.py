from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():

    driver = webdriver.Edge()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    for field, value in fields.items():
        driver.find_element(By.NAME, field).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    zip_code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "zip-code")))

    assert "danger" in zip_code.get_attribute("class")

    assert "rgba(132, 32, 41, 1)" == zip_code.value_of_css_property("color")

    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)

        assert "success" in field.get_attribute("class")

        assert "rgba(15, 81, 50, 1)" == field.value_of_css_property("color")

    driver.quit()
