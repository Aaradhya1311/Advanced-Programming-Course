from datetime import date


def list_years(dates: list[date]) -> list[int]:
    """Return a sorted list of years from a list of date objects.

    Args:
        dates (list[date]): A list of date objects.

    Returns:
        list[int]: A sorted list of years extracted from the date objects.
    """
    year_list: list[int] = []
    for d in dates:
        year_list.append(d.year)
    year_list.sort()
    return year_list


if __name__ == "__main__":
    # Example usage
    dates = [date(2019, 2, 3), date(2006, 10, 10), date(1993, 5, 9)]
    years = list_years(dates)
    print(years)  # Output: [1993, 2006, 2019]
