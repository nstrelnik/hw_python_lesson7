import os
import shutil
import pytest
import zipfile
from script_os import ZIP_PATH, TMP_PATH


@pytest.fixture(scope='function', autouse=True)
def create_archive():
    if not os.path.exists(ZIP_PATH): #проверка существования папки
        os.mkdir(ZIP_PATH) #создание папки если ее нет
    with zipfile.ZipFile(ZIP_PATH+'/zip_resources.zip','w') as zf: #создание архива
        for file in os.listdir(TMP_PATH): #добавление файлов в архив (цикл)
            add_file = os.path.join(TMP_PATH, file) #склейка пути к файлам которые добавляются в архив
            zf.write(add_file, os.path.basename(add_file)) #добавление файлов в архив

    yield

    shutil.rmtree(ZIP_PATH)