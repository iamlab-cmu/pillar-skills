from abc import ABC, abstractmethod
from typing import Generator
from pillar_state import State

from .base_policy import BasePolicy


class BaseSkill(ABC):

    @abstractmethod
    def precondition_satisfied_for_state(self, pillar_state: State) -> float:
        """Computes the probability of whether or not there exists parameters with the given 
        pillar_state such that `precondition_satisfied` returns a non-zero value.

        Args:
            pillar_state: state to be checked.

        Returns:
            A value in [0, 1]
        """
        pass

    @abstractmethod
    def precondition_satisfied(self, pillar_state: State, parameter) -> float:
        """Computes the probability of the given ``pillar_state``
        satisfying the precondition for this skill.

        Args:
            pillar_state: state to be checked.
            parameter: skill parameter with which a policy is made

        Returns:
            A value in [0, 1]
        """
        pass
    
    @abstractmethod
    def termination_condition_satisfied(self, pillar_state: State, parameter, policy: BasePolicy, t_step: int) -> float:
        """Computes the probability of the given ``pillar_state`` 
        satisfying the termination condition for this skill.

        Args:
            pillar_state: state to be checked.
            parameter: skill parameter with which the policy is made
            policy: the policy being executed
            t_step: the discrete time steps elapsed during policy execution

        Returns:
            A value in [0, 1]
        """
        pass

    @abstractmethod
    def skill_execution_successful(self, pillar_state_init: State, pillar_state_end: State, parameter, policy: BasePolicy, t_step: int) -> float:
        """Computes the probability of the skill execution being successful.

        Args:
            pillar_state_init: state from which skill execution started
            pillar_state_end: state at which skill execution ended
            parameter: skill parameter with which the policy is made
            policy: the policy being executed
            t_step: the discrete time steps elapsed during policy execution

        Returns:
            A value in [0, 1]
        """
        pass

    @abstractmethod
    def make_skill_parameter_generator(self, pillar_state: State, max_num_parameters: int) -> Generator:
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
    
