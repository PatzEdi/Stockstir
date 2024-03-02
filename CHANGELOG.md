# StockStir V2 Changelog (Start Date: December 30, 2023 | Version Start Date: V.2)

Check out the [Stockstir ReadtheDocs Documentation](https://stockstir.readthedocs.io/en/latest/index.html).

## CHANGELOG V2.1.3:
Fix dependency issue (Should be fixed. If you have further issues with dependency installs (such as requests) on a fresh Stockstir install, pleace create an issue.)
## CHANGELOG V2.1.2:
This is just a hot fix. Under the get_source function found in the gather_info class, if all provideres failed, the API.getPriceCNBCAPI was used instead of the new code base formatting intoduced in V2.1. This has now been fixed. A small error on my part, yet big enough to be misleading. Sorry about that!

Also added build instructions in the README for those of you who want to build Stockstir directly from your local machine (without having to install via pypi).

## CHANGELOG V2.1.1:

1. CNN Provider had failed. Thankfully, due to the implementation of automated checks checking whether or not the Providers are working properly, I was able to catch the issue soon. So, the CNN Provider has now been switched with a new provider, **business insiders** (cnbc still remains the defaut provider). To use this new provider, you can choose "insider" as your provider upon Stockstir class instantiation, like so:

```
   from stockstir import Stockstir

   stockstir = Stockstir("insider") # Select insider as you provider
```
2. Added function in Providers class that lists out all providers with their respective names that you can use to use them. This way, you know which ones you can use, as you are given their names. It also tests each provider and tells which ones are available and which ones are working. The function can be used like so, with its name being list_available_providers:

```
   stockstir = Stockstir(print_output=True) # Make sure the print_output is set to True, so that the function actually prints out the panel instead of just returning a boolean value.
   stockstir.providers.list_available_providers() # You can also set print_output equal to True within the function itself, in case you need to override the Stockstir instance print_output.
```
The output will be something like this (make sure print_output is set to true, either from the function call itself or from the class instance):

```
0: cnbc (WORKING)
1: insider (WORKING)
2: zacks (WORKING)
```
This new function can also be seen as a less in depth version of the run_provider_checks method to quickly see which providers are working and which ones aren't. Keep in mind, that the function
## CHANGELOG V2.1.0

Stockstir V2.1.0 introduces a better way of using Stockstir, such as a new way of importing the Library, its classes, functions, and formatting changes from camelCase to snake_case, as well as additional functions. Please refer to the  for full instructions of each function found in the documentation linked above.

1. Removed the gatherSourceWithUserAgent function. Now, the only function used to gather the source is getSource, which includes the randomUserAgent as an option.
2. PEP Guidelines are now followed. For example, 1. Migrated all formatting from camelCase to snake_case for function names and variable names. 2. Migrated all formatting from camelCase to PascalCase for the class names. And more enhancmenets for improved readability.
3. Migrated separate classes to separate files, so that functions can be accessed with for example:
   ```
   from stockstir import Stockstir

   # Instantiate the Stockstir class object. With this new method, you can create different "gatherers" and can customize certain parameters such as the provider and random user agent.
   stockstir = Stockstir()

   # You can also instantiate the classes, using the same instance above.
   tools = stockstir.tools
   providers = stockstir.providers
   ```
4. Added a new function gather_multi_tickers(list: symbols, int: num_samples_per_symbol) which allows for a list of ticker symbols to be iterated through. Thank you [PandaStacker](https://github.com/PandaStacker) for this suggestion and pull request! It returns a list in the form of:
   ```
   {"Ticker1": [1,2,3,4,5], "Ticker2": [1,2,3,4,5]}

   ```

   So, the keys represent the stock/ticker symbols, and the values represent arrays of values (the amount is specified as a function parameter).
5. Updated documentation to match current library use, using PEP Guidelines. Now, all methods and variables are snake_case. 
6. By using this new instantiation structure, different data 'gatherers' can be instantiated, with different parameters, including changing the provider, enabling/disabling random_user_agent, and enabling/disabling print_output for certain functions. Refer to the function use section of the documentation to learn how to set those parameters for each Stockstir instantiation.


## CHANGELOG V2.0.0 (December 30, 2023):

Stockstir V2 Introduces many new features, improvements, and fixes to improve your experience:

To check out the documentation, view the [Stockstir ReadtheDocs Documentation](https://stockstir.readthedocs.io/en/latest/index.html) hosted on readthedocs.io.

**New Features:**
- With the new PEP Guidelines following and new method of instantiating Stockstir, you can get the single price like so:

	```
   from stockstir import Stockstir
   # Instantiate a stockstir object:
   stockstir = Stockstir()
   # Gather the price:
   price = stockstir.tools.get_single_price("ticker/stockSymbol") # make sure to replace what is in between the quotations with the actual ticker symbol.
   # Then, print the price:
   print(price)
	```

- Using the new Providers.providers provider system, providers can easily be expanded upon. All that is needed is the URL of the provider, and the regex to find the price based on the source code of the URL. So far, three have been tested, and there are therefore three providers now instead of one, which was only CNBC. Please note that CNBC still remains the default provider, and to manually switch providers, please refer to the [Stockstir ReadtheDocs Documentation](https://stockstir.readthedocs.io/en/latest/index.html).
- New class called API (this class is still in early stages) is an attempt to bring API support to Stockstir (Thank you for this suggestion!). As of now, Alpha Vantage has been tested, yet implementation into Stockstir is very bare-bones, as no functions have been developed yet to extract elements such as price. For more info, check out the documentation.
- The new API class also contains a request to CNBC and its json structure, rather than its source code. (Thank you to [@Gr1pp717](https://www.reddit.com/user/Gr1pp717/))! By using this, the JSON structure provides more details, and an easier way to gather the single price as well as other details. Please note that no API key is required here, and it can be used for free (though I am not responsible for any misuse and mass-sending through this function). This new method of gathering a JSON structure is another way of gathering data in case all Providers using the classic web scraping and regex method fail (which is very unlikely), or gathering data in general, as it includes other details about the stock. Again, I am not responsible for any abuse or damage caused by misuse of this method, yet alone any function to send requests in the library.

**Enhancements:**
- New class called Providers that checks whether or not each provider to get the data is actually working. You can run Provider.runProviderChecks() to check if they are all working.
- Changed the request type. Now, requests using any of the three providers will be conducted with a User agent. This is because some providers (such as provider 3) don’t work without a valid user agent.
- All functions that use getSource, getSourceWithUserAgent, and getPrice have a fail-system that is stored within the getSource and getSourceWithUserAgent functions. With this new fail-safe system, you can be confident in not losing any data if a provider fails, as it automatically switches to any of the other providers in the Providers.providers dictionary.
- Documentation updated to latest version.

**Fixes:**
- Migrated the documentation to work with the newly implemented readthedocs configuration system.
- Fixed pyproject.toml not having a specified requirements.txt file. Now, in case certain dependencies don’t exist on the machine, they will be installed automatically (e.g. requests). [#2](https://github.com/PatzEdi/Stockstir/issues/2)

**Future Plans**
- There are some plans to integrate a multiple Ticker symbol system, where the user puts more than one symbol at one per function call.
- Add proxy support. Proxy support will have to be tested thoroughly before release, and it has not had sufficient testing yet.
