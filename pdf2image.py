import os
import sys
from PythonMagick import Image
from pyPdf import PdfFileWriter, PdfFileReader

def main():
    # os.environ["MAGICK_HOME"] = r"path_to_ImageMagick"

    if len(sys.argv) == 1:
        dirpath = '.'
    else:
        dirpath = sys.argv[1]

    temp_dir = os.path.join(dirpath, '.temp')
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    for file_name in os.listdir(dirpath):
        if not os.path.isfile(file_name) or not file_name.endswith('.pdf'):
            continue
        print('Converting file {} ...'.format(file_name))
        in_path = os.path.join(dirpath, file_name)
        with open(in_path, 'rb') as handle:
            inputpdf = PdfFileReader(handle)
            for i in xrange(inputpdf.numPages):
                outputpdf = PdfFileWriter()
                outputpdf.addPage(inputpdf.getPage(i))
                new_file_name = file_name.replace('.pdf', '') + '_{}.pdf'.format(i)
                new_in_path = os.path.join(temp_dir, new_file_name)
                with open(new_in_path, 'wb') as handle:
                    outputpdf.write(handle)

                output_file_name = new_file_name.replace('.pdf', '.jpeg')
                output_path = os.path.join(dirpath, output_file_name)
                p = Image()
                p.density('1080')
                p.read(os.path.abspath(new_in_path))
                p.write(os.path.abspath(output_path))
                os.remove(new_in_path)
        os.rmdir(temp_dir)


if __name__ == '__main__':
    main()