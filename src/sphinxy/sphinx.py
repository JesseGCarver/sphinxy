from sphinxy.riddle import Riddle


class IncorrectAnswer(Exception):
    ...


class Sphinx:
    ''' a class for messed up lion bird woman things. '''
    def __init__(self, name: str):
        self._name = name
        self._riddle = Riddle(
            question=("What goes by two four legs, two legs and three. But the more legs it goes on the weaker it be."),
            answer="man",
        )

    def introduce(self) -> str:
        '''ETB draw some cards or something. Group hug I bet.'''
        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        '''Normally I fill these in with real info, but this one is more of an injoke'''
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str | None]:
        '''Not actually sure what happens if I mix good and bad docstrings.'''
        hint = (
            f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            if include_hint
            else None
        )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        '''Checks a riddle

        args: the user's answer, a bool to control hinting

        return: string if user == Pericliese

        throws: IncorrectsAnswer
        '''
        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")
