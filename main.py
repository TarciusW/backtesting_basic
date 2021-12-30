# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Trader import Trader

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    soxl = Trader('SOXL',1000, '2021-01-01', '2021-11-30')
    print(soxl.passive_outcome)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
