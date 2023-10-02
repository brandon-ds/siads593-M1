import csv
import gzip


def create_file(output_file: str):
    """
    This function creates a new csv file with the header from the first file in the yearly_player_data folder.

    Parameters
    ----------
    output_file: str
        The name of the file to be created.

    Returns
    -------
    None
    """

    with open("siads593-M1/data/yearly_player_data/players_15.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        with open(output_file, "w") as f:
            writer = csv.writer(f)
            writer.writerow(header + ["year"])


def read_players(years: list, output_file: str):
    """
    This function reads the yearly_player_data files and appends the data to the output_file.

    Parameters
    ----------
    years: list
        A list of years to be read.
    output_file: str
        The name of the file to be appended.

    Returns
    -------
    None
    """

    for year in years:
        with open(f"siads593-M1/data/yearly_player_data/players_{year}.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                with open(output_file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(row + [2000 + year])


def main():
    years = [17, 18, 19, 20, 21]
    output_file = "siads593-M1/data/playersV2.csv"
    create_file(output_file)
    read_players(years, output_file)
    with open(output_file, "rb") as f_in:
        with gzip.open(output_file + ".gz", "wb") as f_out:
            f_out.writelines(f_in)


if __name__ == "__main__":
    main()
