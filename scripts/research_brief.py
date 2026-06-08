#!/usr/bin/env python3
"""
AI ToolKit — Research Brief Generator
Run via Hermes cron to find trending AI tools/topics for content.

Usage: py research_brief.py
Output: JSON research brief saved to content/briefs/
"""
import json
import os
from datetime import datetime

OUTPUT_DIR = os.path.expanduser("~/projects/aitoolkit-blog/content/briefs")

TOPICS = [
    "new AI tools launched this week 2026",
    "best AI tools for content creators 2026",
    "AI writing tools comparison 2026",
    "trending AI productivity tools small business",
    "AI video generation tools launched recently",
    "AI image generation tools comparison 2026",
    "AI marketing automation tools 2026",
    "AI tools for social media management",
    "best AI SEO tools 2026",
    "AI email marketing tools small business",
    "AI customer service chatbot tools",
    "AI data analysis tools for marketers",
]

SEARCH_RESULTS_TEMPLATE = {
    "date": "",
    "topic": "",
    "keywords": [],
    "trending_tools": [],
    "affiliate_opportunities": [],
    "content_angles": [],
    "search_volume_estimate": "",
    "competition_level": "",
}

def generate_brief():
    """Generate a placeholder brief — in production, web_search results populate this."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    brief = {
        "date": today,
        "topic": "ai-writing-tools-comparison",
        "keywords": [
            "best AI writing tools 2026",
            "AI copywriting software comparison",
            "Copy.ai vs alternatives",
            "AI content generator for business"
        ],
        "trending_tools": [
            {"name": "Copy.ai", "category": "AI Writing", "affiliate": True, "commission": "45% first year"},
            {"name": "Writesonic", "category": "AI Writing", "affiliate": True, "commission": "30% lifetime"},
            {"name": "Jasper", "category": "AI Writing", "affiliate": True, "commission": "recurring"},
        ],
        "content_angles": [
            "Head-to-head comparison of top 3 AI writers",
            "Best AI writing tools by use case (blogs vs ads vs social)",
            "AI writing tools pricing comparison 2026",
            "How to choose an AI writing tool: beginner's guide"
        ],
        "search_volume_estimate": "medium-high",
        "competition_level": "medium",
    }
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{OUTPUT_DIR}/brief_{today}.json"
    with open(filename, "w") as f:
        json.dump(brief, f, indent=2)
    
    print(f"Research brief saved: {filename}")
    print(json.dumps(brief, indent=2))

if __name__ == "__main__":
    generate_brief()
