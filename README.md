# best-practices
This package calculates the mean and standard deviation of a column in a data file. It also contains an example file conforming to PEP8 standards

## Installation
Clone this repository and install python3, pip, and pycodestyle

```sh
git clone https://github.com/cu-swe4s-fall-2019/best-practices-sahu0957.git
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3-pip
pip3 install pycodestyle
```
## Running the Program
Specify a tab-delimited file of numbers and a column number

```sh
python3 get_column_stats.py file_name column_number
```

Example output:
```
mean: 10
stdev: 5
```
## Testing the Program
The file basics_test.sh will perform a suite of tests to make sure your program is functioning correctly:
```sh
bash basics_test.sh
```

## Release History
*1.0
	*CHANGE: Updated style.py to conform to PEP8 Best Practices
	*CHANGE: Updated get_column_stats.py to PEP8 Best Practices
	*CHANGE: Updated get_column_stats.py to handle user errors
	*CHANGE: Updated get_column_stats.py to handle inputs via argparse
	*CHANGE: Updated basics_test.sh to test robustness of get_column_stats.py

## To Contribute
1. Fork it (< https://github.com/cu-swe4s-fall-2019/best-practices-sahu0957.git>)
2. Create your feature branch (`git checkout -b feature_branch`)
3. Commit your changes (`git commit -m 'add your notes'`)
4. Push to the branch (`git push origin feature_branch`)
5. Create a new Pull request


