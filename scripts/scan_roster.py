"""英雄詳細画面で「読み取り → 右矢印」を繰り返し、手持ちの名前・ランク・専用装備を集める（閲覧のみ）。

使い方: 詳細画面を開いた状態で  python3 scripts/scan_roster.py [最大件数]
出力: data/my_account/roster_scan.csv。1件ごとに追記し、同じ英雄（素材用の重複）は書かない。
1周して最初の英雄に戻ったら止まる。途中で止めても読んだ分は残る。
"""
import csv, json, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIN = str(ROOT / "mirroring/screen/afk-screen")
SHOT = str(ROOT / "mirroring/captures/scan.png")
OUT = ROOT / "data/my_account/roster_scan.csv"

# 割合座標（左上原点）。iPhone ミラーリング窓 406x890 で調整
NEXT = "0.88,0.555"
# ランク・二つ名・名前・CV の縦並び。レア度で星の段の有無が変わり位置がずれるので、CV 行を目印に読む
R_HEAD = "0.20,0.16,0.60,0.15"
R_SI = "0.03,0.47,0.20,0.06"


def run(*a):
    return json.loads(subprocess.check_output([BIN, *a], text=True))


def boxes(region):
    return sorted((b for b in run("ocr", SHOT, region) if b["text"].strip()), key=lambda b: (b["y"], b["x"]))


def text(region):
    return [b["text"].strip() for b in boxes(region)]


def read():
    run("capture", SHOT)
    head = [b for b in boxes(R_HEAD) if "★" not in b["text"]]
    cv = next((i for i, b in enumerate(head) if b["text"].startswith("CV")), len(head))
    above = head[:cv]
    name = above[-1] if above else None
    si = "".join(text(R_SI))
    return {
        "rank": above[0]["text"] if len(above) >= 3 else "",
        "title": above[-2]["text"] if len(above) >= 2 else "",
        "jp_name": name["text"] if name else "",
        "conf": round(name["conf"], 2) if name else 0,
        "si": si.replace("+", "") if si.startswith("+") else "",
    }


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 600
    fields = ["rank", "title", "jp_name", "conf", "si"]
    seen = set()
    if OUT.exists():
        seen = {(r["title"], r["jp_name"]) for r in csv.DictReader(OUT.open())}
    else:
        with OUT.open("w", newline="") as f:
            csv.DictWriter(f, fieldnames=fields).writeheader()
    first, added = None, 0
    for i in range(limit):
        r = read()
        key = (r["title"], r["jp_name"])
        if first is None:
            first = key
        elif key == first:
            break
        print(i, r, flush=True)
        if key not in seen:
            seen.add(key)
            added += 1
            with OUT.open("a", newline="") as f:
                csv.DictWriter(f, fieldnames=fields).writerow(r)
        if r["conf"] < 0.5:  # 読み取りが怪しい名前は画像を残し、後でまとめて確認する
            run("crop", SHOT, R_HEAD, str(ROOT / f"mirroring/captures/lowconf_{i:03d}.png"))
        before = run("hash", SHOT)["hash"]
        run("tap", NEXT)
        # 画面が切り替わり、アニメーションが落ち着くまで待つ
        for _ in range(20):
            time.sleep(0.4)
            run("capture", SHOT)
            if run("hash", SHOT)["hash"] != before:
                break
        time.sleep(0.6)
    print(f"新規 {added} 件 → {OUT}")


if __name__ == "__main__":
    main()
