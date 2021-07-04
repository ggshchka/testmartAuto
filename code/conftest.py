from data import BASE_URL
from ui.fixtures import *

def pytest_addoption(parser):
    """ add option """
    parser.addoption('--url', default=BASE_URL)
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')


@pytest.fixture(scope='session')
def config(request):
    """ config """
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    return {'browser': browser, 'version': version,
            'url': url, 'download_dir': '/tmp'}
