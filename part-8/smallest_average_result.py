class Person:
    """A class representing a person with a name and a list of results."""

    def __init__(self, name, results: list[int]) -> None:
        """Initialize the person with a name and a list of results.

        Args:
            name (str): The name of the person.
            results (list[int]): A list of integer results for the person.
        """
        self.name = name
        self.results = results

    def __str__(self):
        return f"{self.name}: {self.results}"


def smallest_average_result(persons: list[Person]) -> Person | list[Person]:
    """Find the person(s) with the smallest average result.

    Args:
        persons (list[Person]): A list of Person objects.
    """
    # Calculate the average result for each person
    avg_l = []
    for person in persons:
        avg = sum(person.results) / len(person.results)
        avg_l.append(avg)
    # Find the minimum average
    avg_l.sort()
    min_avg = avg_l[0]
    # Find the person(s) with the minimum average
    result = []
    for person in persons:
        if sum(person.results) / len(person.results) == min_avg:
            result.append(person)
    return result if len(result) > 1 else result[0]


if __name__ == "__main__":
    person1 = Person("Mary", [2, 3, 3])
    person2 = Person("Gary", [5, 1, 8])
    person3 = Person("Larry", [3, 1, 1])

    print(smallest_average_result([person1, person2, person3]))  # Output: [Mary, Larry]
