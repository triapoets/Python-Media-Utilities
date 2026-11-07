#!/bin/bash

# Auto Git Sync Script
# Monitors file changes and automatically commits + pushes to GitHub

WATCH_DIR="/root/python_projects"
cd "$WATCH_DIR" || exit 1

echo "🔄 Auto-sync started for: $WATCH_DIR"
echo "📡 Monitoring changes... (Ctrl+C to stop)"

# Initial sync
git pull origin master 2>/dev/null

# Monitor file changes with inotifywait
inotifywait -m -r -e modify,create,delete,move \
  --exclude '\.git|\.swp|__pycache__|\.pyc' \
  "$WATCH_DIR" | while read -r directory events filename; do

  # Skip if no actual changes
  if git diff --quiet && git diff --staged --quiet; then
    continue
  fi

  # Show what changed
  echo ""
  echo "📝 Change detected: $filename"

  # Add all changes
  git add .

  # Commit with timestamp
  TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
  git commit -m "Auto-sync: $filename - $TIMESTAMP

Co-Authored-By: Claude Sonnet 3.5 <noreply@anthropic.com>" 2>/dev/null

  # Push to remote
  if git push origin master 2>/dev/null; then
    echo "✅ Synced to GitHub"
  else
    echo "⚠️  Push failed (check connection)"
  fi

  # Small delay to batch rapid changes
  sleep 2
done
