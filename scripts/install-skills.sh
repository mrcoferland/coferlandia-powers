#!/usr/bin/env bash
set -euo pipefail

SOURCE=".agents/skills"
TARGET="${HOME}/.hermes/skills/coferlandia-powers"
FORCE=0
SYMLINK=0

usage() {
  cat <<'USAGE'
Usage: bash scripts/install-skills.sh [--force] [--symlink] [--source PATH] [--target PATH]

Copies or symlinks .agents/skills/ into a Hermes-compatible skill directory.
Defaults:
  source: .agents/skills/
  target: ~/.hermes/skills/coferlandia-powers/
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    --symlink) SYMLINK=1; shift ;;
    --source) SOURCE="${2:?missing source}"; shift 2 ;;
    --target) TARGET="${2:?missing target}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 2 ;;
  esac
done

if [[ ! -d "$SOURCE" ]]; then
  echo "Source directory not found: $SOURCE" >&2
  exit 1
fi

mkdir -p "$(dirname "$TARGET")"

if [[ -e "$TARGET" || -L "$TARGET" ]]; then
  if [[ "$FORCE" -ne 1 ]]; then
    echo "Target already exists: $TARGET"
    echo "Pass --force to replace it."
    exit 1
  fi
  rm -rf "$TARGET"
fi

if [[ "$SYMLINK" -eq 1 ]]; then
  ABS_SOURCE="$(cd "$SOURCE" && pwd)"
  ln -s "$ABS_SOURCE" "$TARGET"
  echo "Symlinked skills: $TARGET -> $ABS_SOURCE"
else
  mkdir -p "$TARGET"
  cp -R "$SOURCE"/. "$TARGET"/
  echo "Copied skills from $SOURCE to $TARGET"
fi

echo "Done. Canonical source remains: $SOURCE"
