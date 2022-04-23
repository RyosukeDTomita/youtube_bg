# 作業フローのメモ

- プロジェクトを立ち上げる。
- アプリを作る。
- プロジェクトのディレクトリに入り，settings.pyに作成したアプリケーションを追加する。
- プロジェクト側のurls.pyにアプリのパスを通す。

```python3
アプリ名.urls
```
- アプリ側のurls.pyに函数を追加する。これにviews.pyに追加する函数を追加する。
- views.pyに函数を追加する。
- プロジェクトのsettings.pyに入り，templatesのパスを通す。
- プロジェクトやアプリの格納されているディレクトリと同じ場所にtemplates/を作成
- urls.pyにClass PlayMusicを作成し，メソッドを定義する。[Viewを継承したクラスのメソッドの名前付けルール](https://zenn.dev/ikemo/articles/django-http-method-names)

## やること


## 気づいたこと
- Viewを継承したクラスに対してas.view()を実行するとすべてのメソッドが実行される? --> ブラウザの再読込ではGETメソッドが実行されない。GETは検索欄にurlを入れてアクセスした時に実行されると思われる。
