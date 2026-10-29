"""Usage: python inspect-summary.py <inspect-output-dir> <project-dir>

Prints one line per problem: [SEVERITY] file:line InspectionId - description.
Run without args for a self-check.
"""
import html
import json
import os
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

ORDER = ["ERROR", "WARNING", "WEAK WARNING", "INFO"]
SKIP_DIRS = ("vendor/", "node_modules/", "storage/", ".idea/")


def rel(uri, project):
    path = uri.removeprefix("file://").replace("$PROJECT_DIR$", project).replace("$USER_HOME$", str(Path.home()))
    # realpath expands Windows 8.3 short names so both sides compare equal
    try:
        return Path(os.path.relpath(os.path.realpath(path), os.path.realpath(project))).as_posix()
    except ValueError:
        return path


def summarize(out_dir, project):
    rows = []
    for f in Path(out_dir).glob("*.json"):
        for p in json.loads(f.read_text(encoding="utf-8")).get("problems", []):
            sev = p.get("problem_class", {}).get("severity", "?")
            file = rel(p.get("file", "?"), project)
            if file.startswith(SKIP_DIRS):
                continue
            msg = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", p.get("description", ""))).split())
            rows.append((sev, file, p.get("line", 0), p.get("problem_class", {}).get("id", f.stem), msg))
    rows.sort(key=lambda x: (ORDER.index(x[0]) if x[0] in ORDER else len(ORDER), x[1], x[2]))
    return rows


def render(rows):
    counts = Counter(r[0] for r in rows)
    head = f"PhpStorm inspect: {len(rows)} problems" + (" (" + ", ".join(f"{s}: {n}" for s, n in counts.most_common()) + ")" if rows else "")
    return "\n".join([head] + [f"[{s}] {f}:{l} {rule} - {msg}" for s, f, l, rule, msg in rows])


def _selftest():
    with tempfile.TemporaryDirectory() as d:
        def problem(file, line, sev, rule, msg):
            return {"file": f"file://$PROJECT_DIR$/{file}", "line": line, "description": msg,
                    "problem_class": {"id": rule, "severity": sev}}
        Path(d, "A.json").write_text(json.dumps({"problems": [
            problem("app/A.php", 3, "WEAK WARNING", "PhpUnused", "unused"),
            problem("vendor/x/B.php", 1, "ERROR", "X", "vendor"),
        ]}))
        Path(d, "B.json").write_text(json.dumps({"problems": [
            problem("app/B.php", 9, "WARNING", "PhpUndefinedMethodInspection", "<ul><li>Method &#39;x&#39;</li><li>undefined</li></ul>"),
        ]}))
        out = render(summarize(d, d)).splitlines()
    assert out == [
        "PhpStorm inspect: 2 problems (WARNING: 1, WEAK WARNING: 1)",
        "[WARNING] app/B.php:9 PhpUndefinedMethodInspection - Method 'x' undefined",
        "[WEAK WARNING] app/A.php:3 PhpUnused - unused",
    ], out
    assert render([]) == "PhpStorm inspect: 0 problems"
    print("ok")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        _selftest()
    else:
        print(render(summarize(sys.argv[1], sys.argv[2])))
