# -*- coding: utf-8 -*-
"""把 data.json（机器抓的元数据）+ annotations（人工标注）渲染成中英两版页面。

用法：
    python scripts/build.py                    # 生成 index.html 与 index-en.html
    python scripts/build.py --lang en          # 只生成英文版
    python scripts/build.py --check            # 只校验，不写文件
    python scripts/build.py --check-generated  # 校验并检查产物是否最新

规则：
- 每个仓库都必须在 annotations.json 里有标注，否则报错退出（宁可不生成，也不生成半张卡）。
- 英文标注（annotations.en.json）只需覆盖 pitch / aud / note，其余字段沿用中文标注；
  少一条也报错，避免英文版出现中英混排。
- data.json 里有、annotations.json 里没有的仓库 → 报错；反之 → 报错。
- 组内按星数降序；赛道顺序以 tracks.json / tracks.en.json 为准。
"""
import base64
import datetime
import html
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_FILE = ROOT / "scripts/snapshot.json"
QR_PNG = ROOT / "scripts/partials/wechat-qr.png"
DIFF_CODE = {"易": "easy", "中": "medium", "难": "hard"}
DIFF_N = {"易": 1, "中": 2, "难": 3}


def wechat_qr_uri() -> str:
    """二维码以 data URI 内嵌，页面仍是单文件（断网、双击本地打开都能用）。

    源图是 scripts/partials/wechat-qr.png，改二维码只需替换这个文件后重新 build。
    """
    if not QR_PNG.exists():
        sys.exit(f"缺少 {QR_PNG.relative_to(ROOT)}（页脚微信二维码）")
    raw = base64.b64encode(QR_PNG.read_bytes()).decode("ascii")
    return "data:image/png;base64," + raw

LANG_COLOR = {
    "Python": "#3572A5", "TypeScript": "#3178c6", "JavaScript": "#f1e05a",
    "Rust": "#dea584", "Go": "#00ADD8", "C#": "#68217a",
    "Jupyter Notebook": "#DA5B0B", "Shell": "#89e051", "MDX": "#fcb32c", "-": "#94a3b8",
}
DOTS = {
    1: '<span class="dots"><i class="dot on"></i><i class="dot "></i><i class="dot "></i></span>',
    2: '<span class="dots"><i class="dot on"></i><i class="dot on"></i><i class="dot "></i></span>',
    3: '<span class="dots"><i class="dot on"></i><i class="dot on"></i><i class="dot on"></i></span>',
}


def get_snapshot_date():
    """快照日期由 fetch.py 写入；测试时可用 SNAPSHOT_DATE 环境变量覆盖。"""
    raw = os.environ.get("SNAPSHOT_DATE")
    if not raw:
        raw = json.loads(SNAPSHOT_FILE.read_text(encoding="utf-8"))["date"]
    return datetime.date.fromisoformat(raw)


SNAP_DATE = get_snapshot_date()


def wan(n, style):
    """大数字展示：中文折「万」，英文用 k / M。"""
    if style == "zh":
        if n >= 10000:
            return f"{n / 10000:.1f}".rstrip("0").rstrip(".") + "万"
        return f"{n:,}"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.2f}".rstrip("0").rstrip(".") + "M"
    if n >= 1000:
        return f"{n / 1000:.1f}".rstrip("0").rstrip(".") + "k"
    return f"{n:,}"


def status(meta, T):
    """归档优先级高于提交日期：刚归档的仓库也可能有很新的最后一次提交。"""
    if meta.get("archived"):
        return T["status"]["archived"], "s-off"
    days = (SNAP_DATE - datetime.date.fromisoformat(meta["pushed_at"])).days
    if days <= 45:
        return T["status"]["active"], "s-on"
    if days <= 210:
        return T["status"]["mid"], "s-mid"
    return T["status"]["off"], "s-off"


def esc(value):
    """标注是人工写的自由文本，进 HTML 文本和属性前都必须转义。"""
    return html.escape(str(value), quote=True)


def license_label(value, T):
    if value == "NOASSERTION":
        return T["lic"]["unknown"], T["lic"]["unknownTip"]
    if value == "-":
        return T["lic"]["none"], T["lic"]["noneTip"]
    return value, ""


def card(meta, ann, T, style):
    fn = meta["full_name"]
    owner, _, name = fn.partition("/")
    lang = meta["lang"]
    diff = ann["diff"]
    st, cls = status(meta, T)
    topics = " ".join(meta.get("topics") or [])
    # 搜索用的可见文案；topics 单独放 data-topics，避免同一个词存两份
    data_name = " ".join(x for x in (fn, ann["pitch"], ann["aud"], ann["note"]) if x).lower()
    color = LANG_COLOR.get(lang, "#94a3b8")
    act = 1 if st == T["status"]["active"] else 0
    lic, lic_title = license_label(ann["lic"], T)
    lic_title_attr = f' title="{esc(lic_title)}"' if lic_title else ""
    return f"""    <article class="card" data-cat="{esc(ann['cat'])}" data-lang="{esc(lang)}"
             data-name="{esc(data_name)}"
             data-diff="{DIFF_CODE[diff]}" data-act="{act}" data-topics="{esc(topics)}"
             data-stars="{meta['stars']}" data-upd="{esc(meta['pushed_at'])}">
      <div class="card-top">
        <a class="repo" href="{esc(meta['url'])}" target="_blank" rel="noopener">
          <span class="owner">{esc(owner)}/</span><span class="name">{esc(name)}</span>
        </a>
        <span class="stars" title="{meta['stars']:,} {esc(T['card']['starsTitle'])}">★ {wan(meta['stars'], style)}</span>
      </div>
      <h3 class="pitch">{esc(ann['pitch'])}</h3>
      <p class="note">{esc(ann['note'])}</p>
      <div class="fit"><span class="fitk">{esc(T['card']['fit'])}</span><span class="fitv">{esc(ann['aud'])}</span></div>
      <div class="topics"><span>⑂ {esc(T['card']['fork'])} {wan(meta['forks'], style)}</span><span>{esc(T['card']['since'])} {esc(meta['created_at'])}</span></div>
      <div class="card-foot">
        <span class="meta-item lang"><i class="ldot" style="background:{color}"></i>{esc(lang)}</span>
        <span class="meta-item"{lic_title_attr}>{esc(lic)}</span>
        <span class="meta-item diff">{esc(T['card']['diff'])} <b>{esc(T['diff'][DIFF_CODE[diff]]['label'])}</b>{DOTS[DIFF_N[diff]]}</span>
        <span class="meta-item upd"><span class="s {cls}">{st}</span>{esc(meta['pushed_at'])}</span>
      </div>
    </article>"""


def load_annotations(lang, meta_keys):
    """英文版只读三个文本字段，其余沿用中文标注。"""
    base = json.loads((ROOT / "scripts/annotations.json").read_text(encoding="utf-8"))
    if lang == "zh":
        return base
    overlay = json.loads((ROOT / "scripts/annotations.en.json").read_text(encoding="utf-8"))
    problems = []
    for key in meta_keys:
        en = overlay.get(key)
        if not en:
            problems.append(f"缺少英文标注：{base[key]['name']}（请补到 scripts/annotations.en.json）")
            continue
        for field in ("pitch", "aud", "note"):
            if not isinstance(en.get(field), str) or not en.get(field):
                problems.append(f"英文标注字段缺失：{key} → {field}")
    for key in overlay:
        if key not in base:
            problems.append(f"英文标注找不到仓库：{key}")
    if problems:
        print("\n".join(problems))
        sys.exit(f"\n{len(problems)} 处英文标注问题，未生成页面。")
    return {
        key: {**base[key], "pitch": overlay[key]["pitch"], "aud": overlay[key]["aud"], "note": overlay[key]["note"]}
        for key in base
    }


def load_tracks(lang):
    name = "scripts/tracks.json" if lang == "zh" else "scripts/tracks.en.json"
    tracks = json.loads((ROOT / name).read_text(encoding="utf-8"))
    zh = json.loads((ROOT / "scripts/tracks.json").read_text(encoding="utf-8"))
    if [t["cat"] for t in tracks] != [t["cat"] for t in zh]:
        sys.exit(f"{name} 的赛道顺序或 id 与 scripts/tracks.json 不一致。")
    return tracks


def build(lang, i18n, write=True):
    T = i18n[lang]
    style = T["numStyle"]
    tpl_name = "scripts/template.html" if lang == "zh" else "scripts/template.en.html"
    out_name = "index.html" if lang == "zh" else "index-en.html"

    tracks = load_tracks(lang)
    data = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))

    problems = []
    meta = {}
    for item in data:
        fn = item.get("full_name", "")
        key = fn.lower()
        if not fn:
            problems.append("data.json 里有缺少 full_name 的记录")
        elif key in meta:
            problems.append(f"仓库重复：{fn}（与 {meta[key]['full_name']} 仅大小写不同或完全重复）")
        else:
            meta[key] = item
        try:
            datetime.date.fromisoformat(item.get("pushed_at", ""))
        except (ValueError, TypeError):
            problems.append(f"最后提交日期无效：{fn or '(未命名)'} → {item.get('pushed_at')!r}")

    track_names = [t.get("cat", "") for t in tracks]
    if len(track_names) != len(set(track_names)):
        problems.append("tracks 文件里有重复的赛道 cat")
    valid_cats = set(track_names)
    anns_zh = json.loads((ROOT / "scripts/annotations.json").read_text(encoding="utf-8"))
    for key in meta:
        if key not in anns_zh:
            problems.append(f"缺少标注：{meta[key]['full_name']}（请补到 scripts/annotations.json）")
    for key, a in anns_zh.items():
        name = a.get("name", key)
        if key != key.lower():
            problems.append(f"标注 key 必须小写：{key}")
        if key not in meta:
            problems.append(f"标注找不到仓库：{name}（data.json 里没有，先跑 scripts/fetch.py）")
        for field in ("name", "cat", "pitch", "aud", "note", "diff", "lic"):
            if not isinstance(a.get(field), str) or not a.get(field):
                problems.append(f"标注字段缺失或不是字符串：{key} → {field}")
        if a.get("cat") not in valid_cats:
            problems.append(f"未知赛道：{name} → {a.get('cat')}")
        if a.get("diff") not in DIFF_N:
            problems.append(f"门槛只能是 易/中/难：{name} → {a.get('diff')}")
    if problems:
        print("\n".join(problems))
        sys.exit(f"\n{len(problems)} 处问题，未生成页面。")

    anns = load_annotations(lang, list(meta))

    by_cat = {}
    for key, a in anns.items():
        by_cat.setdefault(a["cat"], []).append(meta[key])
    for cat in by_cat:
        by_cat[cat].sort(key=lambda m: (-m["stars"], m["full_name"].lower()))

    total = sum(m["stars"] for m in meta.values())
    active = sum(1 for m in meta.values()
                 if not m.get("archived")
                 and (SNAP_DATE - datetime.date.fromisoformat(m["pushed_at"])).days <= 45)

    stats = "\n".join([
        f'    <div class="stat"><b>{len(meta)}</b><span>{esc(T["stats"]["repos"])}</span></div>',
        f'    <div class="stat"><b>{wan(total, style)}</b><span>{esc(T["stats"]["stars"])}</span></div>',
        f'    <div class="stat"><b>{len(by_cat)}</b><span>{esc(T["stats"]["tracks"])}</span></div>',
        f'    <div class="stat"><b>{active}</b><span>{esc(T["stats"]["active"])}</span></div>',
    ])

    chips = [f'<button type="button" class="chip on" data-cat="all" aria-pressed="true">{esc(T["chipAll"])}<i>{len(meta)}</i></button>']
    for t in tracks:
        if t["cat"] in by_cat:
            chips.append(f'<button type="button" class="chip" data-cat="{esc(t["cat"])}" aria-pressed="false">{esc(t["title"])}<i>{len(by_cat[t["cat"]])}</i></button>')

    langs = {}
    for m in meta.values():
        langs[m["lang"]] = langs.get(m["lang"], 0) + 1
    lang_opts = [f'<option value="">{esc(T["langAll"])}</option>']
    for lang_name, n in sorted(langs.items(), key=lambda kv: (-kv[1], kv[0] == "-", kv[0])):
        lang_opts.append(f'<option value="{esc(lang_name)}">{esc(lang_name)} ({n})</option>')

    groups = []
    for t in tracks:
        items = by_cat.get(t["cat"], [])
        if not items:
            continue
        star_sum = sum(m["stars"] for m in items)
        body = "\n".join(card(m, anns[m["full_name"].lower()], T, style) for m in items)
        groups.append(f"""  <section class="group" data-cat="{esc(t['cat'])}">
    <div class="group-head">
      <h2>{esc(t['title'])}</h2>
      <span class="gsub">{esc(t['sub'])}</span>
      <span class="gcount"><b class="gc-n">{len(items)}</b> {esc(T['group']['items'])} · ★ <span class="gc-s">{wan(star_sum, style)}</span></span>
    </div>
    <div class="grid">
{body}
    </div>
  </section>""")

    style_css = (ROOT / "scripts/partials/style.css").read_text(encoding="utf-8").replace("\r\n", "\n")
    app_js = (ROOT / "scripts/partials/app.js").read_text(encoding="utf-8").replace("\r\n", "\n")
    page = (ROOT / tpl_name).read_text(encoding="utf-8").replace("\r\n", "\n")
    js_i18n = json.dumps({"numStyle": style, "js": T["js"]}, ensure_ascii=False)
    for ph, val in [
        ("{{STYLE}}", style_css), ("{{APP_JS}}", app_js), ("{{I18N}}", js_i18n),
        ("{{STATS}}", stats), ("{{CHIPS}}", "".join(chips)), ("{{LANGS}}", "".join(lang_opts)),
        ("{{GROUPS}}", "\n".join(groups)), ("{{N_REPOS}}", str(len(meta))),
        ("{{N_TRACKS}}", str(len(by_cat))), ("{{DATE}}", SNAP_DATE.isoformat()),
        ("{{WECHAT_QR}}", wechat_qr_uri()),
    ]:
        assert ph in page, f"{tpl_name} 缺少占位符 {ph}"
        page = page.replace(ph, val)
    page = page.rstrip("\n") + "\n"

    print(f"[{lang}] 项目 {len(meta)} / 赛道 {len(by_cat)} / 星标 {total:,}（{wan(total, style)}） / 近45天 {active}")
    output = ROOT / out_name
    if not write:
        return page, output
    old_bytes = output.read_bytes() if output.exists() else b""
    eol = "\r\n" if b"\r\n" in old_bytes else "\n"
    output.write_bytes(page.replace("\n", eol).encode("utf-8"))
    print(f"  已写入 {out_name}（{len(page):,} 字符，保留 {eol!r} 换行）")
    return page, output


def main():
    args = sys.argv[1:]
    check_only = "--check" in args
    check_generated = "--check-generated" in args
    if "--lang" in args:
        pos = args.index("--lang")
        if pos + 1 >= len(args) or args[pos + 1] not in ("zh", "en", "both"):
            sys.exit("用法：python scripts/build.py [--lang zh|en|both] [--check]")
        want = args[pos + 1]
    else:
        want = "both"
    langs = ["zh", "en"] if want == "both" else [want]

    i18n = json.loads((ROOT / "scripts/i18n.json").read_text(encoding="utf-8"))
    for lang in langs:
        page, output = build(lang, i18n, write=not (check_only or check_generated))
        if check_generated:
            current = output.read_text(encoding="utf-8").replace("\r\n", "\n") if output.exists() else ""
            if current != page:
                sys.exit(f"{output.name} 与源文件不一致，请运行 python scripts/build.py 重新生成。")
            print(f"  {output.name} 与源文件一致")
    if check_only:
        print("校验通过（--check 未写入）")


if __name__ == "__main__":
    main()
