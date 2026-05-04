#!/usr/bin/env bash
# Iron Custom Motors — deploy script
# Run from this folder:  bash deploy.sh

set -e
cd "$(dirname "$0")"

REPO_NAME="iron-moto-cascais"
GIT_USER_NAME="Vadym Grishin"
GIT_USER_EMAIL="vg@abrisart.com"

# ---- 1. Clean any half-initialized .git (created by a previous attempt) ----
if [ -d .git ]; then
  echo "Removing previous .git directory..."
  rm -rf .git
fi

# ---- 2. Init repo, configure identity ----
git init -b main
git config user.name  "$GIT_USER_NAME"
git config user.email "$GIT_USER_EMAIL"

# ---- 3. Stage and commit ----
git add .
git commit -m "feat: initial single-page MVP — EN/RU/UK/PT, real Cascais contacts"

# ---- 4. Create GitHub repo and push (requires gh CLI authenticated) ----
if command -v gh >/dev/null 2>&1; then
  echo
  echo "Using gh CLI to create the repo and push..."
  gh repo create "$REPO_NAME" --public --source=. --push --description "Iron Custom Motors — premium motorcycle service website (Cascais)"
  echo
  echo "Done! Open it:"
  gh repo view --web
else
  echo
  echo "gh CLI not found."
  echo "Install once:    brew install gh && gh auth login"
  echo "Or push manually:"
  echo "  git remote add origin https://github.com/<your-username>/$REPO_NAME.git"
  echo "  git push -u origin main"
fi
