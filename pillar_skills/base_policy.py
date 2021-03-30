from abc import ABC, abstractmethod
from pillar_state import State


class BasePolicy(ABC):

    @abstractmethod
    def __call__(self, pillar_state: State):
        """Queries the policy with pillar_state to obtain an action.

        Args:
            pillar_state: state from which the policy is executed.

        Returns:
            An action object. Specific implementation up to user.
        """
        pass
