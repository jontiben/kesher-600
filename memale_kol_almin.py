from l_letter_values import *
from h_letter_values import *
from y_letter_values import *

ROCHAV_SHEL_BERIAH = 1000
GOVAH_SHEL_BERIAH = 600

SAFOT = ["Latin", "Hebrew", "Greek"]

LAMED_SUGIM = {
    "Ordinal": l_ordinal,
    "Reduction": l_reduction,
    "Reverse": l_reverse,
    "Reverse-Reduction": l_reverse_reduction,
    "Golden Dawn": l_golden_dawn,
}

AYIN_SUGIM = {
    "Mispar Hechrechi (standard)": h_standard,
    "Mispar Hechrechi-Niqqud (with vowels)": h_standard_with_niqqud,
    "Misp. Hech.-S'chum-Niq. (vowel dig. sum)": h_standard_with_niqqud_digit_sum,
    "Mispar Gadol (large)": h_large,
    "Mispar Katan (reduced)": h_reduced,
    "Mispar Siduri (original)": h_original,
    "Mispar Perati (squared)": h_squared,
    "Mispar Meshulash (cubed)": h_cubed,
    "Mispar Shemi (shemi full name)": h_shemi,
    "Mispar Kidmi/Meshulash (triangular)": h_triangular,
    "Mispar Bone'eh (building)": h_building,
    "Mispar Ne'elam-Shemi (hidden)": h_hidden,
    "Mispar haMerubah HaKlali (total squared)": h_total_squared,
    "Mispar Mispari (values of number names)": h_recursive,
    "AtBash": h_atbash,
    "AlBam": h_albam,
}

YOD_SUGIM = {
    "Isopsephy (standard)": g_standard,
    "Ordinal": g_ordinal,
}

LAMED_KORBAN = l_korban
AYIN_KORBAN = h_korban
AYIN_KORBAN_SHEL_TNUOT = k_korban_shel_niqqud
YOD_KORBAN = y_korban

KORBAN_MSHUTAF = [LAMED_KORBAN, AYIN_KORBAN, YOD_KORBAN]

GIMATRIOT = [LAMED_SUGIM, AYIN_SUGIM, YOD_SUGIM]

TSEVA_SHEL_OR = "gray7"
GODEL_SHEL_OHR_MAKIF_OFKIYUT = 5
GODEL_SHEL_OHR_MAKIF_ANAKHIYUT = 5
GODEL_SHEL_MALKUTH = 20
GODEL_SHEL_MISPARAYIM = 12
GODEL_SHEL_KTIVA = GODEL_SHEL_MISPARAYIM + 4