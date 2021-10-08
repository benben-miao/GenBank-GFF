# Author: benben-miao
# Email: benben.miao@outlook.com
# Github: https://github.com/benben-miao

from BCBio import GFF  
from Bio import SeqIO
import gzip

def gbff2gff(input_filename, output_filename):
    input_filename = input_filename
    output_filename = output_filename
    try:
        input_handle = open(input_filename, "r")
        output_handle = open(output_filename, "w")
    except FileNotFoundError as e:
        print(f"Errors: {str(e)}")
        print(f"File Not Found: [{input_filename}]")
        return

    try:
        GFF.write(SeqIO.parse(input_handle, "genbank"), output_handle)
    except Exception as e:
        print("Errors:", str(e))
        input_handle.close()
        output_handle.close()

def uncompress_gz(src_filename):
    print("Uncompressing...")
    try:
        dest_name = src_filename.replace(".gz", "")
        gz_file = gzip.GzipFile(src_filename)
        with open(dest_name, "wb+") as f:
            f.write(gz_file.read())
        gz_file.close()
        print("Uncompressed!")
        return dest_name
    except Exception as e:
        print(f"Errors: {str(e)}")

if __name__ == '__main__':
    _input_filename = input("Please input GenBank format file path/filename(.gbff):\n")
    _output_filename = input("Please input GFF format file path/filename(.gff/.gff3):\n")

    if not _output_filename:
        _output_filename = _input_filename.replace("gbff", "gff")
    confirm = input(f"Confirm Information:\nInput GenBank File:{_input_filename};\nOutput GFF File:{_output_filename}\nPlease ENTER to start conversion.\n")

    if not _input_filename.endswith(".gbff"):
        if _input_filename.endswith(".gz"):
            uncompress_flag = input("Need to uncompress the .gz file! Please input 'yes' to uncompress.\n")
            if uncompress_flag == "yes":
                uncompress_gz(_input_filename)
                _input_filename = _input_filename.replace('.gz','')
            else:
                exit()
        else:
            print(f"Please confirm your input file:\n{_input_filename}")
    else:
        print(f"Please confirm your input file:\n{_input_filename}")

    print("Converting...")
    gbff2gff(_input_filename, _output_filename)
    print("Converted!")
