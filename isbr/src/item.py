
class Item:
    _cost: float = None
    _damaged: bool = False
    _rented: bool = False

    def as_dict(self):
        return {
            'cost': self.cost,
            'damaged': self.damaged,
            'rented': self.is_rented
        }

    @property
    def cost(self) -> float:
        return self._cost

    @cost.setter
    def cost(self, cost: float) -> None:
        self._cost = cost

    @property
    def damaged(self) -> bool:
        return self._damaged

    @damaged.setter
    def damaged(self, is_damaged: bool) -> None:
        self._damaged = is_damaged

    @property
    def is_rented(self) -> bool:
        return self._rented

    @is_rented.setter
    def is_rented(self, rented: bool) -> None:
        self._rented = rented
