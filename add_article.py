#!/usr/bin/env python3

import argparse
import os
import sys
import glob


CONTENT_DIR = os.path.abspath("./content")
PREFIX_SEPARATOR = '-'

parser = argparse.ArgumentParser(description='Hugoのサイトに指定したタイプの記事を追加する\n必ずHugoのサイトディレクトリで実行してください')
subs = parser.add_subparsers(dest='subcommand')
blog = subs.add_parser('blog', usage='blog ARTICLE_NAME', help='see `blog -h`', description='Blog記事を追加する ')
blog.add_argument('name', type=str, metavar='ARTICLE_NAME', help='記事名')

til = subs.add_parser('til', usage='til ARTICLE_NAME', help='see `til -h`', description='TIL記事を追加する')
til.add_argument('name', type=str, metavar='ARTICLE_NAME', help='記事名')

dia = subs.add_parser('dialogue', usage='dialogue ARTICLE_NAME', help='see `dialogue -h`',
                      description='chatGPTとの問答を追加する')
dia.add_argument('name', type=str, metavar='ARTICLE_NAME', help='記事名')

memo = subs.add_parser('memo', usage='til ARTICLE_NAME', help='see `memo -h`', description='メモ記事を追加する')
memo.add_argument('name', type=str, metavar='ARTICLE_NAME', help='記事名')

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

max_no = 0
for f in glob.glob(os.path.join(target_dir, "**.md")):
    info = os.path.basename(f).split(PREFIX_SEPARATOR, 1)
    print(info)
    if len(info) != 2:
        continue
    try:
        no = int(info[0])
        if no > max_no:
            max_no = no
    except ValueError:
        continue

target_file = os.path.join(args.subcommand, f"{max_no+1:02}{PREFIX_SEPARATOR}{args.name}.md")
hugo_command = f"hugo new '{target_file}' --editor code"
# print(hugo_command)
os.system(hugo_command)
