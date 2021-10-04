# Content:
## how to install?

```bash
1. git clone repository
git clone git@github.com:DeepGo-Data-Analysis-Team/deepgo-selenium.git or git clone  https://github.com/DeepGo-Data-Analysis-Team/deepgo-selenium.git
pip install -e .
```


## how to start to use?

```python
from dpg_selenium import DpgSelenium
# headless 为是否显示浏览器
dpg_s = DpgSelenium(headless = True)
url = ""
dpg_s.driver.get(url)
html = dpg_s.driver.page_source
```