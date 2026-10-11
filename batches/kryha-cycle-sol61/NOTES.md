# Failed blind output-ring recovery, no target attempt

For m ordinary presses on the verified selected-stop wheel, total displacement is179, residue23mod26. For ciphertext position i define z_i = O[c_i] - 23 floor(i/m) mod26. Within each residue class i mod m, the unknown mask/phase displacement is constant. Thus equal plaintext at cycle-separated positions implies equal z. The unknown input alphabet does not enter this implication.

Pair objective sums choose(count(z),2) independently within each residue class. An explicit independent enumeration of every lag m,2m,... verifies exactly the same score. Unlike unconstrained global IC, comparisons require the known +23 per-cycle displacement. The substantive second objective sums choose(count(z),3), requiring three mutually consistent positions, rather than independently selected pair edges.

Three fresh385-letter controls use Slovak UD TEST offsets3000/4500/6000, random masks at m20/27/30, random mixed input/output rings and phases. Direct wheel traversal encoding agrees with an independent coordinate-arc inverse at all1155positions. All full-cycle displacement relations pass. Ordinary one press after every letter is intentional, including literal J: selective extra J presses are NOT modeled. Exact385-letter segments are disclosed, with normalization and X sentence separators; no claim that the messages were historically prepared this way.

Each objective uses32 blind random starts,20000 swap proposals/start, followed by up to10 complete best-swap scans. No planted ring, plaintext or stop mask enters optimization. Rotation gauge O[0]=0 allows exact output-ring comparison up to the unavoidable common rotation. m is supplied, making this easier than unknown-m target cryptanalysis.

| m | True pair | Random-null maximum (1000) | Optimized pair max | True triple | Random triple max | Optimized triple max |
|---|---:|---:|---:|---:|---:|---:|
|20|200|190|311|75|106|690|
|27|146|131|232|37|46|374|
|30|130|116|222|30|53|375|

Every one of the32 optimized false keys per case and objective exceeds its planted key score. No exact ring recovered. Triple coherence worsens concentration overfit: rare very large collision clusters dominate a cubic objective; even random null keys can exceed true scores. More identical restarts cannot repair this ranking defect. The cycle identity is correct, but these stand-alone output-ring objectives do not identify the true ring on the fresh385-letter samples. No m20–30 sweep, stopmask/input-ring inference, target350/351 attempt or cipher-family exclusion follows.

All192 optimized ring candidates and scores are independently rescored and verified as permutations. Full truth/false diagnostics are in diagnostics.json; saved ciphertexts, truths, seeds and masks are in controls.json. No source cipher files or markers were changed.

Reproduce:

```sh
python3 batches/kryha-cycle-sol61/prepare.py
clang++ -O3 -std=c++17 batches/kryha-cycle-sol61/cycle.cpp -o batches/kryha-cycle-sol61/cycle
python3 batches/kryha-cycle-sol61/run.py 2
python3 batches/kryha-cycle-sol61/run.py 3
python3 batches/kryha-cycle-sol61/diagnose.py
```
