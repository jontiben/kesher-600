# Hebrew
h_normal_substitution = {
    # Cantillation below
    "׃":"",
    "׀":"",
    "֑‎":"",
    "֓":"",
    "֕":"",
    "֗":"",
    "֙":"",
    "֛":"",
    "֝":"",
    "֟":"",
    "֡":"",
    "֣":"",
    "֥":"",
    "֧":"",
    "֩":"",
    "֫":"",
    "֭":"",
    "֒":"",
    "֔":"",
    "֖":"",
    "֘":"",
    "֚":"",
    "֜":"",
    "֞":"",
    "֠":"",
    "֢":"",
    "֤":"",
    "֦":"",
    "֨":"",
    "֪":"",
    "֬":"",
    "֮":"",
    # Sofit below
    "ם": "מ",
    "ך": "כ",
    "ן": "נ",
    "ף": "פ",
    "ץ": "צ",
    # Geresh below
    "׳": "",
    # Gershayim below
    "״": "",
    # Yiddish below
    "אַ": "אנ",
    # A completely different block? For some reason?
    "ֶ ‎": "",
    "ַ ‎": "",
    "ָ ‎": "",
    "ֹ ‎": "",
    "ֺ ": "",
    "ֻ ‎": "",
    "ּ ‎": "",
    "ֽ ‎": "",
    "־‎": "",
    "ֿ ‎": "",
    "׀‎": "",
    " ‎": "", # Repeats
    "׃‎": "",
    "׆‎": "",

}

h_niqqud_substitution = {
    # Niqqud below
    "ְ": "",
    "ֱ": "",
    "ֲ": "",
    "ֳ": "",
    "ִ": "",
    "ֵ": "",
    "ֶ": "",
    "ַ": "",
    "ָ": "",
    "ֹ": "",
    "ֻ": "",
    "ּ": "",
    "ֿ": "",
    b'\\u05c1': "",
}

h_standard = { # Mispar hechrechi
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 10,
    'כ': 20,
    'ל': 30,
    'מ': 40,
    'נ': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80,
    'צ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400,
}

h_standard_with_niqqud = {
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 10,
    'כ': 20,
    'ל': 30,
    'מ': 40,
    'נ': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80,
    'צ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400,
    "ַ": 6,
    "ִ": 10,
    "ֹ": 10,
    "וּ": 10,
    "ָ": 16,
    "ֵ": 20,
    "ְ": 20,
    "ֲ": 26,
    "ֶ": 30,
    "ֻ": 30,
    "ֳ": 36,
    "ֱ": 40,
}

h_standard_with_niqqud_digit_sum = {
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 10,
    'כ': 20,
    'ל': 30,
    'מ': 40,
    'נ': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80,
    'צ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400,
    "ַ": 6,
    "ִ": 1,
    "ֹ": 1,
    "וּ": 1,
    "ָ": 7,
    "ֵ": 2,
    "ְ": 2,
    "ֲ": 8,
    "ֶ": 3,
    "ֻ": 3,
    "ֳ": 9,
    "ֱ": 4,
}


h_large = { # Mispar gadol
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 10,
    'כ': 20,
    'ל': 30,
    'מ': 40,
    'נ': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80,
    'צ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400,
    '#כ': 500,
    '#מ': 600,
    '#נ': 700,
    '#פ': 800,
    '#צ': 900,
}

h_original = {
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 10,
    'כ': 11,
    'ל': 12,
    'מ': 13,
    'נ': 14,
    'ס': 15,
    'ע': 16,
    'פ': 17,
    'צ': 18,
    'ק': 19,
    'ר': 20,
    'ש': 21,
    'ת': 22,
}

h_reduced = {
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 1,
    'כ': 2,
    'ל': 3,
    'מ': 4,
    'נ': 5,
    'ס': 6,
    'ע': 7,
    'פ': 8,
    'צ': 9,
    'ק': 1,
    'ר': 2,
    'ש': 3,
    'ת': 4,
}

# The same as h_standard, but with all the values squared
h_squared = {
    'א': 1,
    'ב': 4,
    'ג': 9,
    'ד': 16,
    'ה': 25,
    'ו': 36,
    'ז': 49,
    'ח': 64,
    'ט': 81,
    'י': 100,
    'כ': 400,
    'ל': 900,
    'מ': 1600,
    'נ': 2500,
    'ס': 3600,
    'ע': 4900,
    'פ': 6400,
    'צ': 8100,
    'ק': 10000,
    'ר': 40000,
    'ש': 90000,
    'ת': 160000,
}

h_shemi = {
    'א': 111,
    'ב': 412,
    'ג': 83,
    'ד': 434,
    'ה': 6,
    'ו': 12,
    'ז': 67,
    'ח': 418,
    'ט': 419,
    'י': 20,
    'כ': 100,
    'ל': 74,
    'מ': 80,
    'נ': 106,
    'ס': 120,
    'ע': 130,
    'פ': 81,
    'צ': 104,
    'ק': 186,
    'ר': 510,
    'ש': 350,
    'ת': 406,
}

h_triangular = {
    'א': 1,
    'ב': 3,
    'ג': 6,
    'ד': 10,
    'ה': 15,
    'ו': 21,
    'ז': 28,
    'ח': 36,
    'ט': 45,
    'י': 55,
    'כ': 75,
    'ל': 105,
    'מ': 145,
    'נ': 195,
    'ס': 255,
    'ע': 325,
    'פ': 405,
    'צ': 495,
    'ק': 595,
    'ר': 795,
    'ש': 1035,
    'ת': 1495,
}