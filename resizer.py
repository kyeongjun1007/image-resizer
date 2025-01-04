import os
import sys
import argparse
import glob

from PIL import Image


def image_resizing(folder_name, file_name, extention, size, is_width_based = False):
    image = Image.open(f'./{folder_name}/{file_name}.{extention}')
    width, height = image.size

    if is_width_based:
        new_width = size
        new_height = int(height*(new_width/width))
    else:
        new_height = size
        new_width = int(width*(new_height/height))

    resized_image = image.resize((new_width, new_height))
    resized_image.save(f'./resized/{file_name}.{extention}')


def run(**kwargs):

    file_list = list(glob.glob(f"./{kwargs['folder_name']}/*.*"))
    file_list = [file_name.split('\\')[-1] for file_name in file_list]

    is_exist_resized = os.path.exists(f"./resized")
    if not is_exist_resized:
        os.makedirs(f"./resized")
    else:
        n_try_to_resize = len(file_list)
        resized_file_list = list(glob.glob(f"./resized/*.*"))
        resized_file_list = [file_name.split('\\')[-1] for file_name in resized_file_list]

        file_list = [file for file in file_list if file not in resized_file_list]
        n_real_resize = len(file_list)

        if n_real_resize <= 0:
            print(f"resizing되지 않은 이미지가 없습니다.")
            return

        if (n_try_to_resize - n_real_resize) >= 1:
            print(f"전체 {n_try_to_resize}개 이미지 중, 이미 resizing된 이미지가 {n_try_to_resize - n_real_resize}개 존재합니다.")
            print(f"{n_real_resize}개 이미지를 resizing합니다.\n")

    for file_extention in file_list:
        file_name, extention = file_extention.split('.')
        image_resizing(kwargs['folder_name'], file_name, extention, kwargs['size'])


def is_debug_mode():
    return sys.gettrace() is not None


if __name__ == '__main__':

    if is_debug_mode():
        sys.argv = ['resizer.py', '--folder_name', 'images', '--size', '500']

    parser = argparse.ArgumentParser(description="스크립트 설명")

    parser.add_argument('--folder_name', type=str, help="이미지 데이터 폴더명")
    parser.add_argument('--size', type=int, help="출력 이미지 사이즈")
    parser.add_argument('--is_width_base', action='store_true', help="가로를 기준으로 설정")

    args = parser.parse_args()

    kwargs = {
    'folder_name' : args.folder_name,
    'size' : args.size,
    'is_width_base' : args.is_width_base
    }

    run(**kwargs)