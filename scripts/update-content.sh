#!/usr/bin/env bash
# Update the content submodules (intended-learning-outcomes, learning-activities)
# to the latest commit on their tracked branch and record the bump in this repo.
#
# Usage:
#   scripts/update-content.sh            # update all submodules, commit the bump
#   scripts/update-content.sh --no-commit  # update only; leave the bump unstaged
#   scripts/update-content.sh learning-activities   # update just one submodule
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

commit=1
paths=()
for arg in "$@"; do
  case "$arg" in
    --no-commit) commit=0 ;;
    -h|--help) sed -n '2,9p' "$0"; exit 0 ;;
    *) paths+=("$arg") ;;
  esac
done

if [ ${#paths[@]} -eq 0 ]; then
  # all submodule paths from .gitmodules
  while IFS= read -r p; do paths+=("$p"); done < <(git config --file .gitmodules --get-regexp 'submodule\..*\.path' | awk '{print $2}')
fi

# Make sure submodules are initialised (fresh clones without --recurse-submodules)
git submodule update --init -- "${paths[@]}"

before=$(git submodule status -- "${paths[@]}")
git submodule update --remote --merge -- "${paths[@]}"
after=$(git submodule status -- "${paths[@]}")

if [ "$before" = "$after" ]; then
  echo "Content submodules already up to date."
  exit 0
fi

echo "Updated:"
git submodule status -- "${paths[@]}"

if [ "$commit" -eq 1 ]; then
  git add -- "${paths[@]}"
  summary=$(for p in "${paths[@]}"; do
    printf '%s -> %s\n' "$p" "$(git -C "$p" log -1 --format='%h %s')"
  done)
  git commit -q -m "Bump content submodules" -m "$summary"
  echo "Committed: $(git log -1 --oneline)"
  echo "Run 'git push' to publish."
else
  echo "Changes left unstaged (--no-commit)."
fi
