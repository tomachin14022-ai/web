---
name: web-animation-resources
description: >
  Curated map of web animation and motion-UI resources — CSS/JS/SVG animation libraries,
  easing and timing tools, inspiration galleries, performance guidance, and learning material.
  Use when choosing an animation library or tool for the web, looking for motion-design
  inspiration or references, or advising on web animation performance. Backed by two curated
  lists under reference/ (motion-ui-design, awesome-css-animations).
---

# Web Animation Resources

A curated index to help pick the right tool and reference for **web** motion/UI animation work.
Two source lists are bundled under `reference/`:

- `reference/motion-ui-design.md` — the broad list: inspiration sites, articles, software,
  libraries (CSS/JS/SVG), performance, guidelines, books.
- `reference/awesome-css-animations.md` — a short, high-signal list of CSS animation libraries/tools.

Open the relevant reference file for the full, link-rich catalog. The summaries below are the
fast path for common asks.

## Picking a library

**CSS-first / drop-in**
- **Animate.css** — ready-made "just add a class" animations. Great for quick entrance/attention effects.
- **Animista** — generate exactly the CSS keyframes you want, copy-paste.
- **AniCollection** — browsable copy-paste animation collection.
- **SpinKit / css-spinner / Epic spinners** — pure-CSS loading spinners.

**JavaScript engines (fine control, timelines, sequencing)**
- **anime.js** — lightweight, timeline-based; tweens CSS, SVG, DOM attributes, JS objects.
- **GSAP** — the industrial-strength standard: timelines, ScrollTrigger, morphing, robust cross-browser.
- **Framer Motion** (React), **Motion One** (Web Animations API), **Velocity**, **popmotion** — see the list.

**SVG**
- **Snap.svg**, **SVG.js**, **Vivus** (line-drawing), **anime.js** — see `reference/motion-ui-design.md` → Libraries → SVG.

**Guideline**: prefer CSS transitions/keyframes for simple state changes and micro-interactions;
reach for a JS engine (GSAP, anime.js) when you need sequencing, scroll-driven motion, physics, or
runtime-computed values.

## Inspiration & references

Codrops (Tympanus), CodyHouse, Dribbble (animated), CodePen, Awwwards, cssanimation.rocks — full,
annotated list in `reference/motion-ui-design.md` under *Resources for inspiration*.

## Performance

The list's *Web animation performance* section is the canonical reference. Core rules:

- Animate only **`transform`** and **`opacity`** — they're GPU-composited and skip layout/paint.
- Avoid animating layout-triggering properties (`width`, `height`, `top`, `left`, `margin`) — they
  force reflow every frame.
- Promote a layer deliberately with `will-change: transform` (sparingly — each layer costs memory).
- Prefer `requestAnimationFrame` / the Web Animations API over `setInterval` for JS-driven motion.
- Keep animations ≤ 16ms/frame; profile with DevTools' Performance panel and the FPS meter.

## See also

- `motion-design` — the *principles* (timing, easing, choreography, Disney) behind good motion,
  framework-agnostic. Use it to decide how motion should feel; use this skill to pick what to build it with.
- `design-dna` — extract and apply design identity (including visual effects) from references.
