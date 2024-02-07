.. _code structure:

***************
Code Structure
***************

In the library, there are four classes:::
	Providers

	GatherInfo

	Tools

	API

There is also a file called ``__init__.py`` which is used to make the library a package, and that includes the Stockstir class which is used to instantiate the other classes.

The Providers class
--------------------
The **Providers** class consists of a dictionary, called providers, which includes all the providers. A provider consists of a URL, and a regex to find a value, in this case the price.

The **Providers** class has a provider_number variable which is used throughout the library (except the API class) to decide which provider to use.

The dictionary is easily expandable. If a new provider is added to the dictionary, the library will not need any additional setup for the provider.

Functions include:

The ``run_provider_checks`` Function:

This function is used to check if all providers containined in the providers dictionary work.

The ``test_selected_provider`` Function:

This function is used to test the selected provider (set by Providers.provider_number). It checks for both the integrity of the request and the regex.

The ``list_available_providers`` Function:

This function is similar to the run_provider_checks function. However, it does not go into the details of what is working and what is not about a provider. Rather, it lists out the available providers to use, and those that are working.

The GatherInfo class
--------------------
The **GatherInfo** class consists of two main functions: one to gather the source code of a web page and one to return the price based on the source code. These two functions are **get_source** and **gather_price**.

The ``get_source`` Function:

This function works by using the requests module and the URLLIB module in order to make the request to the URL of the selected provider and then add the company name at the end of the URL. It takes in the company name/ticker/stock symbol and returns the web page code in the form of a variable.

It also includes a fail-safe mechanism which is described in detail under the :doc:`fail-safe mechanism` section of this guide.

The ``gather_price`` Function:

This function works by taking the source code that the ``get_source`` function returns as a parameter, and uses the re library to use a regex that finds the price in the web page URL. The regex works by finding what is in between certain keywords which were in the source. I found out that the existing providers did not change in terms of code when switching companies, so this method was universal for all companies in order to get the stock price. 

**Important note of these functions and the GatherInfo Class in general:**

.. note::

   The functions in the **GatherInfo** class should not be used if you want to gather stock price. The only thing these functions do is make it easier to make and structure the functions under the **Tools** class, which combines these two functions together to make the tools you need. Feel free to use these functions if you would like to, though the **Tools** class covers the features that you will actually be using that combines the functions in the **GatherInfo** class.

**Regarding the fail-safe mechanism:**
 
The ``get_source`` function actually contains the fail-safe mechanism within it. To learn more about the fail-safe mechanism, please refer to the :doc:`fail-safe mechanism` section of this guide.

The Tools class
---------------
The **Tools** class is the main class that you as the user will be using as it contains all of the features that you need in order to gather stock data. The **Tools** class consists of the following functions which are described in detail below:

* get_single_price
* mulit_data_gathering
* get_trend
* save_data_to_file

The ``get_single_price`` Function:

This Function provides you with the simplest and quickest way to gather a company's stock value by using the gatherInfo class functions to get the source code, and it then finds the price with the gatherInfo class functions. The returned value will be in the form of a float. There is an optional argument which is if you want to use a random user agent, but optional parameters will be talked about under the :doc:`function use` section of this guide.

The ``multi_data_gathering`` Function:

The ``multi_data_gathering`` function is the biggest function in this stock library. The main ways to use each and every parameter are under the :doc:`function use` section of this guide.

This function works by taking in the amount of iterations/data samples to collect, and gathers data based on a for loop that runs based on the amount of iterations/data samples given. This function works by using the given parameters (most of which are optional) and adjusting its functionality based on those parameters. The main focus of this function however is to collect multiple data samples over time and uses the same methods of the **GatherInfo** class in order to make and process requests. The function then by default returns a list of data that contains each data sample collecting per iteration.
	
	There are many more parameters and options included with this function. These include an antiBan feature, a randomUserAgent feature, returning the time it takes for the process to complete, and more. These parameters however are only optional, and the only two required ones are the ticker symbol as well as the number of iterations of data to collect.
	
	The optional parameters will be discussed and reviewed under the :doc:`function use` section of this guide.

The ``multi_ticker_data_gathering`` Function:

This function uses the ``multi_data_gathering`` function to gather data for multiple companies at once. It takes in a list of ticker symbols and the number of iterations of data to collect. It then uses the ``multi_data_gathering`` function to gather data for each ticker symbol in the list. It then returns a dictionary with the ticker symbol as the key and the data as the value.

The ``get_trend`` Function:

This function is very simple. It gets in the data of stock values as a parameter in the form of a list and compares the last value of the data to the first in order to see the change. If the data of the last sample is less than the first, it means that the trend went down. Vice versa, the trend went up. If the last and first values are equal, then the trend over that time is neutral or the same. This function returns a string containing either:::
	
	up

	down
	
	neutral
	
This function also takes in another optional parameter, but that is talked about in the :doc:`function use` section of this guide.


The ``save_data_to_file`` Function:

This function is another useful function that allows you as the user to save the data you gathered to a text file in any directory. It takes in optional parameters such as time spent and the trend, but required arguments are the price data in list form and the directory of where to create and save the file with the data.

This function provides you with detailed save data as well, showing the time and full date of when the data was collected. More information about this under the :doc:`function use` section of this guide.

The API class
---------------

The API class includes API systems such as AlphaVantage and gathering data in a different way such as through a JSON format (CNBC).

As of now, the functions within this class are still very limited and need to be further developed.

.. _fail-safe mechanism:
How the fail-safe mechanism works:
----------------------------------

The fail-safe mechanism is stored in the ``get_source`` function.

The function works by instantiating a failed_providers list at the start. Then, there is a big while True: loop that contains a try: except: block of code.

In the try: block, a request is made in an attempt to gather the source. If that fails, it goes down to the except: block. In the except block, the failed provider number Providers.provider_number is put into the failed_providers list.

Once put into the list, a new provider is chosen through a while loop which generates a random number 0 through the length of the dicitonary minus 1, until the generated number is no longer in the failed_providers list. Once that is done, the provider number is set to the new provider number, and the while True: loop is run again.

Using this fail-safe method in the ``get_source`` function, there is no need to implement the fail-safe mechanism in other parts of the code, which means that functions such as ``multi_data_gathering`` and ``get_single_price`` remain untouched from the previous version of Stockstir.

If you have questions about the fail-safe mechanism, message me on Reddit! My username is u/PatzEdi.