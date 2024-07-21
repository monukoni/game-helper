import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Створення головного вертикального макету
        main_layout = QVBoxLayout()

        # Створення текстового віджета з прокручуванням
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # Робимо текстовий віджет тільки для читання

        # Додавання прикладового тексту
        example_text = (
            "Did you know you can unhook your teammate?\n"
            "Did you know you can stun killer by dropping palette?\n"
            "Always stay aware of your surroundings to avoid being caught off guard by the killer.\n"
            "Use pallets and windows to create distance between you and the killer.\n"
            "Coordinate with your teammates to complete generators more efficiently.\n"
            "Save the best for last: save pallets in key areas for the late game.\n"
            "Learn the maps to know the locations of generators, pallets, and windows.\n"
            "Use perks that complement your playstyle and strategy.\n"
            "Don't rush to unhook a teammate if the killer is nearby; wait for the right moment.\n"
            "Practice skill checks to minimize failed attempts on generators and healing.\n"
            "Use the environment to your advantage to break the killer's line of sight.\n"
            "Prioritize repairing generators to apply pressure on the killer.\n"
            "Use med-kits, toolboxes, and other items to aid in survival and objective completion.\n"
            "Pay attention to the killer's movements and patterns to anticipate their actions.\n"
            "Communicate with your team using the in-game chat or external communication tools.\n"
            "Don't panic when being chased; stay calm and make calculated decisions.\n"
            "Use flashlight saves to rescue teammates from the killer's grasp.\n"
            "Take advantage of the killer's power cooldowns to make your escape.\n"
            "Use decisive strike to escape the killer's grasp if you are the obsession.\n"
            "Learn the different killer abilities and how to counter them.\n"
            "Use the hatch as a last resort if you are the last survivor.\n"
            "Stay quiet and avoid making noise that could alert the killer to your location.\n"
            "Use urban evasion to move quickly and quietly through the environment.\n"
            "Stay close to walls and obstacles to reduce your visibility to the killer.\n"
            "Use borrowed time to rescue teammates safely from the hook.\n"
            "Take advantage of totems to gain beneficial effects or to cleanse hex totems.\n"
            "Use the killer's terror radius to gauge their proximity and plan your actions accordingly.\n"
            "Use balanced landing to reduce the stun effect from falls and to gain a speed boost.\n"
            "Be mindful of the endgame collapse timer and prioritize your actions accordingly.\n"
            "Use saboteur to disable hooks and hinder the killer's ability to secure sacrifices.\n"
            "Keep track of your teammates' statuses and try to help those who are injured or downed.\n"
            "Use adrenaline to gain an instant heal and speed boost when the last generator is completed.\n"
            "Use empathy to locate injured teammates and provide assistance.\n"
            "Use iron will to reduce the noise you make when injured.\n"
            "Use leader to boost your teammates' action speeds when near you.\n"
            "Use lightweight to reduce your scratch marks and make it harder for the killer to track you.\n"
            "Use quick and quiet to perform fast actions silently, such as vaulting windows.\n"
            "Use resilience to increase your action speed when injured.\n"
            "Use self-care to heal yourself without the need for a med-kit.\n"
            "Use spine chill to detect when the killer is looking in your direction.\n"
            "Use sprint burst to gain a quick burst of speed to escape the killer.\n"
            "Use unbreakable to recover from the dying state once per match.\n"
            "Use vigilance to recover from exhaustion status effects faster.\n"
            "Use wake up to open exit gates faster.\n"
            "Use we’ll make it to increase your healing speed after unhooking a teammate.\n"
            "Use windows of opportunity to see the aura of pallets and windows near you.\n"
            "Learn the different types of hooks and their locations on each map.\n"
            "Use the basement as a last resort for hiding, but be cautious of the killer's proximity.\n"
            "Don't camp near hooked survivors; it reduces your team's chances of winning.\n"
            "Use the fog and shadows to blend in and avoid detection.\n"
            "Keep an eye on the killer's red stain to predict their movements.\n"
            "Use bond to see the aura of nearby teammates and coordinate actions.\n"
            "Use prove thyself to increase generator repair speed when working with others.\n"
            "Use kindred to reveal the killer's location when you or a teammate is hooked.\n"
            "Use small game to detect nearby traps and totems.\n"
            "Use dark sense to reveal the killer's aura when a generator is completed.\n"
            "Use dead hard to dash forward and avoid a hit when injured.\n"
            "Use hope to gain a speed boost when the exit gates are powered.\n"
            "Use inner strength to heal yourself after cleansing a totem.\n"
            "Use open-handed to increase the range of aura reading abilities.\n"
            "Use red herring to create distractions and mislead the killer.\n"
            "Use soul guard to gain endurance when recovering from the dying state.\n"
            "Use tenacity to crawl faster and recover at the same time.\n"
            "Use aftercare to see the aura of teammates you have healed or rescued.\n"
            "Use alert to reveal the killer's location when they perform a break action.\n"
            "Use breakdown to destroy the hook you were rescued from, making it unusable.\n"
            "Use buckle up to see the recovery progress of dying teammates.\n"
            "Use camaraderie to pause the hook timer when teammates are nearby.\n"
            "Use corrective action to prevent failed skill checks when helping teammates.\n"
            "Use deja vu to see the aura of generators when the match starts.\n"
            "Use deliverance to unhook yourself after performing a safe hook rescue.\n"
            "Use distortion to avoid having your aura revealed by the killer.\n"
            "Use flip-flop to convert recovery progress into wiggle progress.\n"
            "Use guardian to gain endurance after unhooking a teammate.\n"
            "Use head on to stun the killer when exiting a locker.\n"
            "Use inner healing to heal yourself by hiding in a locker after cleansing a totem.\n"
            "Use leader to boost your teammates' action speeds when near you.\n"
            "Use left behind to see the hatch when you are the last survivor.\n"
            "Use lightweight to reduce your scratch marks and make it harder for the killer to track you.\n"
            "Use no mither to start the match injured but gain other benefits.\n"
            "Use object of obsession to see the killer's aura but also be revealed to them.\n"
            "Use off the record to avoid detection after being unhooked.\n"
            "Use pharmacy to search chests faster and with a guaranteed med-kit.\n"
            "Use plunderer's instinct to see the aura of chests and their contents.\n"
            "Use premonition to receive a warning when looking in the killer's direction.\n"
            "Use saboteur to sabotage hooks and prevent the killer from using them.\n"
            "Use second wind to automatically heal yourself after being unhooked.\n"
            "Use slippery meat to increase your chances of escaping the hook.\n"
            "Use small game to detect nearby traps and totems.\n"
            "Use solidarity to heal yourself when healing others.\n"
            "Use streetwise to reduce item consumption rates for you and your teammates.\n"
            "Use this is not happening to increase your skill check success zone when injured.\n"
            "Use up the ante to increase luck for all survivors.\n"
            "Use vigil to recover from status effects faster.\n"
            "Use visionary to see the aura of generators.\n"
            "Use we'll make it to increase your healing speed after unhooking a teammate.\n"
            "Use windows of opportunity to see the aura of pallets and windows.\n"
            "Use autodidact to gain progression for successful skill checks when healing.\n"
            "Use boil over to make it harder for the killer to carry you.\n"
            "Use bond to see the aura of teammates.\n"
            "Use calm spirit to prevent crows from giving away your position.\n"
            "Use dance with me to leave no scratch marks after performing a fast action."
        )

        self.text_edit.setPlainText(example_text)

        # Додавання текстового віджета до головного макету
        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)
        self.setWindowTitle('Scrollable Text Example')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
