from DataFrame71 import create_dataframe
import numpy
from pandas import DataFrame, Series


def numpy_dot():
    """
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each
    bronze medal.
    """

    df = create_dataframe()
    medals = df[['gold','silver','bronze']]
    score_system = [4, 2, 1]
    points = numpy.dot(medals, score_system)
    return_set = DataFrame({
        'country_name': df['country_name'],
        'points': points
    })

    return return_set


if __name__ == '__main__':
    olympic_points_df = numpy_dot()
    print(olympic_points_df)
