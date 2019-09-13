# check to see if python scripts conform to Best Practices for Python
pycodestyle style.py
pycodestyle get_column_stats.py

# Download ssshtest if it isn't already installed
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# run one test, with a wrong file name. This should throw an error
run file_error_test python get_column_stats.py foo.bar 1
assert_in_stderr "The specified file doesn't exist! Exiting..."

# run 10 tests, making a random matrix of 100x5 size each time
for i in {1..10}; do
(for i in `seq 1 100`; do
	echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

# run tests on columns that are in range
 for i in {0..4}; do
  run variable_data_test python get_column_stats.py data.txt $i
  assert_exit_code 0
  assert_no_stderr
  assert_stdout
 done

# indexes out of range should throw an error
 for i in {5..10}; do
  run variable_data_test python get_column_stats.py data.txt $i
  assert_in_stderr "Column index not found! Exiting..."
 done

done

# run tests on fixed data frames with known mean and std dev
V=5
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
 done )> data.txt

# Mean should be 5, std. dev should be 0
run fixed_data_test python get_column_stats.py data.txt 2
assert_in_stdout "mean: 5"
assert_in_stdout "stdev: 0" 
assert_exit_code 0
assert_no_stderr

# Run again, with a known standard deviation and mean
(for i in `seq 1 3`; do 
    echo -e "$i\t$i\t$i\t$i\t$i";
 done )> data.txt

# Mean should be 2, std. dev should be 0.816...
run fixed_data_test python get_column_stats.py data.txt 2
assert_in_stdout "mean: 2"
assert_in_stdout "stdev: 0.816"
assert_exit_code 0
assert_no_stderr

