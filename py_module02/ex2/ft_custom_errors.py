
class GardenError(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)


class PlantError(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)


class WaterError(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)
