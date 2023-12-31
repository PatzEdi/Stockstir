# StockStir V2 Changelog (Start Date: December 30, 2023 | Version Start Date: V.2)


## CHANGELOG V2.0.0 (December 30, 2023):

Stockstir V2 Introduces many new features, improvements, and fixes to improve your experience:

To check out the documentation, view the [Stockstir ReadtheDocs Documentation](https://stockstir.readthedocs.io/en/latest/index.html) hosted on readthedocs.io.

**New Features:**
- Added support for more than one source, which was CNBC. Now, you have CNBC, CNN, and Zacks. If one doesn’t work, you can manually change it with Sources.source_number = 0-2 (replace 0-2 with an actual number that is in between 0 and 2 e.g. 1). The default still remains 0, or in other words CNBC. You can also check which providers are working or not by running:

	```
    from Stockstir import Providers
    Providers.runProviderChecks()
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
