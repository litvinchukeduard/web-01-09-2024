'''
Потрібно взяти папку з зображеннями та накласти чорно-білий фільтр 
'''
from threading import Thread
import shutil
from multiprocessing import Pool, cpu_count

source_image = 'source.png'
target_dir = 'target_images'
images_dir = 'source_images'

from PIL import Image


def transfer_photo_to_bw(file_path: str):
    with Image.open(file_path) as file:
        black_and_white_image = file.convert('L')
        black_and_white_image.save(file_path)

def copy_file(i: int):
    # with open(source_image, 'r', encoding='utf-8') as source:
    #     with open(f'{images_dir}/image-{i}.png', 'w', encoding='utf-8') as destination:
    #         destination.write(source.read())
    shutil.copy(source_image, f'{images_dir}/image-{i}.png')


def create_image_copies(n: int):
    threads = []
    for i in range(n):
        thread = Thread(target=copy_file, args=(i,))
        thread.start()

    for thread in threads:
        thread.join()

# create_image_copies(1000)

# print('folder/file.png'.split('/'))
# transfer_photo_to_bw('source_images/image-1.png')
with Pool(cpu_count()) as pool:
    file_names = []
    for i in range(1000):
        file_names.append(f'{images_dir}/image-{i}.png')
    # print(file_names)
    pool.map(transfer_photo_to_bw, file_names)
    # pool.map()
