class ParkingSpace:
    """Represents a single parking space in a parking lot."""
    
    def __init__(self, space_id: int, is_public: bool):
        self.space_id = space_id
        self.is_public = is_public
        self.is_occupied = False
#222

class ParkingLot:
    """Manages a collection of parking spaces."""
    
    def __init__(self):
        self.parking_spaces: dict[int, ParkingSpace] = {}

    def add_parking_space(self, space_id: int, is_public: bool) -> None:
        """Adds a new parking space to the lot."""
        if space_id in self.parking_spaces:
            raise ValueError(f"Parking space {space_id} already exists.")
        self.parking_spaces[space_id] = ParkingSpace(space_id, is_public)

    def remove_parking_space(self, space_id: int) -> None:
        """Removes a parking space from the lot."""
        if space_id not in self.parking_spaces:
            raise ValueError(f"Parking space {space_id} does not exist.")
        del self.parking_spaces[space_id]

    def update_parking_space(self, space_id: int, is_occupied: bool) -> None:
        """Updates the occupancy status of a parking space."""
        if space_id not in self.parking_spaces:
            raise ValueError(f"Parking space {space_id} does not exist.")
        self.parking_spaces[space_id].is_occupied = is_occupied

    def find_parking_space(self, space_id: int) -> ParkingSpace:
        """Finds a parking space by its ID."""
        if space_id not in self.parking_spaces:
            raise ValueError(f"Parking space {space_id} does not exist.")
        return self.parking_spaces[space_id]

    def manage_public_parking(self, space_id: int) -> ParkingSpace:
        """Manages a public parking space."""
        parking_space = self.find_parking_space(space_id)
        if not parking_space.is_public:
            raise ValueError(f"Parking space {space_id} is not public.")
        return parking_space

    def track_parking_usage(self) -> dict[int, bool]:
        """Tracks the occupancy status of all parking spaces."""
        return {space_id: parking_space.is_occupied for space_id, parking_space in self.parking_spaces.items()}


import unittest

class TestParkingLot(unittest.TestCase):
    """Unit tests for the ParkingLot class."""
    
    def setUp(self):
        self.parking_lot = ParkingLot()
        self.parking_lot.add_parking_space(1, True)
        self.parking_lot.add_parking_space(2, False)

    def test_add_remove_parking_space(self):
        self.parking_lot.add_parking_space(3, True)
        self.assertIn(3, self.parking_lot.parking_spaces)
        self.parking_lot.remove_parking_space(3)
        self.assertNotIn(3, self.parking_lot.parking_spaces)

    def test_update_find_parking_space(self):
        self.parking_lot.update_parking_space(1, is_occupied=True)
        self.assertTrue(self.parking_lot.parking_spaces[1].is_occupied)
        parking_space = self.parking_lot.find_parking_space(1)
        self.assertEqual(parking_space.is_occupied, True)

    def test_manage_public_parking(self):
        public_space = self.parking_lot.manage_public_parking(1)
        self.assertTrue(public_space.is_public)
        with self.assertRaises(ValueError):
            self.parking_lot.manage_public_parking(2)  # Space 2 is not public

    def test_track_parking_usage(self):
        usage = self.parking_lot.track_parking_usage()
        self.assertEqual(usage, {1: False, 2: False})
        self.parking_lot.update_parking_space(1, is_occupied=True)
        usage = self.parking_lot.track_parking_usage()
        self.assertEqual(usage, {1: True, 2: False})

if __name__ == '__main__':
    unittest.main()
