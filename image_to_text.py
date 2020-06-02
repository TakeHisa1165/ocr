"""
画像をOCRでテキストに変換
"""
import sys
import os
from PIL import Image
import PySimpleGUI as sg
import pyocr
import pyocr.builders

# import cv2


class Image_to_Text:
    """
    画像からテキストを抽出
    """
    def image_to_text(self, image_path_list, select_lang, window):
        """
        画像からテキストを抽出
        """
        print("文字認識中")
        window.refresh()
        if select_lang == "jpn":
            lang_index = 2
        elif select_lang == "eng":
            lang_index = 0
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("OCRツールがありません")
            sys.exit()

        tool = tools[0]
        print("使用するOCRツール{}".format(tool.get_name()))

        langs = tool.get_available_languages()
        print("選択可能な言語{}".format(langs))
        lang = langs[lang_index]
        print("選択した言語={}".format(lang))

        for path in image_path_list:
            txt = tool.image_to_string(
                Image.open(path),
                lang=lang,
                # builder=pyocr.builders.WordBoxBuilder(tesseract_layout=3))
                builder=pyocr.builders.TextBuilder(tesseract_layout=3))
            print(txt)
            with open("test.text", "w") as f:
                print(txt, file=f)
            window.refresh()

        for path in image_path_list:
            pass
            # os.remove(path)
        sg.popup('完了しました')
        sys.exit()

