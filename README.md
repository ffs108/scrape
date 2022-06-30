Data scraper using Python (specifically pandas and selenium mostly). Checks the NBA website for advanced player stats and places them into a dataframe which can then be used to either convert data into CSV or try some more advanced statistic prediction.

Included a python file which can be run from terminal instead of Jupyter. A chromedriver.exe in path is needed as selenium needs the Google API in order to use Chrome. That being said, this can be run as is if just changed to firefox in the driver variable declaration.

Must be run in the Jupyter Notebook enviroment to actually start scraping and saving onto a new xlsx file. Otherwise if run from a terminal or ide, just PATH error will ensue.
