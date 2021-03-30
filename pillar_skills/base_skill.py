from abc import ABC, abstractmethod, abstractstaticmethod
from typing import Generator
from pillar_state import State

from .base_policy import BasePolicy


class BaseSkill(ABC):

    @abstractstaticmethod
    def are_preconditions_satisfied(pillar_state: State) -> float:
        """Computes the probability of the given ``pillar_state``
        satisfying the preconditions for this skill.

        Args:
            pillar_state: state to be checked.

        Returns:
            A value in [0, 1]
        """
        pass
    
    @abstractstaticmethod
    def are_termination_conditions_satisfied(pillar_state: State) -> float:
        """Computes the probability of the given ``pillar_state`` 
        satisfying the termination conditions for this skill.

        Args:
            pillar_state: state to be checked.

        Returns:
            A value in [0, 1]
        """
        pass

    @abstractstaticmethod
    def make_skill_parameter_generator(pillar_state: State, max_num_parameters: int) -> Generator:
        """Returns a generator that will generate a list of at most 
        ``max_num_parameters`` amount of skill parameters per ``next``.

        Args:
            pillar_state: state from which to generate skill parameters
            max_num_parameters: max number of parameters to generate per call

        Returns:
            A Generator

        Examples: 
            For skill parameters that are numpy arrays of dim 5:

            >>> skill_parameter_generator = skill.make_skill_parameter_generator(state, 10)
            >>> one_batch_of_parameters = next(skill_parameter_generator)
            >>> print(one_batch_of_parameters.shape)
            (10, 5)
        """
        pass

    def effects(self, pillar_state: State, parameter):
        """Returns the predicted terminal ``State``, a list of ``States``, 
        or a distribution of ``States``. Specific implementation up to user.

        Args:
            pillar_state: state from which effects are computed
            parameter: skill parameter with which a policy is made

        Returns:
            A State, a list of States, or a distribution of States
        """
        raise NotImplementedError()

    def effects_batch(self, pillar_states: list, parameters: list):
        """Returns a batch of effects (see ``effects`` docs).

        Length of ``pillar_states`` should equal to that of ``parameters``.

        Args:
            pillar_states: list of states from which effects are computed
            parameters: list of skill parameters with which a policy is made

        Returns:
            A list of N effects where N is the length of ``pillar_states`` and ``parameters``
        """
        raise NotImplementedError()

    @abstractmethod
    def make_policy(self, pillar_state: State, parameter) -> BasePolicy:
        """Makes and returns a policy object that inherits ``BasePolicy`` that
        is meant to be executed from ``pillar_state`` with the 
        skill parameter ``parameter``.

        Args:
            pillar_state: state from which the policy is supposed to execute
            parameter: skill parameter to make the policy

        Returns:
            A policy object that inherits ``BasePolicy`` that is meant to be executed 
            from ``pillar_state`` with the skill parameter ``parameter``.
        """
        pass
    