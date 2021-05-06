from utils import fasta, index, thumbs
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) < 2:
        print("Missing arguments: index/thumbs/fasta/all")
        exit(1)

    if "all" in argv or "index" in argv:
        index.build_dramp_to_pep_index()
        index.build_pep_to_dramp_index()
        index.build_pep_to_activity_and_name_index()

    if "all" in argv or "thumbs" in argv:
        thumbs.generate_thumbnails()

    if "all" in argv or "fasta" in argv:
        fasta.generate_fasta_files()