import unittest
from station_search import StationSearch


class TestStationSearch (unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.filename = './test_data.csv'

    def test_min_temperature(self) -> None:

        search = StationSearch(self.filename)
        (station_id, date) = search.min_temperature()

        self.assertEqual(station_id, '68')
        self.assertEqual(date, '2000.542')

    def test_max_fluctuation(self) -> None:

        search = StationSearch(self.filename)
        station_id = search.max_fluctuation()
        self.assertEqual(station_id, '67')

    def test_max_fluctuations_by_dates(self) -> None:

        search = StationSearch(self.filename)

        start, end = '2000.125', '2000.958'
        station_id = search.max_fluctuation_by_dates(start, end)
        self.assertEqual(station_id, '67')

        start, end = '2000.375', '2000.958'
        station_id = search.max_fluctuation_by_dates(start, end)
        self.assertEqual(station_id, '68')

if __name__ == '__main__':

    unittest.main()
