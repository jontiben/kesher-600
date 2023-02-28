import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from defines import *

script_selection = 0  # 0 is Latin, 1 is Hebrew, 2 is Greek
gematria_dict = ALL_GEMATRIA[script_selection]["Ordinal"]

root = tk.Tk()
root.title("Kesher 600")
root.geometry(f"{START_WIDTH}x{START_HEIGHT}")
root.configure(background=BG_COLOR)

button_label_font = font.Font(weight='bold',size=BUTTON_FONTSIZE)
value_font = font.Font(weight='bold', family="Courier", size=VAL_FONTSIZE)
other_font = font.Font(family="Courier", size=VAL_FONTSIZE)
input_font = font.Font(weight='bold', size=INPUT_FONTSIZE)

longest_gem_list_len = 0
for script_type in ALL_GEMATRIA:
    if len(script_type) > longest_gem_list_len:
        longest_gem_list_len = len(script_type)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def scrollall(*args):
    output_values.xview(*args)
    output_chars.xview(*args)


def get_value(string, charid, gematria):
    char = string[charid]
    if len(char) == 0:
        return "skip"
    char_encode = char.encode('unicode_escape')
    if script_selection == 1 and "ִ" not in gematria.keys(): # Vowel-unimportant script
        if char_encode in H_VOWEL_SUBSTITUTION.keys():
            old_char = char
            char = char_encode
        if char in H_VOWEL_SUBSTITUTION.keys():
            char = H_VOWEL_SUBSTITUTION[char]
            temp_full_string = string[:charid] + char + string[charid+1:]
            if len(char) == 0:
                return "skip"
            if len(char) == 2:
                val1 = get_value(temp_full_string, charid, gematria)[1]
                val2 = get_value(temp_full_string, charid+1, gematria)[1]
                return char, val1+val2
            return get_value(temp_full_string, charid, gematria)
    if script_selection < len(ALL_NORMAL_SUBSTITUTION):
        if char in ALL_NORMAL_SUBSTITUTION[script_selection].keys():
            char = ALL_NORMAL_SUBSTITUTION[script_selection][char]
            temp_full_string = string[:charid] + char + string[charid+1:]
            if len(char) == 0:
                return "skip"
            if len(char) == 2:
                val1 = get_value(temp_full_string, charid, gematria)[1]
                val2 = get_value(temp_full_string, charid+1, gematria)[1]
                return char, val1+val2
            return get_value(temp_full_string, charid, gematria)
    if charid == len(string)-1:
        if '#'+char in gematria:
            return char, gematria['#'+char]
    if charid < len(string)-1:
        if string[charid+1] == ' ':
            if '#'+char in gematria:
                return char, gematria['#'+char]
    if len(string) > charid+1:
        if char+string[charid+1] in gematria:
            return char+string[charid+1], gematria[char+string[charid+1]]
    if char in gematria:
        return char, gematria[char]
    if is_number(char):
        return char, int(char)
    else:
        return None


def calculate(event, gematria):
    global sub_total
    sub_total = 0 # For Mispar Bone'eh
    total = 0
    val_text, char_text = "", ""
    skip_iteration = False
    input_text = input_field.get().replace(u'\u200e', '').replace('\n','').lower().strip()

    for c, char in enumerate(input_text):
        if skip_iteration:
            skip_iteration = False
            continue
        char = char.lower()
        char_analysis = get_value(input_text, c, gematria)
        if char_analysis is not None:
            if char_analysis != "skip":
                char_string = char_analysis[0]
                char_value = char_analysis[1]
                if script_selection == 1 and "bone'eh" in gematria.keys():  # Hacky way to find Mispar Bone'eh
                    char_value += sub_total
                    sub_total = char_value
                total += char_value
                if script_selection == 1:  # Hebrew
                    if "hamerubah" not in gematria.keys():
                        val_text += str(char_value)[::-1] + " " * (4 - len(str(char_value)))
                    else:
                        val_text += "   *"
                else:
                    val_text += str(char_value) + " " * (4 - len(str(char_value)))
                if len(char_string) == 2:
                    skip_iteration = True
                    char_text += char_string.capitalize() + " " * (4 - len(char_string.upper()))
                else:
                    char_text += char_string.upper() + " " * (4 - len(char_string.upper()))
        else:
            #print(c, input_field.get().lower()[c].encode(" unicode_escape"))
            val_text += " " + " " * (4 - len(char))
            char_text += char.upper() + " " * (4 - len(char))
    if script_selection == 1: # Hebrew
        val_text = val_text[::-1]
    if "hamerubah" in gematria.keys():
        total = total ** 2
    return val_text, char_text, total



def fill_out_boxes(event):
    global output_chars, output_values, output_total
    clear_output()
    calculate_out = calculate(None, gematria_dict)
    if script_selection == 1: # Hebrew
        output_values.create_text(root.winfo_width()-20, 40, fill="white", font=value_font, text=calculate_out[0], anchor="ne", justify="right")
        output_chars.create_text(root.winfo_width()-20, 40, fill="white", font=value_font, text=calculate_out[1], anchor="ne", justify="right")
    else:
        output_values.create_text(20, 40, fill="white", font=value_font, text=calculate_out[0], anchor="nw", justify="left")
        output_chars.create_text(20, 40, fill="white", font=value_font, text=calculate_out[1], anchor="nw", justify="left")
    output_total["text"] = "Total:  " + str(calculate_out[2])
    output_values.config(scrollregion=output_values.bbox("all"))
    output_chars.config(scrollregion=output_values.bbox("all"))
    calculate_other()


def calculate_other():
    global other_gematria
    for g in range(1, len(other_gematria), 2):
        try:
            if other_gematria[g-1].cget("text")[:-1] != "":
                    other_gematria[g].config(text=str(calculate(None, ALL_GEMATRIA[script_selection][other_gematria[g-1].cget("text")[:-1]])[2]))
        except: # I'm too tired for this shit
            other_gematria[g].destroy()

def clear_output():
    global output_chars, output_values, output_total, input_field
    output_chars.delete("all")
    output_values.delete("all")
    output_total["text"] = "Total:  "


def new_script(event):
    global script_selection
    global gematria_dict
    global drop_down_box
    global sub_labels
    global other_gematria
    global input_field
    if event is None:
        script_selection = 0
    else:
        script_selection = SCRIPTS.index(event.widget["text"])
    drop_down_box = ttk.Combobox(root, values=list(ALL_GEMATRIA[script_selection].keys()), state="readonly",
                                 background=BG_COLOR,
                                 font=button_label_font)
    drop_down_box.grid(row=1, column=0, columnspan=scripts_count, padx=PADX, pady=PADY)
    drop_down_box.bind("<<ComboboxSelected>>", new_gematria)
    drop_down_box.set(list(ALL_GEMATRIA[script_selection].keys())[0])
    gematria_dict = ALL_GEMATRIA[script_selection][drop_down_box.get()]
    for button in buttons:
        if SCRIPTS.index(button.cget("text")) != script_selection:
            button.config(bg="gray40")
            button.config(highlightthickness=2)
        else:
            button.config(bg=BG_COLOR)
            button.config(highlightthickness=0)
    if script_selection == 1:
        input_field.config(justify="right")
    else:
        input_field.config(justify="left")
    other_gematria = []
    clear_output()
    new_gematria(None)


def new_gematria(event):
    global gematria_dict
    global other_gematria
    selection = drop_down_box.get()
    gematria_dict = ALL_GEMATRIA[script_selection][selection]
    for o in range(len(other_gematria)):
        other_gematria[o].destroy()
    other_gematria = []
    counter = 0
    for gem in ALL_GEMATRIA[script_selection]:
        if gem != drop_down_box.get():
            other_gematria.append(tk.Label(root, text=gem + ':', bg=BG_COLOR, fg="gray50", font=other_font, anchor='w'))
            other_gematria[-1].grid(row=7 + counter, column=0, padx=0, pady=0, sticky="nsew")
            other_gematria.append(tk.Label(root, text=str(calculate(None, ALL_GEMATRIA[script_selection][gem])[2]),
                                           bg=BG_COLOR, fg="gray50", font=other_font, anchor='w'))
            other_gematria[-1].grid(row=7 + counter, column=1, padx=0, pady=0, sticky="nsew")
            counter += 1
    if counter < longest_gem_list_len: # Not disappearing unless I overwrite them for some reason
        for i in range(counter, longest_gem_list_len):
            tk.Label(root, text="", bg=BG_COLOR).grid(row=7 + i, column=0, padx=0, pady=0, sticky="nsew")
            tk.Label(root, text="", bg=BG_COLOR).grid(row=7 + i, column=1, padx=0, pady=0, sticky="nsew")
    fill_out_boxes(None)


# Script selection
buttons = []
for s, script in enumerate(SCRIPTS):
    buttons.append(tk.Button(root, text=script, bg=BG_COLOR, fg="white", font=button_label_font, borderwidth=0))
    buttons[s].grid(row=0, column=s, padx=0, pady=0, sticky="nsew")
    buttons[s].bind("<Button-1>", new_script)
    root.grid_columnconfigure(s, weight=1)
scripts_count = len(buttons)
# Gematria Type Selection
# Output fields
output_chars = tk.Canvas(root, height=20, width=START_WIDTH, bg=BG_COLOR, highlightthickness=0)
output_chars.grid(row=2, column=0, columnspan=scripts_count, padx=PADX, pady=0, sticky="nsew")
output_values = tk.Canvas(root, height=20, width=START_WIDTH, bg=BG_COLOR, highlightthickness=0)
output_values.grid(row=3, column=0, columnspan=scripts_count, padx=PADX, pady=0, sticky="nsew")
scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
scrollbar.grid(row=4, column=0, columnspan=scripts_count, padx=PADX, pady=PADY, sticky="nsew")
scrollbar.config(command=scrollall)
scrollbar.config(command=scrollall)
output_chars.config(xscrollcommand=scrollbar.set)
output_values.config(xscrollcommand=scrollbar.set)
output_total = tk.Label(root, text="Total: ", bg=BG_COLOR, fg="white", font=button_label_font)
output_total.grid(row=5, column=0, columnspan=scripts_count, padx=PADX, pady=PADY)
# Input field
input_field = tk.Entry(root, bg=BG_COLOR, font=input_font, fg="white")
input_field.grid(row=6, column=0, columnspan=scripts_count, padx=PADX*2, pady=PADY*2, sticky="nsew")
input_field.bind("<KeyRelease>", fill_out_boxes)
new_script(None)

if __name__ == '__main__':
    root.mainloop()
