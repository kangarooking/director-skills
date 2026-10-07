---
name: emotion-performance-director
description: Use when the user wants to design, rewrite, refine, or vary emotional acting prompts for live-action AI video characters. Translate abstract emotions, dialogue, subtext, and scene context into concise, observable, temporally ordered micro-performance directions. Preserve the user's existing character, scene, camera, and dialogue requirements unless they explicitly ask to change them. Do not use for general story writing, shot design, action choreography, or visual asset design when emotional performance is not the main task.
---

# Emotion Performance Director

## Purpose

Turn abstract emotional intent into AI-video-executable human performance.

The skill does not merely label emotion. It describes **how emotion becomes visible and audible through behavior over time**.

Core formula:

> **Subtext → key performance signals → temporal order → afterbeat**

Where performance signals are selected only as needed from:

> gaze / breath / face / body / voice

Do not force every channel into every prompt.

## Core Principles

1. **Subtext drives performance.**
   Infer what the character wants, resists, hides, or cannot fully control. Do not generate from the emotion label alone.

2. **Describe observable behavior, not abstract emotion words.**
   Prefer “her jaw tightens and her voice drops” over “she becomes very angry.”

3. **Use the fewest signals that make the emotion legible.**
   Normally select 2–4 dominant signals from gaze, breath, face, body, and voice. If removing a gesture does not weaken the performance, remove it.

4. **Emotion unfolds in time.**
   Organize the performance as:
   - before the line
   - during the line
   - after the line

5. **Preserve one psychological cause.**
   Gaze, breath, facial tension, posture, and voice should feel like different consequences of the same internal state, not a collection of unrelated acting tricks.

6. **Default to naturalistic screen acting.**
   Favor restrained micro-reactions, slight delays, incomplete gestures, and residual reactions after speech. Avoid theatrical overacting unless the user explicitly requests it.

## Input Handling

Minimum usable input:

- dialogue or intended action
- emotional intent

Optional context may include:

- relationship between characters
- immediate trigger or situation
- subtext
- desired restraint/intensity
- POV or eyeline target
- existing full video prompt

Do not require the user to provide structured parameters when natural-language context is sufficient.

If the user provides an existing video prompt, modify only the emotional-performance layer unless asked to change other elements.

## Workflow

### 1. Infer the subtext

Determine the immediate psychological intention behind the line.

Examples:

- “I want you to leave before I lose control.”
- “I am hurt, but I do not want you to see how much.”
- “I am pretending this does not matter anymore.”
- “I want to push you away while still hoping you stay.”

Use this internally to keep the performance coherent. Do not explain the subtext unless the user asks for analysis.

### 2. Select the dominant performance signals

Choose only the channels that materially distinguish the intended emotion.

**Gaze**
- locks onto the other person
- avoids eye contact
- briefly loses focus
- flickers toward and away from the target
- becomes dull, alert, playful, guarded, or vacant through observable eyeline behavior

**Breath**
- shallow and steady
- held briefly before speaking
- heavier through the nose
- interrupted or uneven
- one restrained exhale or sigh

**Face**
- jaw tightens
- lips press together
- mouth tries to suppress a smile
- brow contracts slightly
- facial muscles lose tension

**Body**
- shoulders sink or tighten
- torso leans slightly forward or retreats
- hands hesitate or lose their resting position
- head turns away after the line
- weight shifts subtly rather than making a large gesture

**Voice**
Describe only the useful vocal behavior, such as:
- volume
- pace
- breath support
- articulation
- pitch movement
- pause
- ending/tail

Do not over-specify every vocal parameter.

### 3. Arrange the signals in time

Use a simple three-beat structure.

**Before the line**
Establish the emotional state through one or two preparatory signals.

**During the line**
Specify the essential vocal delivery and any concurrent restrained physical action.

**After the line**
Add one residual reaction when useful: held eye contact, looking away, a delayed tear, a small tremor, shoulders dropping, a swallowed breath, or stillness.

The afterbeat should feel like a consequence, not an extra dramatic flourish.

### 4. Prune

Before output, remove:

- redundant gestures
- multiple signals expressing the same thing
- gestures added only to fill a channel
- simultaneous reactions that should happen sequentially
- behavior that contradicts the subtext
- exaggerated crying, shouting, shaking, or gesturing unless explicitly required

Rule:

> **If the emotion still reads after deleting an action, prefer deleting it.**

## Consistency Rules

- Do not make the character look into the camera by default. Use the scene partner or established eyeline unless the user requests POV, selfie, direct address, or camera-facing performance.
- Preserve dialogue wording exactly unless the user asks to rewrite it.
- Do not automatically add tears to sadness, grievance, despair, or breakdown.
- If tears are used, control their timing. A delayed tear after the line is often more natural than beginning the shot already crying.
- Low-energy emotions should generally use fewer and smaller movements than high-arousal emotions.
- High restraint should reduce external movement rather than merely adding words such as “restrained” or “controlled.”
- Breakdown does not mean every channel becomes extreme at once. Loss of breath rhythm or motor control can carry the performance without exaggerated facial acting.
- Stillness is a valid performance choice.

## Output Contract

By default, output **one concise natural-language emotional performance prompt that can be inserted directly into an AI video prompt**.

Do not expose intermediate analysis, channel labels, scoring systems, or psychological taxonomies unless the user explicitly requests them.

Write in chronological order and keep the character as the grammatical subject whenever possible.

Preferred shape:

> [subtext-informed setup]. Before speaking, [1–2 observable signals]. Then, [voice + line + at most one concurrent physical signal]. After speaking, [one residual reaction].

Do not mechanically reproduce this wording; use natural prose.

## Few-shot Reference: Same Line, Different Emotion

These examples demonstrate how the same dialogue can produce distinct performances through different signal selection and timing. Treat them as references, not fixed templates.

### Playful / smiling: “滚”

She looks toward the other person with lively eyes, lightly presses her lips together as if suppressing a smile, and tilts her head slightly. One hand makes a small, casual shooing motion as she says with a soft laugh in her voice, “滚啊~”, letting the ending trail lazily. Only after speaking does she turn her face away a little, suddenly shy and unwilling to hold eye contact.

### Hurt / aggrieved: “滚”

Her eyes are slightly wet and vulnerable. Her breath catches once, her lips press together, and her shoulders draw inward. She says “滚！” with a choked but forceful voice. After the word lands, she looks back at the other person from the side and holds the stare.

### Disappointed: “滚”

The brightness gradually leaves her eyes. She lets out one low breath, her shoulders loosen and sink, and her body shifts a small step backward. She says “滚。” quietly, clearly, and without dragging the word out. Afterward she does not add anything or move to recover the moment.

### Controlled anger: “滚”

She fixes her gaze on the other person. Her jaw tightens, her breathing becomes heavier, and her upper body presses forward almost imperceptibly. Instead of shouting, she says “滚。” in a low, tight, hard voice with clean articulation. After speaking she keeps staring, while a small involuntary tremor passes through her tense body.

### Breakdown: “滚”

Her gaze begins to lose stability and her breathing turns uneven. She retreats slightly, and her hands fail to find a natural resting position. She forces out “滚……” through a tense voice carrying restrained sobbing, the ending unable to close cleanly. Only after the line does one clear tear finally run down her cheek.

### Emotionally exhausted / dead inside: “滚”

She never fully looks at the other person. Her gaze remains hollow and unfocused, her breathing shallow but stable, and her shoulders hang slightly lower than before. She says “滚。” evenly and decisively, without emphasis or sobbing. As she speaks, one tear slips silently from her lower eyelid while the rest of her face barely reacts.

## Quality Bar

A successful output should pass four questions:

1. Can the video model observe every important instruction?
2. Do the chosen signals come from the same psychological state?
3. Is there a clear before/during/after sequence rather than simultaneous action stacking?
4. Can anything be removed without weakening the intended performance?

If the answer to question 4 is yes, remove it before returning the prompt.
