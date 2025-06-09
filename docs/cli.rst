.. _cli:

***********************
Command Line Interface
***********************

In addition to using Stockstir as a Python library, you can use it directly from the command line to quickly fetch stock prices without writing any code. This is useful for quick checks or for integrating Stockstir into shell scripts and other command line tools.

Installation
===========

When you install Stockstir using pip, the command line tool is automatically installed:

.. code-block:: bash

   pip install Stockstir

Basic Usage
==========

To get the current price of a stock, simply run the ``stockstir`` command followed by the stock symbol:

.. code-block:: bash

   stockstir TSLA

Output:

.. code-block:: text

   TSLA: $196.42

Options
=======

The Stockstir CLI supports several options to customize its behavior:

--provider PROVIDER
   Specify which data provider to use. Options include ``cnbc`` (default), ``insider``, and ``zacks``.

--random-user-agent
   Use a random user agent for the request to help avoid rate limiting.

Examples
========

Get Apple stock price:

.. code-block:: bash

   stockstir AAPL

Use a specific provider:

.. code-block:: bash

   stockstir MSFT --provider=insider

Use a random user agent:

.. code-block:: bash

   stockstir NVDA --random-user-agent

Advanced Usage
=============

The CLI tool first tries to use the CNBC API method to retrieve the stock price. If that fails, it automatically falls back to the tools method that scrapes the data from provider websites.

If you're using Stockstir in scripts, you might want to check the exit code:

.. code-block:: bash

   stockstir AAPL
   if [ $? -eq 0 ]; then
       echo "Successfully retrieved stock price"
   else
       echo "Failed to retrieve stock price"
   fi

Error Handling
=============

If the stock symbol doesn't exist or there's another issue with retrieving the data, the CLI will display an error message and exit with a non-zero status code:

.. code-block:: text

   Error: Could not find 'INVALID'. Please check the stock symbol.
