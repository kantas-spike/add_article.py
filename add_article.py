#!/usr/bin/env python3

import argparse
import os
import re
import sys
import subprocess


PREFIX_SEPARATOR = "-"


def get_content_dir(site_directory, content_dir="content"):
    return expand_path(os.path.join(site_directory, content_dir))


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


def expand_path(path):
    return os.path.abspath(os.path.expanduser(path))


def sanitize_filename(name):
    return re.sub(r"\s+", "-", str(name))


def main():
    args = parse_args()
    content_dir = get_content_dir(args.site_directory)
    target_dir = os.path.join(content_dir, args.subcommand)

    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)

    max_no = get_last_prefix_no(target_dir)

    file_name = sanitize_filename(args.name)
    print(file_name)

    if args.leaf_bundle:
        target_file = os.path.join(
            args.subcommand, f"{max_no + 1:02}{PREFIX_SEPARATOR}{file_name}/index.md"
        )
        leaf_dir = os.path.dirname(target_file)
        if not os.path.isdir(leaf_dir):
            os.mkdir(os.path.join(content_dir, leaf_dir))
    else:
        target_file = os.path.join(
            args.subcommand, f"{max_no + 1:02}{PREFIX_SEPARATOR}{file_name}.md"
        )

    hugo_command = [
        "hugo",
        "new",
        "content",
        target_file,
        "--editor",
        "code",
    ]  # "hugo new '{target_file}' --editor code"
    subprocess.run(hugo_command, shell=False, cwd=expand_path(args.site_directory))


def parse_args():
    DEFAULT_SITE_DIR = "~/blog"
    parser = argparse.ArgumentParser(
        "add_article",
        description=(
            "Hugoのサイトに指定したタイプの記事を追加する。"
            f"デフォルトでは、サイトディレクトリは'{DEFAULT_SITE_DIR}'になります。"
        ),
    )
    parser.add_argument(
        "-l",
        "--leaf-bundle",
        action="store_true",
        help="Leaf Bundle形式で記事を作成する",
    )
    parser.add_argument(
        "-s",
        "--site-directory",
        metavar="SITE_DIR",
        help=f"サイトディレクトリ.(デフォルト値: {DEFAULT_SITE_DIR})",
        default=DEFAULT_SITE_DIR,
    )
    subs = parser.add_subparsers(dest="subcommand")
    articles = subs.add_parser(
        "articles",
        usage="articles ARTICLE_NAME",
        help="see `articles -h`",
        description="Articles用の記事を追加する",
    )
    articles.add_argument("name", type=str, metavar="ARTICLE_NAME", help="記事名")

    til = subs.add_parser(
        "til",
        usage="til ARTICLE_NAME",
        help="see `til -h`",
        description="TIL用の記事を追加する",
    )
    til.add_argument("name", type=str, metavar="ARTICLE_NAME", help="記事名")

    dia = subs.add_parser(
        "dialogues",
        usage="dialogues ARTICLE_NAME",
        help="see `dialogues -h`",
        description="chatGPTとの問答を追加する",
    )
    dia.add_argument("name", type=str, metavar="ARTICLE_NAME", help="記事名")

    args = parser.parse_args()
    if args.subcommand is None:
        print("記事タイプを指定してください\n")
        parser.print_help()
        sys.exit(1)

    if not os.path.exists(expand_path(args.site_directory)):
        print(f"Hugoのサイトディレクトリ({args.site_directory})が存在しません\n")
        parser.print_help()
        sys.exit(1)

    return args


if __name__ == "__main__":
    sys.exit(main())
