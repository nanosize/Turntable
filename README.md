# turntable
このアドオンをBlenderにインストールおよび有効化すると、3Dビューポートの右側に「Turntable」というタブが表示され、ターンテーブルアニメーションを作成するためのUIが提供されます。UIの「Create」ボタンをクリックすると、ターンテーブルアニメーションが設定され、カメラが円の周りを回転するアニメーションが作成されます。

このアドオンを使用する際には、アドオンが提供するUIを介してターンテーブルアニメーションのパラメータを調整できます。また、コード内で定義されている各オペレーターとプロパティにアクセスし、カスタマイズすることも可能です。
### 使い方:

1. **プラグインのインストール:**
   - プラグインのコードをテキストファイルとして保存します。
   - Blenderを起動し、メニューから「編集 (Edit)」 > 「設定 (Preferences)」を選択します。
   - 「アドオン (Add-ons)」タブに移動し、「インストール」ボタンをクリックして保存したプラグインのファイルを選択します。
   - プラグインがリストに表示されたら、チェックボックスをオンにして有効化します.

2. **プラグインの使用:**
   - Blenderの3Dビューポートで、右側に「Turntable」というタブが表示されます。
   - 「Turntable」タブをクリックして、ターンテーブルアニメーションの設定画面にアクセスします.

3. **アニメーションの設定:**
   - 「Frames」フィールドに、アニメーションのフレーム数を入力します。これはカメラが1回の往復にかけるフレーム数です.
   - 「Create Camera」ボタンをクリックして、ターンテーブルアニメーションを作成します。これにより、円形のパス上を移動するカメラが作成されます.

4. **アニメーションの再生:**
   - 作成されたアニメーションを再生するには、Blenderのタイムラインを操作して再生ボタンをクリックします.

### 注意点:

- このプラグインはベータバージョンであり、安定性が保証されていない場合があります。重要なプロジェクトで使用する前にバックアップを作成し、注意して使用してください.

- v0.0.0の問題としてしてフレーム数を変更したい時には一度オブジェクトを削除する必要があります。今後改善されます。多分。




# Warning
このaddonはBETA版です。メインの環境には入れないことをお勧めします。
[GitHubのリンクはこちら](https://github.com/nanosize/turntable/tree/main)です。何か問題がある場合は、ここの[Issue](https://github.com/nanosize/turntable/issues)もしくは[Twitter](https://twitter.com/nao_3dcg)（@nao_3dcg）までお願いします。


# 免責事項
利用者が本アドオンを使用することによって生じるいかなる損害に対して一切責任を負ませんのでご了承ください。

