# add_article.py

hugoで管理しているサイトに記事を追加するためのユーティリティスクリプトです

使い方は以下になります

まず、ターミナルを開き、hugoのサイトのディレクトリに移動します

そして、TILに記事を追加する場合、以下を実行します

~~~shell
~/bin/add_article.py til ARTICLE_NAME
~~~

Notesに記事を追加する場合は以下を実行します

~~~shell
~/bin/add_article.py notes ARTICLE_NAME
~~~

問答(dialogues)を追加する場合は以下を実行します

~~~shell
~/bin/add_article.py dialogues ARTICLE_NAME
~~~

連番をプレフィックスにつけたファイルが作成し、VsCodeでオープンします

`ARTICLE_NAME.md`のような単一のファイルではなく、
[Leaf Bundle](https://gohugo.io/content-management/page-bundles/)形式(`ARTICLE_NAME/index.md`)で記事を作成する場合は、
以下のように`-l`オプションを付けてください

~~~shell
~/bin/add_article.py -l notes ARTICLE_NAME
~~~

## インストール方法

以下を実行すると、`~/bin`に`add_article.py`をコピーし、実行権限を付与します。

~~~shell
make
~~~

## ヘルプ

~~~shell
~/bin/add_article.py -h
usage: add_article.py [-h] [-l] {articles,til,dialogues,notes} ...

Hugoのサイトに指定したタイプの記事を追加する 必ずHugoのサイトディレクトリで実行してください

positional arguments:
  {articles,til,dialogues,notes}
    articles            see `articles -h`
    til                 see `til -h`
    dialogues           see `dialogues -h`
    notes               see `notes -h`

options:
  -h, --help            show this help message and exit
  -l, --leaf-bundle     Leaf Bundle形式で記事を作成する
~~~
