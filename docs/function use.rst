.. _function use:

*************
Function Use
*************

.. note::

    The Function Use section of this documentation will only cover the Tools class and its functions, as those are the only ones needed for your data gathering. As stated before, the gatherInfo class should not be touched for your purposes, as the Tools class combines the functions in gatherInfo to make the tools you will be using.

Importing
----------

If you want to import the full library:

.. code-block:: python

    import Stockstir


**IMPORTANT: For the purpose of this part of the documentation, we will be importing the library like so:**

.. code-block:: python

    from Stockstir import Tools


The reason we do this is because this section of the guide will only be using the **Tools** class as it is the only one we need.

Usage
-----

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
The ``multiDataGathering`` function is the most complex of functions as it has many features to choose from.

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


Overall Usage (Combining Functions)
-----------------------------------

Here is an example of code that you can take a look at which combines all of these functions together except for the getSinglePrice function (as multiDataGathering is being used here), including some of their parameters:

.. code-block:: python

    prices, timeSpent = Tools.multiDataGathering("TSLA", 3 , breakInterval=3, antiBan = True ,returnTimeSpent = True, printOUTPUT = True) 

    #3 total samples to collect, Each request is every 3 seconds, antiBan is set to active (True), time will be returned, and every single price will be printed in real time. 

    Trend = Tools.getTrend(prices) #Get the trend:

    Tools.saveDataToFile(prices, "/path/to/directory/" , timeSpent=timeSpent, trend = Trend) #Save the data to a file:

