import json, sys
TRANS_DELIM = " // "
# TODO query the Scryfall APIs instead
def write_fnames(fname, sets):
    with open(fname, encoding="utf-8") as oracle_f:
        cards = json.loads(oracle_f.read())
        to_write = set({})
        for obj in cards:
            if obj["set_name"] in sets:
                to_write.add(obj["name"])
        print("Writing %d cards." % len(to_write))
        with open("out.txt", "w", encoding="utf-8") as out:
            for line in to_write:
                if TRANS_DELIM in line:
                    line = line.split(TRANS_DELIM)[0]
                out.write(line + "\n")

if __name__ == "__main__":
    write_fnames(sys.argv[1], sys.argv[2:])