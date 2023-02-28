from l_letter_values import *
from h_letter_values import *
from g_letter_values import *

START_WIDTH = 1000
START_HEIGHT = 600

SCRIPTS = ["Latin", "Hebrew", "Greek"]
L_TYPES = {
    "Ordinal": l_ordinal,
    "Reduction": l_reduction,
    "Reverse": l_reverse,
    "Reverse-Reduction": l_reverse_reduction,
    "Golden Dawn": l_golden_dawn,
}

H_TYPES = {
    "Mispar Hechrechi (standard)": h_standard,
    "Mispar Hechrechi-Niqqud (with vowels)": h_standard_with_niqqud,
    "Misp. Hech.-S'chum-Niq. (vowel dig. sum)": h_standard_with_niqqud_digit_sum,
    "Mispar Gadol (large)": h_large,
    "Mispar Katan (reduced)": h_reduced,
    "Mispar Siduri (original)": h_original,
    "Mispar Perati (squared)": h_squared,
    "Mispar Shemi (shemi full name)": h_shemi,
    "Mispar Kidmi (triangular)": h_triangular,
}

G_TYPES = {
    "Isopsephy (standard)": g_standard,
    "Ordinal": g_ordinal,
}

L_NORMAL_SUBSTITUTION = l_normal_substitution
H_NORMAL_SUBSTITUTION = h_normal_substitution
H_VOWEL_SUBSTITUTION = h_niqqud_substitution
G_NORMAL_SUBSTITUTION = g_normal_substitution

ALL_NORMAL_SUBSTITUTION = [L_NORMAL_SUBSTITUTION, H_NORMAL_SUBSTITUTION, G_NORMAL_SUBSTITUTION]

ALL_GEMATRIA = [L_TYPES, H_TYPES, G_TYPES]

BG_COLOR = "gray7"
PADX = 5
PADY = 5
BUTTON_FONTSIZE = 20
VAL_FONTSIZE = 12
INPUT_FONTSIZE = VAL_FONTSIZE+4