# Content:
## pre-installed required
Download the google chrome with version 94

## how to install?

```bash
1. git clone repository
git clone https://github.com/Tiresiasel/wrapped-selenium.git
pip install -e .
```

## how to start to use?

```python
from wrapped_selenium import WrappedSelenium

# headless 为是否显示浏览器
wrapped_selenium = WrappedSelenium(headless=True)
url = "https://www.google.com"
wrapped_selenium.driver.get(url)
html = wrapped_selenium.driver.page_source
```

## Known Issue
This package doesn't support M1 chip.

