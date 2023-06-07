Code Structure
==============

In the code, there are two classes:::

	gatherInfo

	Tools

The gatherInfo class
--------------------
The **gatherInfo** class consists of three functions: two to gather the source code of a web page and one to return the price based on the source code. These three functions are **getSource** , **getSourceWithUserAgent**, and **gatherPrice**.

The ``getSource`` Function:

This function works by using the requests module and the URLLIB module in order to make the request to the URL of https://cnbc.com/ and then add the company name at the end of the URL. It takes in the company name/ticker/stock symbol and returns the web page code in the form of a variable.

The ``getSourceWithUserAgent`` Function:

This function returns the same value as the ``getSource`` function, but uses a method of using user agents. It takes in the same parameter being the company/stock/ticker symbol, but also takes in a second parameter which determines the picked user agent.

The ``gatherPrice`` Function:

This function works by taking the source code that the ``getSource`` function returns as a parameter, and uses the re library to use a regex that finds the price in the web page URL. The regex works by finding what is in between certain keywords which were in the source. I found out that CNBC does not change in terms of code when switching companies, so this method was universal for all companies in order to get the stock price. 

**Important note of these functions and the gatherInfo Class in general:**
.. note::

   The functions in the **gatherInfo** class should not be used if you want to gather stock price. The only thing these functions do is make it easier to make and structure the functions under the **Tools** class, which combines these two functions together to make the tools you need. Feel free to use these functions if you would like to, though the **Tools** class covers the features that you will actually be using.



The Tools class
---------------
The **Tools** class is the main class that you as the user will be using as it contains all of the features that you need in order to gather stock data. The **Tools** class consists of the following functions which are described in detail below:

* getSinglePrice
* multiDataGathering
* getTrend
* saveDataToFile

The ``getSinglePrice`` Function:

This Function provides you with the simplest and quickest way to gather a company's stock value by using the gatherInfo class functions to get the source code, and it then finds the price with the gatherInfo class functions. The returned value will be in the form of a float. There is an optional argument which is if you want to use a random user agent, but optional parameters will be talked about under the :doc:`function use` section of this guide.

The ``multiDataGathering`` Function:

The ``multiDataGathering`` function is the biggest function in this stock library. The main ways to use each and every parameter are under the :doc:`function use` section of this guide.

This function works by taking in the amount of iterations/data samples to collect, and gathers data based on a for loop that runs based on the amount of iterations/data samples given. This function works by using the given parameters (most of which are optional) and adjusting its functionality based on those parameters. The main focus of this function however is to collect multiple data samples over time and uses the same methods of the **gatherInfo** class in order to make and process requests. The function then by default returns a list of data that contains each data sample collecting per iteration.
	
	There are many more parameters and options included with this function. These include an antiBan feature, a randomUserAgent feature, returning the time it takes for the process to complete, and more. These parameters however are only optional, and the only two required ones are the ticker symbol as well as the number of iterations of data to collect.
	
	The optional parameters will be discussed and reviewed under the :doc:`function use` section of this guide.

The ``getTrend`` Function:

This function is very simple. It gets in the data of stock values as a parameter in the form of a list and compares the last value of the data to the first in order to see the change. If the data of the last sample is less than the first, it means that the trend went down. Vice versa, the trend went up. If the last and first values are equal, then the trend over that time is neutral or the same. This function returns a string containing either:::
	
	up

	down
	
	neutral
	
This function also takes in another optional parameter, but that is talked about in the :doc:`function use` section of this guide.


The ``saveDataToFile`` Function:

This function is another useful function that allows you as the user to save the data you gathered to a text file in any directory. It takes in optional parameters such as time spent and the trend, but required arguments are the price data in list form and the directory of where to create and save the file with the data.

This function provides you with detailed save data as well, showing the time and full date of when the data was collected. More information about this under the :doc:`function use` section of this guide.