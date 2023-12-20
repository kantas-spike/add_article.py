# add_article.py

hugoで管理しているサイトに記事を追加するためのユーティリティスクリプトです

使い方は以下になります

TILに記事を追加する場合、以下を実行します

```shell
~/bin/add_article til ARTICLE_NAME
```

問答(dialogues)を追加する場合は以下を実行します

```shell
~/bin/add_article dialogues ARTICLE_NAME
```

連番をプレフィックスにつけたファイルが作成し、VsCodeでオープンします

`ARTICLE_NAME.md`のような単一のファイルではなく、
[Leaf Bundle](https://gohugo.io/content-management/page-bundles/)形式(`ARTICLE_NAME/index.md`)で記事を作成する場合は、
以下のように`-l`オプションを付けてください

```shell
~/bin/add_article -l articles ARTICLE_NAME
```

## インストール方法

以下を実行すると、`add_article.py`を`~/bin/add_article`をコピーし、実行権限を付与します。

```shell
make install
```

## ヘルプ

```shell
~/bin/add_article -h
usage: add_article [-h] [-l] [-s SITE_DIR] {articles,til,dialogues} ...

Hugoのサイトに指定したタイプの記事を追加する デフォルトでは、サイトディレクトリは~/blogになります。

positional arguments:
  {articles,til,dialogues}
    articles            see `articles -h`
    til                 see `til -h`
    dialogues           see `dialogues -h`

options:
  -h, --help            show this help message and exit
  -l, --leaf-bundle     Leaf Bundle形式で記事を作成する
  -s SITE_DIR, --site-directory SITE_DIR
                        サイトディレクトリ.(デフォルト値: ~/blog)
```
