from distutils.core import setup

version = '0.0.2'
name = 'python_selenium_helper'
url = f'https://github.com/SamuelJansen/{name}/'

setup(
    name = name,
    packages = [
        name,
        f'{name}/api',
        f'{name}/api/src',
        f'{name}/api/src/service'
    ],
    version = version,
    license = 'MIT',
    description = 'python selenium helper',
    author = 'Samuel Jansen',
    author_email = 'samuel.jansenn@gmail.com',
    url = url,
    download_url = f'{url}archive/v{version}.tar.gz',
    keywords = ['selenium', 'python selenium helper package', 'python selenium', 'selenium package'],
    install_requires = [
        'webdriver_manager',
        'selenium',
        'pyautogui',
        'pyperclip'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
    ]
)
