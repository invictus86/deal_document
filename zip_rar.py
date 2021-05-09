import tarfile
from unrar import rarfile
import zipfile
# import rarfile
import os


def uncompress(src_file, dest_dir):
    """解压各种类型的压缩包

    :param src_file: 你要解压的压缩包文件
    :type src_file: file
    :param dest_dir: 你要解压到的目标路径
    :type dest_dir: str
    """
    file_type = src_file[-4:]
    # file_name, file_type = os.path.splitext(".")

    try:
        if file_type == '.zip':
            # 需要安装zip包：pip install zipp
            zip_file = zipfile.ZipFile(src_file)
            for names in zip_file.namelist():
                zip_file.extract(names, dest_dir)
            zip_file.close()

        elif file_type == '.rar':
            # 需要安装rar包：pip install rarfile
            rar = rarfile.RarFile(src_file)
            os.chdir(dest_dir)
            rar.extractall()
            rar.close()

        else:
            # file_type == '.tgz' or file_type == '.tar' or file_type == '.gz'
            # Python自带tarfile模块
            tar = tarfile.open(fileobj=src_file)
            for name in tar.getnames():
                tar.extract(name, dest_dir)
            tar.close()

    except Exception as ex:
        return False
    return True


if __name__ == '__main__':
    # uncompress(r"F:\code\get_baiduwenku\ppt_doc\1-1F10Z93532\1-1F10Z93532.rar", r"F:\code\get_baiduwenku\out_ppt")
    uncompress(r"F:\code\get_baiduwenku\ppt_doc\1-1F50Q45137\1-1F50Q45137.zip", r"F:\code\get_baiduwenku\out_ppt1")
