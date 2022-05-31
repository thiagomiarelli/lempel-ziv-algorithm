from Tree import Tree
import sys

def main():
    if len(sys.argv) < 2:
        raise Exception("No file name given")
        
    if(sys.argv[1] == "-c"):
        text = open(sys.argv[2], "r").read()
        tree = Tree(text = text)
        tree.compress()
        output_file_name = sys.argv[2].split(".txt")[0] + ".z78"
        open(output_file_name, "w").write(tree.compressed)
    elif(sys.argv[1] == "-x"):
        compressed = open(sys.argv[2], "r").read()
        tree = Tree(compressed = compressed)
        tree.decompress()
        output_file_name = sys.argv[2].split(".z78")[0] + ".txt"
        open(output_file_name, "w").write(tree.text)
        print(len(tree.text))
    else:
        raise("Os parâmetros de entrada não são válidos")

main()