from Tree import Tree
import sys
import numpy as np
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        raise Exception("No file name given")
        
    if(sys.argv[1] == "-c"):
        text = open(sys.argv[2], "r").read()
        tree = Tree(text = text)
        tree.compress()
        output_file_name = get_file_name()
        np.save(output_file_name, tree.compressed.astype(np.int32))
        swap_extension(output_file_name, type = "compressed")
        print(f"Número de caracteres do texto original: {len(text)}")
        print(f"Número de tokens de compressão {tree.compressed.shape[0]}")
        print(f"Razão entre letras e tokens {(len(text)/tree.compressed.shape[0])}")

    elif(sys.argv[1] == "-x"):
        swap_extension(sys.argv[2], type = "decompressed")
        with open(sys.argv[2].split(".z78")[0] + ".npy", "rb") as f:
            compressed_tree = np.load(f)
        swap_extension(sys.argv[2].split(".z78")[0], type = "compressed")
        tree = Tree(compressed = compressed_tree)
        tree.decompress()
        output_file_name = get_file_name(type = "decompressed")
        open(output_file_name, "w").write(tree.text[1:-1])

    else:
        raise("Os parâmetros de entrada não são válidos")

def get_file_name(type = "compressed"):
    if len(sys.argv) == 5:
        return sys.argv[4]
    else:
        if type == "compressed":
            return sys.argv[2].split(".txt")[0] + "_compressed"
        else:
            output_file_name = sys.argv[2].split(".z78")[0]
            return output_file_name.split("_compressed")[0] + ".txt"

def swap_extension(file_name, type = "compressed"):
    if type == "compressed":
        p = Path(file_name + ".npy")
        p.rename(p.with_suffix('.z78'))
    else:
        p = Path(file_name)
        p.rename(p.with_suffix('.npy'))

main()