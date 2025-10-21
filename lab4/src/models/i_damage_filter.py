from abc import ABC, abstractmethod


class IDamageFilter(ABC):
    @abstractmethod
    def allows(self, weapon) -> bool:
        """Return True if the damage from this weapon should be applied."""
        pass
