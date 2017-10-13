import os


def screenshot(driver, filename):
    base_dir = os.path.dirname(__file__)
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/TestCase')[0]
    file_path = base+'/Report/Screenshot/'+filename
    driver.get_screenshot_as_file(file_path)

