"""
Manages the required data structures.
"""


class Color:
    """
    Color initialization model.
    Represents a single color in the HEX system.
    """

    def __init__(self,
                 code: str,
                 description: str):
        self.code = code
        self.description = description

    def __str__(self) -> str:
        return self.description
