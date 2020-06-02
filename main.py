"""
ファイル選択用gui生成
"""

import sys
import PySimpleGUI as sg
import cropped_image


class MainWindow:
    """
    gui
    """
    def main_window(self):
        """
        メインwindwow
        # """
        sg.theme("systemdefault")

        frame = [
            [sg.Text('読み取る言語')],
            [sg.Radio("日本語", key="-jpn-", group_id=1)],
            [sg.Radio('英語', key="-eng-", group_id=1)],
        ]
        layout = [
            [sg.Text('読み取るファイルを選択してください')],
            [sg.InputText(size=(100, 1), key="-file_path-"), sg.FileBrowse('読み取るファイルを選択')],
            [sg.Frame("言語選択", frame)],
            [sg.Submit(button_text="読み取り開始")],
            [sg.Text('読み取り結果')],
            [sg.Output(size=(100, 30))],
            [sg.Submit(button_text="閉じる")]

        ]
        window = sg.Window("OCR", layout)
        while True:
            event, values = window.read()
            if event is None:
                print("exit")
                break

            if event == "読み取り開始":
                pdf_path = values["-file_path-"]
                if values["-jpn-"]:
                    lang = "jpn"
                elif values["-eng-"]:
                    lang = "eng"

                print(pdf_path)
                print(lang)
                cropped_image.CropImage(image_path=pdf_path, select_lang=lang, window=window)

            if event == "閉じる":
                sys.exit()



        window.close()

if __name__ == "__main__":
    a = MainWindow()
    a.main_window()
