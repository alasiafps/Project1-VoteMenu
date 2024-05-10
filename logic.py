from PyQt6.QtWidgets import *
from gui import Ui_MainWindow


class Logic(QMainWindow):
    def __init__(self) -> None:
        """
        This function sets a couple important variables, the number of votes for each candidate
        It also reads if the vote button is clicked, and sends the code to do the logic
        Return: None
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.john_votes = 0
        self.jane_votes = 0
        self.voted_ids = set()  # Set to store voted IDs
        self.ui.vote_button.clicked.connect(self.cast_vote)
        self.ui.exit_button.clicked.connect(self.close)

    def cast_vote(self) -> None:
        """
        This function does a few things. The first thing it does is it grabs a voter ID
        Each voter ID can only vote one time, and each voter id can be no more or less than 4 digits
        If the voter id has already voted, it will pop an error box saying you've already voted
        It also reads if the voter id is invalid
        Assuming the voter ID is valid, it then reads which candidate the user wants to vote for,
        and adds one to their total vote
        It will then call the updatelabels function.
        :return: None
        """
        voter_id = self.ui.id_input.text()
        if len(voter_id) != 4 or not voter_id.isdigit():
            QMessageBox.warning(self, "Invalid ID", "Please enter a 4-digit numeric ID.")
            return
        if voter_id in self.voted_ids:
            QMessageBox.warning(self, "Already Voted", "This voter ID has already cast a vote.")
            return
        if self.ui.button_john.isChecked():
            self.john_votes += 1
        elif self.ui.button_jane.isChecked():
            self.jane_votes += 1
        self.voted_ids.add(voter_id)  # Add voted ID to the set
        self.update_labels()

    def update_labels(self) -> None:
        """
        This function simply updates the onscreen GUI to ensure the correct amounts of votes are displayed
        It also does the math for total votes by adding votes for jane and john, and displays that
        on screen as well.
        :return: None
        """
        self.ui.john_label.setText(f"John - {self.john_votes}")
        self.ui.jane_label.setText(f"Jane - {self.jane_votes}")
        total_votes = self.john_votes + self.jane_votes
        self.ui.total_label.setText(f"Total - {total_votes}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    logic = Logic()
    logic.show()
    sys.exit(app.exec())