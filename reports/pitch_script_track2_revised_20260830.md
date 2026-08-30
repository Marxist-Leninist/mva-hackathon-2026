# Revised Track 2 pitch — report-aligned 3-minute script

**Status:** source for a new render; the existing MP4 predates the 30 August
scientific reconciliation and must not be uploaded as the final pitch.

**Target:** approximately 2:45-2:55 at 145-155 words per minute.

---

## 0:00-0:25 — The genotype and uncertainty

*Slide 1: two variants, with `phase unproven` and `missense VUS` visible.*

> This child has Mosaic Variegated Aneuploidy and two heterozygous variants in
> BUB1B. One is a premature stop at leucine 737. The other is an ultra-rare
> missense change at asparagine 1002 — one allele among about 1.46 million
> gnomAD exome alleles.
>
> We confirmed both from all eight raw-read lanes without trusting the supplied
> variant caller. But short reads do not prove they are in trans, and the
> missense variant has never been functionally tested. Those uncertainties shape
> the whole proposal.

## 0:25-0:58 — The mechanism

*Slide 2: stop allele -> NMD; missense allele -> three possible fates.*

> BUBR1 helps hold the spindle checkpoint and stabilize chromosome attachment.
> Published MVA cells show that some truncating alleles lose their transcript,
> while some C-terminal missense proteins turn over too quickly. Raising selected
> low-abundance mutants restored checkpoint function.
>
> That does not prove this child's missense protein is unstable. It could be
> unstable, stable but defective, or even functionally neutral. So the first
> experiment is molecular diagnosis: phase the variants, measure allele-specific
> RNA, protein abundance, half-life and checkpoint function.

## 0:58-1:45 — The ranked drug screen

*Slide 3: ranked screen with clear labels: lead, conditional, benchmark, control.*

> If the biological substrate exists, our lead approved-drug screen is
> azithromycin against the exact UGA-A stop context. A reporter signal is not
> enough. We require full-length stop-allele BUBR1, mass-spectrometric
> identification of the inserted residue, and functional rescue near exposure
> achieved in approved use.
>
> Arimoclomol is second, but conditional. It enters only if asparagine 1002 lysine
> is first shown to be a short-lived, chaperone-responsive and recoverable
> protein. No publication shows that arimoclomol rescues BUBR1.
>
> Sirolimus is only an autophagy benchmark, acetylcysteine only a biomarker-gated
> redox comparator, and gentamicin only a laboratory readthrough control.

## 1:45-2:25 — The safety innovation

*Slide 4: `prevents new aneuploidy` versus `preserves abnormal clone`.*

> The central safety problem is unusual. A drug may make an aneuploid culture
> look healthier simply by helping an abnormal clone survive. That is not rescue
> in a cancer-predisposition syndrome.
>
> Our primary endpoint is therefore the rate of newly generated chromosome-
> segregation errors, confirmed by live imaging and single-cell copy-number
> profiling. Every candidate must improve at least two orthogonal functional
> outcomes and pass a rescue-versus-clone-safety index. We reject anything that
> expands pre-existing aneuploid clones, increases micronuclei or DNA damage,
> weakens immune surveillance, or needs non-repurposable exposure.

## 2:25-2:50 — What success means

*Slide 5: a go/no-go decision tree.*

> A positive result gives a precise, independently reproducible path toward
> pharmacology and toxicology. A negative result is also valuable: it tells us
> whether the barrier is NMD, stop context, the inserted amino acid, intrinsic
> missense dysfunction, or downstream tissue stress.
>
> This is not a treatment recommendation and proposes no dose or change to
> current care. It is a falsifiable route from two uncertain alleles to a small,
> safety-aware experimental programme. Thank you.

---

## Production notes

- Use five static slides and burned-in captions.
- Keep `phase unproven`, `missense VUS`, and `no treatment recommendation`
  visible on slide 1.
- Do not state that the child has 5-10% residual BUBR1. That was scenario
  analysis, not a patient measurement.
- Do not use the previous vincristine section. The revised report recommends no
  oncology treatment change and has no patient-specific chemotherapy-response
  data.
- Rebuild narration, captions, slides and MP4 from this source, then re-run the
  runtime, loudness, caption and frame-by-frame checks before hosting.
