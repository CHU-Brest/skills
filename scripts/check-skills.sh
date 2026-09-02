#!/usr/bin/env bash
# Checks that every SKILL.md has a valid frontmatter, that every skill referenced
# by the router, the README and the plugin manifest exists, and that every
# template referenced by a skill exists.
set -euo pipefail
cd "$(dirname "$0")/.."

fail=0
err() { echo "ERROR: $*" >&2; fail=1; }

# 1. Frontmatter of every SKILL.md
declare -A names
while IFS= read -r f; do
  head -1 "$f" | grep -q '^---$' || err "$f: missing frontmatter"
  name=$(awk '/^---$/{c++; next} c==1 && /^name:/{sub(/^name:[ ]*/,""); print; exit}' "$f")
  desc=$(awk '/^---$/{c++; next} c==1 && /^description:/{sub(/^description:[ ]*/,""); print; exit}' "$f")
  [ -n "$name" ] || err "$f: missing name"
  [ -n "$desc" ] || err "$f: missing description"
  dir=$(basename "$(dirname "$f")")
  [ "$name" = "$dir" ] || err "$f: name '$name' differs from directory '$dir'"
  names["$name"]=1
  if [[ "$f" == skills/study/* ]]; then
    grep -q '^disable-model-invocation: true' "$f" || err "$f: user-invoked skill must set disable-model-invocation: true"
  fi
done < <(find skills -name SKILL.md | sort)

# 2. Skills referenced by the router, the README and the manifest exist
for ref in $(grep -ohE '`/?[a-z-]+`' skills/study/ask-eds/SKILL.md README.md | tr -d '`/' | sort -u); do
  case "$ref" in
    clear|compact|plugin|docx|dataviz) continue ;;  # Claude Code built-ins and external skills
  esac
  if [ -d "skills/study/$ref" ] || [ -d "skills/reference/$ref" ]; then :; else
    if grep -q "^/$ref\b\|\`/$ref\`" skills/study/ask-eds/SKILL.md README.md 2>/dev/null; then
      err "referenced skill '/$ref' does not exist"
    fi
  fi
done
for p in $(python3 -c 'import json;print("\n".join(json.load(open(".claude-plugin/plugin.json"))["skills"]))'); do
  [ -f "$p/SKILL.md" ] || err "plugin.json references missing skill $p"
done

# 3. Templates and checklists referenced by skills exist
for t in $(grep -ohE 'templates/[A-Za-z0-9_.-]+\.md' skills -r | sort -u); do
  [ -f "$t" ] || err "missing template $t"
done
for c in $(grep -ohE 'checklists/[a-z]+\.md' skills -r | sort -u); do
  [ -f "skills/reference/reporting-guidelines/$c" ] || err "missing checklist $c"
done

# 4. Cross-references between skills (backticked bare names) exist
for f in $(find skills -name SKILL.md); do
  for ref in $(grep -ohE '`[a-z-]+`' "$f" | tr -d '`' | sort -u); do
    case "$ref" in
      grilling|study-folder|epi-designs|epi-biases|reporting-guidelines|terminologies|regulatory-fr|dataviz|docx)
        [ "$ref" = dataviz ] || [ "$ref" = docx ] || [ -n "${names[$ref]:-}" ] || err "$f references unknown skill '$ref'" ;;
    esac
  done
done

if [ "$fail" -eq 0 ]; then
  echo "OK: ${#names[@]} skills checked"
else
  exit 1
fi
