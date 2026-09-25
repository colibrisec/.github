import collections
import datetime
import html
import json
import os
import pathlib
import urllib.parse
import urllib.request

ORG = os.environ.get("GITHUB_ORG", "colibrisec")
TOKEN = os.environ["GITHUB_TOKEN"]
OUTPUT = pathlib.Path(os.environ.get("OUTPUT", "dist/contribution-stream.svg"))
TODAY = datetime.datetime.now(datetime.UTC).date()
START = TODAY - datetime.timedelta(days=370)


def request(path, params=None):
    url = f"https://api.github.com{path}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "colibrisec-contribution-stream",
    }
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as response:
        return json.load(response), response.headers


def paged(path, params=None):
    params = dict(params or {})
    params["per_page"] = 100
    page = 1
    while True:
        params["page"] = page
        items, _ = request(path, params)
        yield from items
        if len(items) < 100:
            return
        page += 1


def date_from_commit(commit):
    timestamp = commit.get("commit", {}).get("author", {}).get("date")
    if not timestamp:
        return None
    return datetime.datetime.fromisoformat(timestamp.replace("Z", "+00:00")).date()


repositories = [
    repository
    for repository in paged(f"/orgs/{ORG}/repos", {"type": "all", "sort": "updated"})
    if not repository["fork"] and not repository["archived"]
]
counts = collections.Counter()
contributors = set()
for repository in repositories:
    for commit in paged(
        f"/repos/{ORG}/{repository['name']}/commits",
        {"since": f"{START.isoformat()}T00:00:00Z"},
    ):
        committed_on = date_from_commit(commit)
        if committed_on and START <= committed_on <= TODAY:
            counts[committed_on] += 1
            author = commit.get("author")
            if author and author.get("login"):
                contributors.add(author["login"])

first_sunday = START - datetime.timedelta(days=(START.weekday() + 1) % 7)
weeks = 53
cell = 13
gap = 4
left = 26
top = 43
width = left + weeks * (cell + gap) + 24
height = top + 7 * (cell + gap) + 42
maximum = max(counts.values(), default=1)
colors = ["#1B1028", "#48204A", "#9C2F52", "#FF5A36", "#FFD447"]


def color(count):
    if not count:
        return colors[0]
    level = min(4, max(1, round((count / maximum) * 4)))
    return colors[level]

cells = []
for week in range(weeks):
    for day in range(7):
        current = first_sunday + datetime.timedelta(days=week * 7 + day)
        if current < START or current > TODAY:
            continue
        count = counts[current]
        x = left + week * (cell + gap)
        y = top + day * (cell + gap)
        cells.append(
            f'<rect class="cell level-{min(4, max(1, round((count / maximum) * 4))) if count else 0}" x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{color(count)}"><title>{current.isoformat()}: {count} commits</title></rect>'
        )

label = f"{len(repositories)} active repositories · {len(contributors)} contributors · {sum(counts.values())} commits"
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">
<title id="title">ColibriSec contribution stream</title>
<desc id="description">{html.escape(label)} during the past year</desc>
<style>
@keyframes pulse {{ 0%, 100% {{ opacity: .55; }} 50% {{ opacity: 1; }} }}
@keyframes scan {{ 0% {{ transform: translateX(-40px); }} 100% {{ transform: translateX({width + 40}px); }} }}
text {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
.cell {{ animation: pulse 2.8s ease-in-out infinite; }}
.level-1 {{ animation-delay: .2s; }}
.level-2 {{ animation-delay: .4s; }}
.level-3 {{ animation-delay: .6s; }}
.level-4 {{ animation-delay: .8s; }}
@media (prefers-reduced-motion: reduce) {{ .cell, .scan {{ animation: none; }} }}
</style>
<rect width="100%" height="100%" rx="12" fill="#0B0B10"/>
<path d="M18 28H{width - 18}" stroke="#FF5A36" stroke-opacity=".35"/>
<rect class="scan" x="0" y="29" width="32" height="2" fill="#FFD447" opacity=".8"/>
<text x="18" y="19" fill="#FFD447" font-size="12" font-weight="700">COLIBRISEC // CONTRIBUTION STREAM</text>
<text x="18" y="{height - 14}" fill="#FF9A5C" font-size="10">{html.escape(label)}</text>
{''.join(cells)}
</svg>'''
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(svg)
