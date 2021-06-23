import pytest
from selenium import webdriver

l = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'en', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Сhoose any language from the possible")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    if lang not in l:
        raise pytest.UsageError("--language There is no language")
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()