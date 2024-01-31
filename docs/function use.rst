.. _function use:

*************
Function Use
*************

.. note::

    The Function Use section of this documentation will only cover the Providers, Tools, and API classes and their functions, as those are the only ones needed for your data gathering. As stated before, the gatherInfo class should not be touched for your purposes, as the other classes (especially Tools) combine the functions in gatherInfo to make the tools you will be using.

Importing and Instantiating Stockstir
-------------------------------------

If you want to import the full library:

.. code-block:: python

    from stockstir import Stockstir

With the latest release of Stockstir V2, you can now instantiate the library with different parameters, making the process slightly different from before:

.. code-block:: python

    # After importing the library like we did so in the code block above, we can now instantiate the library like so:
    stockstir = Stockstir() # Here, we store the instance of the Stockstir() class into a variable.

By using this method of instantiation, different Stockstir objects, or 'gatherers', with adjusted parameters like so:

.. code-block:: python

    # Instantiate a new Stockstir object:
    stockstir = Stockstir(provider = "cnbc", random_user_agent = True, print_output = True)

.. note::

    This is important. As can be seen, the Stockstir class can take in parameters, which are as follows:
    
    provider - This can be either set to "cnbc", "insider", or "zacks" (You can use the ``list_available_providers`` function to list the providers you can use (explained below)). This is the provider that the Stockstir object will use to gather data (default = "cnbc"). The provider is no longer set by using the provider_number variable in the Providers class, but rather by using this parameter.
    random_user_agent - This can be either set to True or False. This will randomize the user agent for each request. Please note that this only takes effect in all classes other than API (default = False)
    print_output - This can be either set to True or False. This will print the output of each request and general info in the ``multi_data_gathering`` and ``multi_ticker_data_gathering methods``. (default = False)

    Of course, certain parameters such as random_user_agent and print_output can be overriden through function calls by setting those parameters (such as in the get_single_price function, you can set random_user_agent) to True or False.

To access the classes within Stockstir, you can now do so like this:

.. code-block:: python

    # Instantiate a new Stockstir object like we did above:
    stockstir = Stockstir()
    # Instantiate the classes within the Stockstir object (used to access the functions without having to stockstir.classname.function() every time):
    providers = stockstir.providers
    tools = stockstir.tools
    api = stockstir.api

And so after doing this, you can do so many things, such as:

.. code-block:: python

    # Here, we access the get_single_price method, which is found in the tools class.
    price = tools.get_single_price("stock/ticker_symbol") # Replace what is in between the quotes with any other company.
    print(price)

    # Or, you can also create lambda functions to access the methods within a class directly:
    get_single_price = lambda stock_symbol: tools.get_single_price(stock_symbol)
    # Gather the price using the lambda function, and print it:
    price = get_single_price("stock/ticker_symbol") # Replace what is in between the quotes with any other company.
    print(price)

**IMPORTANT: For the purpose of this part of the documentation, we will be importing the library like so:**

.. code-block:: python
    # Instantiate a new Stockstir object:
    stockstir = Stockstir()
    # Instantiate the classes within the Stockstir object (used to access the functions without having to call stockstir.classname.function() every time):
    providers = stockstir.providers
    tools = stockstir.tools
    api = stockstir.api
    

The reason we do this is because this section of the guide will only be using the **Providers, Tools, an API** classes as they are the only ones we need.

Providers Class Usage
---------------------

The **Providers** class stores the dictionary of providers that Stockstir uses to gather data. The dictionary is stored in the variable ``providers``.

The dictionary looks like this:

.. code-block:: python

    providers = {
		"https://www.cnbc.com/quotes/": '(?<="price":")(.*)(?=","priceChange":")',
		"https://markets.businessinsider.com/stocks/": '"currentValue":(.*?),"previousClose":',
		"https://www.zacks.com/stock/quote/": 'last_price">\$(.*?)<span>',
	}
As you can see, the dictionary contains the URL of the provider as the key, and the regex pattern as the value. The regex pattern is used to find the price of the stock in the HTML of the website.

The class itself also contains a ``provider_number`` variable, which can be set when you instantiate a stockstir object like so:

.. code-block:: python
    stockstir = Stockstir(provider = 'insider') # Here, we set the provider to Business Insiders, which is the second provider in the dictionary (in this case, the first provider is CNBC, the second is Business Insiders, and the third is Zacks)

You can also switch the providers. The default is 'cnbc', but for Business Insiders it is 'insider', and Zacks it is 'zacks'. Based on the one picked, the provider_number variable will be set to the index of the provider in the dictionary.

The Providers class has two functions which you can use, but one in particular which is of use:

``run_provider_checks`` function:

This function is used to check if each provider is working properly. It first checks if the request is successful, and then it checks if the regex is successful. If both are successful, then the provider is working properly. If one or both of them are not successful, then the provider is not working properly.

You can run this function like so:

.. code-block:: python

    providers.run_provider_checks() # There is also an optional parameter to change the stock symbol to do the tests with, but the default is AMZN in this case.

This function, along with the optional parameter of changing the stock symbol to do the tests with, also has an optional parameter to exit_on_failure, which by default is true. If one of the providers fails, the function will exit. If you want to continue the function even if one of the providers fails, you can set the parameter exit_on_failure to false.

It returns True or False, True being that all of the providers are working properly, and False being that one or more of the providers are not working properly.

Another function that the Providers class has:

``test_selected_provider`` function:

This function is mostly used by the program itself, but it can be used by you if you want to test a specific provider, which in this case is the one set to the variable Providers.provider_number.

This function will return a boolean value of True if the provider is working properly, and False if it is not.

``list_available_providers`` function:

This function is used to list the available providers that you can use. It prints out a display panel (if print_output is set to True) of the available providers, and returns a boolean (True if working, False if not working).

As stated before, you can set print_output either in the class instance or in the function call. So, if print_output is set to True, the output of this function will look something like this:

.. code-block:: python

    0: cnbc (WORKING)
    1: insider (WORKING)
    2: zacks (WORKING)

The function also returns a True of False statement, depending on whether or not all the providers are working properly.

Tools Class Usage
-----------------

**IMPORTANT INFORMATION BEFORE YOU PROCEED:**

* stock_symbol = company symbol (ticker symbol). Ex: "TSLA". type = str
* iterations = Number of data samples to gather. type = int
* random_user_agent = use a random user agent out of 24 user agents. type = bool
* break_interval = time between each data sample gathered, default is 5 seconds (Lowering this could result in duplicate values). type = int
* anti_ban = Randomizes request time, making it less suspicious that the requests are automated. type = bool
* print_output = print each stock value every iteration. type = bool
* return_time_spent = Returns the total time spent at gathering the samples. type = bool

The parameters listed above are the parameters that you will encounter in this section of the documentation. Please take a look before proceeding.

The optional parameters that are of a boolean type are by default set to False. If you want to enable them, set them to True.

Other optional parameters of for example type int can be modified by specifying their values (such as break_interval, which has a default value of 5, can be edited by doing for example breakInterval = 10)


Usage of the ``get_single_price`` Function:
             ++++++++++++++++++   
The ``get_single_price`` function is the basic function of the Stockstir library. 

It takes in one required parameter: stock_symbol
It also takes in one optional parameter: random_user_agent

If you want the most basic usage, you can do so like this:

.. code-block:: python

    single_price = tools.get_single_price("stock_symbol") #Replace the stock_symbol with any other company, and make sure its in quotations!
    print(single_price)

The above code will store the returned value of the get_single_price function into the variable single_price. You can then view the single price by printing the variable as shown. 

If you want to use the optional parameter "random_user_agent", you can do so like this:

.. code-block:: python

    single_price = tools.get_single_price("stock_symbol", random_user_agent = True) #Replace the stock_symbol with any other company, and make sure its in quotations!
    print(single_price)


Usage of the ``multi_data_gathering`` Function:
             ++++++++++++++++++++++   
The ``multi_data_gathering`` function is one of the most complex of functions in the **Tools** class as it has many features to choose from.

Here is the basic usage that only uses the required parameters:

.. code-block:: python

    stock_prices = tools.multi_data_gathering("stock_symbol", iterations) #The iterations parameter is in the form of an integer.
    print(stock_prices)


Here, the printed value of the variable stockPrices is going to be returned as a list of values, and the amount of those values depends on the number you put as the value for the iterations parameter. 

This is the basic us of this function. Now, lets take a look at the full function with all of its parameters:

.. code-block:: python

    stock_prices = tools.multi_data_gathering("stock_symbol", iterations, break_interval = 5, anti_ban = False, random_user_agent = False, print_output = False, return_time_spent = False)


Here, you can see all of the other parameters. Let's go through them:

The break_interval parameter is in the form of an integer, and is the time between each data sample gathered. The default value of the break interval is 5, which is equivalent to 5 seconds per request. The anti_ban feature randomizes the time of each request by a small amount in order to bypass any systems that look for a constant multi-request time in order to avoid bot-like interactions. The random_user_agent parameter randomizes user agents for each request.

Now, for the print_output and the return_time_spent parameters.

The print_output parameter prints out the values of each data sample while the request is happening. So instead of waiting for each value to be appended and then printing the full list, the print_output parameter prints each value as it is happening. This can be useful if you want to see real time data and the speed all depends on the break_interval parameter. 

The return_time_spent function is best used if you want to analyze data over a function of time. This can also be used with the get_trend function which is discussed after this. If you want to use the return_time_spent function, do so like this:

.. code-block:: python

    stock_prices, time_spent = tools.multi_data_gathering("stock_symbol", iterations, return_time_spent = True)


Using the extra time_spent variable, the time_spent variable will store the value of the time spent to gather the data, and the stock_prices variable will store the prices separately in the form of a list. Make sure to make this separation to avoid confusion in data when you want to see the time spent of the data you collected. 

Usage of the ``multi_ticker_data_gathering`` Function:

The ``multi_ticker_data_gathering`` function is very similar to the ``multi_data_gathering`` function, but it is used to gather data from multiple stock symbols at once.

The parameters it takes in are very similar, but it takes in a list of stock symbols instead of just one stock symbol. Here is the basic usage:

.. code-block:: python

    stock_prices = tools.multi_ticker_data_gathering(["stock_symbol1", "stock_symbol2", "stock_symbol3"], iterations) #The iterations parameter is in the form of an integer.
    print(stock_prices)

In this case, the function returns a dictionary, which contains the stock symbols as the keys, and the values as the list of prices for each stock symbol.

Usage of the ``get_trend`` Function:
             ++++++++++++   
The ``get_trend`` function is very simple and easy to use. Here is the basic usage:

.. code-block:: python

    trend = tools.get_trend(prices_list)


The prices_list is in the form of a list. You can get the prices_list by using the ``multi_data_gathering`` function and storing its output in a variable, or putting the ``get_single_price`` function in a for loop yourself.

The variable Trend will store a value in terms of a string. 

If you want to use the optional parameter return_change, you can do so like this:

.. code-block:: python

    trend, change = tools.get_trend(prices_list, return_change = True)


This will store the change of the last and the first data sample in the variable Change, which can be used to analyze data with the usage of the returnTimeSpent parameter in the ``multi_data_gathering`` function. 

Usage of the ``save_data_to_file`` Function:
             ++++++++++++++++++
The ``save_data_to_file`` function is used to save the data collected to a file. It appends a new "Log" to the file in case the file already exists in the specified directory. If it does not exist in the specified directory, then a new file will be created. Basic usage applies:

.. code-block:: python

    tools.save_data_to_file(data, save_file_path) #Where data is the prices in the form of a list and save_file_path is the directory (in quotes)


This will create a file in the specified directory of parameter save_file_path including the:

* Date 
* Data (Price list)
* Time Spent
* Trend

If you only give the two parameters data and save_file_path, the Time Spent and Trend will be defined as undefined. The format, as an example, is as follows:::

    Sat Mar 18 13:09:16 2023
    Data: [180.13, 180.13, 180.13]
    Time Spent: undefined
    Trend: undefined

If you want to give more parameters, you do not necessarily have to have both the time_spent and the trend parameter defined, but you can have either or (or both, of course).

Say you have the time_spent variable that you gathered from the ``multi_data_gathering`` function, and you got the trend from the ``get_trend`` function:

.. code-block:: python

    tools.save_data_to_file(data, save_file_path, time_spent = time_spent, trend = trend)


This would append the file like this, with time_spent being a number (in this case, 10) and trend being a string (in this case, neutral):::

    Sat Mar 18 13:06:43 2023
    Data: [180.13, 180.13, 180.13]
    Time Spent: 10
    Trend: neutral

API Class Usage
---------------

The **API** class has a few functions that have yet to be developed. However, they can still be used. Initial support for AlphaVantage has been implemented, as well as getting the JSON object through CNBC's API.

The AlphaVantage API can be used to gather the data (in terms of JSON format) of a stock symbol like so:

.. code-block:: python

    data = api.get_alpha_vantage_data("stock_symbol", "api_key") #Replace the stock_symbol with any other company, and make sure its in quotations! Also replace the api_key with your own API key.
    print(data)

The function also has a customizable parameter, type, which can be set to the type of stock. The default value is 'TIME_SERIES_INTRADAY', which is the intraday time series of the stock. You can change this to 'TIME_SERIES_DAILY' to get the daily time series of the stock. You can also change this to 'TIME_SERIES_WEEKLY' to get the weekly time series of the stock. You can also change this to 'TIME_SERIES_MONTHLY' to get the monthly time series of the stock, etc.

Although pretty bare-bones as of now, the AlphaVantage API is a start in order to gather info as an alternative to the class web-scraping and regex method used in the GatherInfo and Tools classes.

The CNBC api extracts the JSON format of a stock symbol, and certain functions have already been made:

``get_cnbc_api_json_data``:

This is a function used to get the whole JSON format of the stock symbol. There have been other functions which will be explained below. Nonetheless, this function takes in one parameter, which is the stock symbol, and returns the json data.

Regarding the functions that use the ``get_cnbc_api_json_data`` function, they are as follows:

``list_cnbc_data``:

This function lists each data point within the data gathering by the ``get_cnbc_api_json_data`` function. It takes in one parameter, which is the stock symbol, and prints out each data point.

Once the data is printed out, it also returns two values: the keys, and the values, each as a list. The keys are the data points, and the values are the values of each data point, within the json data.

You can use it like so:

.. code-block:: python

    keys, values = api.list_cnbc_data("stock_symbol") #Replace the stock_symbol with any other company, and make sure its in quotations.
    print(keys)
    print(values)

The last function of the **API** class is:

``get_price_cnbc_api``:

The function prints out the price of whatever stock symbol you input into it. It can be used as an alternative to the classic tools.get_single_price("stock_symbol") method, in case all providers in the Providers.providers dictionary fail (very unlikely).

You can use it like so:

.. code-block:: python

    price = api.get_price_cnbc_api("stock_symbol") #Replace the stock_symbol with any other company, and make sure its in quotations.

    print(price)