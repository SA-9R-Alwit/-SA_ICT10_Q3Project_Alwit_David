from pyscript import document

tigers = ["⭐ Sir. Pena (Leader)", "ACLARO, JOHN TRISTAN E.", "AGUILAR, ARIANNE S.", "AMANTE, RAILEY L.", "BANZALI, DYLAN EURI M.", "BULO, EADEN RIEV A.", "BUNADO, ATHENA FELICITY B.", "CASIMIRO, REEVER KAL-EL P.", "CATAM, DANIELLA KIRSTEN V.", "CO, ALEXANDER RAIN D.", "DHALIWAL, SAHILPREET S.", "FLORES, ENYA CLARE G.", "FLORES, STEPHANIE BELLE S.", "GILL, SARVEEN K.", "IGNACIO, SASHA NIKOLA M.", "LAJOM, JACOB T."]
hornets = ["⭐ Sir Nixon Sumaoang (Leader)", "ALOTAYA, Margaux J.", "ALWIT, David Andrew K.", "AQUINO, Shean Terrenze O.", "BRAR, Opdesh S.", "CHAVEZ, Cen Mar Gabriel D.", "CHUA, Reese Blesilda W.", "DE LOS SANTOS, Samuel Joshua", "ESTABILLO, Carl Jaden M.", "FANER, Janinna Arelie F.", "FERNANDEZ, Lesvie Mae A.", "GALE, Benjamin Miguel B.", "GARCIA, Joshua Melroy", "GILL, Ekamnoor K.", "KAUR, Simrat", "LAEDA, Lewis Ezekiel B."]
bears = ["LIM, EZEKIEL PHOENIX A.", "LUCAS, SAMANTHA P.", "MANDIA, KYRSTEN AISHA E.", "MATIG-A, CALEB JACOB T.", "MEDINA, LYKA D.", "MENDEZ, CALEV A.", "MIGUEL, JUAN ANTONINO C.", "MISA, JIANNA BEATRIZ M.", "OMBAO, JISELLA DOMINIQUE C.", "OSEA, ELAINE JVALA R.", "SANTOS, JOHANN ISAAC D.", "SUMNDAD, CURTNEY MAE M", "TAGUIBAO, ANTONIO MURCIELAGO R.", "TIU, MAXENE S.", "TOMAS, NICOLLE G.", "UY, CASEY OLIVER O.", "WOO, SHANSANG C."]
bulldogs = ["LUSICA, Alyza Kate O.", "MACALA, Sophia Issabel C.", "MACAS, Zaia Chryzelle D.", "MARANAN, Kaitlin Pia G.", "MONTEMAYOR, Padme Havilah A.", "MUSOR, Hanna Yasmin M.", "OMNES, Wilwen Benedict P.", "OREIRO, Rochel M.", "PLATON, Travis Reiley", "RAMIREZ, Aion P.", "RAZONABLE, Matt Sky L.", "SALVADOR, Eris Russell I.", "SALVADOR, Toni Rianne M.", "SILLEZA, Lucilind A.", "TIWARI, Kushdeep S.", "VILLANUEVA, Sofia Leona S."]

def load_rosters():
    def populate(lid, plist):
        el = document.getElementById(lid)
        if el:
            html = ""
            for name in plist:
                if "(Leader)" in name:
                    html += f"<li style='color:#fff; font-weight:bold; border-bottom:1px solid currentColor;'>{name}</li>"
                else:
                    html += f"<li>{name}</li>"
            el.innerHTML = html

    populate('list-tigers', tigers)
    populate('list-bears', bears)
    populate('list-hornets', hornets)
    populate('list-bulldogs', bulldogs)

load_rosters()