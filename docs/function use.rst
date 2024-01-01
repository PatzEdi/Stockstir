.. _function use:

*************
Function Use
*************

.. note::

    The Function Use section of this documentation will only cover the Providers, Tools, and API classes and their functions, as those are the only ones needed for your data gathering. As stated before, the gatherInfo class should not be touched for your purposes, as the other classes (especially Tools) combine the functions in gatherInfo to make the tools you will be using.

Importing
----------

If you want to import the full library:

.. code-block:: python

    import Stockstir


**IMPORTANT: For the purpose of this part of the documentation, we will be importing the library like so:**

.. code-block:: python

    from Stockstir import Providers
    from Stockstir import Tools
    from Stockstir import API


The reason we do this is because this section of the guide will only be using the **Providers, Tools, an API** classes as they are the only ones we need.

Providers Class Usage
---------------------

The **Providers** class stores the dictionary of providers that Stockstir uses to gather data. The dictionary is stored in the variable ``providers``.

The dictionary looks like this:

.. code-block:: python

    providers = {
		"https://www.cnbc.com/quotes/": '(?<="price":")(.*)(?=","priceChange":")',
		"https://money.cnn.com/quote/quote.html?symb=": 'BatsUS">(.*?)</span>',
		"https://www.zacks.com/stock/quote/": 'last_price">\$(.*?)<span>',
	}
As you can see, the dictionary contains the URL of the provider as the key, and the regex pattern as the value. The regex pattern is used to find the price of the stock in the HTML of the website.

The class itself also contains a ``provider_number`` variable, which can be manually set to be equal to a provider number in the dictionary. This is useful if you want to use a specific provider for your data gathering. The default is set to 0, or in other words, the first provider in the dictionary (CNBC).

The ``provider_number`` variable can be set like so:

.. code-block:: python
    # Here we set the provider_number instance variable to 0, which is the first provider in the dictionary (in this case CNBC, as seen in the dictionary above)
    Providers.provider_number = 0

Do note that the provider_number is 0 by default. Make sure that if you do set the provider_number to a different number that it is in between the range of 0 and the length of the dictionary - 1. This is because the dictionary is a list, and the first index of a list is 0, and the last index is the length of the list - 1.

The Providers class has two functions which you can use, but one in particular which is of use:

``runProviderChecks`` function:

This function is used to check if each provider is working properly. It first checks if the request is successful, and then it checks if the regex is successful. If both are successful, then the provider is working properly. If one or both of them are not successful, then the provider is not working properly.

You can run this function like so:

.. code-block:: python

    Providers.runProviderChecks() # There is also an optional parameter to change the stock symbol to do the tests with, but the default is AMZN in this case.

This function, along with the optional parameter of changing the stock symbol to do the tests with, also has an optional parameter to exitOnFailure, which by default is true. If one of the providers fails, the function will exit. If you want to continue the function even if one of the providers fails, you can set the parameter exitOnFailure to false.

It returns True or False, True being that all of the providers are working properly, and False being that one or more of the providers are not working properly.

Another function that the Providers class has:

``testSelectedProvider`` function:

This function is mostly used by the program itself, but it can be used by you if you want to test a specific provider, which in this case is the one selected by the variable Providers.provider_number. The provider number is the index of the provider in the dictionary. For example, if you want to test the second provider in the dictionary, you would do this:

.. code-block:: python

    Providers.provider_number = 1 # Set the provider number to 1, which is the second provider in the dictionary
    Providers.testSelectedProvider() # Test the provider

This function will return a boolean value of True if the provider is working properly, and False if it is not.

Tools Class Usage
-----------------

**IMPORTANT INFORMATION BEFORE YOU PROCEED:**

* stockSymbol = company symbol (ticker symbol). Ex: "TSLA". type = str
* iterations = Number of data samples to gather. type = int
* randomUserAgent = use a random user agent out of 24 user agents. type = bool
* breakInterval = time between each data sample gathered, default is 5 seconds (Lowering this could result in duplicate values). type = int
* antiBan = Randomizes request time, making it less suspicious that the requests are automated. type = bool
* printOUTPUT = print each stock value every iteration. type = bool
* returnTimeSpent = Returns the total time spent at gathering the samples. type = bool

The parameters listed above are the parameters that you will encounter in this section of the documentation. Please take a look before proceeding.

The optional parameters that are of a boolean type are by default set to False. If you want to enable them, set them to True.

Other optional parameters of for example type int can be modified by specifying their values (such as breakInterval, which has a default value of 5, can be edited by doing for example breakInterval = 10)


Usage of the ``getSinglePrice`` Function:
             ++++++++++++++++++   
The ``getSinglePrice`` function is the basic function of the Stockstir library. 

It takes in one required parameter: stockSymbol
It also takes in one optional parameter: randomUserAgent

If you want the most basic usage, you can do so like this:

.. code-block:: python

    singlePrice = Tools.getSinglePrice("stockSymbol") #Replace the stockSymbol with any other company, and make sure its in quotations!
    print(singlePrice)

The above code will store the returned value of the getSinglePrice function into the variable singlePrice. You can then view the single price by printing the variable as shown. 

If you want to use the optional parameter "randomUserAgent", you can do so like this:

.. code-block:: python

    singlePrice = Tools.getSinglePrice("stockSymbol", randomUserAgent = True) #Replace the stockSymbol with any other company, and make sure its in quotations!
    print(singlePrice)


Usage of the ``multiDataGathering`` Function:
             ++++++++++++++++++++++   
The ``multiDataGathering`` function is the most complex of functions in the **Tools** class as it has many features to choose from.

Here is the basic usage that only uses the required parameters:

.. code-block:: python

    stockPrices = Tools.multiDataGathering("stockSymbol", iterations) #The iterations parameter is in the form of an integer.
    print(stockPrices)


Here, the printed value of the variable stockPrices is going to be returned as a list of values, and the amount of those values depends on the number you put as the value for the iterations parameter. 

This is the basic us of this function. Now, lets take a look at the full function with all of its parameters:

.. code-block:: python

    stockPrices = Tools.multiDataGathering("stockSymbol", iterations, breakInterval = 5, antiBan = False, randomUserAgent = False, printOUTPUT = False, returnTimeSpent = False)


Here, you can see all of the other parameters. Let's go through them:

The breakInterval parameter is in the form of an integer, and is the time between each data sample gathered. The default value of the break interval is 5, which is equivalent to 5 seconds per request. The antiBan feature randomizes the time of each request by a small amount in order to bypass any systems that look for a constant multi-request time in order to avoid bot-like interactions. The randomUserAgent parameter randomizes user agents for each request.

Now, for the printOUTPUT and the returnTimeSpent parameters.

The printOUTPUT parameter prints out the values of each data sample while the request is happening. So instead of waiting for each value to be appended and then printing the full list, the printOUTPUT parameter prints each value as it is happening. This can be useful if you want to see real time data and the speed all depends on the breakInterval parameter. 

The returnTimeSpent function is best used if you want to analyze data over a function of time. This can also be used with the getTrend function which is discussed after this. If you want to use the returnTimeSpent function, do so like this:

.. code-block:: python

    stockPrices, timeSpent = Tools.multiDataGathering("stockSymbol", iterations, returnTimeSpent = True)


Using the extra timeSpent variable, the timeSpent variable will store the value of the time spent to gather the data, and the stockPrices variable will store the prices separately in the form of a list. Make sure to make this separation to avoid confusion in data when you want to see the time spent of the data you collected. 

Usage of the ``getTrend`` Function:
             ++++++++++++   
The ``getTrend`` function is very simple and easy to use. Here is the basic usage:

.. code-block:: python

    Trend = Tools.getTrend(pricesList)


The pricesList is in the form of a list. You can get the pricesList by using the ``multiDataGathering`` function and storing its output in a variable, or putting the ``getSinglePrice`` function in a for loop yourself.

The variable Trend will store a value in terms of a string. 

If you want to use the optional parameter returnChange, you can do so like this:

.. code-block:: python

    Trend, Change = Tools.getTrend(pricesList, returnChange = True)


This will store the change of the last and the first data sample in the variable Change, which can be used to analyze data with the usage of the returnTimeSpent parameter in the ``multiDataGathering`` function. 

Usage of the ``saveDataToFile`` Function:
             ++++++++++++++++++
The ``saveDataToFile`` function is used to save the data collected to a file. It appends a new "Log" to the file in case the file already exists in the specified directory. If it does not exist in the specified directory, then a new file will be created. Basic usage applies:

.. code-block:: python

    Tools.saveDataToFile(data, saveFilePath) #Where data is the prices in the form of a list and saveFilePath is the directory (in quotes)


This will create a file in the specified directory of parameter saveFilePath including the:

* Date 
* Data (Price list)
* Time Spent
* Trend

If you only give the two parameters data and saveFilePath, the Time Spent and Trend will be defined as undefined. The format, as an example, is as follows:::

    Sat Mar 18 13:09:16 2023
    Data: [180.13, 180.13, 180.13]
    Time Spent: undefined
    Trend: undefined

If you want to give more parameters, you do not necessarily have to have both the timeSpent and the trend parameter defined, but you can have either or (or both, of course).

Say you have the timeSpent variable that you gathered from the ``multiDataGathering`` function, and you got the trend from the ``getTrend`` function:

.. code-block:: python

    Tools.saveDataToFile(data, saveFilePath, timeSpent = timeSpent, trend = Trend)


This would append the file like this, with timeSpent being a number (in this case, 10) and trend being a string (in this case, neutral):::

    Sat Mar 18 13:06:43 2023
    Data: [180.13, 180.13, 180.13]
    Time Spent: 10
    Trend: neutral

API Class Usage
---------------

The **API** class has a few functions that have yet to be developed. However, they can still be used. Initial support for AlphaVantage has been implemented, as well as getting the JSON object through CNBC's API.

The AlphaVantage API can be used to gather the data (in terms of JSON format) of a stock symbol like so:

.. code-block:: python

    data = API.getAlphaVantageData("stockSymbol", apiKey) #Replace the stockSymbol with any other company, and make sure its in quotations! Also replace the apiKey with your own API key.
    print(data)

The function also has a customizable parameter, type, which can be set to the type of stock. The default value is 'TIME_SERIES_INTRADAY', which is the intraday time series of the stock. You can change this to 'TIME_SERIES_DAILY' to get the daily time series of the stock. You can also change this to 'TIME_SERIES_WEEKLY' to get the weekly time series of the stock. You can also change this to 'TIME_SERIES_MONTHLY' to get the monthly time series of the stock, etc.

Although pretty bare-bones as of now, the AlphaVantage API is a start in order to gather info as an alternative to the class web-scraping and regex method used in the gatherInfo and Tools classes.

The CNBC api extracts the JSON format of a stock symbol, and certain functions have already been made:

``getCNBCAPIJSONData``:

This is a function used to get the whole JSON format of the stock symbol. There have been other functions which will be explained below. Nonetheless, this function takes in one parameter, which is the stock symbol, and returns the json data.

Regarding the functions that use the ``getCNBCAPIJSONData`` function, they are as follows:

``listCNBCData``:

This function lists each data point within the data gathering by the ``getCNBCAPIJSONData`` function. It takes in one parameter, which is the stock symbol, and prints out each data point.

Once the data is printed out, it also returns two values: the keys, and the values, each as a list. The keys are the data points, and the values are the values of each data point, withint the json data.

You can use it like so:

.. code-block:: python

    keys, values = API.listCNBCData("stockSymbol") #Replace the stockSymbol with any other company, and make sure its in quotations.
    print(keys)
    print(values)

The last function of the **API** class is:

``getPriceCNBCAPI``:

The function prints out the price of whatever stock symbol you input into it. It can be used as an alternative to the classic Tools.getSinglePrice("stockSymbol") method, in case all providers in the Providers.providers dictionary fail (very unlikely).

You can use it like so:

.. code-block:: python

    price = API.getPriceCNBCAPI("stockSymbol") #Replace the stockSymbol with any other company, and make sure its in quotations.

    print(price)