from .constants import *

class Melody:
    def __init__(self, notes):
        self.notes = notes

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__.update(d)

    def __add__(self, other):
        from .note import Note
        if isinstance(other, Note):
            return Melody(self.notes + [other])
        if isinstance(other, Melody):
            return Melody(self.notes + other.notes)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        from .note import Note
        if isinstance(other, Note):
            return self.__eq__(Melody([other]))
        return isinstance(other, Melody) and str(other) == str(self)

    def get_pitches(self, chord, track_idx, time, last_note_array=None):
        pitches = []
        for note in self.notes:
            result = note.pitch(chord, track_idx, time, last_note_array)
            if not last_note_array[SILENCE] and not last_note_array[CONTINUATION]:
                last_note_array = result

            pitches.append(result)
        return pitches


    def replace_pitch(self, to_replace, new_note):

        new_melody = []
        for note in self.notes:
            to_add = note.copy()
            if note.val == to_replace.val and note.type == to_replace.type:
                to_add.type = new_note.type
                to_add.val = new_note.val
            new_melody.append(to_add)
        return sum(new_melody, None)

    def to_sequence(self, chord, inst):
        """
        Transform in a list of [(start_time, end_time, pitch, self)]
        :return:
        """
        time = 0
        sequence = []
        for note in self.notes:
            pitch = chord.to_pitch(note)
            start = time
            end = time + note.duration
            sequence.append([start, end, pitch, chord.to_chord(), inst, note])
            time += note.duration
        return sequence


    def to_code(self):
        return " + ".join([n.to_code() for n in self.notes])

    @property
    def is_continuation(self):
        return all([n.is_continuation for n in self.notes])

    @property
    def starts_with_absolute_note(self):
        if len(self.notes) > 0:
            return self.notes[0].starts_with_absolute_note
        else:
            return False

    @property
    def had_absolute_note(self):
        return any([n.starts_with_absolute_note for n in self.notes])

    @property
    def starts_with_absolute_or_silence(self):
        if len(self.notes) > 0:
            return self.notes[0].starts_with_absolute_or_silence
        else:
            return False

    @property
    def starts_with_note(self):
        if len(self.notes) > 0:
            return self.notes[0].starts_with_note
        else:
            return False

    def augment(self, value):
        return Melody([n.augment(value) for n in self.notes])

    @property
    def duration(self):
        return sum([n.duration for n in self.notes])

    def __iter__(self):
        return self.notes.__iter__()

    def __radd__(self, other):
        if other is None:
            return self.copy()

    def __and__(self, other):
        return Melody([n & other for n in self.notes])

    def __matmul__(self, other):
        # Apply a function to each note
        return Melody([n @ other for n in self.notes])

    def __mul__(self, other):
        from .note import Note
        if isinstance(other, int):
            melody_copy = self.copy()
            return Melody(melody_copy.notes * other)
        if isinstance(other, Note):
            return self * Melody([other.copy()])
        else:
            raise Exception('Cannot multiply Melody and ' + str(type(other)))

    def __len__(self):
        return len(self.notes)

    def o(self, octave):
        return Melody([n.o(octave) for n in self.notes])

    def __hasattr__(self, item):
        try:
            self.__getattr__(item)
        except:
            return False
        return True

    def __getattr__(self, item):
        try:
            res = Melody([getattr(n, item) for n in self.notes])
            return res
        except:
            raise AttributeError("")

    def copy(self):
        return Melody([s.copy() for s in self.notes])

    def __repr__(self):
        return self.to_code()