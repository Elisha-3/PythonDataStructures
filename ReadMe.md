# Leap Year Checker

This Python script determines whether a given year is a leap year.  
It reads an integer year from standard input and prints `True` if the year is a leap year, otherwise `False`.

## How It Works

The script uses the following rules to check for leap years:
- If the year is not divisible by 4, it is **not** a leap year.
- If the year is divisible by 4 but **not** by 100, it is a leap year.
- If the year is divisible by 100 but **not** by 400, it is **not** a leap year.
- If the year is divisible by 400, it is a leap year.

## Usage

1. Run the script:
    ```
    python leap-year.py
    ```
2. Enter a year (e.g., `1990`).
3. The script will output `True` or `False`.

## Example

**Input:**
```
1990
```

**Output:**
```
False
```

## Function

The main function is:
```python
def is_leap(year):
    # Returns True if year is a leap year, else False
```

## License

This project is for educational purposes only.