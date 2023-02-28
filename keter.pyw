import tkinter as maaseh_breishit
from tkinter import ttk as maaseh_merkavah
import tkinter.font as ktav
from memale_kol_almin import *

ktav_amiti = 0  # 0 is Latin, 1 is Hebrew, 2 is Greek
haam_hanivhar = GIMATRIOT[ktav_amiti]["Ordinal"]

shoresh = maaseh_breishit.Tk()
shoresh.title("Kesher 600")
shoresh.geometry(f"{ROCHAV_SHEL_BERIAH}x{GOVAH_SHEL_BERIAH}")
shoresh.configure(background=TSEVA_SHEL_OR)

ktav_shel_malkuth = ktav.Font(weight='bold', size=GODEL_SHEL_MALKUTH)
ktav_shel_misparayim = ktav.Font(weight='bold', family="Courier", size=GODEL_SHEL_MISPARAYIM)
ktav_acher = ktav.Font(family="Courier", size=GODEL_SHEL_MISPARAYIM)
ktav_shel_ktiva = ktav.Font(weight='bold', size=GODEL_SHEL_KTIVA)

hitrachkut_miohr_elyon = 0
for ktav in GIMATRIOT:
    if len(ktav) > hitrachkut_miohr_elyon:
        hitrachkut_miohr_elyon = len(ktav)


def mispar_amiti(m):
    try:
        int(m)
        return True
    except ValueError:
        return False


def tenuah(*shikhnua):
    ohr_hochma_shel_totsaa.xview(*shikhnua)
    ohr_hochma_shel_emet.xview(*shikhnua)


def pianuach(mishpat, mispar_shel_ot, gematriot):
    ot = mishpat[mispar_shel_ot]
    if len(ot) == 0:
        return "shvirat_kli"
    emet_nistarat = ot.encode('unicode_escape')
    if ktav_amiti == 1 and "ִ" not in gematriot.keys():  # Vowel-unimportant script
        if emet_nistarat in AYIN_KORBAN_SHEL_TNUOT.keys():
            ot = emet_nistarat
        if ot in AYIN_KORBAN_SHEL_TNUOT.keys():
            ot = AYIN_KORBAN_SHEL_TNUOT[ot]
            ohr_hadash = mishpat[:mispar_shel_ot] + ot + mishpat[mispar_shel_ot + 1:]
            if len(ot) == 0:
                return "shvirat_kli"
            if len(ot) == 2:
                za = pianuach(ohr_hadash, mispar_shel_ot, gematriot)[1]
                nukva = pianuach(ohr_hadash, mispar_shel_ot + 1, gematriot)[1]
                return ot, za + nukva
            return pianuach(ohr_hadash, mispar_shel_ot, gematriot)
    if ktav_amiti < len(KORBAN_MSHUTAF):
        if ot in KORBAN_MSHUTAF[ktav_amiti].keys():
            ot = KORBAN_MSHUTAF[ktav_amiti][ot]
            ohr_hadash = mishpat[:mispar_shel_ot] + ot + mishpat[mispar_shel_ot + 1:]
            if len(ot) == 0:
                return "shvirat_kli"
            if len(ot) == 2:
                za = pianuach(ohr_hadash, mispar_shel_ot, gematriot)[1]
                nukva = pianuach(ohr_hadash, mispar_shel_ot + 1, gematriot)[1]
                return ot, za + nukva
            return pianuach(ohr_hadash, mispar_shel_ot, gematriot)
    if mispar_shel_ot == len(mishpat) - 1:
        if '#' + ot in gematriot:
            return ot, gematriot['#' + ot]
    if mispar_shel_ot < len(mishpat) - 1:
        if mishpat[mispar_shel_ot + 1] == ' ':
            if '#' + ot in gematriot:
                return ot, gematriot['#' + ot]
    if len(mishpat) > mispar_shel_ot + 1:
        if ot + mishpat[mispar_shel_ot + 1] in gematriot:
            return ot + mishpat[mispar_shel_ot + 1], gematriot[ot + mishpat[mispar_shel_ot + 1]]
    if ot in gematriot:
        return ot, gematriot[ot]
    if mispar_amiti(ot):
        return ot, int(ot)
    else:
        return None


def mocha(event, gematriot):
    global ihud_katan
    ihud_katan = 0  # For Mispar Bone'eh
    ihud = 0
    kamut_makom, ihut_makom = "", ""
    miut_yareach = False
    milla = halal_panui.get().replace(u'\u200e', '').replace('\n', '').lower().strip()

    for o, ot in enumerate(milla):
        if miut_yareach:
            miut_yareach = False
            continue
        ot = ot.lower()
        limud_shel_ot = pianuach(milla, o, gematriot)
        if limud_shel_ot is not None:
            if limud_shel_ot != "shvirat_kli":
                ot_amiti = limud_shel_ot[0]
                erekh_shel_ot = limud_shel_ot[1]
                if ktav_amiti == 1 and "bone'eh" in gematriot.keys():  # Hacky way to tell Mispar Bone'eh
                    erekh_shel_ot += ihud_katan
                    ihud_katan = erekh_shel_ot
                ihud += erekh_shel_ot
                if ktav_amiti == 1:  # Hebrew
                    if "hamerubah" not in gematriot.keys():
                        kamut_makom += " " * (4 - len(str(erekh_shel_ot))) + str(erekh_shel_ot)[::-1]
                    else:
                        kamut_makom += "   *"
                else:
                    kamut_makom += str(erekh_shel_ot) + " " * (4 - len(str(erekh_shel_ot)))
                if len(ot_amiti) == 2:
                    miut_yareach = True
                    ihut_makom += ot_amiti.capitalize() + " " * (4 - len(ot_amiti.upper()))
                else:
                    ihut_makom += ot_amiti.upper() + " " * (4 - len(ot_amiti.upper()))
        else:
            kamut_makom += " " + " " * (4 - len(ot))
            ihut_makom += ot.upper() + " " * (4 - len(ot))
    if ktav_amiti == 1:  # Hebrew
        kamut_makom = kamut_makom[::-1]
    if "hamerubah" in gematriot.keys():
        ihud = ihud ** 2
    return kamut_makom, ihut_makom, ihud


def milui(event):
    global ohr_hochma_shel_emet, ohr_hochma_shel_totsaa, maleh
    halal()
    tosaa_shel_mocha = mocha(None, haam_hanivhar)
    if ktav_amiti == 1:  # Hebrew
        ohr_hochma_shel_totsaa.create_text(shoresh.winfo_width() - 20, 40, fill="white", font=ktav_shel_misparayim,
                                           text=tosaa_shel_mocha[0], anchor="ne", justify="right")
        ohr_hochma_shel_emet.create_text(shoresh.winfo_width() - 20, 40, fill="white", font=ktav_shel_misparayim,
                                         text=tosaa_shel_mocha[1], anchor="ne", justify="right")
    else:
        ohr_hochma_shel_totsaa.create_text(20, 40, fill="white", font=ktav_shel_misparayim, text=tosaa_shel_mocha[0],
                                           anchor="nw", justify="left")
        ohr_hochma_shel_emet.create_text(20, 40, fill="white", font=ktav_shel_misparayim, text=tosaa_shel_mocha[1],
                                         anchor="nw", justify="left")
    maleh["text"] = "Total:  " + str(tosaa_shel_mocha[2])
    ohr_hochma_shel_totsaa.config(scrollregion=ohr_hochma_shel_totsaa.bbox("all"))
    ohr_hochma_shel_emet.config(scrollregion=ohr_hochma_shel_totsaa.bbox("all"))
    calculate_other()


def calculate_other():
    global mita
    for m in range(1, len(mita), 2):
        try:
            if mita[m - 1].cget("text")[:-1] != "":
                mita[m].config(text=str(mocha(None, GIMATRIOT[ktav_amiti][mita[m - 1].cget("text")[:-1]])[2]))
        except:  # I'm too tired for this shit
            mita[m].destroy()


def halal():
    global ohr_hochma_shel_emet, ohr_hochma_shel_totsaa, maleh, halal_panui
    ohr_hochma_shel_emet.delete("all")
    ohr_hochma_shel_totsaa.delete("all")
    maleh["text"] = "Total:  "


def neshamot_hadashot(event):
    global ktav_amiti
    global haam_hanivhar
    global neshama
    global sub_labels
    global mita
    global halal_panui
    if event is None:
        ktav_amiti = 0
    else:
        ktav_amiti = SAFOT.index(event.widget["text"])
    neshama = maaseh_merkavah.Combobox(shoresh, values=list(GIMATRIOT[ktav_amiti].keys()), state="readonly",
                                       background=TSEVA_SHEL_OR,
                                       font=ktav_shel_malkuth)
    neshama.grid(row=1, column=0, columnspan=sfira_shel_atzamot, padx=GODEL_SHEL_OHR_MAKIF_OFKIYUT,
                 pady=GODEL_SHEL_OHR_MAKIF_ANAKHIYUT)
    neshama.bind("<<ComboboxSelected>>", zivug_pnimi_shel_atzilut)
    neshama.set(list(GIMATRIOT[ktav_amiti].keys())[0])
    haam_hanivhar = GIMATRIOT[ktav_amiti][neshama.get()]
    for atzam in atzamot:
        if SAFOT.index(atzam.cget("text")) != ktav_amiti:
            atzam.config(bg="gray40")
            atzam.config(highlightthickness=2)
        else:
            atzam.config(bg=TSEVA_SHEL_OR)
            atzam.config(highlightthickness=0)
    if ktav_amiti == 1:
        halal_panui.config(justify="right")
    else:
        halal_panui.config(justify="left")
    mita = []
    halal()
    zivug_pnimi_shel_atzilut(None)


def zivug_pnimi_shel_atzilut(event):
    global haam_hanivhar
    global mita
    bkhira = neshama.get()
    haam_hanivhar = GIMATRIOT[ktav_amiti][bkhira]
    for m in range(len(mita)):
        mita[m].destroy()
    mita = []
    sfira = 0
    for gimatria in GIMATRIOT[ktav_amiti]:
        if gimatria != neshama.get():
            mita.append(
                maaseh_breishit.Label(shoresh, text=gimatria + ':', bg=TSEVA_SHEL_OR, fg="gray50", font=ktav_acher,
                                      anchor='w'))
            mita[-1].grid(row=7 + sfira, column=0, padx=0, pady=0, sticky="nsew")
            mita.append(maaseh_breishit.Label(shoresh, text=str(mocha(None, GIMATRIOT[ktav_amiti][gimatria])[2]),
                                              bg=TSEVA_SHEL_OR, fg="gray50", font=ktav_acher, anchor='w'))
            mita[-1].grid(row=7 + sfira, column=1, padx=0, pady=0, sticky="nsew")
            sfira += 1
    if sfira < hitrachkut_miohr_elyon:  # Not disappearing unless I overwrite them for some reason
        for i in range(sfira, hitrachkut_miohr_elyon):
            maaseh_breishit.Label(shoresh, text="", bg=TSEVA_SHEL_OR).grid(row=7 + i, column=0, padx=0, pady=0,
                                                                           sticky="nsew")
            maaseh_breishit.Label(shoresh, text="", bg=TSEVA_SHEL_OR).grid(row=7 + i, column=1, padx=0, pady=0,
                                                                           sticky="nsew")
    milui(None)


# Script selection
atzamot = []
for s, safa in enumerate(SAFOT):
    atzamot.append(
        maaseh_breishit.Button(shoresh, text=safa, bg=TSEVA_SHEL_OR, fg="white", font=ktav_shel_malkuth, borderwidth=0))
    atzamot[s].grid(row=0, column=s, padx=0, pady=0, sticky="nsew")
    atzamot[s].bind("<Button-1>", neshamot_hadashot)
    shoresh.grid_columnconfigure(s, weight=1)
sfira_shel_atzamot = len(atzamot)
# Output fields
ohr_hochma_shel_emet = maaseh_breishit.Canvas(shoresh, height=20, width=ROCHAV_SHEL_BERIAH, bg=TSEVA_SHEL_OR,
                                              highlightthickness=0)
ohr_hochma_shel_emet.grid(row=2, column=0, columnspan=sfira_shel_atzamot, padx=GODEL_SHEL_OHR_MAKIF_OFKIYUT, pady=0,
                          sticky="nsew")
ohr_hochma_shel_totsaa = maaseh_breishit.Canvas(shoresh, height=20, width=ROCHAV_SHEL_BERIAH, bg=TSEVA_SHEL_OR,
                                                highlightthickness=0)
ohr_hochma_shel_totsaa.grid(row=3, column=0, columnspan=sfira_shel_atzamot, padx=GODEL_SHEL_OHR_MAKIF_OFKIYUT, pady=0,
                            sticky="nsew")
achiza = maaseh_breishit.Scrollbar(shoresh, orient=maaseh_breishit.HORIZONTAL)
achiza.grid(row=4, column=0, columnspan=sfira_shel_atzamot, padx=GODEL_SHEL_OHR_MAKIF_OFKIYUT,
            pady=GODEL_SHEL_OHR_MAKIF_ANAKHIYUT, sticky="nsew")
achiza.config(command=tenuah)
achiza.config(command=tenuah)
ohr_hochma_shel_emet.config(xscrollcommand=achiza.set)
ohr_hochma_shel_totsaa.config(xscrollcommand=achiza.set)
maleh = maaseh_breishit.Label(shoresh, text="Total: ", bg=TSEVA_SHEL_OR, fg="white", font=ktav_shel_malkuth)
maleh.grid(row=5, column=0, columnspan=sfira_shel_atzamot, padx=GODEL_SHEL_OHR_MAKIF_OFKIYUT,
           pady=GODEL_SHEL_OHR_MAKIF_ANAKHIYUT)
# Input field
halal_panui = maaseh_breishit.Entry(shoresh, bg=TSEVA_SHEL_OR, font=ktav_shel_ktiva, fg="white")
halal_panui.grid(row=6, column=0, columnspan=sfira_shel_atzamot, padx=GODEL_SHEL_OHR_MAKIF_OFKIYUT * 2,
                 pady=GODEL_SHEL_OHR_MAKIF_ANAKHIYUT * 2, sticky="nsew")
halal_panui.bind("<KeyRelease>", milui)
neshamot_hadashot(None)

if __name__ == '__main__':
    shoresh.mainloop()
