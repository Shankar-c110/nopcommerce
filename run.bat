
@echo off
REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run pytest with HTML report and browser option
rem pytest -s -v -m "sanity" --html=.\reports\report.html --browser=chrome
pytest -s -v -m "regression" --html=.\reports\report.html --browser=chrome
rem pytest -s -v -m "sanity and regression" --html=.\reports\report.html --browser=chrome
rem pytest -s -v -m "sanityor regression" --html=.\reports\report.html --browser=chrome

pause
