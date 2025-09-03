import pytest
from dash import html, dcc

# Selenium + webdriver-manager setup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Monkey-patch Selenium so dash[testing] uses webdriver-manager
import selenium.webdriver.chrome.webdriver
selenium.webdriver.chrome.webdriver.Service = lambda *a, **kw: Service(ChromeDriverManager().install())

# Import your app
import app


# ---------- Tests ----------

def test_header_present(dash_duo):
    dash_duo.start_server(app.app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel Sales Visualiser" in header.text   # ✅ matches your app


def test_graph_present(dash_duo):
    dash_duo.start_server(app.app)
    graph = dash_duo.find_element("#sales-line-chart")    # ✅ matches id in app.py
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app.app)
    region_picker = dash_duo.find_element("#region-selector")  # ✅ matches id in app.py
    assert region_picker is not None
