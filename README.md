# Todo List Application

## Setup
1. Clone repository
2. Install dependencies: Collecting Flask==2.1.0 (from -r requirements.txt (line 1))
  Downloading Flask-2.1.0-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: Flask-SQLAlchemy==2.5.1 in /opt/venv/lib/python3.12/site-packages (from -r requirements.txt (line 2)) (2.5.1)
Collecting pytest==7.1.2 (from -r requirements.txt (line 3))
  Downloading pytest-7.1.2-py3-none-any.whl.metadata (7.8 kB)
Requirement already satisfied: Werkzeug>=2.0 in /opt/venv/lib/python3.12/site-packages (from Flask==2.1.0->-r requirements.txt (line 1)) (3.1.3)
Requirement already satisfied: Jinja2>=3.0 in /opt/venv/lib/python3.12/site-packages (from Flask==2.1.0->-r requirements.txt (line 1)) (3.1.4)
Requirement already satisfied: itsdangerous>=2.0 in /opt/venv/lib/python3.12/site-packages (from Flask==2.1.0->-r requirements.txt (line 1)) (2.2.0)
Requirement already satisfied: click>=8.0 in /opt/venv/lib/python3.12/site-packages (from Flask==2.1.0->-r requirements.txt (line 1)) (8.2.1)
Requirement already satisfied: SQLAlchemy>=0.8.0 in /opt/venv/lib/python3.12/site-packages (from Flask-SQLAlchemy==2.5.1->-r requirements.txt (line 2)) (2.0.41)
Requirement already satisfied: attrs>=19.2.0 in /opt/venv/lib/python3.12/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (25.3.0)
Collecting iniconfig (from pytest==7.1.2->-r requirements.txt (line 3))
  Downloading iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Requirement already satisfied: packaging in /opt/venv/lib/python3.12/site-packages (from pytest==7.1.2->-r requirements.txt (line 3)) (24.2)
Collecting pluggy<2.0,>=0.12 (from pytest==7.1.2->-r requirements.txt (line 3))
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting py>=1.8.2 (from pytest==7.1.2->-r requirements.txt (line 3))
  Downloading py-1.11.0-py2.py3-none-any.whl.metadata (2.8 kB)
Collecting tomli>=1.0.0 (from pytest==7.1.2->-r requirements.txt (line 3))
  Downloading tomli-2.2.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (11 kB)
Requirement already satisfied: MarkupSafe>=2.0 in /opt/venv/lib/python3.12/site-packages (from Jinja2>=3.0->Flask==2.1.0->-r requirements.txt (line 1)) (2.1.5)
Requirement already satisfied: greenlet>=1 in /opt/venv/lib/python3.12/site-packages (from SQLAlchemy>=0.8.0->Flask-SQLAlchemy==2.5.1->-r requirements.txt (line 2)) (3.2.3)
Requirement already satisfied: typing-extensions>=4.6.0 in /opt/venv/lib/python3.12/site-packages (from SQLAlchemy>=0.8.0->Flask-SQLAlchemy==2.5.1->-r requirements.txt (line 2)) (4.12.2)
Downloading Flask-2.1.0-py3-none-any.whl (95 kB)
Downloading pytest-7.1.2-py3-none-any.whl (297 kB)
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
Downloading tomli-2.2.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (233 kB)
Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Installing collected packages: tomli, py, pluggy, iniconfig, pytest, Flask
  Attempting uninstall: Flask
    Found existing installation: Flask 2.0.3
    Uninstalling Flask-2.0.3:
      Successfully uninstalled Flask-2.0.3

Successfully installed Flask-2.1.0 iniconfig-2.1.0 pluggy-1.6.0 py-1.11.0 pytest-7.1.2 tomli-2.2.1
3. Initialize database: 

## Running Locally


## Testing
============================= test session starts ==============================
platform linux -- Python 3.12.10, pytest-7.1.2, pluggy-1.6.0 -- /opt/venv/bin/python3.12
cachedir: .pytest_cache
rootdir: /root/todo_app
plugins: anyio-4.9.0, langsmith-0.3.45
collecting ... collected 0 items / 1 error

==================================== ERRORS ====================================
_________________________ ERROR collecting test_app.py _________________________
ImportError while importing test module '/root/todo_app/test_app.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_app.py:2: in <module>
    from app import app, db, Todo
app.py:1: in <module>
    from flask import Flask, render_template, request, redirect, url_for
/opt/venv/lib/python3.12/site-packages/flask/__init__.py:7: in <module>
    from .app import Flask as Flask
/opt/venv/lib/python3.12/site-packages/flask/app.py:27: in <module>
    from . import cli
/opt/venv/lib/python3.12/site-packages/flask/cli.py:17: in <module>
    from .helpers import get_debug_flag
/opt/venv/lib/python3.12/site-packages/flask/helpers.py:14: in <module>
    from werkzeug.urls import url_quote
E   ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (/opt/venv/lib/python3.12/site-packages/werkzeug/urls.py)
=============================== warnings summary ===============================
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:962
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:962
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:962
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:962
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:962
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:962
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:962
  /opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:962: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    inlocs = ast.Compare(ast.Str(name.id), [ast.In()], [locs])

../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:965
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:965
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:965
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:965
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:965
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:965
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:965
  /opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:965: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expr = ast.IfExp(test, self.display(name), ast.Str(name.id))

../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1075
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1075
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1075
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1075
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1075
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1075
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1075
  /opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1075: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    syms.append(ast.Str(sym))

../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1077
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1077
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1077
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1077
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1077
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1077
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1077
  /opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:1077: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expls.append(ast.Str(expl))

../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:826: 30 warnings
  /opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:826: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    keys = [ast.Str(key) for key in current.keys()]

../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:936
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:936
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:936
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:936
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:936
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:936
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:936
  /opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:936: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    assertmsg = ast.Str("")

../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:938
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:938
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:938
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:938
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:938
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:938
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:938
  /opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:938: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    template = ast.BinOp(assertmsg, ast.Add(), ast.Str(explanation))

../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:950
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:950
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:950
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:950
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:950
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:950
../../opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:950
  /opt/venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:950: DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead
    clear = ast.Assign(variables, ast.NameConstant(None))

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
ERROR test_app.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
======================== 79 warnings, 1 error in 0.31s =========================

## Deployment
1. Configure AWS credentials in GitHub Secrets
2. Push to main branch to trigger CI/CD pipeline
3. Application will be deployed to EC2 instance on successful build
