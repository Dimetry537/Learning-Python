import pathlib
from game.dialog import Dialog

file_dir = pathlib.Path(__file__).parent.resolve()

dialog = Dialog(str(file_dir) + '/assets/dialogs/test_dialog.txt')
print(dialog)