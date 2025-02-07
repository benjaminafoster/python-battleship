import regex

class Coordinate():
    def __init__(self):
        self.test = input("Enter a coordinate: ")
        self.validateCoordinate(self.test) 

    def validateCoordinate(self, test_coordinate:str) -> str:
        valid_pattern = regex.compile(r"[A-J][0-9]")
        validated_coordinate = None
        # Checks whether the whole string matches the re.pattern or not
        if regex.fullmatch(valid_pattern, test_coordinate):
            return str(self.test)
        else:
            raise Exception("Invalid coordinate")

    def __repr__(self):
        return f"{self.test}"
