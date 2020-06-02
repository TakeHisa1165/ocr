from PIL import Image
import image_to_text


def crop_by_pil(select_lang, window):
    im = Image.open("cropped_image.png")
    im_crop = im.crop((500, 170, 990, 629))
    im_crop.save("cropped.png")

    image_path_list = []
    image_path_list.append(r"D:\ドキュメント\python\ocr\cropped.png")
    itt = image_to_text.Image_to_Text()
    itt.image_to_text(image_path_list=image_path_list, select_lang=select_lang, window=window)