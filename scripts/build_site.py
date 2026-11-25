#!/usr/bin/env python3
"""Build the Markdown guide into a static site for GitHub Pages."""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
SITE_NAME = "Antigravity Hotfix"
REPO_URL = "https://github.com/beyondcy1013/antigravity-hotfix"

MD_EXTENSIONS = ["extra", "toc", "sane_lists"]

ALERT_LABELS = {
    "TIP": "提示",
    "NOTE": "说明",
    "IMPORTANT": "重要",
    "WARNING": "注意",
    "CAUTION": "警告",
}

CSS = """
:root {
  --bg: #ffffff;
  --fg: #1f2328;
  --muted: #59636e;
  --border: #d1d9e0;
  --soft: #f6f8fa;
  --accent: #1a73e8;
  --sidebar: #f6f8fa;
  --code-bg: #f6f8fa;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0d1117;
    --fg: #e6edf3;
    --muted: #9198a1;
    --border: #3d444d;
    --soft: #151b23;
    --accent: #6cb0ff;
    --sidebar: #10161d;
    --code-bg: #151b23;
  }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font: 16px/1.75 -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
    "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
header.topbar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  height: 56px;
  padding: 0 24px;
  background: color-mix(in srgb, var(--bg) 88%, transparent);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
}
header.topbar .brand { font-weight: 700; font-size: 16px; color: var(--fg); }
header.topbar .brand span { color: var(--muted); font-weight: 400; margin-left: 8px; }
header.topbar .links { display: flex; gap: 18px; font-size: 14px; }
.layout {
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}
aside { padding: 28px 24px 48px 0; border-right: 1px solid var(--border); }
aside .nav-title {
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 0 0 10px;
}
aside nav { display: flex; flex-direction: column; gap: 2px; }
aside nav a {
  padding: 7px 10px;
  border-radius: 6px;
  color: var(--fg);
  font-size: 14px;
  line-height: 1.45;
}
aside nav a:hover { background: var(--soft); text-decoration: none; }
aside nav a.active { background: var(--soft); color: var(--accent); font-weight: 600; }
aside nav a .num { color: var(--muted); margin-right: 6px; font-variant-numeric: tabular-nums; }
aside nav a.active .num { color: var(--accent); }
main { min-width: 0; padding: 40px 0 80px 40px; }
article { max-width: 860px; }
article h1 { font-size: 30px; line-height: 1.3; margin: 0 0 20px; }
article h2 { font-size: 22px; margin: 40px 0 14px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
article h3 { font-size: 18px; margin: 28px 0 10px; }
article h4 { font-size: 16px; margin: 22px 0 8px; }
article p, article li { color: var(--fg); }
article ul, article ol { padding-left: 1.5em; }
article li + li { margin-top: 4px; }
article hr { border: none; border-top: 1px solid var(--border); margin: 32px 0; }
article blockquote {
  margin: 18px 0;
  padding: 10px 16px;
  border-left: 3px solid var(--border);
  background: var(--soft);
  color: var(--muted);
  border-radius: 0 6px 6px 0;
}
article blockquote p { margin: 6px 0; }
blockquote.alert { color: var(--fg); border-left-width: 4px; }
blockquote.alert .alert-label {
  display: inline-block;
  font-weight: 700;
  font-size: 13px;
  margin-right: 8px;
  padding: 1px 8px;
  border-radius: 999px;
  background: var(--border);
}
blockquote.alert.tip { border-left-color: #1f883d; background: color-mix(in srgb, #1f883d 8%, var(--bg)); }
blockquote.alert.tip .alert-label { background: #1f883d; color: #fff; }
blockquote.alert.important { border-left-color: #8250df; background: color-mix(in srgb, #8250df 8%, var(--bg)); }
blockquote.alert.important .alert-label { background: #8250df; color: #fff; }
blockquote.alert.note { border-left-color: #0969da; background: color-mix(in srgb, #0969da 8%, var(--bg)); }
blockquote.alert.note .alert-label { background: #0969da; color: #fff; }
blockquote.alert.warning, blockquote.alert.caution { border-left-color: #bf8700; background: color-mix(in srgb, #bf8700 10%, var(--bg)); }
blockquote.alert.warning .alert-label, blockquote.alert.caution .alert-label { background: #bf8700; color: #fff; }
article table { width: 100%; border-collapse: collapse; margin: 18px 0; font-size: 14px; display: block; overflow-x: auto; }
article th, article td { border: 1px solid var(--border); padding: 8px 12px; text-align: left; vertical-align: top; }
article th { background: var(--soft); white-space: nowrap; }
article tr:nth-child(even) td { background: color-mix(in srgb, var(--soft) 55%, transparent); }
article code {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  font-size: 0.88em;
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 5px;
}
article pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px 16px;
  overflow-x: auto;
  line-height: 1.55;
}
article pre code { background: none; border: none; padding: 0; font-size: 13px; }
article img { max-width: 100%; height: auto; }
footer {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
  border-top: 1px solid var(--border);
  color: var(--muted);
  font-size: 13px;
}
@media (max-width: 900px) {
  .layout { grid-template-columns: 1fr; padding: 0 16px; }
  aside { border-right: none; border-bottom: 1px solid var(--border); padding: 16px 0; }
  aside nav { flex-direction: row; overflow-x: auto; gap: 4px; padding-bottom: 4px; }
  aside nav a { white-space: nowrap; font-size: 13px; }
  aside .nav-title { display: none; }
  main { padding: 24px 0 56px; }
  article h1 { font-size: 24px; }
}
"""


def doc_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def short_number(title: str) -> str:
    match = re.match(r"^(\d+)\.\s*(.+)$", title)
    return match.group(1) if match else ""


def display_title(title: str) -> str:
    return re.sub(r"^\d+\.\s*", "", title)


LIST_ITEM = re.compile(r"^(\s*)(\d+\.|[-*+])\s+")


def separate_lists(md_text: str) -> str:
    """CommonMark allows lists to interrupt paragraphs; Python-Markdown does not."""
    lines = md_text.splitlines()
    result: list[str] = []
    in_fence = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and LIST_ITEM.match(line):
            prev = result[-1] if result else ""
            if (
                prev.strip()
                and not LIST_ITEM.match(prev)
                and not prev.lstrip().startswith((">", "|", "#"))
            ):
                result.append("")
        result.append(line)
    return "\n".join(result)


def render(md_text: str) -> str:
    body = markdown.markdown(
        separate_lists(md_text), extensions=MD_EXTENSIONS, output_format="html5"
    )

    def alert_repl(match: re.Match[str]) -> str:
        kind = match.group(1).lower()
        label = ALERT_LABELS[kind.upper()]
        return (
            f'<blockquote class="alert {kind}"><p>'
            f'<span class="alert-label">{label}</span>'
        )

    body = re.sub(
        r"<blockquote>\s*<p>\[!(TIP|NOTE|IMPORTANT|WARNING|CAUTION)\]\s*",
        alert_repl,
        body,
        flags=re.IGNORECASE,
    )
    return body


def rewrite_links(body: str, prefix: str) -> str:
    def repl(match: re.Match[str]) -> str:
        href = match.group(2)
        if href.startswith(("http://", "https://", "#", "mailto:")):
            return match.group(0)
        if href.endswith(".md"):
            if href.startswith("docs/"):
                href = href[5:] if prefix else href
            elif href.lower() == "readme.md":
                href = "index"
            href = href[:-3] + ".html"
            if href.startswith("index.html") or "index.html" in href:
                href = prefix + "index.html"
            return f'{match.group(1)}"{href}"'
        return match.group(0)

    return re.sub(r'(href=)"([^"]+)"', repl, body)


NAV_STYLE = ""


def nav_html(items: list[tuple[str, str, str]], active_href: str, prefix: str) -> str:
    rows = [
        f'<a class="{"active" if href == active_href else ""}" href="{prefix}{href}">'
        f'<span class="num">{num}</span>{html.escape(display_title(title))}</a>'
        for href, title, num in items
    ]
    return "\n".join(rows)


def page_html(title: str, nav: str, body: str, prefix: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="Google Antigravity（agy CLI / IDE / 桌面端 / Python SDK）急救技巧、规则与扩展实战手册。">
<style>{CSS}</style>
</head>
<body>
<header class="topbar">
  <a class="brand" href="{prefix}index.html">Antigravity Hotfix<span>救火 · 排障 · 高效实战</span></a>
  <div class="links"><a href="{REPO_URL}">GitHub 仓库</a></div>
</header>
<div class="layout">
  <aside>
    <p class="nav-title">目录导航</p>
    <nav>{nav}</nav>
  </aside>
  <main>
    <article>{body}</article>
  </main>
</div>
<footer>基于 Google Antigravity 官方文档与一线实战经验整理。</footer>
</body>
</html>
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "docs").mkdir(parents=True)

    docs = sorted((ROOT / "docs").glob("*.md"))
    items: list[tuple[str, str, str]] = []
    for path in docs:
        title = doc_title(path)
        items.append((f"docs/{path.stem}.html", title, short_number(title)))
    nav_items = [("index.html", "总览与导航", "")] + items

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    index_body = rewrite_links(render(readme), "")
    (OUT / "index.html").write_text(
        page_html(
            SITE_NAME,
            nav_html(nav_items, "index.html", ""),
            index_body,
            "",
        ),
        encoding="utf-8",
    )

    for path in docs:
        title = doc_title(path)
        body = rewrite_links(render(path.read_text(encoding="utf-8")), "../")
        (OUT / "docs" / f"{path.stem}.html").write_text(
            page_html(
                f"{title} · {SITE_NAME}",
                nav_html(nav_items, f"docs/{path.stem}.html", "../"),
                body,
                "../",
            ),
            encoding="utf-8",
        )

    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(docs) + 1} pages into {OUT}")


if __name__ == "__main__":
    main()
