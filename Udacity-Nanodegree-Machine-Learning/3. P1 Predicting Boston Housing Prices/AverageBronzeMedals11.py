from DataFrame71 import create_dataframe
from pandas import DataFrame, Series
import numpy


def avg_medal_count():
    """
    Compute the average number of bronze medals earned by countries who
    earned at least one gold medal.
    """
    df = create_dataframe()
    result = df['bronze'][df['gold'] >= 1]

    return numpy.mean(result)


if __name__ == '__main__':
    print(avg_medal_count())
