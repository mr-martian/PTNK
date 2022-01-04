#!/usr/bin/env python3

import yaml

def extract_lang(blob, lang):
    if lang not in blob:
        return []
    ret = []
    dct = {}
    n = 0
    for k in blob[lang]:
        n1, n2 = blob[lang][k].split('-')
        n = max(n, int(n2))
        for i in range(int(n1), int(n2)+1):
            dct[i] = k
    for i in range(1, n+1):
        ret.append(dct.get(i, ''))
    return ret

def process_block(blob, langs):
    ret = []
    idents = [extract_lang(blob, l) for l in langs]
    # TODO: check that they're the same length
    for tup in zip(*idents):
        ls = list(tup)
        real = [s for s in ls if s]
        if len(real) < 2 and len(real) != len(langs):
            continue
        ln = '\t'.join(ls)
        if ln not in ret:
            ret.append(ln)
    return '\n'.join(ret)

def process_file(fname, langs):
    with open(fname) as fin:
        blob = yaml.safe_load(fin)
        blocks = [process_block(b, langs) for b in blob]
        return '\n'.join(blocks) + '\n'

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('Convert YAML source files to TSV.')
    parser.add_argument('infile', action='store')
    parser.add_argument('outfile', action='store')
    parser.add_argument('langs', nargs='+')
    args = parser.parse_args()
    print(args)

    with open(args.outfile, 'w') as fout:
        fout.write(process_file(args.infile, args.langs))
