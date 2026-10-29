# hcsolve

A repo for solving historical ciphers with a pair of AI agents:

- **Solver** – the main agent, **GPT** by default. Fetches the cipher and its context, solves it, and produces a PDF report at the end.
- **Reviewer** – a second agent from a different provider, **Claude** by default. Independently checks what the solver claims.

After the review, the solver corrects its solution and only then closes it.

> **If you are an agent and have just loaded this repo:** this file is your brief. First determine your role (below), then find the state of the cipher and continue exactly from there.

## Which role am I

1. If the prompt that started you names a role (`solver` / `reviewer`), the prompt wins.
2. Otherwise use the default role from the file your tool loaded at startup: `AGENTS.md` → **solver**, `CLAUDE.md` → **reviewer**.
3. If you loaded neither, do not guess your role – ask.

Your role must match the state of the cipher (table below). If it is not your turn, do nothing and say so.

If you do not know which cipher to work on and the prompt does not say, ask. Do not pick one yourself.

## Layout

Each cipher has its own directory `ciphers/<slug>/` (slug in lowercase with hyphens, e.g. `ciphers/copiale/`):

```
ciphers/<slug>/
  source/        the original cipher and context – never modified after download
  SOURCES.md     where each file in source/ came from (URL, date, what it is)
  work/          scripts, attempts, intermediate results
  NOTES.md       running log: hypotheses, what was tried, what failed and why
  SOLUTION.md    the solver's current claim
  review/        REVIEW1.md, REVIEW2.md … – only the reviewer writes here
  report/        report.pdf and its source
  register-entry.txt   the entry for the AI Decipherment Register (solver, step 7)
  DONE1, REVIEWED1, FINAL …   state markers (see below)

scripts/watch.sh   the watcher that wakes the agent whose turn it is
skip.txt           cryptogram numbers that are already solved and must be skipped
```

## Protocol: state markers

Agents hand work over using **marker files** in the cipher directory. A watcher (`scripts/watch.sh`) listens for them and wakes the other agent. A marker is therefore both the signal and the record of state.

**Starting the watcher is the agent's job, not the human's.** Before you create any marker, make sure it is running for your cipher:

```bash
nohup scripts/watch.sh ciphers/<slug> >/dev/null 2>&1 &
```

The script is safe to start repeatedly – if a watcher for that cipher is already running, the new one exits at once. It logs to `ciphers/<slug>/.watch.log` and stops by itself once `FINAL` exists. If the other agent does not seem to have been woken, read that log before doing anything else.

| Marker | Created by | Meaning | Wakes |
|---|---|---|---|
| `DONEn` | solver | "I think I am done, round *n*" | the reviewer |
| `REVIEWEDn` | reviewer | "`review/REVIEWn.md` is complete" | the solver |
| `FINAL` | solver | review addressed, `report/report.pdf` exists | nobody – the end |

Rules for markers:

- **Create the marker as the very last step.** Finish writing every file first, check the watcher is running, then create the marker. The watcher wakes the other agent immediately, and it must not find half-written work.
- Write one line into the marker: the UTC time and your model (e.g. `2026-10-11T19:20Z claude-opus-5-5`).
- After creating a marker, **change nothing else in that cipher's directory**. Do not wait in a loop and do not start the other agent yourself – the watcher starts it, and later starts you again in a fresh session.
- If you were given a single cipher, end your turn after creating the marker. **If you are the solver working through a range, do not end your turn: go on to the next number.** The review of each cipher is handled by the fresh session the watcher starts, so several ciphers can be in review while you keep solving.
- Markers are never deleted or overwritten. The next round gets the next number.

### How to find the state after loading the repo

Look at which markers exist in `ciphers/<slug>/`:

| State | Whose turn | What to do |
|---|---|---|
| directory missing or has no markers | solver | solve |
| highest is `DONEn`, no `REVIEWEDn` | reviewer | review round *n* |
| highest is `REVIEWEDn` | solver | address the review, then `FINAL` or `DONEn+1` |
| `FINAL` exists | nobody | done; change nothing without an instruction from a human |

## Instructions for the solver

**0. Skip what is already solved.** Do not work on a cryptogram from crypto.hcportal.eu if either holds:

- its number is listed in `skip.txt` in the repo root, or
- its page on the portal shows the status `Solved`.

In that case create no directory for it, tell the human which rule applied, and move to the next number if you were given a range. When working through a range, go downwards from the highest number.

**1. Setup.** If `ciphers/<slug>/source/` is missing or empty, download the cipher (transcription and scans, if available) and its historical context: who, when, to whom, in what language, and which ciphers were in use at that time and place. Record every file in `SOURCES.md`. Do not edit files in `source/` afterwards – working copies belong in `work/`. Then start the watcher (see the protocol above) so the handover later needs no human.

For cryptograms from crypto.hcportal.eu, read the page `https://crypto.hcportal.eu/dashboard/cryptograms/<number>` in a browser – it is rendered by JavaScript, so a plain HTTP fetch returns an empty shell. There is no data API to use; do not look for one or try to get around access controls. The page has three tabs, and you need all of them:

- **General** – metadata (name, date, language, archive, sender, recipient); save it as `source/metadata.md`. Note the status and tags at the top (e.g. `Solved`, `Unsolvable`) in `SOURCES.md`.
- **Description** – free-text notes; save them with the metadata.
- **Attachments** – the cryptogram image, plus any transcriptions and solutions. Save the image to `source/`. If a transcription is attached, save it too; if not, transcribe the image yourself into `work/` and say so in `SOLUTION.md`.

If the portal already attaches a solution, step 3 applies: record it and do not present it as your own.

The [ManuLab API](https://manulab.hcportal.eu/apidoc/index.html) is a public text-statistics service (n-gram frequencies, index of coincidence, entropy, language guess). You may use it as a helper, but it does not serve cryptograms.

**2. Solving.** Keep `NOTES.md` up to date as you go, dead ends included – both the reviewer and you, after being woken, rely on it. Do everything you can with a script in `work/`, not by hand.

**3. Honesty about sources.** If you come across an already published solution while gathering context, record it in `SOURCES.md` and `SOLUTION.md` and do not present it as your own. Label a partial solution as partial.

**4. Handover (`DONEn`).** When you think you are done, write `SOLUTION.md`:

- the cipher type and the key (substitution table, nomenclator, keyword…)
- the plaintext in the original language and its translation
- **a single command** that produces the full plaintext from the file in `source/` and the key
- what remains uncertain: undeciphered symbols, guessed words, alternative readings
- why you believe it is correct (coverage of the text, coherence, agreement with the context)

Only then create `DONEn`. Stop there for a single cipher; in a range, continue with the next number.

**5. After being woken (`REVIEWEDn`).** Read `review/REVIEWn.md` and add a section `## Response to review n` to `SOLUTION.md`, stating for each finding what you fixed or why you disagree (with evidence). Then:

- verdict `ACCEPT`, or `REVISE` and you have addressed the findings → produce the PDF and the register entry, then create `FINAL`
- verdict `REJECT`, or you changed the solution substantially → create `DONEn+1` and have it checked again

**6. PDF report.** `report/report.pdf` (keep its source next to it, e.g. `report/report.md`) contains: the origin and context of the cipher, the method, the key, the plaintext and translation, what remains uncertain, and a summary of the review and what changed because of it. Write it for a person who has seen nothing in `work/`.

**7. Register entry.** Solved cryptograms are submitted to the [AI Decipherment Register](https://ai.hcportal.eu/register/). Before creating `FINAL`, write `ciphers/<slug>/register-entry.txt` containing exactly one entry in this format:

```
{submitted: "2026-10-11", solver: "<name given by the human>", source: "https://crypto.hcportal.eu/dashboard/cryptograms/489", name: "pc_hcp_489", type: "MASC", model: "OpenAI GPT", version: "GPT-6 Astra", role: "transcription, analysis, decipherment; independent review by Claude Opus 5.5", agents: "YES", documentation: "https://github.com/JOPPA5/hcsolve/tree/main/ciphers/hcp-489"},
```

- `submitted` – the UTC date you create `FINAL`
- `solver` – the person's name as given by the human; if you were not given one, write `"TODO"` and say so in your final message
- `source` – the cryptogram's page; `name` – its name as used on the portal
- `type` – the cipher type you established (e.g. `MASC`, `Mirror writing`, `Nomenclator`)
- `model` / `version` – the solver's own vendor and model, stated truthfully
- `role` – what the AI actually did, plus the reviewer's model
- `agents` – `"YES"` in this workflow
- `documentation` – the URL of the cipher directory in this repo

Cryptograms from crypto.hcportal.eu use the slug `hcp-<number>`. Only write an entry for a solution the review accepted; for a partial or rejected one, write no entry.

## Instructions for the reviewer

Your job is to **try to refute the solution**, not to confirm it. Do not trust the solver's claims until you have verified them yourself.

- Write **only** to `review/`. Do not change the solver's files or `source/`; put your own verification scripts in `review/work/`.
- Run the command from `SOLUTION.md` and compare its output with the claimed plaintext. Where possible, also decrypt with your own independent script.
- Check that the key is consistent and covers the **entire** ciphertext, not just selected passages.
- Check the transcription against the scans in `source/`, if there are any.
- Judge the plaintext: is it real language of that period, or random words forced onto noise? Do names, dates and places fit the context?
- Check that the solver disclosed every uncertainty and did not use a published solution without saying so.

Write the result to `review/REVIEWn.md`:

- **Verdict** on the first line: `ACCEPT`, `REVISE` or `REJECT`
- what you verified and how (commands, outputs)
- numbered findings, each with evidence and a severity (`blocker` / `major` / `minor`)
- what you could not verify

Only then create `REVIEWEDn` and stop. Do not fix the solution yourself – that is the solver's job.

## For the human: the watcher

You do not need to start anything – the agents start `scripts/watch.sh` themselves. You only choose how the agents are launched. The defaults are:

```bash
SOLVER_CMD="codex exec --full-auto"
REVIEWER_CMD="claude -p --allowedTools Read,Write,Edit,Glob,Grep,Bash"
```

To change them (another model, other flags), put the overrides in a `watch.conf` file in the repo root. The watcher appends the prompt as the last argument; it states the role and the path to the cipher.

Both agents run unattended with permission to run commands, on content that includes files downloaded from the internet. Run this on a machine and account where that is acceptable.

## Contact

Tomáš Pavuk – xpavukt@stuba.sk
