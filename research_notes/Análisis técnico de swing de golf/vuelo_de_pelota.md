# Golf ball flight laws, club delivery parameters and inferring swing mechanics from ball flight

Researched 2026-11-04. Conventions: right-handed golfer (mirror everything for a left-hander). TrackMan sign convention: positive club path = in-to-out (right of target), positive face angle = open (right of target), Face to Path = FACE ANGLE − CLUB PATH, positive spin axis = ball curving right. Source-quality flags: **[PRIMARY]** = manufacturer's own page/data or peer-reviewed paper read in full; **[SECONDARY]** = blog, forum, coaching site, or a third party repeating someone else; **[SNIPPET]** = page blocked our fetch (HTTP 403), so only the search-engine excerpt was seen; verify the wording before quoting it publicly.

## 1. Start direction: how much comes from face angle vs club path (the "75/25 irons, 85/15 driver" figures)

### Takeaway
The "face ≈ 75 % (mid-iron) / ≈ 85 % (driver)" split is a TrackMan University teaching figure. It reaches the public through Titleist's Learning Lab (attributed to Niklas Bergdahl, TrackMan University). I could not find a TrackMan primary document that states it with its test conditions. The only peer-reviewed measurement I found (PING engineers, ISEA 2018, centred strikes only) gives lower shares: driver 76 %, 7-iron 69 %, 58° wedge 61 %, robot 7-iron 63 %. The share falls as spin loft rises. The safe statement is: "with centred contact the ball starts much closer to the face than to the path, roughly 60–85 % toward the face, more with low-loft clubs."

### Cited Findings
- Titleist Learning Lab credits TrackMan data. With irons, face angle is ~75 % of initial launch direction and club path ~25 %. With a driver, the face's share rises to ~85 % and path falls to ~15 %. **[SECONDARY, SNIPPET]**: Titleist repeats TrackMan, and the page returned 403 to our fetch. — [Titleist Learning Lab, "Physics of ball striking in golf"](https://www.titleist.com/learning-lab/performance/physics-of-ball-striking-in-golf); [Titleist, "Face Angle"](https://www.titleist.com/learning-lab/performance/golf-club-face-angle)
- One Titleist piece attributes the 75/25 (mid-iron) and 85/15 (driver) figures to **Niklas Bergdahl, Head of TrackMan University**. **[SECONDARY, SNIPPET]** — [Titleist Learning Lab (search excerpt)](https://www.titleist.com/learning-lab/performance/physics-of-ball-striking-in-golf); also repeated in a 2013 blog: [0to300golf, April 2013](https://0to300golf.blogspot.com/2013/04)
- A Titleist video description says the face is 75 % of starting direction "on mid-iron shots" and that "on driver shots face angle contributes even more." It is a claim in a video description, not a published study. **[SECONDARY, SNIPPET]** — [Titleist Learning Lab](https://www.titleist.com/learning-lab/performance/physics-of-ball-striking-in-golf)
- Conflicting figures: a simulator-forum post says TrackMan Academy taught ~87 % face for driver and ~81 % for 6-iron/PW. A Sand Trap forum commenter citing TrackMan said the iron figure is "almost never below ~80 %." These are forum posts, so treat them as unreliable. — [Golf Simulator Forum](https://golfsimulatorforum.com/forum/foresight-sports/345478-experiment-rough-calculation-of-clubface-using-launch-direction-and-club-path); [The Sand Trap forum](https://thesandtrap.com/forums/topic/41333-ball-flight-laws)
- **Peer-reviewed measurement (PING, 2018) [PRIMARY]:** Wood, Henrikson & Broadie, "The Influence of Face Angle and Club Path on the Resultant Launch Angle of a Golf Ball," *Proceedings* 2018, 2, 249 (12th ISEA conference, Brisbane; published 23 Feb 2018; doi:10.3390/proceedings2060249). Funded by PING. — [MDPI PDF](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf)
  - Player test: 157 right-handed golfers (handicap 10.1 ± 10.0), 5 driver + 5 7-iron shots each. A subset of 10 low handicappers (1.2 ± 1.7) also hit 10 shots each with a 58° wedge. Club measured with Vicon motion capture at 720 fps; ball measured with Foresight GC2.
  - Filters: only strikes within **0.25″ (6.35 mm) of face centre**, vertical and horizontal, "to minimize changes in initial angle caused by the twisting of the club head". Only shots with face-to-path ≥ 1.5° counted for the horizontal ratio.
  - Results (% of launch direction toward the face angle, 95 % CI, n after filtering): **driver 76 % ± 8 % (89), 7-iron 69 % ± 3 % (172), wedge 61 % ± 7 % (28).** Robot test (PING Man, 7-iron, 91 mph, centred strikes): **63 % ± 4 % (15)**, R² = 0.986.
  - Vertical plane (launch toward dynamic loft vs attack angle): **driver 83 % ± 8 %, 7-iron 81 % ± 5 %, wedge 72 % ± 6 %.**
  - Conclusion: "the ball starts in general between 61% and 83% toward the face angle, with higher numbers when the dynamic loft is lower". The ratio falls as obliqueness (dynamic loft − attack angle, i.e. spin loft) rises.
  - Historical values in the same paper: Cochran & Stobbs (1968) example ≈ 65 % toward face; Sweeney et al. ≈ 62 %; Jorgensen's equations ≈ 80 % toward dynamic loft (vertical); McCloy et al. ≈ 68 % (vertical). The paper also notes that the PGA of America test "for many years required candidates to state that the initial direction of the ball is equal to the club path", the old ball flight law, which it calls a misunderstanding.
- FlightScope: I found no FlightScope-published face/path percentage. A GolfWRX piece says face determines "roughly 75 to 80 percent" of start direction **[SECONDARY]**. — [GolfWRX, "Use the new ball flight laws"](https://www.golfwrx.com/251459/use-the-new-ball-flight-laws-to-understand-your-tendencies/); FlightScope's definitions: [FlightScope Face to Path](https://flightscope.com/pages/face-to-path), [FlightScope Spin Axis](https://flightscope.com/pages/spin-axis) **[SNIPPET]**
- Foresight: no Foresight statement found. Foresight's role in the evidence is as the ball-measuring device (GC2) in the PING study. — [PING 2018](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf)

### Inferences
- Useful approximation: **start ≈ path + k·(face − path) = face − (1 − k)·(Face to Path)**. Take k ≈ 0.75–0.85 for the driver and 0.65–0.75 for mid-irons (TrackMan/Titleist teaching numbers vs the PING measurement), and lower for wedges. Example: a 7-iron with face 0° and path −6° (out-to-in) starts ≈ −1.9° (k = 0.69) or ≈ −1.5° (k = 0.75), only slightly left. That is why over-the-top players with an open-to-path face often start the ball near the target and slice it.
- For a paid product reviewed by coaches, prefer wording like "the face controls most of the start direction (roughly two-thirds to over three-quarters, depending on club and strike)". Precise single numbers like "75 %" read as false precision, and the only published test with stated conditions gives lower numbers.
- The figures assume **centred contact**. Off-centre strikes (gear effect, Q3) can move start direction away from what face/path alone predict.

### Gaps
- No TrackMan primary document (newsletter, TrackMan University page or PDF) stating the 75/25 and 85/15 split, with its sample and conditions, could be retrieved. TrackMan support/University pages return 403. A TrackMan University account may expose it.
- Titleist Learning Lab pages returned 403 (direct and via archive.org), so the exact Titleist wording was seen only in search excerpts.
- No FlightScope or Foresight primary statement of a face/path split was found.

## 2. The D-plane, spin axis, spin loft, and why attack angle shifts path (irons vs driver)

### Takeaway
The D-plane is the plane containing the clubhead's 3-D direction of travel and the face normal at impact. The ball launches inside it, between the two. The spin axis is perpendicular to it. The angle between the two vectors is the **spin loft**, which mainly sets spin rate. The **tilt** of the plane (from face-to-path) sets the spin axis and therefore the curve. The same face-to-path tilts the axis more when spin loft is small (driver) than when it is large (wedge). Because the club swings on an inclined plane, hitting down (irons) moves the instantaneous path to the right of the swing direction, and hitting up (driver) moves it left.

### Cited Findings
- Origin: the D-plane model comes from Theodore Jorgensen's *The Physics of Golf* and was "later popularized by Trackman Golf" **[SECONDARY]**. — [The DIY Golfer, "D-Plane"](https://thediygolfer.com/d-plane-golf). Jorgensen, *The Physics of Golf* (Springer, 1999 ed.; first ed. AIP Press 1994) is cited by the PING paper for his launch equations. — [PING 2018, ref. 3](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf)
- D-plane geometry: the plane is defined by the club-head path at impact and the clubface normal, and contains the ball's initial path. The spin axis is perpendicular to the D-plane, so tilting the plane tilts the axis **[SECONDARY]**. — [The DIY Golfer](https://thediygolfer.com/d-plane-golf)
- PING 2018 (primary) describes the oblique impact the same way: the ball "launches between the club path and the face angle" with spin "which causes the ball to curve in the air." — [PING 2018](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf)
- TrackMan's "D Plane Tilt (Tee to Green)" parameter: the tilt of the D-plane relative to the plumb line, i.e. "the expected spin axis without gear effect or other off-center factors". If face-to-path is zero, D Plane Tilt is zero **[PRIMARY, SNIPPET]**. — [TrackMan Support, "Parameters | D Plane Tilt"](https://support.trackmangolf.com/hc/en-us/articles/39726207070875-Parameters-D-Plane-Tilt-Tee-to-Green)
- TrackMan definitions (TrackMan Editorial Team, 14 Jan 2020) **[PRIMARY]** — [TrackMan, "40+ Trackman Parameters Explained"](https://www.trackman.com/blog/golf/40-trackman-parameters):
  - Club Path: "The in-to-out or out-to-in movement of the club head's geometric center at the time of maximum compression."
  - Face Angle: "The direction the club face is pointing at the center-point of contact."
  - Attack Angle: "The up or down movement of the club head's geometric center at the time of maximum compression."
  - Dynamic Loft: "The vertical angle of the club face at the center-point of contact."
  - Spin Loft: "The angle between the direction of the club head's movement and the club face's orientation."
  - Spin Axis: "The angle relative to the horizon of the imaginary line that the golf ball rotates around."
  - Swing Direction: "The angle between the base of the plane created by the club head's geometric center movement and the target line."
  - Swing Plane: "The vertical angle between the plane created by the club head's geometric center movement and the horizon."
  - Low Point: "Distance from the club head's geometric center to the lowest point on the swing arc at the time of maximum compression."
  - Impact Height / Impact Offset: vertical / horizontal strike location relative to face centre.
  - Smash Factor: ball speed ÷ club speed.
- Face to Path (TrackMan, 23 Sep 2024) **[PRIMARY]**: "FACE ANGLE minus CLUB PATH". Positive means the face points right of the path, "regardless of dexterity". It is "important in determining the expected curvature (spin axis)". Assuming centred contact, "the ball should curve towards the face angle and away from the club path". It is not measured relative to the target line. — [TrackMan, "What is Face to Path?"](https://trackman.com/blog/golf/face-to-path)
- Curvature per degree of face-to-path, centred contact, from TrackMan's own examples **[PRIMARY]** (these use the older tour carry distances) — [TrackMan Face to Path](https://trackman.com/blog/golf/face-to-path):
  - PGA TOUR driver (275 yd carry): −2° ≈ 19 yd left; +5° ≈ 44 yd right.
  - PGA TOUR 6-iron (183 yd): +2° ≈ 8 yd right; −5° ≈ 20 yd left.
  - LPGA driver (218 yd): +2° ≈ 14 yd right; −5° ≈ 32 yd left.
  - LPGA 6-iron (152 yd): −2° ≈ 6 yd left; +5° ≈ 14 yd right.
  - John Parkinson (TrackMan University Master): "One degree Face to Path difference at 300 yards will produce a shot with 12 yards of curve"; "a maximum of 1 degree Face to Path difference is essential for consistent, accurate drives."
- Spin axis (TrackMan, 23 Sep 2024) **[PRIMARY]** — [TrackMan, "What is Spin Axis?"](https://www.trackman.com/blog/golf/spin-axis):
  - Positive axis = curve right, negative = curve left.
  - For a right-hander, a small positive axis is a fade and a large positive axis a slice.
  - "a Spin Axis between -2 and 2 can be considered a straight shot."
  - Examples: on an optimized 150-yd shot, −2 ≈ 2.2 yd left and +10 ≈ 11 yd right. On an optimized 200-yd shot, −10 ≈ 15 yd left and +2 ≈ 3 yd right.
  - Indoors, TrackMan calculates spin axis from club delivery ("spin loft and face to path"). Outdoors it measures the ball flight.
- Fredrik Tuxen (TrackMan inventor) estimated empirically that, for a driver, a 5° spin-axis tilt moves the ball ~4.5 yd sideways per 100 yd of travel **[SECONDARY]**. — [Oxford University Press blog, March 2016](https://blog.oup.com/2016/03/golf-balls-science/)
- Spin loft (TrackMan, 23 Sep 2024) **[PRIMARY]** — [TrackMan, "Spin Loft"](https://www.trackman.com/blog/spin-loft):
  - It is the 3-D angle between club-head travel and face orientation. "Simply subtracting attack angle from dynamic loft will give a close approximation," but this "will vary from the actual Spin Loft" when face-to-path ≠ 0.
  - Spin rate "is largely influenced by the Spin Loft". Higher spin loft gives a lower smash factor, all else equal.
  - Tour spin loft listed: **PGA TOUR driver 14.7°, 6-iron 24.3°; LPGA driver 15.0°, 6-iron 25.9°**. The page does not say which data year these come from.
- High spin loft (wedges) "stretch the D-Plane upwards resulting in flatter, less tilted Spin Axis numbers than low Vertical Differential shots (like drivers)" **[SECONDARY]**. — [Stronger Golf blog, 2011](https://strongergolf.blogspot.com/2011/11/spin-loft-part-ii-spin-rate-and-spin.html)
- Attack angle and path: hitting down on a neutral plane gives an in-to-out path (path right of target). Hitting up gives out-to-in (path left). To neutralise a downward strike, "the swing plane must actually be rotated to the left of the target line" **[SECONDARY: Andrew Rice, citing TrackMan research, 25 Jul 2011]**. — [Andrew Rice Golf, "Understanding Swing Plane and Club Path"](https://terri-rice-0z1d.squarespace.com/andrew-rice-golf/tag/hitting+down)
- Magnitude: "With the driver you need the same value for attack angle and horizontal swing plane in order to obtain a 0° club path", and for irons "it is half effect". Example: −5° attack needs swing direction shifted ~2.5° left for a neutral path **[SECONDARY: coaching blog, self-described work in progress, April 2013]**. — [Hattrick Golf Instruction](https://hattrickgolfinstruction.blogspot.com/2013/04/work-in-progress-understanding-ball.html)
- Peer-reviewed: Morrison, McGrath & Wallace (2017), *Journal of Sports Sciences*, doi:10.1080/02640414.2017.1303187. In 52 golfers × 40 drives, the clubhead trajectory near impact fits an ellipse (RMSE 1.2 mm), and the authors derived "rule of thumb" values relating club path, angle of attack and delivery-plane angle. I could not retrieve the values. — [Ulster University record](https://pure.ulster.ac.uk/en/publications/the-relationship-between-the-golf-swing-plane-and-ball-impact-cha-3/)
- Caveat on the model: Mitchell Golf argues that the laws also need face "attitude" (lie at impact). If the face is not level, the spin axis tilts even with face = path **[SECONDARY, SNIPPET]**. — [Mitchell Golf, "Tilt Axis Spin vs. Sidespin"](https://www.mitchellgolf.com/tilt-axis-spin-vs-sidespin/)

### Inferences
- Geometry consistent with the Rice and Hattrick sources (my own small-angle derivation, not a TrackMan-published formula): **club path ≈ swing direction − attack angle / tan(swing plane)**.
  - Iron (plane ≈ 60°, 1/tan 60° ≈ 0.58): AoA −4° shifts path ≈ +2.3° (right) of swing direction. This matches the "half effect" rule.
  - Driver (plane ≈ 45°, 1/tan 45° = 1): AoA +3° shifts path ≈ −3° (left). This matches the "1:1" rule.
  - Practical meaning: a player whose iron path is neutral will tend to swing left of target (swing direction negative). A player who hits up on driver with the same body motion gets a more out-to-in path. This is why "driver slices, irons fine" (or the reverse) can come from attack angle rather than a different swing.
- Using the tour spin-loft numbers, the same 2° face-to-path tilts the spin axis more on a driver (spin loft ≈ 15°) than on a 6-iron (≈ 24°) or a wedge (≈ 40°). Drivers curve more from the same face/path error. Ball speed and time in the air add to this.
- Rough driver curvature from TrackMan's examples: ~9 yd per degree of face-to-path at tour speed (275 yd carry), ~7 yd/degree at LPGA speed (218 yd). For a 6-iron, ~4 yd/degree at tour speed and ~3 yd/degree at LPGA speed. Slower amateurs curve fewer yards per degree.

### Gaps
- Exact Jorgensen chapter/page for the D-plane derivation was not verified (book not accessible online).
- Morrison et al. (2017) rule-of-thumb coefficients not retrieved (paywall; the repository host did not resolve).
- TrackMan's own published statement of the attack-angle → path relationship (Tuxen newsletter) could not be retrieved; TrackMan support pages return 403.
- Data year of TrackMan's tour spin-loft values (14.7° / 24.3° / 15.0° / 25.9°) is not stated.

## 3. Gear effect and strike location

### Takeaway
On woods, especially the driver, off-centre strikes twist the head about its centre of mass. A **toe** strike opens the face (starts right) and adds draw spin. A **heel** strike closes it (starts left) and adds fade spin. A **high** strike launches higher with less spin; a **low** strike launches lower with more spin. Bulge and roll are designed to offset this. A spin axis that contradicts the face-to-path sign is TrackMan's tell for an off-centre strike. Gear effect is weaker in irons, and no quantitative source was found here.

### Cited Findings
- Off-centre strikes rotate the head around its centre of mass: the face "effectively opens and closes" (horizontal gear effect) or changes loft (vertical). Effects:
  - toe strikes start farther right and carry draw spin back toward the target;
  - heel strikes start farther left and carry slice spin;
  - spin increases the farther from centre the strike is;
  - high strikes launch higher with less spin, low strikes launch lower with more spin;
  - bulge (heel–toe curvature) and roll (crown–sole curvature) are built into drivers, fairway woods and hybrids to optimise mishits.
  **[SECONDARY: GOLFTEC, 9 May 2018]** — [GOLFTEC Scramble, "The influence of bulge and roll (and gear effect) on ball flight"](https://scramble.golftec.com/blog/2018/05/bulge-and-roll-and-gear-effect/)
- TrackMan University Master Mark Anderson uses the mismatch as a diagnostic. If face-to-path is positive (which should curve right) but the spin axis is negative (curves left), the strike was toward the toe **[PRIMARY: TrackMan blog quote]**. — [TrackMan, "What is Spin Axis?"](https://www.trackman.com/blog/golf/spin-axis). Ryan Johnson: "One could see a negative Face to Path but a positive spin axis." Hugh Marr uses face-to-path "in conjunction with spin axis to check for centered contact." — [TrackMan, "What is Face to Path?"](https://trackman.com/blog/golf/face-to-path)
- TrackMan's D Plane Tilt is defined as the spin axis "without gear effect or other off-center factors". The measured spin axis minus D-plane tilt is therefore the strike-location contribution **[SNIPPET]**. — [TrackMan Support, D Plane Tilt](https://support.trackmangolf.com/hc/en-us/articles/39726207070875-Parameters-D-Plane-Tilt-Tee-to-Green)
- "Almost all golf shots experience some amounts of gear effect", so the measured spin axis often differs from what D-plane components predict **[SECONDARY]**. — [Stronger Golf blog](https://strongergolf.blogspot.com/2011/11/spin-loft-part-ii-spin-rate-and-spin.html)
- PING 2018 filtered to strikes within 0.25″ of centre precisely because head twisting on off-centre impacts changes start angle. It lists impact-location variation as a main error source. **[PRIMARY]** — [PING 2018](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf)
- Forum and coaching commentary says gear effect does not override face-to-path: a heel strike can still draw if the face is closed enough to the path, and gear effect is much weaker in irons **[SECONDARY]**. — [The Sand Trap forum](https://thesandtrap.com/forums/topic/77545-gear-effect-and-driver-face-curvature/?page=3); [Plugged In Golf, "Ball Flight Laws #5 – Gear Effect"](https://pluggedingolf.com/ball-flight-laws-5-gear-effect/)

### Inferences
- In the decision table, "toe strike with driver" can turn a push-fade into a push-draw. "Heel strike with driver" produces the classic "starts left and fades/slices", which looks like a pull-slice even when the path is fine. Do not diagnose "over the top" from one heel-struck slice. Ask for strike location (impact tape, foot spray) first.
- For irons, assume gear effect is small. A curving iron shot is mostly face-to-path. This is an inference from the absence of bulge/roll in irons; no measured value was found.

### Gaps
- No quantitative figure (e.g., degrees of spin-axis change per mm of offset, by club) from a primary source. TrackMan/Titleist pages on gear effect were not retrievable, and the physics literature (e.g., Penner 2002, *Rep. Prog. Phys.*) was not accessed.

## 4. Tour average club delivery and ball data (TrackMan), by club

### Takeaway
The latest TrackMan table is **"2023" PGA TOUR and LPGA Tour averages**, published 2 May 2024. It covers club speed, attack angle, ball speed, smash factor, launch angle, spin, max height, land angle and carry. **It does not include club path, face angle, face-to-path, dynamic loft or spin loft.** TrackMan's assumed norm for face-to-path is 0° for all clubs. Spin loft is given separately, for driver and 6-iron only, with no year. The older table, still in a TrackMan support PDF, is shown below for comparison.

### Cited Findings
- **TrackMan "2023 PGA & LPGA Tour Averages"**, Trackman Editorial Team, published **2 May 2024** **[PRIMARY]**. Data from 40+ events and 200+ male players (PGA TOUR + DP World Tour, mostly PGA TOUR) and 30+ events and 150+ female players (LPGA + LET, mostly LPGA). Includes competition and range shots. Non-driver shots in competition were filtered out (< 0.5 % may remain). Stat holes were picked in opposite directions to cancel wind. — [TrackMan blog](https://www.trackman.com/blog/introducing-updated-tour-averages); tables: [PGA image](https://a.storyblok.com/f/117513/1920x883/6aefae601d/pga_tour-averages_trackman_blog.jpg), [LPGA image](https://a.storyblok.com/f/117513/1920x883/9617e89ecd/lpga_tour-averages_trackman_blog.jpg)

**PGA TOUR 2023 (TrackMan)** — club speed mph · attack angle ° · ball speed mph · smash · launch ° · spin rpm · max height yd/m · land angle ° · carry yd/m

| Club | Club spd | AoA | Ball spd | Smash | Launch | Spin | Height | Land | Carry |
|---|---|---|---|---|---|---|---|---|---|
| Driver | 115 | −0.9 | 171 | 1.49 | 10.4 | 2545 | 35/32 | 39 | 282/258 |
| 3-wood | 110 | −2.3 | 162 | 1.47 | 9.3 | 3663 | 32/29 | 44 | 249/228 |
| 5-wood | 106 | −2.5 | 156 | 1.47 | 9.7 | 4322 | 33/30 | 48 | 236/216 |
| Hybrid | 102 | −2.4 | 149 | 1.47 | 10.2 | 4587 | 31/28 | 49 | 231/211 |
| 3 iron | 100 | −2.5 | 145 | 1.46 | 10.3 | 4404 | 30/27 | 48 | 218/199 |
| 4 iron | 98 | −2.9 | 140 | 1.44 | 10.8 | 4782 | 31/28 | 49 | 209/192 |
| 5 iron | 96 | −3.4 | 135 | 1.41 | 11.9 | 5280 | 33/30 | 50 | 199/182 |
| 6 iron | 94 | −3.7 | 130 | 1.39 | 14.0 | 6204 | 32/29 | 50 | 188/172 |
| 7 iron | 92 | −3.9 | 123 | 1.34 | 16.1 | 7124 | 34/31 | 51 | 176/161 |
| 8 iron | 89 | −4.2 | 118 | 1.33 | 17.8 | 8078 | 33/30 | 51 | 164/150 |
| 9 iron | 87 | −4.3 | 112 | 1.29 | 20.0 | 8793 | 32/29 | 52 | 152/139 |
| PW | 84 | −4.7 | 104 | 1.24 | 23.7 | 9316 | 32/29 | 52 | 142/130 |

**LPGA Tour 2023 (TrackMan)** — same columns

| Club | Club spd | AoA | Ball spd | Smash | Launch | Spin | Height | Land | Carry |
|---|---|---|---|---|---|---|---|---|---|
| Driver | 96 | +2.8 | 143 | 1.49 | 12.6 | 2506 | 26/24 | 36 | 223/204 |
| 3-wood | 92 | −0.8 | 135 | 1.47 | 11.6 | 2595 | 25/23 | 38 | 200/183 |
| 5-wood | 90 | −1.6 | 130 | 1.46 | 12.3 | 4320 | 25/23 | 43 | 189/173 |
| Hybrid | 87 | −1.9 | 125 | 1.44 | 13.9 | 4504 | 25/23 | 45 | 178/163 |
| 4 iron | 82 | −1.7 | 118 | 1.43 | 13.9 | 4608 | 25/23 | 43 | 175/160 |
| 5 iron | 81 | −2.0 | 114 | 1.42 | 14.6 | 4966 | 25/23 | 45 | 166/152 |
| 6 iron | 80 | −2.3 | 111 | 1.41 | 16.7 | 5904 | 25/23 | 46 | 155/142 |
| 7 iron | 78 | −2.5 | 106 | 1.38 | 18.5 | 6630 | 26/24 | 47 | 143/131 |
| 8 iron | 76 | −2.8 | 102 | 1.36 | 20.8 | 7413 | 27/25 | 47 | 133/122 |
| 9 iron | 74 | −3.2 | 95 | 1.30 | 23.5 | 7605 | 27/25 | 48 | 123/112 |
| PW | 72 | −3.2 | 88 | 1.25 | 25.2 | 8465 | 27/25 | 48 | 111/101 |

- TrackMan's attack-angle article (23 Sep 2024) repeats the 2023 values: PGA TOUR driver −0.9°, 6-iron −3.7°; LPGA driver +2.8°, 6-iron −2.3° **[PRIMARY]**. — [TrackMan, "What is Attack Angle?"](https://trackman.com/blog/golf/attack-angle)
- TrackMan says that since the previous table "players are now hitting further, with greater ball speed and less spin rate" **[PRIMARY]**. — [TrackMan blog, 2 May 2024](https://www.trackman.com/blog/introducing-updated-tour-averages)
- **Previous TrackMan table** (TrackMan support PDF "PGA TOUR AVERAGES METERS"; file metadata created 16 Jul 2020; collection year not stated; the same figures were covered as "2019 PGA Tour and LPGA Tour stats" by GolfMagic/Golf.com) **[PRIMARY PDF, year uncertain]**. — [TrackMan Support PDF](https://support.trackmangolf.com/hc/en-us/article_attachments/7349801987483); [GolfMagic 2019](https://www.golfmagic.com/equipment-news/revealed-trackman-launches-2019-pga-tour-and-lpga-tour-stats); [Golf.com, 23 Apr 2019](https://www.golf.com/instruction/2019/04/23/pga-tour-lpga-players-trackman-stats)
  - PGA (club mph / AoA / ball mph / smash / launch / spin / carry m):
    - Driver 113 / −1.3 / 167 / 1.48 / 10.9 / 2686 / 251 m (≈ 275 yd)
    - 3-wood 107 / −2.9 / 158 / 1.48 / 9.2 / 3655 / 222
    - 5-wood 103 / −3.3 / 152 / 1.47 / 9.4 / 4350 / 210
    - Hybrid 100 / −3.5 / 146 / 1.46 / 10.2 / 4437 / 206
    - 3i 98 / −3.1 / 142 / 1.45 / 10.4 / 4630 / 194
    - 4i 96 / −3.4 / 137 / 1.43 / 11.0 / 4836 / 186
    - 5i 94 / −3.7 / 132 / 1.41 / 12.1 / 5361 / 177
    - 6i 92 / −4.1 / 127 / 1.38 / 14.1 / 6231 / 167
    - 7i 90 / −4.3 / 120 / 1.33 / 16.3 / 7097 / 157
    - 8i 87 / −4.5 / 115 / 1.32 / 18.1 / 7998 / 146
    - 9i 85 / −4.7 / 109 / 1.28 / 20.4 / 8647 / 135
    - PW 83 / −5.0 / 102 / 1.23 / 24.2 / 9304 / 124
  - LPGA:
    - Driver 94 / +3.0 / 140 / 1.48 / 13.2 / 2611 / 199 m
    - 3-wood 90 / −0.9 / 132 / 1.48 / 11.2 / 2704 / 178
    - 5-wood 88 / −1.8 / 128 / 1.47 / 12.1 / 4501 / 169
    - 7-wood 85 / −3.0 / 123 / 1.46 / 12.7 / 4693 / 159
    - 4i 80 / −1.7 / 116 / 1.45 / 14.3 / 4801 / 155
    - 5i 79 / −1.9 / 112 / 1.43 / 14.8 / 5081 / 147
    - 6i 78 / −2.3 / 109 / 1.41 / 17.1 / 5943 / 139
    - 7i 76 / −2.3 / 104 / 1.38 / 19.0 / 6699 / 129
    - 8i 74 / −3.1 / 100 / 1.33 / 20.8 / 7494 / 119
    - 9i 72 / −3.1 / 93 / 1.32 / 23.9 / 7589 / 109
    - PW 70 / −2.8 / 86 / 1.28 / 25.7 / 8403 / 98
- Tour spin loft (no year given): PGA driver 14.7°, 6-iron 24.3°; LPGA driver 15.0°, 6-iron 25.9° **[PRIMARY]**. — [TrackMan, "Spin Loft"](https://www.trackman.com/blog/spin-loft)
- Face-to-path: "The standard assumption for Face to Path is zero for all clubs" **[PRIMARY]**. TrackMan publishes no tour average path or face angle. — [TrackMan Face to Path](https://trackman.com/blog/golf/face-to-path)
- Andrew Rice (2011, citing TrackMan): PGA Tour players hit down on a 7-iron "slightly more than 4 degrees", and better drivers hit up "anywhere from 1-5 degrees" **[SECONDARY]**. — [Andrew Rice Golf](https://terri-rice-0z1d.squarespace.com/andrew-rice-golf/tag/hitting+down)
- Low point: in a 2015 GolfWRX TrackMan test (a major champion plus PGA/Web.com players, 6-iron), the average low point was ~4.2–4.6 in **after** the ball, with a shot-to-shot spread of ~0.5–1.8 in. Lower-skill players had a wider and less forward spread **[SECONDARY, SNIPPET, small sample]**. — [GolfWRX, "Low point: can TrackMan's newest parameter indicate golfer skill level?"](https://golfwrx.com/326978/low-point-can-trackmans-newest-parameter-indicate-golfer-skill-level/). TrackMan-attributed guidance: low point ~3–4 in ahead of the ball for crisp turf irons **[SECONDARY, SNIPPET]**. — [National Club Golfer](https://www.nationalclubgolfer.com/gb/equipment/trackman-phrases-every-golfer-should-understand)

### Inferences
- Approximate tour dynamic loft from spin loft + attack angle (dynamic loft ≈ spin loft + AoA). This mixes data years and assumes face-to-path ≈ 0, so it is only an order of magnitude:
  - PGA driver ≈ 14.7 + (−0.9) ≈ 13.8°;
  - PGA 6-iron ≈ 24.3 + (−3.7) ≈ 20.6°;
  - LPGA driver ≈ 15.0 + 2.8 ≈ 17.8°.
  It is better not to publish these as "tour averages"; TrackMan does not publish dynamic loft averages.
- Tour attack angles are only moderately negative with irons (−3.7° to −4.7° PGA, −2.3° to −3.2° LPGA). On the 2023 table, PGA driver AoA is slightly negative (−0.9°) and LPGA driver AoA is positive (+2.8°). A paid analysis should not tell a viewer to "hit down hard" by default.
- For an Argentine/Spanish-speaking audience, show the metres version: PGA 7-iron carry 161 m, driver 258 m; LPGA 7-iron 131 m, driver 204 m (2023).

### Gaps
- No TrackMan tour averages for club path, face angle, face-to-path, dynamic loft, swing plane, swing direction or low point were found.
- Collection year of the "previous" table is not stated on the PDF.
- No FlightScope or Foresight tour-average tables were retrieved.

## 5. What a smartphone video plus the golfer's ball-flight report can and cannot tell you; what to ask

### Takeaway
Video from down-the-line and face-on can show **body and club-shaft patterns** that tend to produce certain deliveries. Examples: the club above the "slot" in transition (TPI's over-the-top test), pelvis moving toward the ball, lack of forward shift, shaft lean at impact. Normal phone video cannot measure **face angle, club path or strike location** to the degree-level that ball-flight laws need. Those must come from the **ball flight** (start line ≈ face, curve ≈ face-to-path sign) and from **contact evidence** (divot start, strike mark). So the analysis needs a structured ball-flight questionnaire.

### Cited Findings
- TPI diagnoses Over the Top from the down-the-line view:
  - draw a line up the shaft plane at address;
  - draw a second line along the club when the lead forearm is just past parallel (the "slot");
  - "If the club is above the slot they have the Over the Top swing fault."
  **[PRIMARY]** — [TPI, Over the Top](https://www.mytpi.com/improve-my-game/swing-characteristics/over-the-top)
- TPI's Casting page: "At impact we should see the shaft leaning slightly toward the target, this helps to deloft the club". Shaft lean is a visible proxy for dynamic loft **[PRIMARY]**. — [TPI, Casting](https://www.mytpi.com/improve-my-game/swing-characteristics/casting)
- TPI's Hanging Back page: in a normal weight shift "the player is about four inches closer to the target at impact compared to address". This is visible from face-on **[PRIMARY, TPI's own figure, no study cited]**. — [TPI, Hanging Back](https://www.mytpi.com/improve-my-game/swing-characteristics/hanging-back)
- Divots do not reveal true path: "the divot only tells us the general swing direction at the bottom of the arc," and true path also depends on attack angle **[SECONDARY]**. — [GolfWRX, "Understanding swing direction vs swing path"](https://golfwrx.com/112812/understanding-swing-direction-vs-swing-path/)
- Start direction and curvature of a centred shot are set by face (mostly) and face-to-path (curve). Off-centre strikes break this. — [PING 2018](https://mdpi-res.com/proceedings/proceedings-02-00249/article_deploy/proceedings-02-00249.pdf); [TrackMan Face to Path](https://trackman.com/blog/golf/face-to-path); [TrackMan Spin Axis](https://www.trackman.com/blog/golf/spin-axis)
- A spin axis between −2° and +2° "can be considered a straight shot", so very small curves are not diagnosable from a viewer's description **[PRIMARY]**. — [TrackMan Spin Axis](https://www.trackman.com/blog/golf/spin-axis)
- Project context (internal): the project's pose pipeline (MediaPipe) does not see the club face. Ball behaviour must be asked of the viewer. — `/home/user/web/swing-analisis/CLAUDE.md`

### Inferences
- **Frame-rate arithmetic (own calculation from TrackMan 2023 speeds):** a tour 7-iron at 92 mph (41 m/s) moves ~69 cm per frame at 60 fps, ~34 cm at 120 fps and ~17 cm at 240 fps. A tour driver at 115 mph (51 m/s) moves ~86 cm per frame at 60 fps and ~21 cm at 240 fps. Slower amateurs move somewhat less. With motion blur on top, phone video cannot resolve face angle at impact to within 1–2°. From TrackMan's examples, 1–2° of face-to-path is already 4–19 yd of curve, so the face must not be "measured" from phone video.
- **Inverting the laws (approximate, centred strike):**
  1. From the curve, estimate the sign and rough size of face-to-path, using TrackMan's yards-per-degree (Q2). Example: a tour-speed 6-iron curving ~20 yd right means F2P ≈ +5°.
  2. Then **face ≈ start + (1 − k)·F2P** and **path ≈ face − F2P** (k from Q1).
  3. Worked example: a 6-iron that starts 2° left and slices ~20 yd gives face ≈ −2 + 0.3·5 ≈ −0.5°, path ≈ −5.5° (out-to-in). That is a classic over-the-top signature.
  4. At amateur speeds the yards per degree are smaller, so the same curve means a larger F2P.
  The result is only directional: the viewer's start-line estimate is the weak link. At 150 yd, 1° ≈ 2.6 yd of lateral offset (tan 1° × 150).
- **Questions to ask the golfer (each tied to a law):**
  1. Club used, right- or left-handed, and where they were aimed (the target line vs body alignment).
  2. Start line relative to the target: left / at / right, and roughly how far at landing, if it had not curved. This estimates the face.
  3. Curve direction and size: none / gentle / big. Did it get worse with longer clubs or driver? This estimates face-to-path. Larger with driver means low spin loft amplifies it.
  4. Is it the usual pattern or a two-way miss (both blocks and hooks)? TPI links two-way misses to early extension and loss of posture.
  5. Height vs normal for that club: ballooning/high and short points to added loft or spin (casting, scooping, chicken wing); low points to delofted or low-face strikes.
  6. Contact: fat (ground before ball), thin (leading edge, low runner), top, shank (sharp right off the hosel), toe or heel feel. Ideally ask for **impact tape or foot-powder spray on the face** and a photo of the mark, and for irons a photo of where the divot starts relative to the ball position.
  7. Distance vs expectation for that club (compare with tour tables only as a ceiling, never a target).
  8. Conditions: wind, sidehill lie, mat vs grass. Lie angle and slope tilt the axis (Mitchell Golf).
  9. If they have any launch monitor (even a consumer unit), ask for club path, face angle, attack angle and strike location. Treat those numbers as device-dependent.

### Gaps
- I found no peer-reviewed study validating face-angle or path estimates from smartphone video, nor one on how accurately golfers report start line and curve. Treat golfer reports as low precision.
- No source gives the minimum frame rate needed to estimate path from video. The frame-rate figures above are arithmetic, not validated thresholds.

## 6. Decision table: reported ball flight → face/path/strike → likely swing patterns; how classic faults show up in launch-monitor data

### Takeaway
Map start line → face, curve → face-to-path, and contact → low point/strike. Then check the video for the body pattern that usually causes that delivery. TPI documents several links directly:
- Over the Top → out-to-in → pull (square face) or slice (open face).
- Early Extension and Loss of Posture → block right + hook left.
- Casting, Scooping and Chicken Winging → added loft and spin, lost power.
- Hanging Back → heavy divots starting behind the ball.
Most of the launch-monitor "signatures" below are mechanical inferences from the D-plane and low-point definitions, not published TrackMan statistics.

### Cited Findings
- **Over the Top (TPI, primary):** the club "will be thrown on the outside of the intended swing plane with the club head approaching the ball from outside to in. This creates a pull if the clubface is square or a slice if the club face is open." TPI calls it "perhaps the most common swing fault among high handicap golfers" and says it is due to "an overuse of the upper body on the downswing." — [TPI, Over the Top](https://www.mytpi.com/improve-my-game/swing-characteristics/over-the-top)
- Titleist's over-the-top instruction: an attack angle "steeper than ideal" with a path "from outside the golf ball to inside", cutting across the ball, giving a pull or a slice **[SECONDARY, SNIPPET]**. — [Titleist EU, "Solutions for swinging over the top"](https://titleist.eu/instruction/over-the-top-solutions)
- **Early Extension (TPI, primary):**
  - definition: "any forward movement (thrust) of the lower body towards the golf ball during the downswing";
  - it causes the arms and club to get "stuck behind your body" and the torso to rise through impact;
  - "usually causes two typical miss hits, the block to the right and a hook to the left."
  - The TPI index page words it more broadly ("any movement towards the golf ball during the swing").
  — [TPI, Early Extension](https://www.mytpi.com/improve-my-game/swing-characteristics/early-extension); [TPI index](https://www.mytpi.com/improve-my-game/swing-characteristics)
- Early extension "can cause the club to work more from the inside out, which often results in hooks" **[SECONDARY, SNIPPET]**. — [RotarySwing](https://rotaryswing.com/goaty/videos/eliminate-early-extension-golf-swing.html). Rapsodo suggests checking for early extension when a golfer has a two-way miss **[SECONDARY, SNIPPET]**. — [Rapsodo](https://rapsodo.com/blogs/golf/early-extension-and-two-way-miss)
- **Loss of Posture (TPI, primary):** "any significant alteration from your body's original set up angles". It "usually causes two typical miss hits, the block to the right and a hook to the left." — [TPI, Loss of Posture](https://www.mytpi.com/improve-my-game/swing-characteristics/loss-of-posture)
- **Casting (TPI, primary):** "one of the most common causes of loss of power and excessive spin". It is "an early release of the golf club during the downswing", with a lead wrist "cupped at impact". It "adds loft to the face of the club". At impact the shaft should lean "slightly toward the target." — [TPI, Casting](https://www.mytpi.com/improve-my-game/swing-characteristics/casting)
- **Scooping (TPI, primary):** "a premature release of the wrist angles". It "adds loft to the face"; "the club head passes the hands through impact and the student is trying to lift the ball." — [TPI, Scooping](https://www.mytpi.com/improve-my-game/swing-characteristics/scooping)
- **Chicken Winging (TPI, primary):** lead elbow bends and wrist cups through impact; "tends to add loft to the club and excessive spin to the golf ball." — [TPI, Chicken Winging](https://www.mytpi.com/improve-my-game/swing-characteristics/chicken-winging)
- **Hanging Back (TPI, primary):** "a lack of weight shift towards the target on the downswing". The player is often on the back foot at impact. "Many times the player will hit heavy divots that begin behind the ball or they may have compensated with a ball position that is too far back". It is "a major cause of loss of speed." — [TPI, Hanging Back](https://www.mytpi.com/improve-my-game/swing-characteristics/hanging-back)
- **Sway / Slide (TPI, primary):** Sway is "any excessive lower body lateral movement away from the target during your backswing that forces your weight to the outside of your trail side foot". Slide is excessive lateral movement toward the target in the downswing. TPI states only power and sequencing losses for both, no specific ball flight. — [TPI, Sway](https://www.mytpi.com/improve-my-game/swing-characteristics/sway); [TPI, Slide](https://www.mytpi.com/improve-my-game/swing-characteristics/slide)
- **Low point → fat/thin:** TrackMan says the low point is mainly driven by the body pivot. A faulty pivot makes it wander, giving both fat and thin strikes **[PRIMARY, SNIPPET]**. — [TrackMan, "Top 8 ways to practice indoors"](https://www.trackman.com/blog/golf/top-8-ways-to-practice-indoors-with-trackman). GOLFTEC treats fat and thin as the same low-point problem: setup for short shots, head and hip movement for full swings **[SECONDARY, SNIPPET]**. — [GOLFTEC](https://golftec.com/blog-posts/how-to-stop-hitting-fat-shots-thin-shots)
- **Spin loft consequences:** higher spin loft gives more spin and a lower smash factor **[PRIMARY]**. — [TrackMan Spin Loft](https://www.trackman.com/blog/spin-loft)

### Inferences
**Decision table (right-handed; centred strike unless noted; F2P = face − path).** The "launch-monitor signature" and "swing patterns to check on video" columns are inferences from the laws above and the TPI definitions. Treat them as hypotheses to confirm on video and with contact evidence, not as diagnoses.

| Reported flight | Face (to target) | Path | Face-to-path | Likely strike/low point | Swing patterns to check on video | Source basis |
|---|---|---|---|---|---|---|
| Straight pull (starts left, no curve) | Closed (left) | Out-to-in, ≈ face | ≈ 0 | Centred | Over the Top with face square to path (TPI); also aim/alignment left | TPI OTT; TrackMan F2P |
| Pull-slice (starts left, curves right) | Left, but less left than path | Strongly out-to-in | Positive | Centred, or heel with driver (gear effect mimics it) | Over the Top + open face (TPI); upward driver AoA adds out-to-in path | TPI OTT; Rice 2011; GOLFTEC gear effect |
| Slice (starts ~at target, big curve right) | ≈ square/slightly open | Out-to-in | Large positive | Centred | Over the Top; open face from grip/wrist (not visible on video) | TPI; PING k-ratio |
| Push-slice / push-fade (starts right, curves right) | Open (right) | In-to-out less than face, or out-to-in | Positive | Centred; or toe with irons | Face open from the top; hanging back with an open face (ask about contact) | TrackMan F2P |
| Straight push / block (starts right, no curve) | Open ≈ path | In-to-out | ≈ 0 | Centred | Early Extension and Loss of Posture (TPI: "block to the right") | TPI EE, LoP |
| Push-hook / push-draw (starts right, curves left) | Right, less than path | Strongly in-to-out | Negative | Centred; or toe with driver | Early Extension "stuck" (TPI hook/block); very negative iron AoA adds in-to-out path | TPI EE; Rice 2011; Hattrick |
| Hook / pull-hook (starts at or left, curves left hard) | Closed | In-to-out or neutral, right of face | Large negative | Centred | Early Extension/Loss of Posture timing ("hook to the left", TPI); flip of the hands | TPI EE, LoP |
| Two-way miss (blocks and hooks) | Variable | Usually in-to-out | Swings ± | Variable | Early Extension, Loss of Posture (TPI's stated two-way miss) | TPI |
| Fat (ground before ball) | n/a | n/a | n/a | Low point behind the ball | Hanging Back ("heavy divots that begin behind the ball", TPI); Casting/Scooping; Sway not recovered | TPI HB; TrackMan low point |
| Thin / topped | n/a | n/a | n/a | Low point behind the ball (club rising at impact) or strike low on the face | Same pivot faults as fat (TrackMan: a faulty pivot gives fat **and** thin); Early Extension/standing up | TrackMan low point; GOLFTEC |
| High, weak, spinny ("balloon"), short | — | — | — | High dynamic and spin loft | Casting, Scooping, Chicken Winging (TPI: "adds loft", "excessive spin") | TPI; TrackMan spin loft |
| Low, knuckling (irons) | — | — | — | Low spin loft / low strike | Excessive shaft lean or low-face strikes; check ball position | TrackMan spin loft; GOLFTEC vertical gear |
| Toe strike, driver | Effectively opens | — | — | Toe | Starts right, draw spin; posture or distance to ball changes | GOLFTEC; TrackMan (Anderson) |
| Heel strike, driver | Effectively closes | — | — | Heel | Starts left, fade spin: can masquerade as a pull-slice/OTT | GOLFTEC |
| Shank (shoots sharply right) | — | — | — | Hosel contact | No source retrieved; commonly linked by coaches to the body moving toward the ball (early extension) or an in-to-out handle path. **Unsourced, verify** | — |

**Launch-monitor signatures of common faults** (direction of effect, inferred from definitions; magnitudes not published):
- **Over the Top:**
  - club path negative (out-to-in), often several degrees;
  - attack angle more negative (steeper) with irons;
  - swing direction left;
  - spin axis positive (slice) if the face is open to the path, near 0 (pull) if the face matches it.
  Basis: TPI, Titleist EU snippet, D-plane.
- **Casting / early release / scooping:**
  - higher dynamic loft and spin loft;
  - higher spin, lower smash factor (TPI "adds loft", "excessive spin"; TrackMan: higher spin loft gives more spin and a lower smash factor);
  - low point tends to move back toward or behind the ball;
  - attack angle less negative or positive with irons.
  The low point and attack angle effects are inference, not measured in sources.
- **Early Extension:**
  - path tends in-to-out ("stuck"; RotarySwing snippet);
  - face timing varies, so face-to-path swings sign (TPI: blocks and hooks);
  - strike location may drift toward heel or hosel as the body moves closer to the ball (inference);
  - low point varies.
- **Hanging Back / reverse pivot:**
  - low point behind the ball (TPI heavy divots behind);
  - with irons, a shallower or less negative attack angle and more fat/thin variation;
  - with the driver, more upward AoA, which by the D-plane geometry also pushes path out-to-in (inference).
- **Sway (backswing):** TPI states no ball-flight effect. Inference: if the lateral shift is not recovered, the low point moves back (fat/thin); if over-recovered into a slide, the low point moves forward and contact gets steeper.
- **Slide (downswing):** TPI states power loss only. Inference: the low point moves forward and the face is often left open (push/push-fade), but this is not sourced.

**Rules for the paid product (inferences):**
1. Never name a swing fault from ball flight alone. Pair each fault with the video frame that shows it (TPI slot lines for OTT; pelvis line for EE; face-on head and pelvis for hanging back/sway/slide).
2. Ask for strike evidence before calling a driver pull-slice "over the top" (heel gear effect).
3. Report face/path only as tendencies ("out-to-in path is likely"), not degrees.

### Gaps
- No published TrackMan (or other) dataset quantifying club path / AoA / low point for golfers classified with each TPI fault. The signatures above are mechanistic inferences.
- Shank, toe-shank and top causes were not covered by a retrieved primary source.
- TPI's statistics, such as the "67 % of 90,000 golfers have early extension" figure in the project notes, were not re-verified in this session; the current TPI pages fetched show no statistics.
