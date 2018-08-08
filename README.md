# pyunit-samples

This repo contains some very basic unit test examples using PyUnit framework 

Learn how-to from this introduction: http://pyunit.sourceforge.net/pyunit.html

## Test Cases

Contained in `numberstest.py` and can be run directly from command line using: `python numberstest.py`

Need to add at the end of file:
```
if __name__ == "__main__":
  unittest.main()
```

## Test Suites

Test suites are split in 2 categories: **critical** and **extended**

They can be executed directly from command line using: `python criticaltests.py` and `python extendedtests.py`

In addition, `alltests.py` and `alltestsalt.py` are provided to see how to group several test suites.
