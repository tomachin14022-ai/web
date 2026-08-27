---
name: flutter-ui-animations
description: >
  Flutter UI and animation patterns — AnimationController, Tween/CurvedAnimation,
  AnimatedBuilder, implicit animations, CustomPainter, staggered timelines, glassmorphism,
  particles, and 3D transforms. Use when building animated Flutter widgets, transitions,
  loaders, micro-interactions, custom-painted effects, or polished screen UIs. Backed by
  189 runnable example screens under examples/.
---

# Flutter UI & Animations

Practical patterns for building animated, polished Flutter UI. The skill ships **189 self-contained
example screens** under `examples/` (one Dart file each). When a request matches an example, read that
file for a complete, working implementation and adapt it — don't reinvent it. Browse
`reference/examples-index.md` to find the closest example by category.

## Quick Start — an explicit animation

```dart
class PulseBox extends StatefulWidget {
  const PulseBox({super.key});
  @override
  State<PulseBox> createState() => _PulseBoxState();
}

class _PulseBoxState extends State<PulseBox> with SingleTickerProviderStateMixin {
  late final AnimationController _controller = AnimationController(
    duration: const Duration(seconds: 2),
    vsync: this,
  )..repeat(reverse: true);

  late final Animation<double> _scale = Tween(begin: 0.9, end: 1.1).animate(
    CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
  );

  @override
  void dispose() {
    _controller.dispose(); // ALWAYS dispose controllers
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _scale,
      builder: (context, child) => Transform.scale(scale: _scale.value, child: child),
      child: const FlutterLogo(size: 120), // built once, not rebuilt each frame
    );
  }
}
```

## Core building blocks

- **`AnimationController`** — the clock. Needs a `vsync` (`SingleTickerProviderStateMixin` for one
  controller, `TickerProviderStateMixin` for several). Drives values 0→1 over a `Duration`. Methods:
  `forward()`, `reverse()`, `repeat(reverse: true)`, `stop()`, `..value = x`.
- **`Tween<T>`** — maps 0→1 to a value range (`Tween(begin:, end:)`, `ColorTween`, `AlignmentTween`,
  `Tween<Offset>`). Combine with `.animate(controller)`.
- **`CurvedAnimation`** — applies easing (`Curves.easeInOut`, `elasticOut`, `bounceOut`,
  `easeOutCubic`). Wrap the controller before the tween for non-linear motion.
- **`AnimatedBuilder` / `ListenableBuilder`** — rebuilds only its `builder` on each tick; pass static
  subtrees via the `child` argument so they're built once.
- **Implicit animations** — no controller needed for simple state→state tweens:
  `AnimatedContainer`, `AnimatedOpacity`, `AnimatedAlign`, `AnimatedPositioned`,
  `AnimatedSwitcher`, `TweenAnimationBuilder`. Reach for these first; drop to a controller only when
  you need looping, staggering, or fine control.

## Common patterns

**Staggered timeline** — one controller, multiple `Interval` curves:
```dart
final fade = CurvedAnimation(parent: c, curve: const Interval(0.0, 0.5, curve: Curves.easeOut));
final slide = Tween(begin: const Offset(0, .3), end: Offset.zero)
    .animate(CurvedAnimation(parent: c, curve: const Interval(0.4, 1.0, curve: Curves.easeOutCubic)));
```

**Custom-painted effects** — `CustomPaint(painter: MyPainter(progress: anim.value))`; repaint by
passing the animation to `super(repaint: animation)` in the painter and reading `animation.value` in
`paint()`. Used across the particle, wave, and progress examples.

**Glassmorphism** — `BackdropFilter(filter: ImageFilter.blur(sigmaX: 15, sigmaY: 15))` inside a
`ClipRRect`, over a semi-transparent gradient `Container` with a subtle white border. See
`examples/76-glass-morphism-effect-ui/`, `examples/96-liquid-glass-effect-ui/`.

**3D transforms** — `Transform(transform: Matrix4.identity()..setEntry(3, 2, 0.001)..rotateY(angle))`
for perspective flips and tilt cards. See `examples/18-flip-card/`, `examples/72-animated-3d-card-effect/`.

**Physics / gestures** — `GestureDetector` feeding a controller, or `AnimationController.animateWith(
SpringSimulation(...))` for spring-back. Drag, throw, and trail examples live under the
Particles & Physics group in the index.

## Finding the right example

`reference/examples-index.md` groups all 189 screens: Loaders & Spinners, Text & Typography,
Buttons & Toggles, Cards & 3D, Glassmorphism & Neon, Forms & Inputs, Feedback & Micro-interactions,
Navigation & Transitions, Lists & Scroll, Dashboards & App UIs, Particles & Physics, and Other Effects.
Match the user's ask to a group, open the listed Dart file, and adapt it.

## Performance tips

- Scope rebuilds: give `AnimatedBuilder` a `child` for anything static; never rebuild the whole screen
  per frame.
- Prefer implicit animations and `TweenAnimationBuilder` for simple cases — less code, fewer leaks.
- **Always `dispose()`** every `AnimationController` (and `TabController`, `ScrollController`).
- Use `const` constructors aggressively so Flutter can skip rebuilding unchanged subtrees.
- Keep `CustomPainter.shouldRepaint` honest — return `false` when nothing relevant changed.
- Avoid allocating objects (Paint, Path, gradients) inside `paint()` hot paths where you can hoist them.
- Test animation-heavy screens on a real device / profile mode, not just debug.

## See also

- `motion-design` — timing, easing, choreography, and Disney principles for deciding *how* motion
  should feel (framework-agnostic); pair it with this skill's Flutter mechanics.
