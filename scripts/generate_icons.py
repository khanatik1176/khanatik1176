#!/usr/bin/env python3
"""Generate consistent Tokyo Night animated SVG icons for the profile README.

Uses SMIL animations so motion works when icons are embedded via <img> on GitHub.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOCIAL_DIR = ROOT / "assets" / "icons" / "social"
SKILLS_DIR = ROOT / "assets" / "icons" / "skills"

SIZE = 72


def tile(slug: str, accent: str, inner: str, delay: float = 0.0) -> str:
    # SMIL animates reliably for GitHub README <img> tags
    begin = f"{delay}s"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}" role="img" aria-label="{slug}">
  <defs>
    <linearGradient id="bg-{slug}" x1="0" y1="0" x2="{SIZE}" y2="{SIZE}">
      <stop offset="0%" stop-color="#1a1b27"/>
      <stop offset="100%" stop-color="#24283b"/>
    </linearGradient>
  </defs>

  <!-- soft accent glow -->
  <rect x="3" y="3" width="66" height="66" rx="18" fill="{accent}" opacity="0.28">
    <animate attributeName="opacity" values="0.18;0.42;0.18" dur="2.8s" begin="{begin}" repeatCount="indefinite"/>
  </rect>

  <!-- floating card -->
  <g>
    <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="3.2s" begin="{begin}" repeatCount="indefinite"/>
    <rect x="6" y="6" width="60" height="60" rx="16" fill="url(#bg-{slug})" stroke="{accent}" stroke-opacity="0.55" stroke-width="1.4"/>
    <rect x="6" y="6" width="60" height="4" rx="2" fill="{accent}">
      <animate attributeName="opacity" values="0.75;1;0.75" dur="2.4s" begin="{begin}" repeatCount="indefinite"/>
    </rect>
    <g opacity="0.95">
      <animate attributeName="opacity" values="0.9;1;0.9" dur="4s" begin="{begin}" repeatCount="indefinite"/>
      {inner}
    </g>
  </g>
</svg>
'''


def monogram(text: str, color: str, size: int = 22) -> str:
    return (
        f'<text x="36" y="42" text-anchor="middle" fill="{color}" '
        f'font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" '
        f'font-size="{size}" font-weight="700" letter-spacing="-0.5">{text}</text>'
    )


SOCIAL = {
    "linkedin": (
        "#0A66C2",
        '''<g fill="#7AA2F7">
      <rect x="22" y="30" width="5.5" height="18" rx="1"/>
      <circle cx="24.8" cy="24" r="3.2"/>
      <path d="M31 30h5.8v2.5c1.3-2 3.3-3.1 6-3.1 5.6 0 6.8 3.7 6.8 8.5V48H43.7v-9.2c0-2.2 0-5-3.1-5s-3.6 2.4-3.6 4.8V48H31V30Z"/>
    </g>''',
    ),
    "facebook": (
        "#1877F2",
        '<path fill="#7AA2F7" d="M38 48V35h4.8l.9-5.5H38v-3.5c0-1.6.4-2.7 2.8-2.7h3V18.2c-.5-.1-2.3-.3-4.4-.3-4.4 0-7.4 2.7-7.4 7.6v4.5h-5V35h5V48h5.6Z"/>',
    ),
    "leetcode": (
        "#FFA116",
        '''<g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="3.2">
      <path d="M38 18 24 31c-4.8 4.8-4.8 11.8 0 16.6s11.8 4.8 16.6 0l3.8-3.8" stroke="#E0AF68"/>
      <path d="M27 39h18" stroke="#FFA116"/>
      <path d="M28 25l6.5-6.5L41 25" stroke="#FFA116"/>
    </g>''',
    ),
    "codechef": (
        "#5B4638",
        '''<g fill="none" stroke="#E0AF68" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
      <path d="M22 33c-3.8-1-4.8-6.5-2-9.4 2-2 4.8-2 6.7-1 .9-3.8 4.8-5.7 8.6-3.8 2 1 3.8 2.9 3.8 5.7 3.8-1 7.6 2 7.6 5.7 0 2.9-2 4.8-4.8 5.7"/>
      <path d="M23 33v14h20V33M26 42h13"/>
    </g>''',
    ),
}

SKILLS = {
    "python": ("#3776AB", '''<g>
      <path fill="#3776AB" d="M36 16c-7.5 0-7 3.2-7 3.2v3.6h7.1v1.2H25.3s-5.2-.6-5.2 7.6 4.6 7.3 4.6 7.3h2.8v-3.5s-.2-4.2 4.1-4.2h7.1s4-.1 4-4.7V19.2S43.5 16 36 16Zm-3.7 2.3a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z"/>
      <path fill="#FFD43B" d="M36.1 56c7.5 0 7-3.2 7-3.2v-3.6h-7.1v-1.2h10.8s5.2.6 5.2-7.6-4.6-7.3-4.6-7.3h-2.8v3.5s.2 4.2-4.1 4.2h-7.1s-4 .1-4 4.7v7.3S28.6 56 36.1 56Zm3.6-2.3a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3Z"/>
    </g>'''),
    "javascript": ("#F7DF1E", '''<g>
      <rect x="18" y="18" width="36" height="36" rx="6" fill="#F7DF1E"/>
      <path fill="#1a1b27" d="M33.2 42.6c0 3.2-1.9 4.7-4.6 4.7-2.5 0-3.9-1.3-4.7-3l2.5-1.5c.5.9 1 1.6 2.1 1.6 1.1 0 1.8-.5 1.8-2.3V31.5h2.9v11.1Zm7.3 4.7c-2.9 0-4.8-1.4-5.7-3.3l2.5-1.4c.6 1.1 1.5 1.9 2.9 1.9 1.3 0 2.1-.6 2.1-1.6 0-1.1-.9-1.5-2.4-2.2l-.8-.4c-2.4-1-4-2.3-4-5 0-2.5 1.9-4.4 4.9-4.4 2.1 0 3.7.7 4.8 2.7l-2.4 1.5c-.5-.9-1.1-1.3-2.4-1.3-1.1 0-1.8.7-1.8 1.5 0 1 .6 1.4 2.1 2.1l.8.3c2.8 1.2 4.4 2.5 4.4 5.3 0 3-2.4 4.6-5.5 4.6Z"/>
    </g>'''),
    "typescript": ("#3178C6", '''<g>
      <rect x="18" y="18" width="36" height="36" rx="6" fill="#3178C6"/>
      <path fill="#fff" d="M29.8 33.2h-4.3v-2.4h12.4v2.4h-4.3V48h-3.8V33.2Zm10.2 14.5c-1.1.6-2.6.9-4.2.9-1.9 0-3.4-.5-4.5-1.4-1.1-1-1.6-2.3-1.6-4h3.5c0 .8.3 1.4.8 1.8.5.4 1.2.6 2.1.6 1 0 1.8-.2 2.4-.6.6-.4.9-.9.9-1.5 0-.6-.2-1-.7-1.3-.5-.3-1.3-.6-2.5-.9l-1.5-.4c-1.7-.5-3-1.2-3.8-2.1-.8-.9-1.2-2-1.2-3.4 0-1.5.6-2.8 1.7-3.7 1.1-.9 2.7-1.4 4.6-1.4 1.5 0 2.8.3 3.9.8 1.1.5 1.9 1.3 2.4 2.3l-3 1.5c-.3-.6-.8-1.1-1.4-1.4-.6-.3-1.3-.4-2-.4-.9 0-1.6.2-2.1.6-.5.4-.7.9-.7 1.4 0 .6.3 1 .8 1.3.5.3 1.4.7 2.7 1l1.4.4c1.8.5 3.1 1.2 3.9 2.1.8.9 1.2 2 1.2 3.4 0 1.7-.6 3-1.9 3.9Z"/>
    </g>'''),
    "csharp": ("#68217A", monogram("C#", "#BB9AF7", 24)),
    "cplusplus": ("#00599C", monogram("C++", "#7AA2F7", 22)),
    "html5": ("#E34F26", '''<g>
      <path fill="#E34F26" d="M20 18h32l-2.9 32.6L36 54l-13.1-3.4L20 18Z"/>
      <path fill="#EF652A" d="M36 20.2V51.5l10.6-2.9L49.2 20.2H36Z"/>
      <path fill="#EBEBEB" d="m24.2 27.2.6 6.8h11.2v-3.4H28l.2-2.4h11.2l.6-6.8H24.8l-.6 5.8Zm.9 10.2.5 5.5L36 45.8v-3.5l-6.4-1.7-.2-2.2H25.1Z"/>
      <path fill="#fff" d="M36 34h6.4l-.5 5.6-5.9 1.6v3.5l10.3-2.8.1-1.2.9-10.1.1-1.1H36V34Z"/>
    </g>'''),
    "css3": ("#1572B6", '''<g>
      <path fill="#1572B6" d="M20 18h32l-2.9 32.6L36 54l-13.1-3.4L20 18Z"/>
      <path fill="#33A9DC" d="M36 20.2V51.5l10.6-2.9L49.2 20.2H36Z"/>
      <path fill="#EBEBEB" d="M25 27.5h11v3.3H28.4l.3 3.2H36v3.3H25.8L25 27.5Zm.8 13.2 1.2 12.2L36 45.8v3.5l-9.3-2.6-.2-1.8.5-5.2h-1.2Z"/>
      <path fill="#fff" d="M36 40.7h6.2l-.5 5.1L36 47.5v3.5l9.3-2.6.1-1.1 1-11.3H36v3.3h6.5l-.3 3.4H36v3Z"/>
    </g>'''),
    "django": ("#092E20", monogram("dj", "#9ECE6A", 24)),
    "fastapi": ("#009688", '''<g fill="#9ECE6A">
      <path d="M36 16a20 20 0 1 0 0 40 20 20 0 0 0 0-40Zm0 4.2a15.8 15.8 0 1 1 0 31.6 15.8 15.8 0 0 1 0-31.6Z"/>
      <path d="M33.2 24.5h5.6v9.2l5.4 8.8h-6.2l-2.1-3.8-2.1 3.8h-6.1l5.5-8.8v-9.2Z"/>
    </g>'''),
    "nodejs": ("#339933", '''<g fill="#9ECE6A">
      <path d="M35.2 15.8 20.6 24.2v16.8l14.6 8.4 14.6-8.4V24.2L35.2 15.8Zm0 4.2 10.2 5.9v11.8L35.2 43.6 25 37.7V25.9l10.2-5.9Z"/>
      <path d="M32.5 28.2h5.4c2.5 0 4.2 1.5 4.2 3.7 0 1.8-1 3-2.6 3.5l3.2 4.8h-3.6l-2.7-4.2h-1.1v4.2h-2.8V28.2Zm2.8 2.3v2.8h2.2c.9 0 1.4-.4 1.4-1.4s-.5-1.4-1.4-1.4h-2.2Z"/>
    </g>'''),
    "react": ("#61DAFB", '''<g fill="none" stroke="#7DCFFF" stroke-width="2.2">
      <ellipse cx="36" cy="36" rx="18" ry="7.2" transform="rotate(60 36 36)"/>
      <ellipse cx="36" cy="36" rx="18" ry="7.2" transform="rotate(-60 36 36)"/>
      <ellipse cx="36" cy="36" rx="18" ry="7.2"/>
      <circle cx="36" cy="36" r="3.4" fill="#7DCFFF" stroke="none"/>
      <animateTransform attributeName="transform" type="rotate" from="0 36 36" to="360 36 36" dur="12s" repeatCount="indefinite"/>
    </g>'''),
    "reactnative": ("#61DAFB", '''<g>
      <g fill="none" stroke="#7DCFFF" stroke-width="2">
        <ellipse cx="36" cy="33" rx="16" ry="6.4" transform="rotate(60 36 33)"/>
        <ellipse cx="36" cy="33" rx="16" ry="6.4" transform="rotate(-60 36 33)"/>
        <ellipse cx="36" cy="33" rx="16" ry="6.4"/>
        <animateTransform attributeName="transform" type="rotate" from="0 36 33" to="360 36 33" dur="14s" repeatCount="indefinite"/>
      </g>
      <circle cx="36" cy="33" r="3" fill="#7DCFFF"/>
      <text x="36" y="52" text-anchor="middle" fill="#7AA2F7" font-family="Segoe UI, Arial, sans-serif" font-size="9" font-weight="700">NATIVE</text>
    </g>'''),
    "expo": ("#BB9AF7", monogram("EX", "#BB9AF7", 22)),
    "nextjs": ("#FFFFFF", '''<g fill="#C0CAF5">
      <circle cx="36" cy="36" r="16" fill="none" stroke="#C0CAF5" stroke-width="2.4"/>
      <path d="M32 26h4.2l8.8 13.2V26H49v20h-4.1L36 32.6V46h-4V26Z"/>
    </g>'''),
    "express": ("#C0CAF5", monogram("ex", "#C0CAF5", 22)),
    "nestjs": ("#E0234E", '''<g fill="#F7768E">
      <path d="M36 16c-8.5 4.2-14 11.8-14 20.4 0 9.2 6.4 16.4 14 19.6 7.6-3.2 14-10.4 14-19.6C50 27.8 44.5 20.2 36 16Zm0 6.2c5.8 3.1 9.4 8.4 9.4 14.2S41.8 47.5 36 50.6c-5.8-3.1-9.4-8.4-9.4-14.2S30.2 25.3 36 22.2Z"/>
      <path d="M36 26.5c-3.8 2-6.2 5.4-6.2 9.2S32.2 43 36 45c3.8-2 6.2-5.4 6.2-9.3S39.8 28.5 36 26.5Z"/>
    </g>'''),
    "dotnet": ("#512BD4", monogram(".NET", "#BB9AF7", 16)),
    "docker": ("#2496ED", '''<g fill="#7AA2F7">
      <path d="M48.5 33.2c-1.1-.7-3.6-1-4.4-1 .3-2.2-.2-5-2.2-6.7-1.4-1.2-3.4-1.4-4.5-1.4-.4 0-.7 0-1 .1l-.3 1.9c.2 0 .5-.1.8-.1 1.6 0 3.2.4 4 1.7.8 1.3.8 3.3.5 4.6H20.8c-.4 0-.7.4-.6.8.7 4.3 3.9 8 9.3 8 5.8 0 10.1-3.1 12.1-8.2 1.4.1 4.4.1 5.9-1.8.1-.1.1-.3 0-.4-.3-.3-.6-.5-1-.7Z"/>
      <rect x="23" y="28" width="4" height="4" rx=".6"/>
      <rect x="28" y="28" width="4" height="4" rx=".6"/>
      <rect x="33" y="28" width="4" height="4" rx=".6"/>
      <rect x="28" y="23" width="4" height="4" rx=".6"/>
      <rect x="33" y="23" width="4" height="4" rx=".6"/>
      <rect x="33" y="18" width="4" height="4" rx=".6"/>
    </g>'''),
    "tailwind": ("#38BDF8", '''<path fill="#7DCFFF" d="M22 34c2.7-5.4 6.4-8.1 11.1-8.1 3.5 0 5.7 1.7 7.4 5.2 1.1 2.3 2.3 3.4 4.1 3.4 2.1 0 3.9-1.3 5.4-3.9C47.3 36 43.6 38.7 38.9 38.7c-3.5 0-5.7-1.7-7.4-5.2-1.1-2.3-2.3-3.4-4.1-3.4-2.1 0-3.9 1.3-5.4 3.9Zm0 10.8c2.7-5.4 6.4-8.1 11.1-8.1 3.5 0 5.7 1.7 7.4 5.2 1.1 2.3 2.3 3.4 4.1 3.4 2.1 0 3.9-1.3 5.4-3.9-2.7 5.4-6.4 8.1-11.1 8.1-3.5 0-5.7-1.7-7.4-5.2-1.1-2.3-2.3-3.4-4.1-3.4-2.1 0-3.9 1.3-5.4 3.9Z"/>'''),
    "mongodb": ("#47A248", '''<g fill="#9ECE6A">
      <path d="M37.2 15.8c-.4-.3-1-.3-1.4 0-1.6 1.3-3 3.3-3.9 5.5-1.6 4-2.1 8.7-1.7 13.4.1 1.5.4 3 .8 4.4-.8 1.7-1.2 3.5-1.1 5.3.1 2.4 1.1 4.5 2.8 5.8.4.3 1 .3 1.4 0 1.7-1.3 2.7-3.4 2.8-5.8.1-1.8-.3-3.6-1.1-5.3.4-1.4.7-2.9.8-4.4.4-4.7-.1-9.4-1.7-13.4-.9-2.2-2.3-4.2-3.9-5.5Z"/>
      <path d="M36 50.5v5.2" stroke="#9ECE6A" stroke-width="2.2" stroke-linecap="round"/>
    </g>'''),
    "mysql": ("#4479A1", monogram("My", "#7AA2F7", 20)),
    "mssql": ("#CC2927", monogram("SQL", "#F7768E", 18)),
    "postgresql": ("#4169E1", '''<g fill="#7AA2F7">
      <path d="M36 16c-8.8 0-12.5 4.4-12.5 8.2 0 2.4 1.4 5.7 5.2 7.3l.7 6.4c-2.5.8-4 2.3-4 4.2 0 3.3 4.2 5.5 10.6 5.5s10.6-2.2 10.6-5.5c0-1.9-1.5-3.4-4-4.2l.7-6.4c3.8-1.6 5.2-4.9 5.2-7.3C48.5 20.4 44.8 16 36 16Zm-5.8 8.1c0-1.5 1.3-2.6 3-2.6s3 1.1 3 2.6-1.3 2.6-3 2.6-3-1.1-3-2.6Zm11.6 0c0 1.5-1.3 2.6-3 2.6s-3-1.1-3-2.6 1.3-2.6 3-2.6 3 1.1 3 2.6Z"/>
    </g>'''),
    "git": ("#F05032", '''<g fill="#F7768E">
      <path d="M48.8 34.7 37.3 23.2a3.2 3.2 0 0 0-4.5 0l-2.7 2.7 3.5 3.5a2.6 2.6 0 0 1 3.2 3.3l3.4 3.4a2.6 2.6 0 1 1-1.6 1.5l-3.3-3.3v8.8a2.6 2.6 0 1 1-1.7.1V34.4a2.6 2.6 0 0 1-1.4-3.4l-3.4-3.4-9 9a3.2 3.2 0 0 0 0 4.5l11.5 11.5a3.2 3.2 0 0 0 4.5 0l11.5-11.5a3.2 3.2 0 0 0 0-4.5Z"/>
    </g>'''),
    "postman": ("#FF6C37", '''<g fill="#FF9E64">
      <circle cx="36" cy="36" r="16"/>
      <path fill="#1a1b27" d="M24.5 34.2c4.8-1.2 14.4-2.4 22.8 1.1-2.1 1.6-5.2 3.4-8.4 4.2-4.8-3.6-10.2-4.5-14.4-5.3Z"/>
    </g>'''),
    "shadcn": ("#C0CAF5", '''<g fill="none" stroke="#C0CAF5" stroke-width="3.2" stroke-linecap="round">
      <path d="M26 28 36 18l10 10"/>
      <path d="M26 44 36 54l10-10"/>
      <path d="M30 36h12"/>
    </g>'''),
    "antd": ("#0170FE", '''<g fill="#7AA2F7">
      <path d="M36 17 20 46h8.4l2.1-4.2h10.9L45.6 46H54L36 17Zm0 10.2 4.2 8.4H31.8L36 27.2Z"/>
    </g>'''),
    "mui": ("#007FFF", '''<g fill="none" stroke="#7AA2F7" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      <path d="M20 42V28l8 8 8-10v16"/>
      <path d="M44 28v14"/>
      <circle cx="44" cy="24" r="2.2" fill="#7AA2F7" stroke="none"/>
    </g>'''),
    "jest": ("#C21325", monogram("J", "#F7768E", 28)),
    "playwright": ("#2EAD33", '''<g fill="#9ECE6A">
      <circle cx="28" cy="30" r="8" fill="none" stroke="#9ECE6A" stroke-width="2.4"/>
      <circle cx="44" cy="30" r="8" fill="none" stroke="#9ECE6A" stroke-width="2.4"/>
      <circle cx="28" cy="30" r="2.4"/>
      <circle cx="44" cy="30" r="2.4"/>
      <path d="M24 44c2.5-3 6-4.5 12-4.5S45.5 41 48 44" fill="none" stroke="#9ECE6A" stroke-width="2.4" stroke-linecap="round"/>
    </g>'''),
}


def write_icons(mapping: dict, out_dir: Path, delay_step: float = 0.12) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, (slug, (accent, inner)) in enumerate(mapping.items()):
        path = out_dir / f"{slug}.svg"
        path.write_text(tile(slug, accent, inner, delay=round(i * delay_step % 1.8, 2)), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


def main() -> None:
    write_icons(SOCIAL, SOCIAL_DIR, delay_step=0.18)
    write_icons(SKILLS, SKILLS_DIR, delay_step=0.08)
    print(f"done: {len(SOCIAL)} social + {len(SKILLS)} skill icons")


if __name__ == "__main__":
    main()
