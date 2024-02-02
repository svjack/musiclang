
from musiclang.write.out.to_mxl import QUALITIES_INV, QUALITIES_TO_CHORDS, QUALITIES, NOTES_TO_ROOT

def chord_analysis(chord_root, chord_type):
    from musiclang import Chord, Tonality
    # Step 1: Identify Chord Type (Triad or Seventh)
    chord_type_label = '7' if len(chord_type) == 4 else ''

    # Step 2: Find Possible Tonality Degrees and Modes
    results = []
    possible = QUALITIES_TO_CHORDS[chord_type]
    possible = [(deg, (tone + chord_root) % 12, mode, ext) for deg, tone, mode, ext in possible]
    #chords = [Chord(deg, extension=ext, tonality=Tonality(tone, mode)) for deg, tone, mode, ext in possible]

    return possible


def chord_repr_to_chord(chord):

    real_chord = chord.split('/')
    chord = real_chord[0]
    bass = real_chord[1] if len(real_chord) > 1 else None

    chord_type = None
    for quality, quality_value in QUALITIES_INV.items():
        if chord.endswith(quality):
            chord_type = quality_value
            root_note = chord.replace(quality, '')
            break
    else:
        raise Exception('Unknown chord')

    chord_root = NOTES_TO_ROOT[root_note]
    possible =  chord_analysis(chord_root, chord_type)

    return possible


def chord_repr_list_to_chords(chords):
    possibles = [chord_repr_to_chord(chord) for chord in chords]
    from musiclang.analyze.chord_inference import optimal_chord_inference
    from musiclang import Score
    chords = optimal_chord_inference(possibles)
    return Score(chords)
