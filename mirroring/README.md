# ミラーリング自動取得

`screen/afk-screen`（poke-assist の pa-screen を流用し、tap/swipe を追加したもの）。ビルド: `screen/build.sh`

| コマンド | 用途 |
|---|---|
| `find` / `capture out.png` | 窓の検出・撮影 |
| `ocr png [x,y,w,h]` | 端末内OCR（Vision・日英）。**画像をLLMに送らずに文字を取る** |
| `tap x,y` / `swipe x1,y1 x2,y2 [ms]` | 窓内の割合座標（0〜1）で操作 |
| `hash png` | 画面遷移の検知（スクロール終端の判定など） |
| `crop` / `sig` | 調整用・アイコン識別 |

## トークン節約の方針
- 基本は capture → ocr（JSON）で取得。画像そのものを Claude が見るのは、座標合わせ（キャリブレーション）とOCRが失敗したときだけ。
- 画面ごとの座標は `layouts.json`（今後作成）に保存して、以降は使い回す。
- 許可: 画面収録（capture）、アクセシビリティ（tap/swipe）。それぞれ実行元のターミナル/VSCode に付与する。
