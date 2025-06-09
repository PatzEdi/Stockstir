#!/usr/bin/env python3
import sys
import argparse
from . import Stockstir

def main():
    parser = argparse.ArgumentParser(
        description='Stockstir CLI - Easily fetch stock data from the command line'
    )

    parser.add_argument(
        'symbol',
        type=str,
        help='Stock symbol to query (e.g. TSLA, AAPL)'
    )

    parser.add_argument(
        '--provider',
        type=str,
        default='cnbc',
        help='Data provider to use (default: cnbc)'
    )

    parser.add_argument(
        '--random-user-agent',
        action='store_true',
        help='Use random user agent for requests'
    )

    args = parser.parse_args()

    try:
        # Initialize Stockstir with provided parameters
        stockstir = Stockstir(
            provider=args.provider,
            random_user_agent=args.random_user_agent,
            print_output=False
        )

        # First try the API method as it's generally more reliable
        try:
            price = stockstir.api.get_price_cnbc_api(args.symbol)
            print(f"{args.symbol}: ${price:.2f}")
        except Exception:
            # Fall back to the tools method if API fails
            price = stockstir.tools.get_single_price(args.symbol)
            print(f"{args.symbol}: ${price:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
