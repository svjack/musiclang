from .constants import *

class Tonality:
    """
    Represents a tonality, it can be applied via % operator to a chord to modulate it on another tonality
    It is represented by a degree, an accident, a mode, and an octave

    """
    def __init__(self, degree, mode="M", octave=0):
        """
        Degree is absolute degree (between 0 and 12)
        :param degree:
        :param accident:
        :param mode:
        :param octave:
        """
        self.degree = degree
        self.mode = mode
        self.octave = octave

    def change_mode(self, mode):
        new_tonality = self.copy()
        new_tonality.mode = mode
        return new_tonality


    @property
    def scale_set(self):
        return frozenset({s % 12 for s in self.scale_pitches})

    @property
    def scale_pitches(self):
        abs_degree = self.abs_degree
        mode = self.mode
        pitch_scale = [n + abs_degree for n in SCALES[mode]]
        return pitch_scale

    def _eq(self, other):
        return self.degree == other.degree and self.mode == other.mode and self.octave == other.octave

    def __eq__(self, other):
        if not isinstance(other, Tonality):
            return False
        # To get equalities between enharmonies we need to reformulate chord adding neutral modulation
        return (Tonality(0) + self )._eq(Tonality(0) + other )

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__.update(d)

    def copy(self):
        return Tonality(self.degree, self.mode, self.octave)

    def __radd__(self, other):
        if other is None:
            return self
        else:
            raise Exception('Not valid addition of tonality')

    def add(self, other):
        new_abs_degree = self.degree + other.degree
        new_octave = self.octave + other.octave
        delta_octave = new_abs_degree // 12
        new_degree = new_abs_degree % 12
        new_mode = other.mode
        return Tonality(degree=new_degree, mode=new_mode, octave=new_octave + delta_octave)

    @property
    def abs_degree(self):
        return self.degree + + 12 * self.octave

    def __add__(self, other):
        """
        Add another tonality
        :param other:
        :return:
        """
        if other is None:
            return self
        else:
            return self.add(other)

    @property
    def b(self):
        tone = self.copy()
        tone.degree -= 1
        return tone

    @property
    def s(self):
        tone = self.copy()
        tone.degree += 1
        return tone

    @property
    def m(self):
        tone = self.copy()
        tone.mode = "m"
        return tone

    @property
    def M(self):
        tone = self.copy()
        tone.mode = "M"
        return tone

    @property
    def mm(self):
        tone = self.copy()
        tone.mode = "mm"
        return tone


    @property
    def dorian(self):
        tone = self.copy()
        tone.mode = "dorian"
        return tone

    @property
    def phrygian(self):
        tone = self.copy()
        tone.mode = "phrygian"
        return tone

    @property
    def lydian(self):
        tone = self.copy()
        tone.mode = "lydian"
        return tone

    @property
    def mixolydian(self):
        tone = self.copy()
        tone.mode = "mixolydian"
        return tone

    @property
    def aeolian(self):
        tone = self.copy()
        tone.mode = "aeolian"
        return tone

    @property
    def locrian(self):
        tone = self.copy()
        tone.mode = "locrian"
        return tone


    def d(self):
        return self.o(-1)

    def o(self, octave):
        tonality = self.copy()
        tonality.octave += octave
        return tonality

    def degree_to_str(self):
        return DEGREE_TO_STR[self.degree]

    def __repr__(self):
        return self.to_code()

    def to_code(self):
        result = f"{self.degree_to_str()}.{self.mode}"
        if self.octave != 0:
            result += f".o({self.octave})"

        return result
