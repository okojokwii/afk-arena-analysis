# AFK Arena 無課金育成・編成分析プロジェクト

## 目的
AFKアリーナ（スマホ）を**無課金**で効率育成し、以下のモードで高順位を取るための最適編成を常に更新する。
- トレジャーハント（TS / Treasure Scramble）
- 捻じられた夢境（Twisted Realm）
- 呪われた夢境（Cursed Realm）
- 悪夢の回廊（英語名は要確認。Dream Realm 等との対応を検証すること）

最終アウトプット:
1. 環境の強編成（モード別・ボス別）
2. ユーザーの手持ちで**今組める最適解**
3. 目指すべき**理想編成**
4. 育成優先順位の提案 — **リソース温存（次の環境キャラ待ち）も正式な選択肢として必ず比較する**。中途半端な投資は避ける。

## 最重要ルール: 名称の一致
- 情報源は英語（Reddit r/afkarena、Discord系まとめ、海外Wiki/Tier list）。日本語サイトは古いため原則使わない。
- 英語名 ↔ ゲーム内日本語表記の不一致で編成が組めない事故が過去多発。**提案に出すキャラ名・用語は必ず `data/glossary/` で verified=true のものを使う**。未検証なら英語名併記＋「未検証」と明示する。
- 日本語名の検証は、ユーザーのiPhoneミラーリング画面（スクショ）から自動で取得する。ユーザーの手入力は極力求めない。

## ディレクトリ
- `data/glossary/hero_names.csv` — 英日キャラ名対応表（faction, class, role, aliases, verified, source）
- `data/glossary/terms.csv` — モード・装備・ステータス等の用語対応表
- `data/heroes/` — キャラ詳細（スキル・シナジー）。1キャラ1ファイル `<en_name_snake>.md`
- `data/meta/` — モード別の環境編成。`<mode>_<YYYY-MM-DD>.md`（日付で版管理、上書きしない）
- `data/my_account/roster.csv` — ユーザーの育成状況。`screenshots/` は git 管理外
- `research/raw/` — 収集した生情報（URL・投稿日・要約）。`research/summaries/` — 整理済み要約
- `analysis/teams/`, `analysis/recommendations/` — 分析結果・育成提案（日付付き）
- `scripts/` — 集計・突合スクリプト
- `mirroring/` — ミラーリング自動操作関連

## 情報収集の作法（サーチ担当セッション向け）
- 各情報に **出典URL・投稿日・ゲームバージョン/シーズン** を記録。古い情報（目安3ヶ月以上前）はフラグを立てる。
- 一次情報（Redditの具体的なダメージ報告・編成スクショ）を tier list より優先。
- 無課金で入手困難なキャラ（課金限定・入手経路が限定的）はその旨を記録。
- 推測と事実を区別する。

## 作業方針
- データはCSV/Markdownで人間にもAIにも読める形を保つ。
- コミットはユーザーの依頼時のみ。リモート: https://github.com/okojokwii/afk-arena-analysis
