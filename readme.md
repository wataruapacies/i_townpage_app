## タウンページのスクレイピング

[WEBアプリリンク](http://52.198.22.89/)
<br>
* [タウンページ](https://itp.ne.jp/)で任意の検索結果をスクレイピングし，その結果をcsvファイルとしてダウンロードできます．
* AWSの無料枠のEC2にデプロイしました
* スクレイピングしたい条件を入力するとバックエンドでスクレイピングが開始されます．
* 現在は，スクレイピングプログラムはcronで15分に1回の定期実行と設定しています．これは同時に複数のスクレイピングを実行してしまってEC2が落ちることを防ぐためです．（無料枠のため，Dockerが落ちやすい）
* 新規ユーザー登録機能は公開していません．
* こちらで登録したユーザーでしかログインできません

### ログイン情報
**採用担当の方がログインするために作成したアカウントです．**
<dl>
  <dt>E-Mail Address</dt>
  <dd>test@recruit.com</dd>
  <dt>Password</dt>
  <dd>test12345</dd>
</dl> 
<br>
