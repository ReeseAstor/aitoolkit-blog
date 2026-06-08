// AI ToolKit - Main JavaScript
// Dynamic article loading + newsletter handling

const ARTICLES = [
    {
        slug: "best-ai-writing-tools-2026",
        title: "Best AI Writing Tools in 2026: The Only 5 You Actually Need",
        excerpt: "We tested 20+ AI writing tools. These 5 stand out for content creators — from blog posts to marketing copy.",
        category: "Reviews",
        date: "2026-06-08",
        readTime: "8 min read"
    },
    {
        slug: "copyai-vs-jasper-vs-writesonic",
        title: "Copy.ai vs Jasper vs Writesonic: Which AI Writer Wins in 2026?",
        excerpt: "Side-by-side comparison of the top 3 AI writing platforms. Pricing, features, and real output quality tested.",
        category: "Comparison",
        date: "2026-06-07",
        readTime: "12 min read"
    },
    {
        slug: "ai-tools-small-business-owners",
        title: "10 AI Tools Every Small Business Owner Should Use in 2026",
        excerpt: "From automating emails to generating social content — these AI tools save 10+ hours per week.",
        category: "Guide",
        date: "2026-06-06",
        readTime: "10 min read"
    },
    {
        slug: "ai-video-tools-creators",
        title: "AI Video Creation Tools Compared: Synthesia vs Colossyan vs HeyGen",
        excerpt: "Create professional videos without a camera. We compare the top AI video platforms for creators and marketers.",
        category: "Comparison",
        date: "2026-06-05",
        readTime: "9 min read"
    },
    {
        slug: "ai-seo-tools-rank-higher",
        title: "AI SEO Tools That Actually Help You Rank Higher in 2026",
        excerpt: "Surfer, Frase, and MarketMuse go head-to-head. Which AI SEO tool delivers the best ROI?",
        category: "Guide",
        date: "2026-06-04",
        readTime: "7 min read"
    }
];

const TOOLS = [
    {
        name: "Copy.ai",
        icon: "✍️",
        commission: "45% for 1st year",
        slug: "copyai-vs-jasper-vs-writesonic"
    },
    {
        name: "Writesonic",
        icon: "📝",
        commission: "30% lifetime",
        slug: "copyai-vs-jasper-vs-writesonic"
    },
    {
        name: "Canva",
        icon: "🎨",
        commission: "Up to 20%",
        slug: "ai-tools-small-business-owners"
    },
    {
        name: "Synthesia",
        icon: "🎬",
        commission: "20% for 12 months",
        slug: "ai-video-tools-creators"
    },
    {
        name: "Speechify",
        icon: "🔊",
        commission: "50% flat",
        slug: "best-ai-writing-tools-2026"
    },
    {
        name: "AdCreative.ai",
        icon: "📊",
        commission: "30% lifetime",
        slug: "ai-tools-small-business-owners"
    }
];

function renderArticles() {
    const grid = document.getElementById('article-grid');
    if (!grid) return;
    grid.innerHTML = ARTICLES.map(a => `
        <article class="article-card" onclick="location.href='/articles/${a.slug}.html'">
            <div class="category">${a.category}</div>
            <h3><a href="/articles/${a.slug}.html">${a.title}</a></h3>
            <p class="excerpt">${a.excerpt}</p>
            <div class="meta">
                <span>${a.date}</span>
                <span>${a.readTime}</span>
            </div>
        </article>
    `).join('');
}

function renderTools() {
    const grid = document.getElementById('tools-grid');
    if (!grid) return;
    grid.innerHTML = TOOLS.map(t => `
        <div class="tool-card" onclick="location.href='/articles/${t.slug}.html'">
            <div class="tool-icon">${t.icon}</div>
            <h3>${t.name}</h3>
            <div class="commission">${t.commission}</div>
            <a href="/articles/${t.slug}.html" class="tool-link">Read review →</a>
        </div>
    `).join('');
}

document.addEventListener('DOMContentLoaded', () => {
    renderArticles();
    renderTools();

    const form = document.getElementById('newsletter-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const input = form.querySelector('input');
            const btn = form.querySelector('button');
            btn.textContent = 'Subscribed! ✓';
            btn.style.background = '#4ade80';
            input.value = '';
            setTimeout(() => { btn.textContent = 'Subscribe Free'; btn.style.background = ''; }, 3000);
        });
    }
});
