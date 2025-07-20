class DecreasingCounter:
    """A Decreasing counter with an initial value."""

    def __init__(self, initial_value: int) -> None:
        self.value = initial_value
        self.initial_val = initial_value

    def __str__(self) -> str:
        return f"Value: {self.value}"

    def decrease(self) -> None:
        """Decreases the counter by 1, but not below 0."""
        if self.value > 0:
            self.value -= 1
        else:
            self.value = 0

    def set_to_zero(self) -> None:
        """Set the counter to zero."""
        self.value = 0

    def reset_original_value(self) -> None:
        """Reset the counter to its original value."""
        self.value = self.initial_val

if __name__ == "__main__":
    # Example usage
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    print(counter)
    counter.reset_original_value()
    print(counter)
