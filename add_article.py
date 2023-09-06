#!/usr/bin/env python3

import argparse
import os
import re
import sys


CONTENT_DIR = os.path.abspath("./content")
PREFIX_SEPARATOR = '-'


def get_last_prefix_no(target_dir, prefix_separator=PREFIX_SEPARATOR):
    max_no = 0
    for f in os.listdir(target_dir):
        f_name = os.path.basename(f)
        if result := re.match("([0-9]+)-.*", f_name):
            # print(f_name)
            no = int(result[1])
            if no > max_no:
                max_no = no
    return max_no


parser = argparse.ArgumentParser(description='Hugoのサイトに指定したタイプの記事を追加する\n必ずHugoのサイトディレクトリで実行してください')
parser.add_argument('-l', '--leaf-bundle', action='store_true', help="Leaf Bundle形式で記事を作成する")
subs = parser.add_subparsers(dest='subcommand')
articles = subs.add_parser('articles', usage='articles ARTICLE_NAME', help='see `articles -h`',
                           description='Articles用の記事を追加する')
articles.add_argument('name', type=str, metavar='ARTICLE_NAME', help='記事名')

til = subs.add_parser('til', usage='til ARTICLE_NAME', help='see `til -h`', description='TIL用の記事を追加する')
til.add_argument('name', type=str, metavar='ARTICLE_NAME', help='記事名')

dia = subs.add_parser('dialogues', usage='dialogues ARTICLE_NAME', help='see `dialogues -h`',
                      description='chatGPTとの問答を追加する')
dia.add_argument('name', type=str, metavar='ARTICLE_NAME', help='記事名')

args = parser.parse_args()

if args.subcommand is None:
    print("記事タイプを指定してください\n")
    parser.print_help()
    sys.exit(1)

if not os.path.isdir(CONTENT_DIR):
    print("Hugoのサイトディレクトリで実行してください\n")
    parser.print_help()
    sys.exit(1)

target_dir = os.path.join(CONTENT_DIR, args.subcommand)

if not os.path.isdir(target_dir):
    os.mkdir(target_dir)

max_no = get_last_prefix_no(target_dir)

if args.leaf_bundle:
    target_file = os.path.join(args.subcommand, f"{max_no+1:02}{PREFIX_SEPARATOR}{args.name}/index.md")
    leaf_dir = os.path.dirname(target_file)
    if not os.path.isdir(leaf_dir):
        os.mkdir(os.path.join(CONTENT_DIR, leaf_dir))
else:
    target_file = os.path.join(args.subcommand, f"{max_no+1:02}{PREFIX_SEPARATOR}{args.name}.md")

hugo_command = f"hugo new '{target_file}' --editor code"
# print(hugo_command)
os.system(hugo_command)
