#!/usr/bin/env python3
"""
AI ToolKit — Publish Pipeline
Stages, commits, and pushes new content to deploy.

Usage: py publish.py --message "feat: New article title"
"""
import argparse
import os
import subprocess
import sys

BLOG_ROOT = os.path.expanduser("~/projects/aitoolkit-blog")

def run(cmd, cwd=BLOG_ROOT):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}", file=sys.stderr)
    return result.returncode == 0

def publish(message):
    print(f"Publishing with message: {message}")
    
    # Stage changes
    if not run("git add articles/ assets/main.js index.html"):
        return False
    
    # Check if there's anything to commit
    result = subprocess.run("git diff --cached --quiet", shell=True, cwd=BLOG_ROOT)
    if result.returncode == 0:
        print("No changes to commit.")
        return True
    
    # Commit
    if not run(f'git commit -m "{message}"'):
        return False
    
    # Push
    if not run("git push origin main"):
        print("Push failed. Is the remote configured?")
        return False
    
    print("Published successfully! Vercel/Netlify will auto-deploy.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", required=True, help="Git commit message")
    args = parser.parse_args()
    
    success = publish(args.message)
    sys.exit(0 if success else 1)
