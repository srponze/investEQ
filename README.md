# Weight Equally Invest Tool

This tool helps automate the process of allocating investments equally across selected assets.
The objective is to try to invest the same amount of cash in each of the assets, and this is achieved with linear programming.


## Installation
1. Clone this repository or download the ZIP file and extract it:
   ```bash
   git clone https://github.com/srponze/investEQ.git
   ```
2. Install the required dependencies:
   ```bash
   pip install yfinance ortools -y
   ```


## Usage
1. Enter the list of tickers to invest in client.py
2. Enter the margin percentage to avoid losing the operation, this margin will be increased to the price of each asset. You must leave an adequate margin to ensure the proper functioning of the tool (a requirement of linear programming).
3. Enter the cash you want to invest
4. Run the main script:
   ```bash
   python client.py
   ```
5. In listStocks you will have the price plus the margin and the number of shares to invest


## Documentation
(pending)


## License
This project is licensed under the MIT License.


## Contact
For questions or support, contact [srponze](https://github.com/srponze).
