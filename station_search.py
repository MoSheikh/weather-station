class StationSearch:

    def __init__(self, filename='./data.csv'):

        self.filename = filename

    def min_temperature(self) -> (str, str):
        """
        Returns the station_id and date associated with the
        lowest temperature on record.

        :return: station_id, date
        """
        with open(self.filename, 'r', newline='', encoding='utf-8') as f:

            f.readline()
            min_temp = 9999.9
            out = (None, None)

            for line in f:

                # Remove carriage return from line, extract data to tuple
                d = line[:-2].split(',')
                temp = float(d[2])

                if temp < min_temp:

                    min_temp = temp
                    out = (d[0], d[1])

            return out[0], out[1]

    def max_fluctuation(self) -> str:
        """
        Returns the station_id that recorded the largest fluctuations.

        :return: station_id
        """
        with open(self.filename, 'r', newline='', encoding='utf-8') as f:

            record = {}
            max_fluc = -9999
            max_id = None
            f.readline()

            for line in f:

                d = line[:-2].split(',')
                station_id = d[0]
                new_temp = float(d[2])

                if station_id not in record:

                    record[station_id] = (0, new_temp)

                else:

                    prev_fluc, prev_temp = record[station_id]
                    new_fluc = prev_fluc + abs(new_temp - prev_temp)
                    record[station_id] = (new_fluc, new_temp)

                    if new_fluc > max_fluc:

                        max_fluc = new_fluc
                        max_id = station_id

        return max_id

    def max_fluctuation_by_dates(self, start: str, end: str) -> str:
        """
        Returns the station_id that recorded the largest fluctuations
        within the provided date range.

        :return: station_id
        """
        with open(self.filename, 'r', newline='', encoding='utf-8') as f:

            record = {}
            max_fluc = -9999
            max_id = None
            f.readline()

            for line in f:

                d = line[:-2].split(',')
                station_id = d[0]
                new_temp = float(d[2])

                if station_id not in record:

                    record[station_id] = (0, new_temp)

                elif start <= d[1] <= end:

                    prev_fluc, prev_temp = record[station_id]
                    new_fluc = prev_fluc + abs(new_temp - prev_temp)
                    record[station_id] = (new_fluc, new_temp)

                    if new_fluc > max_fluc:

                        max_fluc = new_fluc
                        max_id = station_id

        return max_id
