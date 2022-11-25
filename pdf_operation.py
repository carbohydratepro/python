# 即席のものなのでデバッグしてません
from PyPDF2 import PdfFileReader, PdfFileWriter


def page_delete(file_name, page_nums): # 第二引数以降は削除したいページ番号
    with open(file_name, 'rb') as input_file:
        reader = PdfFileReader(input_file)
        writer = PdfFileWriter()

        for i in range(reader.numPages):
            if str(i+1) not in page_nums:
                writer.addPage(reader.getPage(i))

        with open(file_name.split('.')[0] + '_new.' + file_name.split('.')[-1], 'wb') as output_file:
            writer.write(output_file)

def page_combine(first_file_name, second_file_name):
    writer = PdfFileWriter()
    with open(first_file_name, 'rb') as first_file:
        reader = PdfFileReader(first_file)
        for i in range(reader.numPages):
            writer.addPage(reader.getPage(i))

        with open(second_file_name, 'rb') as second_file:
            reader = PdfFileReader(second_file)
            for i in range(reader.numPages):
                writer.addPage(reader.getPage(i))

            with open('combined_'+ first_file_name.split('.')[0] + '_and_' + second_file_name.split('.')[0] + '.pdf', 'wb') as output_file:
                writer.write(output_file)

def explain(): # 一度のみ実行される関数
    global explain
    def explain():
        return False

    print('-----command-------------------------------\n',
          ' delete ファイル名.pdf 削除したいページ番号...\n',
          ' combine 先頭ファイル名.pdf ファイル名.pdf\n',
          '-------------------------------------------\n')
    return True

def main():
    explain()

    command = input('command : ').split(' ')
    if command[0] == 'delete':
        page_delete(command[1], command[2])
    elif command[0] == 'combine':
        page_combine(command[1], command[2])
    else:
        main()


if __name__ == "__main__":
    main()