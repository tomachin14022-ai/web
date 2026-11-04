# Golf swing biomechanics: measurable parameters and reference (normative) values

> Scope notes for the report writer. Researched 04/11/2026.
> Conventions: values are copied as reported (sign conventions differ between sources; each one is stated). Inches converted to cm (×2.54) in brackets.
> Source quality tags: **[PEER]** peer-reviewed journal paper · **[CONF]** conference proceedings (ISBS) / preprint · **[VENDOR]** company data or marketing (HackMotion, Sportsbox, K-Motion) · **[MEDIA]** golf media citing vendor data · **[FORUM]** user post · **[UNVERIFIED]** seen only in a search snippet, or page now unreachable.
> Measurement systems: optical marker 3D mocap (Motion Analysis, Peak Motus, Vicon, GEARS) · IMU/electromagnetic sensors (K-Vest, HackMotion wrist sensor) · markerless AI from phone video (Sportsbox AI) · club-mounted accelerometers (Grober).
> Cross-source warning (applies to every table): the same word ("pelvis rotation", "X-factor") means different things in different systems. Example: in one 7-handicap golfer, the 3D shoulder-vs-pelvis rotation at the top with a driver was −71.9° with a ZYX Cardan sequence and −123.5° with a ZXY sequence ([Joyce et al. 2010, Sports Biomech, PDF](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Joyce%202010%20Methodological%20considerations%20for%20the%203D%20measurement%20of%20the%20X-factor.pdf)). Horizontal-plane projections (Meister, Myers) give much smaller X-factor values (~45–60°). Never mix numbers from different systems in one judgement.

## 1. Pelvis and thorax/shoulder rotation at top and impact; X-factor and X-factor stretch (tour vs amateur)

### Takeaway
Tour-level full swings show roughly 90–106° of chest/upper-torso turn and 33–50° of pelvis turn at the top (separation ≈55–69°), with the pelvis more open than the chest at impact (pelvis ≈30–45° open, chest ≈20–34° open). Separation (X-factor) at the top and its increase early in the downswing (stretch) are the rotational variables that best separate faster/better players. Pelvis turn on its own does not.

### Cited Findings

**A. Meister et al. 2011, J Appl Biomech 27:242–251 [PEER]**: 10 male tour/teaching professionals (age 31 ± 5.9) vs 5 amateurs (hcp 4, 15, 30, 2 novices). Own **5-iron**, easy/medium/hard swings. 8-camera Motion Analysis optical system, **240 Hz**, 42 markers. Definitions: pelvic and upper-torso rotation "with respect to the intended line of flight and projected into the horizontal plane". X-factor = angle between the ASIS–ASIS line and the acromion–acromion line, projected into the horizontal plane. O-factor = 3D ASIS line vs horizontal (pelvic obliquity). S-factor = 3D acromion line vs horizontal (shoulder obliquity). Impact = frame before the ball starts to move. ([PDF](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Meister%20-%20Rotational%20Biomechanics%20of%20the%20Elite%20Golf%20Swing.pdf))

| Parameter (5-iron) | Pros, hard swing (mean ± SD) | Hcp 4 | Hcp 15 | Hcp 30 | Novice 1 | Novice 2 |
|---|---|---|---|---|---|---|
| Clubhead speed at impact (m/s) | 35.4 ± 2.1 | 34.0 | 34.2 | 29.3** | 30.2** | 25.2** |
| Peak upper-torso rotation (°) | 99 ± 6 | 90* | 104 | 107* | 79** | 91* |
| Peak pelvic rotation (°) | 46 ± 6 | 41 | 53* | 59** | 39* | 49 |
| Peak X-factor (°) | 56 ± 4 | 52 | 54 | 48** | 46** | 46** |
| X-factor at impact (°) | 33 ± 6 | 33 | 23* | 23* | 25* | 1** |
| S-factor (shoulder obliquity) at impact (°) | 25 ± 3 | 21* | 19** | 21* | 27 | 12** |
| Peak S-factor (°) | 48 ± 4 | 47 | 42* | 50 | 42* | 33** |
| O-factor (pelvic obliquity) at impact (°) | 12 ± 3 | 18** | 5** | 3** | 15 | –7** |
| Peak O-factor (°) | 16 ± 4 | 19 | 13 | 12* | 17 | 8** |
(*1–2 SD from the pro mean; **≥2 SD. Source table: "Table 4". Easy/medium/hard pro peak X-factor 52/54/56°, X-factor at impact 24/28/33°.)
- Peak X-factor varied only ~7.4 % (coefficient of variation) among pros. Within-subject correlations with clubhead speed: peak X-factor ρ median 0.900, X-factor at impact 0.943, peak upper-torso rotation 0.900, peak pelvic rotation only 0.572 ([Meister 2011](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Meister%20-%20Rotational%20Biomechanics%20of%20the%20Elite%20Golf%20Swing.pdf)).
- Peak X-factor happened "in late backswing or early downswing", before peak free moment. This is the X-factor-stretch timing ([Meister 2011](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Meister%20-%20Rotational%20Biomechanics%20of%20the%20Elite%20Golf%20Swing.pdf)).

**B. Myers et al. 2008, J Sports Sci 26(2):181–188 [PEER]**: 100 recreational golfers with a USGA handicap, own **driver**. Peak Motus 8 optical cameras, **200 Hz**. Rotation = segment angle vs the global x-axis, set so that address = 0°. Backswing rotation is negative. Separation = pelvis minus upper torso. "Maximum torso–pelvic separation… during the downswing… representative of 'x-factor stretch'". Groups by ball speed. ([PDF](https://chs.uky.edu/sites/default/files/2023-12/Myers_2008_Role%20of%20upper%20torso%20and%20pelvis%20during%20golf%20swing.pdf))

| Driver (mean ± SD) | Low ball speed (n=21, hcp 15.1 ± 5.2) | Medium (n=65, hcp 7.8 ± 6.9) | High (n=14, hcp 1.8 ± 3.2) |
|---|---|---|---|
| Ball speed (m/s) | 55.7 ± 2.7 | 65.6 ± 3.7 | 75.4 ± 4.4 |
| Upper torso rotation at top (°) | −94.0 ± 13.5 | −97.0 ± 20.2 | −104.0 ± 10.3 |
| Pelvic rotation at top (°) | −49.8 ± 11.4 | −47.5 ± 17.4 | −44.9 ± 10.3 |
| Separation (X-factor) at top (°) | −44.2 ± 7.7 | −49.5 ± 9.6 | −59.1 ± 8.2 (p < 0.0001) |
| Max separation in downswing (X-factor stretch) (°) | −45.6 ± 8.0 | −51.7 ± 10.3 | −61.8 ± 7.8 (p < 0.0001) |
| Upper torso rotation at lead-arm parallel (°) | −36.1 ± 9.1 | −39.6 ± 15.9 | −37.4 ± 9.4 |
| Pelvic rotation at lead-arm parallel (°) | −4.3 ± 7.4 | −1.3 ± 16.6 | +6.4 ± 7.2 |
| Upper torso rotation at impact (°, + = open) | 20.3 ± 10.2 | 22.8 ± 16.1 | 25.2 ± 8.9 |
| Pelvic rotation at impact (°, + = open) | 29.4 ± 8.6 | 35.3 ± 17.0 | 38.3 ± 7.2 |
- Upper torso and pelvic rotation at the top did NOT differ between groups (p = 0.264 and 0.660). Separation did ([Myers 2008](https://chs.uky.edu/sites/default/files/2023-12/Myers_2008_Role%20of%20upper%20torso%20and%20pelvis%20during%20golf%20swing.pdf)).
- (Note: the PDF text layer renders "−" as "7" and "°" as "8"; the values above were decoded from that.)

**C. Cheetham et al. 2001, "The importance of stretching the X-factor in the downswing of golf: the X-factor stretch" (Optimising Performance in Golf, pp. 192–199) [book chapter, abstract only]**: X-factor stretch happened early in the downswing in both groups but was "significantly greater for the highly skilled players (19%) than the less skilled golfers (13%)". X-factor at the top was similar between groups ([abstract, bepress](https://works.bepress.com/philip_martin/5/)). The 2001 chapter reportedly used a 5-iron; full text not checked.

**D. Zheng et al. 2008, Int J Sports Med 29:487–493 [PEER, abstract only]**: 18 pros + 18 low + 18 mid + 18 high handicap golfers, optoelectronic system, 240 fps. At the top, pros had the largest left-shoulder horizontal adduction, right-shoulder external rotation and "trunk rotation (125 ± 6°, 66 ± 11°, and 60 ± 7°, respectively)". Mid and high handicaps showed "flawed swing mechanics" ([abstract](https://www.bisp-surf.de/Record/PU200809002851)). Full table by handicap not retrieved.
- Zheng et al. 2008 (male vs female pros, IJSM 29:965–970): pelvis rotation at impact "LPGA: −52 ± 11° and PGA: −42 ± 12°" ([Thieme abstract page](https://thieme-connect.de/products/ejournals/html/10.1055/s-2008-1038732)). Seen in a snippet; sign convention not verified.

**E. Sportsbox AI [VENDOR/MEDIA]**: markerless 3D estimated by AI from phone video. Turn is measured from the target line, address = reference ([App Store listing](https://apps.apple.com/au/app/id1578921026)).
- Golf Digest (Kerr-Dineen, 01/11/2024) on Sportsbox tour data: chest turn at the top "−98 degrees and −102 degrees" (male/female tour averages). Pelvis about −40° at the top. At impact the pelvis is ~40° open vs chest ~30° open. Sample and club not stated ([Australian Golf Digest mirror](https://www.australiangolfdigest.com.au/useful-golf-swingfacts-sportsbox-ai-graph); [original, 403 when fetched](https://www.golfdigest.com/story/useful-golf-swingfacts-sportsbox-ai-graph)).
- GOLF.com: pelvis more open than chest at impact is "seen in 100 percent of Tour players, according to Sportsbox AI data" (irons) ([GOLF.com](https://golf.com/instruction/three-musts-solid-ball-striking-sportbox-ai-playsmart/)).
- Japanese Golf Digest (Sportsbox data): chest turn at impact for overseas male tour players "26 to 34 degrees" open [UNVERIFIED, snippet only] ([golfdigest-minna.jp](https://www.golfdigest-minna.jp/_ct/17859011)).
- "Swing Score Reports" in Sportsbox format list "Tour Range" values (apparently mean ± 1 SD of the "Sportsbox tour database"). They are hosted on an unofficial file host, so the producer is not confirmed [VENDOR, UNVERIFIED host]:

| Sportsbox "Tour Range" | Male, 6-iron ([D1 report](https://moccasin-micheline-88.tiiny.site/D1-Male-Player-Swing-Score-Report.pdf)) | Male, driver ([Bryson report](https://moccasin-micheline-88.tiiny.site/Bryson-Driver-Swing-Score-Report-1.pdf)) | Female LPGA, driver ([LPGA report](https://moccasin-micheline-88.tiiny.site/LPGA-Tour-Player-Swing-Score-Report.pdf)) |
|---|---|---|---|
| Chest turn max (°) | 90–100 | 94–106 | 96–110 |
| Pelvis turn max (°) | 33–43 | 39–47 | 41–50 |
| X-factor max (°) | 59–69 | 59–68 | 58–67 |

**F. Method dependence [PEER]**: Joyce et al. 2010 (1 golfer, hcp 7, driver and 5-iron, Vicon 250 Hz + Fastrak electromagnetic): with the recommended ZYX sequence (lateral bend → flexion → axial rotation), shoulder-vs-pelvis rotation at the top was −71.9° (driver) and −70.3° (5-iron), and at impact −17.8° and −27.4°. Other sequences gave values from −17.2° to −123.5° for the same swing ([Joyce 2010](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Joyce%202010%20Methodological%20considerations%20for%20the%203D%20measurement%20of%20the%20X-factor.pdf)).

### Inferences
- Rough consensus for a tour full swing (horizontal-plane or Sportsbox-style turn from address): chest/upper torso ≈90–106° at the top (women slightly more), pelvis ≈33–50°, separation ≈55–69°. At impact the pelvis is ≈30–45° open and the chest ≈20–34° open, so the pelvis leads the chest.
- Myers' stretch increment (max separation − top separation) is small in absolute terms: about 1.4°, 2.2° and 2.7° for the low/medium/high groups (≈3–5 % of the top value), computed from Table II. That does not match Cheetham's 19 % vs 13 %, which suggests a different definition or normalisation. Do not quote "stretch %" without saying whose definition it is.
- Pelvis turn at the top is not a quality marker by itself: high-speed players in Myers had slightly less pelvis turn, and Meister's hcp-30 amateur had more pelvis turn (59°) than the pros.
- Less skilled amateurs often show a SMALLER X-factor at impact (Meister: 23–25° vs pros 33°). That points to the chest "catching up" with the pelvis early (upper body unwinding first).

### Gaps
- Full Cheetham 2001 chapter and Zheng 2008 pro/amateur tables (values by handicap at address/top/impact) were not retrieved.
- No official, publicly documented Sportsbox/GEARS/K-Vest tour-average table with sample size; the Sportsbox numbers come from media articles and reports on an unofficial host.
- Most peer-reviewed tour values are 5-iron (Meister) or recreational driver (Myers); there are no peer-reviewed tour-pro driver vs iron rotation norms with n > 10.

## 2. Sway, thrust, lift (cm) at top and impact; pelvis/thorax bend and side bend; early extension quantified

### Takeaway
At impact, tour pelvises are typically 3–6 in (8–14 cm) toward the target from address (more with irons than driver), while the chest/ribs stay near address with a driver (~1 cm) and move ~6 cm with irons. The pelvis drops early in the downswing and then rises 1.4–4.3 in (4–11 cm) into impact. No published normative value for pelvis "thrust" (early extension, in cm) was found.

### Cited Findings

**GEARS (3D optical capture) tour data, impact (A7), [FORUM]**: 61 swings of men and women tour or ex-tour players: 29 driver, 32 irons (2 wedges). Pelvis sway = movement of the pelvis centre from its address position (0.0"), + toward the target. Axis tilt = face-on angle of the pelvis-centre-to-shoulder-centre line, vertical = 90°, >90° = leaning away from the target ([Sand Trap post](https://thesandtrap.com/forums/topic/111900-gears-pro-data-axis-tilt-vs-pelvis-sway-shift/)):

| At impact | Irons: avg (25th–75th pct) [SD] | Driver: avg (25th–75th pct) [SD] |
|---|---|---|
| Pelvis sway toward target | 4.7" [11.9 cm] (3.2–5.5" [8.1–14.0 cm]) [1.72"] | 3.5" [8.9 cm] (2.4–4.1" [6.1–10.4 cm]) [2.03"] |
| Rib sway (upper body) | 2.3" [5.8 cm] (1.5–3.1") [1.39"] | 0.4" [1.0 cm] (−0.9–0.9") [1.68"] |
| Axis tilt (spine tilt away from target) | 103.9° (101.2–106.5°) [4.42°] | 108.0° (104.0–111.1°) [4.73°] |
- Full ranges were wide: pelvis sway irons 1.6–9.0", driver −0.5–10.8" ([same post](https://thesandtrap.com/forums/topic/111900-gears-pro-data-axis-tilt-vs-pelvis-sway-shift/)).

**Sportsbox AI (markerless) via Golf Digest [MEDIA/VENDOR]**: tour pelvis "moves upwards of five inches [12.7 cm] towards the target by impact" and less than a couple of inches away from the target in the backswing. The chest "sways away from the target just two inches [5 cm] on the takeaway" (driver) and returns near zero. Male pros' "Sway Gap of more than 6.5 inches [16.5 cm] by impact" (pelvis ahead of chest). Chest drops ~2" (5 cm) mid-downswing and rises ~1" at impact. Pelvis is ~2" lower than address early in the downswing and ~1" higher at impact. Chest bend ~30° at setup and impact. Chest side bend ~15° away from the target at setup and >30° at impact. Pelvis side bend: level at setup, about −8° at the top (lead hip lower), about +8° at impact (trail hip lower) ([Australian Golf Digest](https://www.australiangolfdigest.com.au/useful-golf-swingfacts-sportsbox-ai-graph)).
- Sportsbox definition: "Pelvis Sway… using the address position as the 0" reference point" ([App Store listing](https://apps.apple.com/au/app/id1578921026)). Thrust = movement of a segment toward (+) or away from (−) the ball [third-party description, UNVERIFIED] ([vectorgolf-ai](https://vectorgolf-ai.pages.dev/metrics/)).
- GOLF.com: lead hip closer to the target at impact than at address "seen in 100 percent of Tour players swings" (irons) ([GOLF.com](https://golf.com/instruction/three-musts-solid-ball-striking-sportbox-ai-playsmart/)).

**Sportsbox "Tour Range" from reports [VENDOR, UNVERIFIED host]:**

| Tour Range | Male 6-iron ([D1](https://moccasin-micheline-88.tiiny.site/D1-Male-Player-Swing-Score-Report.pdf)) | Male driver ([Bryson](https://moccasin-micheline-88.tiiny.site/Bryson-Driver-Swing-Score-Report-1.pdf)) | LPGA driver ([LPGA](https://moccasin-micheline-88.tiiny.site/LPGA-Tour-Player-Swing-Score-Report.pdf)) |
|---|---|---|---|
| Pelvis slide in transition | 0.6–1.8" (1.5–4.6 cm) | 0.7–2.1" (1.8–5.3 cm) | 0.5–1.3" (1.3–3.3 cm) |
| Chest side (lateral) in transition | 0.6–2.0" (1.5–5.1 cm) | 0.7–2.1" (1.8–5.3 cm) | 0.9–2.1" (2.3–5.3 cm) |
| Pelvis drop (early downswing) | 1.0–2.8" (2.5–7.1 cm) | 1.0–3.2" (2.5–8.1 cm) | 1.1–3.3" (2.8–8.4 cm) |
| Pelvis lift into impact | 1.4–3.8" (3.6–9.7 cm) | 1.9–3.9" (4.8–9.9 cm) | 1.9–4.3" (4.8–10.9 cm) |
- The same reports give the tour "pelvis movement order" in transition as Sway (1) → Turn (2) → Lift (3) ([D1 report](https://moccasin-micheline-88.tiiny.site/D1-Male-Player-Swing-Score-Report.pdf)).

**Peer-reviewed obliquity/side bend (5-iron pros)**: S-factor (shoulder line vs horizontal) at impact 25 ± 3°, peak 48 ± 4°. O-factor (pelvis line vs horizontal) at impact 12 ± 3°, peak 16 ± 4° ([Meister 2011](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Meister%20-%20Rotational%20Biomechanics%20of%20the%20Elite%20Golf%20Swing.pdf)). One golfer (hcp 7): shoulder-vs-pelvis lateral bend at impact −35.4° (driver) and −36.3° (5-iron); flexion −22.5° and −32.5° (ZYX) ([Joyce 2010](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Joyce%202010%20Methodological%20considerations%20for%20the%203D%20measurement%20of%20the%20X-factor.pdf)).

**Early extension**: TPI defines early extension as any movement of the pelvis toward the ball in the backswing or downswing and reports it in 67 % of 90,000 golfers screened. This is TPI's own figure, from the project notes (page read on 04/11/2026, not re-opened here) ([TPI swing characteristics](https://www.mytpi.com/improve-my-game/swing-characteristics)). TPI-related write-up: limited pelvic tilt in the TPI screen gives a "70% chance of… early extension" and top players tilt the pelvis back "up to 20 degrees" in the downswing [secondary, UNVERIFIED] ([Pinnacle Fitness blog](https://pinnaclefitness.squarespace.com/blog/the-power-of-golf-tpi-screen-pelvic-tilt)).

### Inferences
- A practical face-on reference: at impact, pelvis centre ≈ 8–14 cm toward the target with irons and ≈ 6–10 cm with driver (GEARS interquartile range). Chest/rib centre ≈ 4–8 cm (irons) and ≈ −2 to +2 cm (driver). So the pelvis is ahead of the chest at impact (positive "sway gap"). A pelvis that ends at or behind its address position at impact is outside every tour sample cited (hanging back). Very large lateral pelvis shift in the backswing (away from the target) is not tour-like either: Golf Digest says "less than a couple of inches".
- Spine tilt away from the target at impact is larger with driver (≈18° from vertical) than irons (≈14°) in GEARS, consistent with the ball being further forward with driver.
- The "drop then lift" vertical pattern (pelvis ~2.5–8 cm down early in the downswing, then 4–11 cm up into impact) is normal for tour players. Pelvis lift into impact should not be flagged as a fault by itself; the fault is pelvis movement TOWARD THE BALL (thrust/early extension), which these sources do not give in cm.

### Gaps
- No published normative value for pelvis/hip "thrust" (depth toward the ball) at top or impact from Sportsbox, GEARS or peer-reviewed work. Early extension cannot be judged against a tour cm value; it has to be judged against the golfer's own address (e.g. TPI's "tush line").
- GEARS data come from a forum post by a GEARS owner (no system validation or player list). Values at address and top were not posted.
- No peer-reviewed tour value for chest/pelvis forward bend at top/impact in degrees was retrieved (see Q5).

## 3. Knee flexion at address/top/impact (trail and lead); lead-knee extension at impact

### Takeaway
Reliable tour normative knee angles at address and impact were not found in accessible sources. The best number is lead-knee flexion at the top: 35 ± 5° in experienced men vs 17 ± 6° in women (Egret et al. 2006, via a systematic review). Pros vs amateurs differ significantly in lead-knee flexion at impact (Thai 3D study), but the accessible text does not give the values.

### Cited Findings
- Baker et al. 2017 systematic review (Sports Med 47:2621–2639) [PEER]: lead-knee flexion at the top "varied only little across most studies". Knee flexion at impact "remains less clear". The trail knee has a smaller range than the lead knee. Egret et al.: lead-knee flexion at the top: males 35° ± 5°, females 17° ± 6° ([Baker 2017, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5684267/)).
- Egret et al. 2006 (IJSM 27:463–467; 7 male, 5 female experienced golfers, 3D): men bent the lead knee more in the backswing; women had larger hip and shoulder rotation at the top; clubhead speed did not differ ([Thieme abstract](https://thieme-connect.de/products/all/doi/10.1055/s-2005-865818)).
- Somjarod et al. (Thai pros vs amateurs, 3D): "The knee flexion/extension angle of the lead leg in both groups were significantly different at ball contact (p=0.04)". Pros had less lead-leg external rotation ([JSST](https://he01.tci-thaijo.org/index.php/JSST/article/view/44004)). Numeric flexion values not in the accessible text. Axial-rotation values in the review: lead-knee rotation at impact 2° ± 2° vs 10° ± 3° (pros vs amateurs, n = 2 + 2) ([Baker 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5684267/)).
- Sportsbox "pelvis lift into impact" tour range 1.4–3.8" (6-iron) / 1.9–3.9" (driver) [VENDOR, UNVERIFIED host] ([D1](https://moccasin-micheline-88.tiiny.site/D1-Male-Player-Swing-Score-Report.pdf), [Bryson](https://moccasin-micheline-88.tiiny.site/Bryson-Driver-Swing-Score-Report-1.pdf)) is the closest quantified proxy for lead-leg extension into impact.

### Inferences
- Lead-knee straightening into impact is normal in tour swings: it is consistent with the pelvis rising 4–10 cm into impact (Sportsbox) and with the ground-force "lift" pattern. A straightening lead knee at P7 should not be called a fault. A trail knee that collapses toward the ball, or loss of flex in the trail knee in the backswing, can be described relative to the golfer's own address angle.

### Gaps
- No accessible table of tour knee flexion at address (trail/lead), at the top (trail) or at impact (lead), by club. The Egret 2003/2006 and Somjarod full texts were not retrieved (paywall / HTML only).

## 4. Head movement (lateral, vertical, depth) in pros

### Takeaway
Skilled golfers' heads do move. In the only quantified skill comparison found (driver), category-1 golfers (hcp ≈4.5) moved the head ~5.5 cm away from the target at the top and finished ~3 cm behind address at impact. Mid-handicaps moved it ~12 cm at the top and were still ~5 cm toward the target at impact. Tour chest (≈ head carrier) sway is ~5 cm away from the target on the takeaway with driver.

### Cited Findings
- Byrne & Kenny 2008, ISBS [CONF, preliminary]: 8 males: 4 category 1 (hcp 4.5 ± 0.5), 4 category 3&4 (hcp 17.8 ± 1.3). Own **driver**, 7 trials. Motion Analysis 6 cameras, **200 Hz**. Head movement "defined as a movement away from the initial address position… in millimetres". Frontal plane (x-axis): top of backswing 54.66 (±29.56) mm vs 123.68 (±17.22) mm; impact −31.18 (±8.89) mm vs 52.33 (±5.71) mm (cat 1 vs cat 3&4). "Sagittal plane (y-axis)" at the top: 19.66 (±21.01) mm vs 117.8 (±37.59) mm ([ISBS 2008](https://ojs.ub.uni-konstanz.de/cpa/article/view/1991/1859)).
- Sportsbox tour data: chest sways ~2" (5 cm) away from the target on the takeaway with driver, then back near zero. The chest drops ~2" mid-downswing and rises ~1" at impact ([Australian Golf Digest](https://www.australiangolfdigest.com.au/useful-golf-swingfacts-sportsbox-ai-graph)).
- GEARS rib sway at impact: driver avg 0.4" (1 cm), irons 2.3" (5.8 cm) toward the target ([Sand Trap](https://thesandtrap.com/forums/topic/111900-gears-pro-data-axis-tilt-vs-pelvis-sway-shift/)).

### Inferences
- A tour-like face-on pattern: the head shifts a few cm away from the target in the backswing (≈3–6 cm) and is at or slightly behind its address position at impact, especially with driver. Head movement ≥10 cm at the top, or the head ahead of address at impact with driver, matches the less-skilled group. These are inferences from an n = 8 study plus vendor chest data, not norms.

### Gaps
- No peer-reviewed tour-professional head displacement in cm (lateral, vertical, depth) with n > 8 was found. Sportsbox/GEARS head-specific tour ranges were not found publicly.

## 5. Spine angle / forward bend at address and its change; side tilt at address and impact

### Takeaway
Tour chest forward bend is ≈30° at setup and again at impact (Sportsbox), with most of it lost at the top and after impact. Side tilt away from the target is ≈15° at setup and >30° at impact (chest side bend), or ≈14° (irons) and ≈18° (driver) using GEARS' pelvis-to-shoulder "axis tilt". Values depend heavily on definition (chest segment vs spine line vs trunk from hip).

### Cited Findings
- Sportsbox (Golf Digest): chest bend about 30° at setup and impact. Chest side bend ~15° away from the target at setup and >30° at impact ([Australian Golf Digest](https://www.australiangolfdigest.com.au/useful-golf-swingfacts-sportsbox-ai-graph)). Sportsbox sign: negative chest bend = chest arched back, positive = bent forward [snippet] ([golfdigest-minna.jp](https://www.golfdigest-minna.jp/_ct/17744052)).
- GEARS axis tilt at impact (vertical = 90°): irons 103.9° avg (IQR 101.2–106.5°), driver 108.0° (IQR 104.0–111.1°) ([Sand Trap](https://thesandtrap.com/forums/topic/111900-gears-pro-data-axis-tilt-vs-pelvis-sway-shift/)).
- Meister 2011 S-factor (shoulder obliquity) at impact, 5-iron pros: 25 ± 3° ([Meister](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Meister%20-%20Rotational%20Biomechanics%20of%20the%20Elite%20Golf%20Swing.pdf)).
- Yamamoto et al. 2023 (27 university golfers, 7-iron, single 240 Hz down-the-line camera, HRNet 2D pose): forward tilt angle range 45–60° (their 2D definition). The SD of forward tilt across shots correlated with average score (r = 0.801), i.e. less consistent posture went with worse scores ([Frontiers 2023](https://frontiersin.org/articles/10.3389/fspor.2023.1272038/full)).
- Nozawa et al. 2012 (5 female pros, driver/5-iron/9-iron, 250 Hz): forward tilt of the upper body changes across address/top/impact (reported only in a figure). Stance width / body height 30.2 ± 2.6 % (driver), 26.8 ± 2.7 % (5-iron), 26.0 ± 2.0 % (9-iron) ([ISBS 2012](https://ojs.ub.uni-konstanz.de/cpa/article/view/5236)).
- Within-golfer consistency at tour level (Sportsbox report, one tour player's driver swings): SD of chest bend 1.2° at address and 0.4° at impact; chest turn SD 0.3° at impact ([Bryson report](https://moccasin-micheline-88.tiiny.site/Bryson-Driver-Swing-Score-Report-1.pdf)) [VENDOR, single player].

### Inferences
- For 2D down-the-line judging, the most defensible criterion is CHANGE in trunk forward angle from the golfer's own address to impact, not an absolute norm. Tour players return to roughly their setup bend at impact (Sportsbox ~30° → ~30°). The 2D "trunk vs vertical" number is not comparable to Sportsbox's "chest bend" (different segment and method); Yamamoto's 45–60° shows how definitions shift the absolute value.
- Face-on side tilt at impact should be larger with driver than irons (GEARS +4° on average).

### Gaps
- No peer-reviewed tour forward-bend (spine/trunk flexion) values in degrees at address/top/impact by club were retrieved. Nozawa's values are only in a figure.
- No official Sportsbox tour table for chest/pelvis bend.

## 6. Shaft lean at impact (irons vs driver); hand position; dynamic loft

### Takeaway
No primary (peer-reviewed or published launch-monitor/3D) tour average for shaft lean in degrees was found. Secondary sources agree on forward lean with irons and wedges ("10–15°" for the best wedge players, per Titleist) and roughly neutral lean with driver. Hand/pelvis position ahead of address at impact is universal on tour (Sportsbox).

### Cited Findings
- Titleist: "the best players in the world lean the shaft forward at impact by 10°-15°" (distance wedges) [secondary] ([Titleist Tips](https://www.titleist.com/teamtitleist/b/tourblog/posts/titleist-tips-lean-the-shaft-for-more-consistent-distance-wedges)).
- HackMotion: with driver, "very little or almost no shaft lean" is acceptable. Pros reduce lead-wrist extension by about 20–25° from the top toward impact (vendor data, ">1,000,000 swings") ([HackMotion](https://hackmotion.com/shaft-lean-at-impact/)).
- CaddieHQ worked example: a 32° 7-iron delivered with ~24° dynamic loft through forward shaft lean (illustrative, not data) [secondary] ([CaddieHQ](https://www.caddiehq.com/resources/what-is-dynamic-loft-in-golf)).
- Sportsbox: lead hip closer to the target at impact than at address in "100 percent of Tour players" (irons). Golf Digest summary: shaft lean comes from the body being more forward at impact, not from pushing the hands ([GOLF.com](https://golf.com/instruction/three-musts-solid-ball-striking-sportbox-ai-playsmart/); [Golf Digest](https://www.golfdigest.com/story/low-handicap-swing-breakthrough-shaft-lean-lag-golfiq)).
- HackMotion tour player (3-iron): lead wrist at impact 1° extended ("almost perfectly flat"), typical tour range +10° to −10° ([HackMotion PGA Tour data](https://hackmotion.com/learn-from-pga-tour-player-wrist-data)).

### Inferences
- Approximate relation (an approximation, not from a source): dynamic loft ≈ static loft − forward shaft lean (plus or minus wrist/face rotation and shaft bend). On face-on 2D video, shaft lean at P7 can be estimated as the angle of the shaft from vertical. It is reliable only if the camera is perpendicular to the target line at hand height and the frame is the real impact frame (≥240 fps helps). Judge irons as "forward lean present / absent / backward". Treat driver near 0° (or slightly forward or back) as normal.

### Gaps
- No primary tour shaft-lean dataset (GEARS, Sportsbox, TrackMan dynamic loft by club) was accessible. Do not publish a degree "norm" for shaft lean.

## 7. Kinematic sequence and peak rotational speeds (pelvis, thorax, arm, club); can it be inferred from 2D?

### Takeaway
Pros peak in proximal-to-distal order (pelvis → thorax → arm → club) and reach higher peak speeds than amateurs. Values depend on method: the IMU/markerless global speeds are larger than horizontal-plane rotation rates. Roughly, tour men peak at ≈370–540 °/s (pelvis), ≈640–860 °/s (chest), ≈880–1230 °/s (arm) and ≈1960–2360 °/s (club/shaft) depending on club. 2D video cannot measure these speeds.

### Cited Findings
- Myers 2008 (driver, 100 recreational, horizontal-plane rotation rate, 200 Hz). Max upper-torso velocity 591.2 ± 66.8 / 675.1 ± 84.4 / 766.6 ± 73.0 °/s and max pelvis velocity 357.6 ± 58.3 / 410.4 ± 66.4 / 433.6 ± 90.9 °/s (low/medium/high ball-speed groups). Max separation velocity 278.1 / 311.8 / 389.6 °/s. Upper-torso velocity at lead-arm parallel was the strongest correlate of ball speed (r = 0.61) ([Myers 2008](https://chs.uky.edu/sites/default/files/2023-12/Myers_2008_Role%20of%20upper%20torso%20and%20pelvis%20during%20golf%20swing.pdf)).
- Zhou et al. 2022 (same Stanford 10 pros as Meister, 5-iron, 240 Hz optical, horizontal-plane): peak downswing rotational velocity: upper torso 551.7 ± 47.6 °/s, pelvis 415.2 ± 32.9 °/s. At impact: 458.5 ± 73.0 and 288.8 ± 70.9 °/s. Follow-through upper torso 929.2 ± 185.1 °/s ([Frontiers 2022](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2022.986281/pdf)).
- Callaway et al. 2012 (K-Vest IMU, 7/8-iron): peak pelvis rotation speed 503.21 °/s in low handicaps (<5, n = 38) vs 380.06 °/s in high handicaps (≥18, n = 18). Cites Cheetham et al. 2008: professionals 477 ± 53 °/s vs amateurs 395 ± 53 °/s (p = 0.011) ([IJSPT 2012, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3362989)).
- Sportsbox "Tour Range" [VENDOR, UNVERIFIED host]:

| Peak speed (°/s) | Male 6-iron ([D1](https://moccasin-micheline-88.tiiny.site/D1-Male-Player-Swing-Score-Report.pdf)) | Male driver ([Bryson](https://moccasin-micheline-88.tiiny.site/Bryson-Driver-Swing-Score-Report-1.pdf)) | LPGA driver ([LPGA](https://moccasin-micheline-88.tiiny.site/LPGA-Tour-Player-Swing-Score-Report.pdf)) |
|---|---|---|---|
| Pelvis | 366–470 | 440–543 | 413–498 |
| Chest | 637–729 | 754–857 | 702–794 |
| Arm | 880–1050 | 1046–1231 | 897–1059 |
| Shaft (club) | 1958–2262 | 2054–2356 | 1734–1958 |
| Transition order | Pelvis 1 → Chest 2 → Arm 3 → Club 4 | same | same |
- K-Motion (TPI kinematic sequence page, now redirects elsewhere): efficient speed gains > 250 °/s pelvis→torso, > 250 °/s torso→arm, > 500 °/s arm→hand, varying "with the size and age of the player". A rule of thumb of pelvis > 500, torso > 700, arm > 1100 °/s for mature elite players was reported in one search summary [VENDOR, UNVERIFIED] ([k-motion.com](https://www.k-motion.com/TPI-Kinematic-Sequence)).
- Phil Cheetham (AMM3D, TPI 3D protocol): in pros each peak occurs later than the previous one (pelvis, thorax, lead arm, club). The pelvis decelerates before impact. The club peaks at about impact ([Cheetham blog 2009](https://philcheethamthe3dguy.blogspot.com/2009/11/kinematic-sequence-signature-of.html)). Zhou 2022 notes that Cheetham's group found the timing of peaks is partly "participant-specific" ([Frontiers 2022](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2022.986281/pdf)).
- Skilled golfers' wrist peaks (driver, Vicon 400 Hz, n = 10, hcp 2.7): lead-wrist flexion 636 ± 213 °/s, lead ulnar deviation 669 ± 210 °/s, trail-wrist flexion 1531 ± 345 °/s ([Sweeney et al. 2012, ISBS](https://ojs.ub.uni-konstanz.de/cpa/article/view/5195/4770)).

### Inferences
- From 2D video you cannot measure segment angular velocities. Pelvis and chest rotation is mostly transverse-plane, and a single camera sees it only as foreshortening. At best, 2D at ≥240 fps can show the timing ORDER of some visible events (lead hip clearing before shoulders before hands). Even that would be a qualitative "sequence look", not a kinematic sequence. Do not report °/s or "speed gain" from phone video.
- Never compare a K-Vest or Sportsbox speed with a Myers/Meister horizontal-plane speed: different definitions give systematically different values (e.g. tour 5-iron pelvis 415 °/s horizontal-plane vs Sportsbox 6-iron 366–470 °/s; low-handicap K-Vest 503 °/s).

### Gaps
- Full Cheetham et al. 2008 table (pro vs amateur peaks for thorax, arm, club and timing) not retrieved; only the pelvis values (477 vs 395 °/s) via Callaway 2012.
- No published validation of Sportsbox speeds against optical mocap was found.

## 8. Wrist angles (lead wrist flexion/extension at top and impact)

### Takeaway
Skilled players are usually somewhat extended ("cupped") at the top: ≈27 ± 8° in a 3D lab study of skilled drivers, and 0–30° per HackMotion's tour patterns. They then flex the lead wrist strongly in the downswing to near flat, ±10°, at impact. Amateurs carry ~10° more extension at the top (vendor data).

### Cited Findings
- Sweeney et al. 2012 (ISBS) [CONF]: 10 highly skilled males (hcp 2.7 ± 1.6), **driver**, 12-camera Vicon 400 Hz, ISB anatomical axes. At the top: lead wrist "27° (±8) extended and 9° (±15) radially deviated". Trail wrist "58° (±12) extended and 16° (±21) ulnar deviated". Downswing: lead wrist flexed 46 ± 10° and ulnar-deviated 44 ± 10°. "Each participant's left wrist was extended to some degree" at the top ([ISBS 2012](https://ojs.ub.uni-konstanz.de/cpa/article/view/5195/4770)).
- HackMotion (IMU wrist sensor) [VENDOR]: sign convention extension + (cupping), flexion − (bowing). Address typical 10–40° extension (weak grip ~10°, strong ~40°). Top typical 0–30° extension, "most pros are slightly extended". Impact: one PGA Tour player (3-iron) 1° extension, typical tour range +10° to −10°. Tour players cock the wrist about 20–40° ([HackMotion PGA Tour data](https://hackmotion.com/learn-from-pga-tour-player-wrist-data)).
- HackMotion: higher-handicap golfers average 24.3° lead-wrist extension vs about 14.5° for lower handicaps at the top [VENDOR, snippet] ([HackMotion learning center](https://hackmotion.com/learning-center/identifying-the-root-causes-for-extension-at-the-top/)). Extension at the top is "almost always about 10 degrees more for amateurs than it is for professionals" [VENDOR, snippet] ([HackMotion insights](https://hackmotion.com/insights-from-hackmotion-data/)).

### Inferences
- A cupped lead wrist at the top is NOT a fault by itself (all 10 skilled players were extended). The relevant check is whether the wrist flexes toward flat in the downswing (from 3D: ~46°). Wrist flexion/extension cannot be measured reliably from 2D phone video (small segment, out-of-plane), so any statement must be qualitative ("looks cupped/bowed") and backed by the frame.

### Gaps
- No peer-reviewed lead-wrist angle at impact for tour players with n > 1 was found. HackMotion's handicap comparison has no published methodology.

## 9. Tempo ratio (backswing:downswing); verification of "Tour Tempo" 3:1

### Takeaway
The 3:1 ratio comes from John Novosel's book *Tour Tempo* (with John Garrity, Doubleday 2004). It was measured in 30 fps video frames: most tour players ≈24/8 frames, range 21/7 to 30/10. An independent club-sensor study (Grober & Cholewicki, 5-iron) confirmed playing pros at 2.5–3.5 (mean ≈3.0), with a backswing of ≈0.7–0.8 s. Amateurs also average ≈3.0 but vary much more and swing slower overall. So the ratio alone does not separate skill.

### Cited Findings
- Grober & Cholewicki 2006 (arXiv physics/0611291) [preprint]: cites Novosel & Garrity, *Tour Tempo* (Doubleday, 2004). Tour pros Tb ≈ 24 frames and Td ≈ 8 frames at 30 Hz video, "range from 21/7 to 30/10". Own data: club-shaft accelerometers ~250 Hz, 10–20 swings each with a **5-iron**. Playing pros n = 12, teaching pros/good amateurs n = 13, other golfers n = 18. Pros: ratio "varies between 2.5 and 3.5, with the average being nearer to 3.0". Backswing "Tb ≈ 0.7–0.8 sec". Other groups: average ratio "centered at 3.0, but varies widely". Pros' swings are "uniformly faster" with much smaller swing-to-swing SD ([arXiv](https://arxiv.org/abs/physics/0611291)).
- Grober accelerometer paper: one professional, 7 swings: backswing 731 ± 21 ms, downswing 258 ± 8 ms, ratio 2.8:1 ([arXiv 1001.0761](https://arxiv.org/abs/1001.0761)).
- Nozawa et al. 2012 (5 female pros, 250 Hz mocap, backswing start from club-head motion): backswing 1.22 ± 0.08 s / downswing 0.33 ± 0.05 s (driver), 1.12 / 0.32 s (5-iron), 1.20 / 0.31 s (9-iron) ([ISBS 2012](https://ojs.ub.uni-konstanz.de/cpa/article/view/5236)).
- Tour Tempo frame chart (via secondary sources): Nicklaus 24/8, Snead 24/8, Tiger Woods 24/8 (2000–02, 2006), Bobby Jones 27/9 [secondary] ([practical-golf](https://practical-golf.com/swing-tempo); [Golf Digest](https://www.golfdigest.com/story/tiger-woods-tempo-golf-swing)).

### Inferences
- Computed from Nozawa: ratios ≈3.7 (driver), 3.5 (5-iron), 3.9 (9-iron). The ratio depends on how "start of backswing" is detected (first club-head motion gives a longer backswing than a visual takeaway start). Always state the event definitions.
- In video terms, 24/8 at 30 fps = 0.80 s / 0.27 s = 48/16 frames at 60 fps = 192/64 at 240 fps. Tempo can be measured from 2D video only if the file plays at real time (no baked-in slow motion) and the frame rate is known.
- The ratio is not a skill marker by itself (amateur mean ≈3.0 too). Total swing time and swing-to-swing consistency differ more.

### Gaps
- The *Tour Tempo* book itself (its exact sample and method) was not accessed; its figures are known here through Grober's citation and secondary sources.

## 10. What can be measured reliably from 2D phone video (down-the-line vs face-on) vs what needs 3D

### Takeaway
No study validating smartphone 2D (or MediaPipe-type) golf joint angles against 3D mocap was found. 2D is defensible for event timing and for in-plane, address-relative measures (lateral sway/slide, head movement, spine tilt, shaft lean face-on; forward bend, hip depth/early extension, plane DTL), reported as approximate. Rotations (pelvis/chest turn, X-factor), segment speeds (kinematic sequence), wrist angles, club face and dynamic loft need 3D/IMU/launch monitors.

### Cited Findings
- Golf-specific 2D: Yamamoto et al. 2023 used a single 240 Hz down-the-line camera with HRNet. The authors state the method "is inferior with respect to accuracy, compared with 3D motion analysis" and still needs verification against 3D mocap ([Frontiers 2023](https://frontiersin.org/articles/10.3389/fspor.2023.1272038/full)).
- 2D event detection: GolfDB (1,400 mostly tour-pro YouTube swings, 8 events). SwingNet detected all 8 events at an average rate of 76.1 % and 6 of 8 at 91.8 % ([McNally et al. 2019, CVPRW](https://arxiv.org/abs/1903.06528)).
- [UNVERIFIED] A search summary described a 2022 study (12 golfers) that found no significant differences in swing time and phase timing between low-cost 2D apps (Kinovea, SiliconCoach) and a comparison system. The exact paper was not identified or opened; a possible match is ([IJSPT](https://ijspt.scholasticahq.com/article/30994)). Do not cite without checking.
- Non-golf 2D vs 3D frontal-plane trunk/pelvis (39 adults; stepping, landing, cutting): mean agreement < 5°, but 95 % limits of agreement as wide as −12.8° to 21.3° for the pelvis. "Caution is advised when high levels of agreement or accuracy is required" ([IJSPT 2022, DOAJ](https://doaj.org/article/f12ab9f81be643da965e432c6585f3d2)).
- Pose estimation vs marker capture in athletic movements: mean joint-angle errors ≈9.7 ± 4.7° and 9.0 ± 3.3°. Accuracy drops in the transverse and frontal planes for fast, complex motion [snippet] ([Sports Engineering 2024](https://link.springer.com/content/pdf/10.1007/s12283-024-00460-w.pdf)).
- Even in 3D, X-factor values change by tens of degrees with the Cardan sequence ([Joyce 2010](https://people.stfx.ca/smackenz/Courses/DirectedStudy/Articles/Joyce%202010%20Methodological%20considerations%20for%20the%203D%20measurement%20of%20the%20X-factor.pdf)).

### Inferences
Practical classification for a single phone camera, judged against the golfer's own address frame (inference based on the above plus camera geometry):

| Parameter | Down-the-line (DTL) | Face-on (FO) | Verdict for 2D |
|---|---|---|---|
| Event timing (P1–P10), tempo ratio | yes | yes | Reliable if real-time file and ≥60 fps (GolfDB-type detection) |
| Lateral pelvis sway/slide, chest/rib sway (cm vs address) | — | yes | Approximate (compare with GEARS/Sportsbox ranges, ±2–3 cm error) |
| Head lateral movement | — | yes | Approximate |
| Head vertical / depth | yes | (vertical yes) | Approximate |
| Spine side tilt (axis tilt) at address/impact | — | yes | Approximate; definition differs from GEARS/Sportsbox |
| Shaft lean at impact | — | yes (camera perpendicular, hand height) | Approximate, needs the real impact frame |
| Forward bend at address and its change | yes | — | Approximate; judge the CHANGE, not an absolute norm |
| Hip depth / early extension (pelvis toward ball vs tush line) | yes | — | Approximate; no tour cm norm exists |
| Pelvis vertical drop / lift | yes | yes | Approximate |
| Knee flexion (trail DTL, lead FO) | partially | partially | Rough; out-of-plane error |
| Hand/club plane, over-the-top (club vs backswing path) | yes | — | Approximate |
| Pelvis / chest rotation, X-factor, stretch | no | no | Needs 3D (transverse plane) |
| Kinematic sequence speeds (°/s), speed gains | no | no | Needs 3D/IMU |
| Lead wrist flexion/extension | no | no | Needs sensor (HackMotion) or 3D; only "looks cupped/bowed" |
| Club face, path in degrees, dynamic loft, clubhead speed | no | no | Needs launch monitor |

### Gaps
- No validation of MediaPipe/BlazePose (or Sportsbox) golf measurements against optical mocap was found. The Nagoya 2023 paper reports none, and a Belarusian Qualisys vs Simi markerless golf comparison was seen only as an abstract without results ([DOAJ](https://doaj.org/article/8cc64311aed74557ae64631ce2a5cbf1)). Any 2D number should be labelled "approx." with a range.
