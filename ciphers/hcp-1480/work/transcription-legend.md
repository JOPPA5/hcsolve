# CURRENT LABEL SET (2026-10-30, after review 1) -- read this first
The labels used in work/transcription.txt and work/key.json are:
TRI=D, RIGHT_TRI=H, DOWN=S, RECT=T, BOX=E, BOX_BAR=E, BOX_CROSS=K, CROSS=I,
CIRCLE=A, CROSS_CIRCLE=J, CUP=U, DIV=R, CURVED_BAR_TWO_DOTS=R, UNDER=C,
WAVE=W, BAR=L, SLANT_BAR=L, C_SHAPE=O, DOTTED_C=O, CARET=V, CURL_N=N,
ARCH=Y, T_STEM=M.
SUPERSEDED labels (kept below only as history, no longer used anywhere):
HOOK (= faded ARCH, Y), CURVED_DIV (split into CURVED_BAR_TWO_DOTS=R and
DOTTED_C=O), BAR_LOWER_MARK (= T_STEM, M). The descriptions of these three
in the sections below are out of date.

# Shape labels, manually read from scan
TRI: upright triangle; RIGHT_TRI: triangle pointing right; DOWN: downward
triangle with internal/extended vertical stroke; RECT: narrow tall rectangle.
BOX: plain square; BOX_BAR: square with stronger internal horizontal bar;
BOX_CROSS: square with internal cross/diagonals. CROSS: X.
CIRCLE: open oval; CROSS_CIRCLE: circle with +; CUP: vertical stem between
curved top/bottom strokes; DIV: short bar with dot above/below.
UNDER: shallow curved line with short horizontal below. WAVE: sine-like stroke.
BAR: horizontal stroke; SLANT_BAR: short slanting stroke at end of signature.
C_SHAPE: curved C-like stroke; CARET: inverted V; CURL_N: cursive2-like curl.
ARCH: round-topped triangle/arch at start of final5-symbol word.
CURVED_DIV: division-like glyph with curved/sloping bar; may be a DIV variant,
but not normalized to it without evidence. HOOK: shallow upward curved hook.
BOX and BOX_BAR currently mapped E as handwriting variants (hypothesis).
BAR and SLANT_BAR currently mapped L as handwriting variants (hypothesis).
These are glyph labels, not direct source letters, and not a standard Pigpen
key. Slashes mark word spaces, physical line breaks retained.

## Offline visual correction2026-10-26
Earlier CURVED_DIV conflated two visibly different source shapes. The final
glyph of EVE… has a dot above and below a short curved bar: now
CURVED_BAR_TWO_DOTS, normalized to DIV=R because dot count and bar structure
match repeated R elsewhere. The second glyph of the next word has a C-like
open curved stroke plus a lower horizontal stroke and one upper dot; no
separate lower dot is visible. It is now DOTTED_C and remains unmapped.
Compare work/offline-ever-large.jpg and work/offline-yours-large.jpg. These
are sips crops/enlargements of the immutable address, not new source detail.
The earlier generic CURVED_DIV description above is superseded.

## Third visual correction —2026-10-26
BAR_LOWER_MARK: horizontal stroke plus a separate dark lower hook/dot-like
mark, in the first position of the2-symbol group after ARCH DOTTED_C CUP DIV
DOWN. Previously BAR=L; now unknown because the lower mark was omitted by
that normalization. Function and exact segmentation are uncertain. Compare
work/singletons-atlas.png, source rectangle(269,471,306,513).61positions is
the retained manual grouping; it does not claim independent letter count.

## Claude correction — 2026-10-29
T_STEM: horizontal bar with a faint vertical stem and small foot below it
(the former BAR_LOWER_MARK, seen as one T-shaped sign) = M (context MY).
HOOK no longer used: that sign is ARCH with a faded upper arc (= Y).
DOTTED_C mapped O (pointed C as in LOVE, plus one dot).
