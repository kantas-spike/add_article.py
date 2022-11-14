# add_article.py

hugoで管理しているサイトに記事を追加するためのユーティリティスクリプトです

使い方は以下になります

まず、ターミナルを開き、hugoのサイトのディレクトリに移動します

そして、TILに記事を追加する場合、以下を実行します

~~~shell
~/bin/add_article.py til ARTICLE_NAME
~~~

BLOGに記事を追加する場合は以下を実行します

~~~shell
~/bin/add_article.py blog ARTICLE_NAME
~~~

連番をプレフィックスにつけたファイルが作成し、VsCodeでオープンします

## インストール方法

以下を実行すると、`~/bin`に`add_article.py`をコピーし、実行権限を付与します。

~~~shell
make
~~~
