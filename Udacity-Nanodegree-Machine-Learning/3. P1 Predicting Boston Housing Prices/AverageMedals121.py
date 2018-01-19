from DataFrame71 import create_dataframe
import numpy
from pandas import DataFrame, Series


def avg_medal_count():
    """
    Using the dataframe's apply method, create a new Series called
    avg_medal_count that indicates the average number of gold, silver,
    and bronze medals earned amongst countries who earned at
    least one medal of any kind at the 2014 Sochi olympics.  Note that
    the countries list already only includes countries that have earned
    at least one medal. No additional filtering is necessary.
    """

    df = create_dataframe().drop('country_name', axis=1)
    avarages = df.apply(numpy.mean, axis=1)

    return avarages


if __name__ == '__main__':
    df = avg_medal_count()
    print df
