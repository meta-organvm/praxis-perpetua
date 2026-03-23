---
sgo_id: SGO-2026-RP-006
title: "The Fourfold Correspondence"
tier: Dissertation
status: LOCAL (second draft — TRP amendments incorporated)
target_venues: [J. Logic Language and Information, Mathematical Structures in Computer Science, arXiv cs.FL]
dependencies: [RP-01]
date: 2026-03-20
revision_history:
  - version: v1
    date: 2026-03-21
    note: "First draft"
  - version: v2
    date: 2026-03-20
    note: "TRP amendments incorporated: cross-linguistic evidence (A4), multiword expression problem (A3), Shieber critical treatment (A4/critique), stratified precision claims (A1), gradient grammaticality (A3), worked Type 1 example (A2), MCS gap conjecture (A6), consolidated four-column table (A5), transformer probing tempered (A10), generativist vs. usage-based debate (A3)"
trp_gate:
  review_id: TRP-RP-06
  verdict: "Advance with amendments"
  amendments_addressed: [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A14, A15]
  amendments_deferred: [A12, A13]
---

# The Fourfold Correspondence: Grammar, Automaton, Type, and Proof from Chomsky to Curry-Howard-Lambek

**Studium Generale ORGANVM -- Research Paper SGO-2026-RP-006**

---

## Abstract

This dissertation establishes and investigates a fourfold structural correspondence linking formal grammars, abstract automata, type systems, and proof calculi. The classical result in formal language theory pairs each level of the Chomsky hierarchy with a class of abstract machines: regular grammars with finite automata, context-free grammars with pushdown automata, context-sensitive grammars with linear bounded automata, and unrestricted grammars with Turing machines. We extend this well-known twofold correspondence to a fourfold one by demonstrating that each level admits, in addition, a canonical type-theoretic characterisation and a corresponding proof-theoretic regime. The extension is mediated by categorial grammar (Ajdukiewicz, Bar-Hillel, Lambek) and by the Curry-Howard-Lambek correspondence, which identifies propositions with types, proofs with programs, and logical systems with categories. We argue that these are not four independent correspondences but four projections of a single mathematical structure, while carefully stratifying the strength of evidence at each level: the correspondence ranges from a constructive isomorphism at the context-free level, through a structural embedding at the context-sensitive level, to an analogy at the unrestricted level. We ground our linguistic claims in typologically diverse evidence spanning agglutinative (Turkish), isolating/tonal (Mandarin), sign (ASL), non-configurational (Warlpiri), and polysynthetic (Mohawk) languages, and we address the limitations posed by gradient grammaticality, multiword expressions, and the contested status of key empirical arguments. We survey the historical development from Chomsky's 1956 hierarchy through Lambek's 1958 syntactic calculus to the DisCoCat framework of Coecke, Sadrzadeh, and Clark; we examine where the fourfold correspondence holds precisely and where it breaks down; and we identify three open problems: the type-theoretic characterisation of mildly context-sensitive languages (for which we propose a conjecture), the question of whether neural language models learn type-theoretic structure, and the formal relationship between Chomsky's Merge operation and typed function application.

**Keywords:** Chomsky hierarchy, type theory, Curry-Howard correspondence, categorial grammar, Lambek calculus, formal language theory, mildly context-sensitive languages, compositional semantics, cross-linguistic typology, gradient grammaticality

---

## 1. Introduction

In 1956, Noam Chomsky proposed a classification of formal grammars into four types, arranged by increasing generative power, that has since become one of the most consequential taxonomies in the mathematical sciences (Chomsky, 1956). The *Chomsky hierarchy*, as it came to be known, stratifies formal grammars into regular grammars (Type 3), context-free grammars (Type 2), context-sensitive grammars (Type 1), and unrestricted grammars (Type 0). Each class generates a strictly larger family of formal languages than its predecessor, and each admits recognition by a correspondingly more powerful class of abstract machines: finite automata, pushdown automata, linear bounded automata, and Turing machines, respectively. This grammar-automaton correspondence, established through the combined efforts of Chomsky (1959), Rabin and Scott (1959), Myhill (1957), and others, constitutes one of the foundational results of theoretical computer science.

The significance of the hierarchy extends well beyond its original domain. Chomsky formulated it to characterise the structural properties of natural language; within a decade, the same formal apparatus had been adopted by computer scientists as the basis for programming language definition. Backus and Naur's notation for the syntax of ALGOL 60 (Backus, 1959; Naur, 1960) is a context-free grammar in Chomsky's precise sense, and the phrase-structure rules that Chomsky proposed for English in *Syntactic Structures* (Chomsky, 1957) are formally identical to the production rules that define programming language parsers. The hierarchy thus serves as a shared substrate linking linguistics and computer science -- a mathematical Rosetta Stone that permits phenomena in one discipline to be translated into the vocabulary of the other.

Yet the grammar-automaton correspondence, for all its elegance, captures only two of the relevant dimensions. There exists a third dimension -- type-theoretic -- that is less widely recognised but arguably runs at least as deep. In this dimension, each level of the Chomsky hierarchy corresponds to a regime of type-system expressiveness: regular grammars to finite (enumeration) types, context-free grammars to recursive algebraic types, context-sensitive grammars to parametrically polymorphic types, and unrestricted grammars to fully dependent types. This correspondence is not merely analogical. It can be made precise through the framework of *categorial grammar*, in which syntactic categories are function types, grammatical derivations are proofs, and sentence formation is typed function application (Ajdukiewicz, 1935; Bar-Hillel, 1953; Lambek, 1958).

The bridge from types to proofs is provided by the *Curry-Howard correspondence* (Curry, 1934; Howard, 1969/1980), which demonstrates that propositions are types and proofs are programs. Lambek (1972, 1980) extended this to a three-way equivalence by showing that typed lambda calculi correspond to Cartesian closed categories: propositions are types are objects, proofs are programs are morphisms, and logical systems are type theories are categories. When combined with the observation that Lambek's own 1958 syntactic calculus is simultaneously a grammar formalism, a logical system, and a typed calculus, the three-way correspondence becomes fourfold: grammatical derivations are proofs are typed terms are morphisms in a category.

### 1.1 Stratification of Correspondence Strength

A critical methodological point must be established at the outset. The nature of the fourfold correspondence varies significantly across the levels of the Chomsky hierarchy, and conflating these different degrees of strength would undermine the contribution's formal credibility. We distinguish three tiers of correspondence strength:

**Isomorphism.** A constructive bijection exists between the structures on both sides of the correspondence, with inverse maps that preserve all relevant structure. At this tier, the two descriptions are provably the same mathematical object.

**Structural embedding (homomorphism).** A structure-preserving map exists from one side to the other, such that the grammar-side structures can be faithfully represented in the type-theoretic structures, but the map is not necessarily surjective or invertible. At this tier, the type-theoretic domain is a faithful model of the grammatical domain but may contain additional structure.

**Analogy.** The two sides share structural features -- similar closure properties, similar decidability boundaries, similar compositional principles -- but no single formal map has been established. At this tier, the correspondence is a productive heuristic supported by partial formal results.

The following table classifies each level of the fourfold correspondence according to this stratification:

| Chomsky Level | Grammar-Automaton | Grammar-Type | Grammar-Proof | Overall Strength |
|---------------|-------------------|--------------|---------------|------------------|
| Type 3 (Regular) | Isomorphism (Kleene, 1956) | Structural embedding | Structural embedding | Embedding |
| Type 2 (Context-free) | Isomorphism (Chomsky, 1962) | **Isomorphism** (BNF = algebraic types) | Isomorphism (Lambek calculus) | **Isomorphism** |
| MCS (Mildly context-sensitive) | Isomorphism (Vijay-Shanker & Weir, 1994) | **Open problem** | Partial (CCG = combinatory logic) | Partial |
| Type 1 (Context-sensitive) | Isomorphism (Kuroda, 1964) | Structural embedding (conjectured) | Analogy | Embedding |
| Type 0 (Unrestricted) | Isomorphism (by definition) | Analogy (undecidability parallel) | Analogy | Analogy |

This stratification has a crucial consequence: the paper's strongest contribution is at the context-free level, where the fourfold correspondence is a genuine isomorphism. Claims about the other levels must be qualified accordingly, and we do so throughout.

### 1.2 Scope and Framing

This dissertation is framed within the generativist tradition of formal grammar, for the straightforward reason that the Chomsky hierarchy *is* a generativist construct. We acknowledge at the outset that substantial traditions in linguistics -- including Construction Grammar (Goldberg, 1995, 2006), Cognitive Grammar (Langacker, 1987, 2008), and usage-based approaches (Bybee, 2006, 2010) -- reject the premise that natural language structure is best described by formal grammars in the Chomsky sense. These traditions emphasise the gradient, probabilistic, construction-specific, and usage-driven nature of linguistic knowledge, and their empirical critiques of the generativist programme are well-documented and serious. Section 5.6 addresses this debate directly. The fourfold correspondence, as developed here, applies most cleanly to *formal* and *computational* languages, where compositionality is exact and grammaticality is binary. Its extension to natural language is conjectural and approximate, and we are explicit about where the fit degrades.

Three research questions guide the inquiry:

**RQ1.** What is the precise type-theoretic characterisation of each level of the Chomsky hierarchy, and can this characterisation be extended to the class of *mildly context-sensitive* languages -- the conjectured complexity class of natural language (Joshi, 1985)?

**RQ2.** Do neural language models (transformer architectures) implicitly learn type-theoretic structure, and if so, at what level of the Chomsky hierarchy does their implicit grammar reside?

**RQ3.** Is the Merge operation of Chomsky's Minimalist Program (Chomsky, 1995) formally equivalent to function application in the typed lambda calculus, and what does this equivalence or inequivalence imply for the relationship between linguistic competence and computational capacity?

The principal contribution of this work is the systematic extension of the classical grammar-automaton correspondence to a fourfold grammar-automaton-type-proof correspondence, with explicit stratification of the correspondence strength at each level. We argue that this extension reveals structural constraints with practical consequences for programming language design, natural language processing, and the theory of linguistic competence. In particular, we show that the decidability properties of each Chomsky level -- which determine whether parsing, type-checking, and proof search terminate -- are broadly preserved across the four dimensions of the correspondence, and we identify the precise points at which the correspondence breaks down.

The remainder of this dissertation is organised as follows. Section 2 presents a detailed account of the four levels of the Chomsky hierarchy, enriched at each level with the type-theoretic and linguistic correspondences and grounded in typologically diverse linguistic evidence. Section 3 examines the classical grammar-automaton correspondence and its computational-complexity implications. Section 4 develops the grammar-type correspondence through categorial grammar, Montague semantics, and pregroup grammars. Section 5 presents the Curry-Howard-Lambek triangle and its linguistic extension to a fourfold correspondence, including a consolidated correspondence table and a treatment of the limitations posed by gradient grammaticality, non-compositionality, and the generativist-vs.-usage-based debate. Section 6 surveys modern developments in programming language theory, computational linguistics, and theoretical linguistics that bear on the correspondence. Section 7 draws out implications for system design. Sections 8 and 9 offer discussion and conclusions.

---

## 2. The Chomsky Hierarchy

The hierarchy that Chomsky proposed between 1956 and 1959 classifies formal grammars into four nested types, each defined by progressively weaker constraints on the form of production rules. A formal grammar is a quadruple $G = (V, \Sigma, R, S)$, where $V$ is a finite set of nonterminal symbols, $\Sigma$ is a finite set of terminal symbols disjoint from $V$, $R$ is a finite set of production rules, and $S \in V$ is a distinguished start symbol. The form of the rules in $R$ determines the grammar's type and, consequently, the complexity of the language it generates and the computational resources required for its recognition.

### 2.1 Type 3: Regular Languages

**Grammar restriction.** A regular grammar restricts production rules to one of two canonical forms. In the right-linear variant, every production has the form $A \to aB$ or $A \to a$, where $A, B \in V$ and $a \in \Sigma$. In the left-linear variant, every production has the form $A \to Ba$ or $A \to a$. The critical constraint is that at most one nonterminal may appear on the right-hand side of any production, and it must occur at the edge -- rightmost or leftmost, but not both within the same grammar.

**Formal languages generated.** Regular grammars generate exactly the class of *regular languages*. A language $L \subseteq \Sigma^*$ is regular if and only if it can be described by a regular expression over $\Sigma$, or equivalently, if it is accepted by some finite-state automaton. Kleene's theorem (1956) established the equivalence of regular expressions and finite automata, thereby linking the algebraic (regular expressions), generative (regular grammars), and machine-theoretic (finite automata) characterisations of this class.

Regular languages are closed under union, intersection, complementation, concatenation, and Kleene star. Their closure properties make them exceptionally well-behaved from an algebraic standpoint. Every regular language has a unique minimal deterministic finite automaton (the Myhill-Nerode theorem), and the equivalence problem -- whether two regular languages are identical -- is decidable in polynomial time.

The defining limitation of regular languages is their inability to express unbounded nesting or matching. The language $\{a^n b^n \mid n \geq 1\}$ of matched pairs is not regular: no finite automaton can count to an arbitrary depth. This limitation, demonstrated via the pumping lemma for regular languages, marks the precise boundary between what can be recognised with finite memory and what requires auxiliary storage.

**Linguistic examples.** In natural language, regular grammars capture phenomena that do not involve recursive embedding or long-distance dependencies. Phonotactic constraints -- the rules governing permissible sequences of phonemes within a syllable or word -- are largely regular.

*Turkish vowel harmony* provides a well-studied example from a typologically distinct language. Turkish is an agglutinative language in which suffixes are added to stems in a transparent, linear fashion, with each suffix typically encoding a single grammatical function. Vowel harmony -- the requirement that vowels in suffixes agree in backness and rounding with the stem vowel -- can be modelled by a finite-state transducer (Kaplan and Kay, 1994). The two-way backness harmony (front/back) and four-way rounding harmony create a finite set of harmonic classes that determine suffix allomorphy. For example, the plural suffix alternates between *-lar* and *-ler* depending on the backness of the stem's last vowel: *kitaplar* ("books") vs. *evler* ("houses"). The agglutinative structure of Turkish, where suffixes string together in fixed order (*ev-ler-im-de*, "in my houses"), is especially amenable to finite-state modelling precisely because each suffix's form depends only on a finite, locally determined harmonic context -- no unbounded memory is required.

*Mandarin Chinese tone sandhi* offers an example from an isolating, tonal language. In Mandarin, the phenomenon of third-tone sandhi -- where a third tone becomes a second tone before another third tone -- is a local, context-dependent phonological process that operates on adjacent syllables and can be captured by finite-state rules. More broadly, Mandarin's relatively fixed SVO word order and sparse morphology mean that its phonological processes occupy a simpler stratum of the hierarchy than its syntax. The tone-sandhi system illustrates that regular-level phenomena operate across typologically diverse languages, not merely in Indo-European morphology.

Morphological processes such as regular verb conjugation in English (walk, walks, walked, walking) follow patterns expressible by finite-state rules. The Two-Level Morphology framework of Koskenniemi (1983) formalises morphophonological alternations as compositions of finite-state transducers, demonstrating that a substantial portion of word-level linguistic structure resides within the regular domain.

**Computational examples.** In computer science, regular languages are the workhorses of lexical analysis. The first phase of a compiler -- the *lexer* or *tokeniser* -- breaks source code into tokens (identifiers, keywords, operators, literals) using patterns that are invariably regular expressions compiled into deterministic finite automata. The Unix utilities `grep`, `sed`, and `awk` operate on regular expressions. Network protocol state machines, configuration file formats without nesting (such as INI files), and simple command-line option parsers all operate within the regular domain.

**Type-theoretic analogue.** The type-theoretic counterpart of a regular language is a *finite type* or *enumeration type*. A regular language is one whose recognition requires no memory of unbounded depth; correspondingly, the type-theoretic structures that model regular phenomena have finitely many inhabitants and no recursive component. In Haskell notation, a simple sum type such as `data Colour = Red | Green | Blue` is finite in exactly the way that a regular language's state space is finite. The states of a finite automaton correspond to the variants of an enumeration type, and the transition function corresponds to a case-analysis (pattern match) over those variants. No recursive type constructor is needed because the structure being classified has bounded depth.

More precisely, the Myhill-Nerode theorem provides the connection: a language is regular if and only if the equivalence relation defined by the Nerode right-congruence has finitely many classes. Each equivalence class corresponds to a state of the minimal DFA, and the finiteness of the state space is the machine-theoretic expression of the type-theoretic finiteness of the corresponding enumeration.

The correspondence at this level is a *structural embedding* rather than an isomorphism: every regular language can be faithfully modelled by a finite type (the states of its minimal DFA), but the mapping from finite types to regular languages is not bijective in the same clean way that the context-free correspondence is. The finite type captures the *recognition structure* of the language, not its generative structure directly.

### 2.2 Type 2: Context-Free Languages

**Grammar restriction.** A context-free grammar (CFG) restricts production rules to the form $A \to \alpha$, where $A$ is a single nonterminal and $\alpha$ is any string of terminals and nonterminals (including the empty string $\varepsilon$, subject to certain conventions). The defining property is that the left-hand side of every production is a *single* nonterminal symbol -- no contextual conditions constrain when a rule may be applied. The nonterminal $A$ may be rewritten as $\alpha$ regardless of what symbols surround $A$ in the sentential form.

**Formal languages generated.** Context-free grammars generate the *context-free languages* (CFLs). This class strictly contains the regular languages: every regular language is context-free, but the language $\{a^n b^n \mid n \geq 1\}$ is context-free but not regular. Context-free languages can express unbounded nesting and matching -- the hallmark of recursive structure -- but cannot express certain cross-serial dependencies, such as the language $\{a^n b^n c^n \mid n \geq 1\}$, which requires tracking three matched sequences simultaneously.

The class of context-free languages is closed under union, concatenation, and Kleene star, but *not* under intersection or complementation (a result with important practical consequences for language engineering). The emptiness problem -- whether a CFG generates any strings at all -- is decidable, as is the finiteness problem, but the equivalence problem for CFGs is undecidable (a result of Hopcroft and Ullman, 1979).

**The recognition machine: pushdown automata.** The class of abstract machines that recognises exactly the context-free languages is the *pushdown automaton* (PDA). A pushdown automaton augments a finite-state automaton with a single stack -- an unbounded last-in, first-out (LIFO) memory structure. The stack provides precisely the memory resource needed to track nested structure: when an opening delimiter is encountered, a symbol is pushed; when a closing delimiter is expected, the stack is popped and the symbol verified. The formal result is that a language is context-free if and only if it is accepted by some (nondeterministic) pushdown automaton (Chomsky, 1962; Evey, 1963).

The distinction between deterministic and nondeterministic pushdown automata is significant and has no analogue at the regular level (where DFAs and NFAs recognise the same languages). The *deterministic* context-free languages -- those accepted by a deterministic PDA -- form a proper subset of the context-free languages, and it is this deterministic subset that is targeted by practical parsing algorithms such as LR and LL parsers.

**Linguistic examples.** Context-free grammars capture the phrase-structure backbone of natural language syntax. The canonical phrase-structure rules -- $S \to NP \; VP$, $NP \to Det \; N$, $VP \to V \; NP$ -- are context-free productions that decompose sentences into hierarchically nested constituents. Centre-embedding constructions, such as "The rat that the cat that the dog chased caught ate the malt," exhibit the recursive nesting that is the signature capability of CFGs. Parenthetical embedding, relative clause nesting, and the recursive structure of noun phrases all fall within the context-free domain.

*Warlpiri and the challenge of free word order.* The Australian language Warlpiri provides an instructive challenge to the context-free model. Warlpiri is a *non-configurational* language (Hale, 1983): it permits extensive free word order, with discontinuous constituents and pervasive pro-drop (null arguments). In Warlpiri, a sentence like "The child is chasing the dog" can be expressed with the words for "child," "dog," "chasing," and the case markers in nearly any linear order, with grammatical relations determined by case marking rather than position. Standard context-free grammars, which generate strings by hierarchical decomposition, produce constituents that are contiguous -- they cannot directly generate the discontinuous, interleaved word-order patterns attested in Warlpiri. This has led to analyses using *scrambling* rules or *free word-order* extensions to CFGs (Becker, Rambow, and Niv, 1992), or to non-configurational frameworks such as Lexical-Functional Grammar's f-structure (Bresnan, 2001). The Warlpiri case demonstrates that while context-free grammars capture the *hierarchical dependency* structure of sentences (which is present in Warlpiri, encoded in case morphology), they do not capture the *linear realisation* of that structure in free word-order languages. The Lambek calculus and pregroup grammars, which encode word order via directional type connectives ($/$, $\backslash$), face a related challenge: their inherent order-sensitivity makes them a poor direct fit for languages where order is pragmatically rather than syntactically determined.

However, there is a well-known gap between what CFGs can express and what natural languages require. Chomsky himself noted as early as 1957 that certain natural language phenomena -- particularly those involving long-distance dependencies, such as wh-movement and topicalisation -- are difficult or impossible to capture with context-free rules alone. This observation motivated the introduction of transformational rules and, much later, the recognition that natural language is "mildly context-sensitive" (see Section 2.5).

**Computational examples.** The context-free level is the heart of programming language design. Nearly all mainstream programming languages have their syntax defined by context-free grammars, typically expressed in Backus-Naur form (BNF) or extended BNF. The BNF specification of ALGOL 60 (Naur, 1960) was the first formal language definition in the history of programming, and it is a context-free grammar in Chomsky's precise sense. Arithmetic expressions with operator precedence and associativity, block-structured control flow, nested function definitions, and the hierarchical structure of XML and JSON documents are all context-free phenomena.

The parser phase of a compiler -- which transforms a flat sequence of tokens into a hierarchically structured parse tree or abstract syntax tree -- operates on the context-free grammar of the language. LL parsers (top-down, predictive), LR parsers (bottom-up, shift-reduce), Earley parsers (chart-based, handling all CFGs), and CYK parsers (dynamic programming, $O(n^3)$) are all algorithms for recognising context-free languages. The output of the parser -- the AST -- is a tree whose structure mirrors the derivation tree of the CFG, stripped of syntactically redundant nodes.

**Type-theoretic analogue: recursive algebraic types.** The type-theoretic counterpart of a context-free grammar is a system of *recursive algebraic data types*. This correspondence is exact and constitutive, not merely analogical. A context-free grammar is a system of equations defining nonterminals in terms of terminals and other nonterminals, possibly recursively. A recursive algebraic data type is a system of equations defining types in terms of base types and other type constructors, possibly recursively. The structural identity is direct.

Consider the BNF rule for arithmetic expressions:

```
Expr ::= Expr '+' Term | Term
Term ::= Term '*' Factor | Factor
Factor ::= '(' Expr ')' | Number
```

This is isomorphic to the following Haskell type definition:

```haskell
data Expr   = Add Expr Term | ETerm Term
data Term   = Mul Term Factor | TFactor Factor
data Factor = Parens Expr | Num Int
```

The BNF rule and the type definition are the same mathematical object expressed in two notations. The nonterminals of the grammar correspond to the type names; the alternatives separated by `|` correspond to the data constructors (sum type); the sequencing of symbols in a production corresponds to the product type forming a constructor's argument tuple. Parsing a string according to the grammar is exactly the same operation as constructing a value of the corresponding algebraic type -- both produce a tree whose shape is determined by the recursive structure of the definitions.

The pushdown automaton's stack, in this reading, corresponds to the call stack of a recursive descent parser, which is itself a structural recursion over the recursive algebraic type. Every recursive descent parser is a catamorphism (fold) over the type defined by the grammar.

This is the most consequential level of the hierarchy for the relationship between linguistics and computer science. The fact that Chomsky's phrase-structure grammars for natural language and Backus-Naur form for programming languages are both context-free grammars, independently formulated within two years of each other (Chomsky, 1957; Backus, 1959), is not a coincidence. It reflects a deep structural truth: the hierarchical, recursively nested organisation of both human language and programming languages arises from the same mathematical substrate -- the substrate of context-free rewriting, pushdown recognition, and recursive algebraic typing.

### 2.3 Type 1: Context-Sensitive Languages

**Grammar restriction.** A context-sensitive grammar (CSG) permits production rules of the form $\alpha A \beta \to \alpha \gamma \beta$, where $A$ is a nonterminal, $\alpha$ and $\beta$ are (possibly empty) strings of terminals and nonterminals providing the *context* in which $A$ may be rewritten, and $\gamma$ is a non-empty string. The critical generalisation over CFGs is that the applicability of a rewriting rule may depend on the symbols surrounding the nonterminal being rewritten. Additionally, context-sensitive grammars are *non-contracting*: no production may reduce the length of the sentential form (except possibly a rule $S \to \varepsilon$ if $S$ does not appear on the right-hand side of any production).

**Formal languages generated.** Context-sensitive grammars generate the *context-sensitive languages* (CSLs), which strictly contain the context-free languages. The canonical example of a context-sensitive language that is not context-free is $\{a^n b^n c^n \mid n \geq 1\}$: three sequences that must match in length. This language requires the recogniser to "count" across three distinct regions of the input -- a capability beyond the single stack of a pushdown automaton.

The context-sensitive languages are closed under union, intersection, complementation, concatenation, and Kleene star. The membership problem -- given a CSG $G$ and a string $w$, is $w \in L(G)$? -- is decidable but PSPACE-complete (Kuroda, 1964), rendering it intractable for large inputs in the worst case.

**The recognition machine: linear bounded automata.** A *linear bounded automaton* (LBA) is a nondeterministic Turing machine whose tape is restricted to a length that is a linear function of the input length. It has all the computational capabilities of a Turing machine -- arbitrary read-write access, multiple passes over the input -- but is constrained to use space proportional to the input. The Kuroda normal form theorem (Kuroda, 1964) establishes that a language is context-sensitive if and only if it is accepted by some LBA.

The LBA occupies a less clean position in the hierarchy than the finite automaton or pushdown automaton. It is powerful enough to perform sophisticated computations but constrained enough that the membership problem remains decidable. The open question of whether deterministic LBAs are as powerful as nondeterministic LBAs (the LBA problem) has been unresolved since Kuroda's work and is closely related to open questions in computational complexity theory.

**Linguistic examples.** Context-sensitive phenomena in natural language include cross-serial dependencies, agreement, and case assignment. The most frequently cited example is the cross-serial dependency construction in Swiss German, identified by Shieber (1985). In Swiss German subordinate clauses, a sequence of noun phrases is followed by a sequence of verbs, where the $i$-th verb agrees in case with the $i$-th noun phrase:

> ... das mer d'chind em Hans es huus haelfed aastriiche.
> ... that we the-children(ACC) Hans(DAT) the-house(ACC) helped(DAT) paint(ACC).
> "... that we helped Hans paint the house for the children."

The pattern of NP-verb agreement across clause boundaries generates a language of the form $\{a^n b^n c^n\}$ (with appropriate abstractions), which Shieber argued is not context-free.

**The status of Shieber (1985): the standard argument and its contestation.** Shieber's result is the standard argument that natural language is not context-free, and it has been widely influential. However, intellectual honesty requires acknowledging that the argument is not uncontested. Pullum and Gazdar (1982), writing *before* Shieber's paper, had surveyed prior claims of non-context-freeness in natural language and found them all wanting -- either the formal argument was flawed or the linguistic data admitted alternative analyses. Shieber's 1985 argument was specifically designed to address Pullum and Gazdar's objections, and it is generally regarded as having succeeded. Nevertheless, the formal argument depends on specific assumptions about the analysis of Swiss German: that the cross-serial dependencies are genuinely unbounded and that the relevant agreement patterns cannot be reanalysed in a way that preserves context-freeness. Subsequent work by Michaelis and Kracht (1997) showed that the formal argument is sensitive to the precise grammatical analysis adopted, and construction-specific accounts have been proposed that handle the Swiss German data without invoking full context-sensitivity. The consensus view in formal linguistics treats Shieber's result as establishing that natural language *as a class* is beyond context-free, but the degree of non-context-freeness is mild -- a conclusion that supports the mildly context-sensitive hypothesis (Section 2.5) rather than full context-sensitivity.

*Mohawk noun incorporation: polysynthetic challenges.* The Iroquoian language Mohawk (Baker, 1988, 1996) presents a different kind of context-sensitive phenomenon. Mohawk is *polysynthetic*: a single Mohawk word can express what English requires an entire clause for. In Mohawk, noun roots may be *incorporated* into the verb, forming a single complex word:

> *Wa'-k-akya'tawi'tsher-ú:ni* ("I made a dress")

Here, the noun root for "dress" (*-akya'tawi'tsher-*) is incorporated into the verb root for "make" (*-u:ni-*), with pronominal prefixes and aspectual morphology fused into a single morphological word. The noun incorporation process is productive and depends on the semantic relationship between noun and verb, the argument structure of the verb, and the discourse context -- all of which constitute context-sensitive information. Polysynthetic languages challenge the Chomsky hierarchy in a fundamental way: they blur the boundary between word and sentence that the hierarchy presupposes. A "word" in Mohawk is, from the standpoint of information content, closer to a "sentence" in English, and its internal structure exhibits the kind of context-dependency (agreement across multiple incorporated morphemes, argument structure constraints) that is characteristically context-sensitive.

Other context-sensitive phenomena include number agreement between subject and verb across intervening material, case concord in languages with rich morphology (Latin, Finnish, Georgian), and certain reduplication patterns in Bambara (Culy, 1985), which generate the copy language $\{ww \mid w \in \Sigma^*\}$, also not context-free.

**Computational examples.** In compiler design, the context-sensitive level corresponds to *semantic analysis* -- the phase that follows context-free parsing. Type checking, name resolution (looking up identifiers in their lexical scope), overload resolution, and access control verification are all context-sensitive operations. They require information about the *context* in which an expression appears: the surrounding declarations, the types of previously encountered subexpressions, the scope chain. This is why compilers bifurcate their front ends into a context-free parser and a separate semantic analysis pass -- the split reflects the grammar hierarchy itself.

**Type-theoretic analogue: parametric polymorphism and refinement types.** Context-sensitivity in grammar corresponds to *context-dependency* in typing: the type of an expression depends on the context in which it is used. In type-theoretic terms, this is the domain of *parametric polymorphism* and *bounded quantification*.

In System F (Girard, 1972; Reynolds, 1974), the polymorphic lambda calculus, a term may have a type that is universally quantified over type variables: $\Lambda \alpha. \lambda x{:}\alpha. x$ has the type $\forall \alpha. \alpha \to \alpha$. The concrete type of this term is determined by the *context* of its application -- when applied to a natural number, it has type $\mathbb{N} \to \mathbb{N}$; when applied to a Boolean, it has type $\mathbb{B} \to \mathbb{B}$. This context-dependency in typing mirrors the context-sensitivity in grammar: what is "grammatical" (well-typed) depends on the surrounding structure.

Bounded quantification, as in System F$_{<:}$ (Cardelli and Wegner, 1985), adds subtype constraints to polymorphism: a polymorphic function may constrain its type variable to range only over subtypes of a given bound. This corresponds to context-sensitive grammar rules whose applicability is conditioned on specific contextual features. Type classes in Haskell and interfaces in Java and Go serve a similar function: they impose context-dependent constraints on type variables.

Refinement types (Freeman and Pfenning, 1991) push further by attaching predicates to types: the type $\{x : \mathbb{N} \mid x > 0\}$ classifies natural numbers that are strictly positive. The predicate constitutes a "context" -- an additional constraint that must be verified against the surrounding program state. The connection to context-sensitive grammar is suggestive: in both cases, well-formedness depends not only on the local structure of a constituent but on its relationship to its environment.

**A worked example: encoding {a^n b^n c^n} in System F.** The Type 1 / parametric polymorphism mapping is the weakest link in the fourfold correspondence, and it is important to be precise about what can and cannot be established. Consider the canonical context-sensitive language $L = \{a^n b^n c^n \mid n \geq 1\}$. Can membership in $L$ be encoded as a type-checking problem in System F?

The answer is yes, but only through an *encoding*, not through a direct isomorphism. We can define Church numerals in System F:

$$\underline{n} \equiv \Lambda \alpha. \lambda f{:}\alpha \to \alpha. \lambda x{:}\alpha. f^n(x) : \forall \alpha. (\alpha \to \alpha) \to \alpha \to \alpha$$

A string $a^i b^j c^k$ can be represented by the triple $(\underline{i}, \underline{j}, \underline{k})$. The predicate $i = j = k$ can be verified in System F by constructing a term that applies an equality test on Church numerals. Specifically, the Church numeral equality function can be typed in System F (using the standard encoding via Booleans), and a term:

$$\text{check} : \text{Nat} \to \text{Nat} \to \text{Nat} \to \text{Bool}$$
$$\text{check} \; m \; n \; p = \text{and} \; (\text{eq} \; m \; n) \; (\text{eq} \; n \; p)$$

returns true exactly when $m = n = p$. The triple $(\underline{i}, \underline{j}, \underline{k})$ satisfies the type $\{(m, n, p) : \text{Nat}^3 \mid \text{check} \; m \; n \; p = \text{true}\}$ if and only if $a^i b^j c^k \in L$.

However, this encoding has two crucial limitations. First, it operates at the level of *refinement types* (types with predicates) rather than pure System F, because the membership condition is expressed as a predicate on type inhabitants rather than as a type structure. Second, the encoding is not *structural* in the way that the BNF-to-algebraic-type correspondence at the context-free level is structural: we are encoding the membership predicate, not exhibiting a type whose inhabitants are in bijection with the derivations of the grammar. The context-free isomorphism works because the *shape* of a value of an algebraic type mirrors the *shape* of a derivation tree. No analogous shape-preserving correspondence has been established between context-sensitive derivations and System F terms.

We therefore classify the Type 1 / parametric polymorphism correspondence as a *structural embedding*: context-sensitive phenomena can be faithfully represented in a System F type-checking framework, but the representation is an encoding rather than an isomorphism. Establishing a tighter connection -- or proving that no tighter connection exists -- remains an open problem.

### 2.4 Type 0: Recursively Enumerable Languages

**Grammar restriction.** An unrestricted grammar (Type 0) imposes no constraints on production rules beyond the requirement that the left-hand side contains at least one nonterminal. Any string $\alpha$ containing a nonterminal may be rewritten as any string $\beta$, including the empty string. Rules may lengthen, shorten, rearrange, or delete portions of the sentential form without restriction.

**Formal languages generated.** Unrestricted grammars generate exactly the *recursively enumerable* (RE) languages. A language is recursively enumerable if there exists a Turing machine that halts and accepts on every string in the language (but may fail to halt on strings not in the language). This class is the outermost boundary of computability: it includes every language that is recognisable by *any* effective procedure, including those for which recognition may not terminate.

The RE languages are closed under union, intersection, and concatenation, but *not* under complementation. The complement of an RE language that is not recursive (decidable) is not RE -- a fact that underlies the undecidability of the halting problem and, by extension, the undecidability of membership in certain Type 0 languages.

**The recognition machine: Turing machines.** An unrestricted grammar generates a language $L$ if and only if some Turing machine accepts $L$. The Turing machine (Turing, 1936) is the canonical model of universal computation: an abstract machine with a finite control, an unbounded tape, and the ability to read, write, and move in both directions along the tape. The Church-Turing thesis asserts that any effectively computable function can be computed by a Turing machine, making the Turing machine the upper bound on mechanical computation.

**Linguistic examples.** Chomsky argued, and the consensus view in theoretical linguistics concurs, that natural language does not require the full generative power of unrestricted grammars. No known natural language phenomenon demands a grammar that cannot be expressed within the context-sensitive or mildly context-sensitive domain. The Type 0 level therefore functions primarily as a theoretical upper bound rather than a practical description of linguistic capacity.

However, one may observe that the *pragmatic* dimension of language -- contextual inference, conversational implicature, presupposition accommodation -- involves computations whose complexity approaches the unrestricted level. The process of recovering speaker intention from an utterance in context may, in principle, require arbitrary background knowledge and unbounded inference chains. Whether this observation has formal implications for the grammar hierarchy depends on how one draws the boundary between grammar (linguistic competence) and pragmatics (performance and world knowledge).

**Computational examples.** In programming, the Type 0 level corresponds to *arbitrary computation*: any program, any Turing-complete language, any metaprogramming system. The template metaprogramming system of C++ is Turing-complete (Veldhuizen, 2003), meaning that C++ compilation can involve computations whose termination is undecidable. Similarly, Haskell's type-level computation with type families and GADTs can express Turing-complete type-level programs, and TypeScript's conditional types and mapped types have been shown to be Turing-complete in the type system. In all these cases, the type-checker is effectively a Turing machine, and type-checking may not terminate.

**Type-theoretic analogue: full dependent types.** The type-theoretic counterpart of unrestricted grammars is *full dependent type theory*, in which types may depend on arbitrary values and type-checking involves arbitrary computation. In the Calculus of Constructions (Coquand and Huet, 1988) and in Martin-Lof's Intuitionistic Type Theory (Martin-Lof, 1975, 1984), types are first-class objects that may be parameterised by terms: the type $\text{Vec}(A, n)$ of vectors of $n$ elements of type $A$ is a type that depends on the value $n$. Constructing a term of type $\text{Vec}(A, n{+}m)$ from terms of types $\text{Vec}(A, n)$ and $\text{Vec}(A, m)$ requires the type-checker to verify the arithmetic identity $n + m = n + m$ -- a computation at the type level.

In their full generality, dependent type systems are Turing-complete: type-checking is equivalent to theorem-proving, which is undecidable for sufficiently expressive logics. The proof assistants Agda, Lean, and Rocq (formerly Coq) inhabit this space. They ensure decidability of type-checking not by restricting the type system but by requiring all functions to be *total* (terminating), thereby ensuring that type-level computations always complete. This is a pragmatic restriction analogous to the restriction from RE languages to recursive (decidable) languages: the expressive power is curtailed to guarantee termination, but the underlying framework has the full power of Type 0.

The correspondence between unrestricted grammars and dependent types is the most extreme and the least precise of the four levels -- an *analogy* rather than an isomorphism or embedding (see Section 1.1). At the lower levels, the grammar-type correspondence is constructive and practically useful. At the Type 0 / dependent-type level, it becomes a correspondence between two forms of uncomputability: the undecidability of membership in an RE language and the undecidability of type-checking in a fully dependent type system without termination checking. Both involve the same fundamental barrier (the halting problem), but the structural parallel is less detailed than at the context-free level.

### 2.5 Beyond the Hierarchy: Mildly Context-Sensitive Languages

The four levels of the Chomsky hierarchy do not exhaust the landscape of formal language classes. Between the context-free and context-sensitive levels lies a family of language classes collectively termed *mildly context-sensitive*, introduced by Joshi (1985) to characterise the conjectured complexity class of natural language.

Joshi proposed four properties that a grammar formalism must satisfy to qualify as mildly context-sensitive:

1. It generates all context-free languages.
2. It can generate some (but not all) context-sensitive languages, in particular $\{a^n b^n c^n \mid n \geq 1\}$.
3. It has the *constant growth property*: the lengths of strings in the language grow at most polynomially, and consecutive string lengths differ by at most a constant.
4. Its recognition problem is solvable in polynomial time.

Several independently developed grammar formalisms satisfy these criteria: *tree-adjoining grammars* (TAGs; Joshi, Levy, and Takahashi, 1975), *combinatory categorial grammars* (CCGs; Steedman, 1987, 2000), *head grammars* (Pollard, 1984), and *linear indexed grammars* (Gazdar, 1988). These formalisms were subsequently shown to be weakly equivalent -- they generate the same class of string languages (Vijay-Shanker and Weir, 1994) -- confirming that "mildly context-sensitive" is a robust natural class and not an artefact of a particular formalism.

*American Sign Language and simultaneous structure.* The mildly context-sensitive class is of particular interest when considering *sign languages*, which challenge the very foundation of the Chomsky hierarchy: the assumption that language is a string over a finite alphabet -- a sequential, one-dimensional structure. American Sign Language (ASL) uses *simultaneous* articulation across multiple channels: two hands, facial expression, eye gaze, head tilt, and body posture can all carry grammatical information concurrently (Sandler and Lillo-Martin, 2006). Classifiers in ASL involve one hand representing a ground object while the other represents a figure object, with spatial relationships expressed by the relative positions of the hands -- a two-dimensional, parallel structure that has no natural encoding as a string. Facial expressions in ASL mark syntactic boundaries (questions, topics, negation), operating as a suprasegmental channel analogous to intonation in spoken language but with greater structural load.

The implications for the fourfold correspondence are significant. If natural language is not fundamentally a string language, then the Chomsky hierarchy -- which classifies *string* languages -- may not be the right framework for its characterisation. Steedman (2000) has argued that CCG's ability to handle the syntax-prosody interface (including the interaction of syntactic and phonological phrasing) makes it better suited than phrase-structure approaches to capturing the multi-channel nature of linguistic structure, and extensions of CCG to sign language have been proposed (Lillo-Martin and Sandler, 2006). For the type-theoretic dimension, the challenge is to extend the correspondence from string grammars to *multi-dimensional* or *geometric* grammars that can model the simultaneous structure of sign languages. This remains an open problem but connects to the programme of higher-dimensional grammar mentioned in Section 6.1.

The mildly context-sensitive class is of paramount importance for the present inquiry because it appears to be the *correct* complexity class for natural language. It can handle the cross-serial dependencies that demonstrate natural language is not context-free (Shieber, 1985 -- though see the discussion of contestation in Section 2.3), while remaining polynomially parsable (unlike general context-sensitive languages, which are PSPACE-complete). The identification of a type-theoretic characterisation for this intermediate class is one of the central open problems investigated in this dissertation (see Sections 4.5 and 6.2).

### 2.6 Summary: The Hierarchy as Table

The following table consolidates the grammar-automaton-type correspondence across all four levels, together with the linguistic and computational scope of each:

| Type | Grammar | Automaton | Language Class | Decidability | Linguistic Scope | Type-Theoretic Analogue | Correspondence Strength |
|------|---------|-----------|----------------|-------------|-----------------|------------------------|------------------------|
| 3 | Regular | Finite automaton | Regular | O(n) | Phonology, morphology (Turkish vowel harmony, Mandarin tone sandhi) | Enumerations, finite types | Embedding |
| 2 | Context-free | Pushdown automaton | Context-free | O(n^3) (CYK) | Phrase structure syntax (Warlpiri: hierarchy without fixed order) | Recursive algebraic types | **Isomorphism** |
| (MCS) | TAG/CCG | Embedded PDA | Mildly context-sensitive | O(n^6) | Natural language syntax (ASL: simultaneous structure) | *(Conjecture: bounded 2nd-order; see Section 4.5)* | Partial |
| 1 | Context-sensitive | Linear bounded automaton | Context-sensitive | PSPACE-complete | Agreement, cross-serial deps (Mohawk noun incorporation) | Parametric polymorphism | Embedding |
| 0 | Unrestricted | Turing machine | Recursively enumerable | Undecidable | (Beyond natural language) | Full dependent types | Analogy |

---

## 3. From Grammars to Machines

The grammar-automaton correspondence is the oldest and most thoroughly established dimension of the fourfold correspondence. Its development, spanning from Kleene (1956) through Chomsky (1959) to the textbook treatments of Hopcroft and Ullman (1979), constitutes one of the defining achievements of theoretical computer science. This section examines the correspondence in detail, with particular attention to the computational complexity of recognition at each level and the engineering implications for language processing.

### 3.1 The Classical Correspondence

The correspondence between grammar types and automaton types can be stated with unusual precision. For each level $i$ of the Chomsky hierarchy, the class of languages generated by Type $i$ grammars is identical to the class of languages recognised by the corresponding automaton type:

- **Type 3 / Finite automata.** Kleene's theorem (1956): A language is regular if and only if it is accepted by some finite automaton. Equivalently, it is described by some regular expression. The proof is constructive in both directions: given a regular grammar, one can build a finite automaton accepting the same language (by treating nonterminals as states and productions as transitions), and given a finite automaton, one can construct a regular grammar generating its language.

- **Type 2 / Pushdown automata.** A language is context-free if and only if it is accepted by some nondeterministic pushdown automaton. The proof proceeds by converting a CFG in Greibach normal form into a PDA (treating the grammar's leftmost derivations as sequences of push and pop operations) and conversely converting a PDA into a CFG (by encoding the PDA's stack configurations as nonterminals).

- **Type 1 / Linear bounded automata.** A language is context-sensitive if and only if it is accepted by some nondeterministic linear bounded automaton (Kuroda, 1964). The non-contracting property of CSG rules ensures that derivations never produce sentential forms shorter than the input, which is exactly the tape-length constraint of the LBA.

- **Type 0 / Turing machines.** A language is recursively enumerable if and only if it is accepted by some Turing machine. This is essentially the definition of recursive enumerability.

### 3.2 Parsing as Recognition: The Engineering Perspective

The grammar-automaton correspondence is not merely a theoretical classification; it has direct engineering consequences. The *parser* of a compiler or natural language processing system implements, in effect, the automaton corresponding to the grammar of the language being processed. The choice of grammar formalism determines the parsing algorithm, its computational complexity, and the class of languages it can handle.

In compiler engineering, the standard pipeline reflects the Chomsky hierarchy in microcosm. The *lexer* operates at Type 3: it uses a deterministic finite automaton (typically compiled from regular expressions) to break the input into tokens. The *parser* operates at Type 2: it uses a pushdown automaton (typically an LR or LL parser) to construct the parse tree. The *semantic analyser* operates at Type 1: it performs context-sensitive checks (type checking, name resolution, access control) that require information beyond the immediate syntactic context. The *optimiser* and *code generator* operate at Type 0: they perform arbitrary computations on the intermediate representation.

This architectural stratification is not accidental. It is a direct engineering consequence of the grammar hierarchy: each phase operates at the most restrictive level of the hierarchy that suffices for its task, thereby minimising computational cost. Lexing in $O(n)$, parsing in $O(n)$ for LR(1) grammars (or $O(n^3)$ for general CFGs), and type-checking in time that depends on the specific type system but is typically polynomial for practical languages.

### 3.3 Computational Complexity of Each Level

The computational complexity of the *membership problem* -- given a grammar $G$ and a string $w$, is $w \in L(G)$? -- varies dramatically across the hierarchy:

- **Regular:** $O(n)$ for deterministic finite automata (single pass over the input, constant space). This is optimal.
- **Context-free:** $O(n^3)$ for the CYK algorithm (Cocke, Younger, Kasami) and the Earley parser (with $O(n^2)$ for unambiguous grammars). For the restricted subclass of LR(k) grammars, recognition is $O(n)$.
- **Context-sensitive:** PSPACE-complete. The membership problem is decidable but, in the worst case, requires space polynomial in the input length. For practical purposes, this renders general context-sensitive recognition intractable.
- **Recursively enumerable:** Undecidable. There exists no algorithm that, given an arbitrary unrestricted grammar $G$ and string $w$, always correctly determines whether $w \in L(G)$.

The sharp jump from polynomial (context-free) to PSPACE-complete (context-sensitive) is one of the most practically significant boundaries in the hierarchy. It explains why programming languages are designed to have context-free syntax: context-free grammars can be parsed efficiently, while context-sensitive grammars, in general, cannot. The context-sensitive aspects of programming languages (type checking, scope resolution) are handled by separate algorithms specifically designed for the structure of the particular type system, rather than by general CSG recognition.

### 3.4 Why Natural Languages Cluster at "Mildly Context-Sensitive"

A striking empirical observation is that natural languages appear to cluster not at any of the four Chomsky levels but in the interstitial class of mildly context-sensitive languages. This observation, crystallised by Joshi (1985) and corroborated by decades of subsequent work, raises a fundamental question: *why?*

Several explanations have been proposed. The *learnability* hypothesis (Joshi, 1985; Joshi et al., 1991) suggests that mildly context-sensitive grammars strike the optimal balance between expressiveness and learnability: they are powerful enough to express the constructions attested in natural language (including cross-serial dependencies) while remaining learnable from finite positive data under reasonable inductive biases. The *processing* hypothesis (Stabler, 2013) argues that the polynomial parsability of MCS languages explains their evolutionary selection: a grammar whose recognition complexity is PSPACE-complete would impose unsustainable processing costs on the human parser. The *interface* hypothesis (Steedman, 2000) proposes that the constraint arises from the requirement that syntactic structure be transparently interpretable by the semantic component: the tight syntax-semantics interface enforced by categorial grammar naturally limits syntactic complexity to the MCS level.

For the fourfold correspondence investigated in this dissertation, the mildly context-sensitive class poses a particular challenge. The grammar-automaton correspondence for MCS languages is well-established: TAGs correspond to embedded pushdown automata (Vijay-Shanker, 1987), and CCGs correspond to a particular class of linear indexed grammars. But the type-theoretic characterisation of MCS languages remains an open problem. If the fourfold correspondence is to extend to the complexity class of natural language itself, a type system must be identified that stands in the same relationship to MCS grammars as recursive algebraic types stand to CFGs and as dependent types stand to unrestricted grammars. We return to this problem in Section 4.5.

---

## 4. From Grammars to Types

The grammar-type correspondence is the less well-trodden dimension of the fourfold correspondence and the principal focus of this dissertation. While the grammar-automaton correspondence is a standard topic in computer science education, the grammar-type correspondence is not -- yet it runs at least as deep. This section develops the correspondence through three major traditions: categorial grammar, Montague semantics, and Lambek's algebraic approach.

### 4.1 The Lambek Calculus: Grammar as Logic

The pivotal insight that grammar *is* logic was formalised by Joachim Lambek in a 1958 paper published, coincidentally, the same year as Chomsky's *Syntactic Structures*. Lambek's *syntactic calculus* (Lambek, 1958) reformulates categorial grammar as a *logical system* in the precise sense of proof theory: it has axioms, inference rules, and a notion of derivability, and a sentence is grammatical if and only if its grammaticality can be *proved* within the system.

The Lambek calculus operates over a set of *basic types* (typically $S$ for sentence, $N$ for noun, $NP$ for noun phrase) and two type-forming connectives: right division $A / B$ (read "A over B") and left division $A \backslash B$ (read "A under B"). Intuitively:

- $A / B$ is the type of an expression that combines with a $B$ to its right to produce an $A$.
- $B \backslash A$ is the type of an expression that combines with a $B$ to its left to produce an $A$.

The Lambek calculus includes introduction and elimination rules for both connectives, analogous to the introduction and elimination rules for implication in natural deduction:

- **Right elimination (application):** From a proof that $x : A/B$ and a proof that $y : B$, derive $xy : A$.
- **Left elimination (application):** From a proof that $x : B$ and a proof that $y : B \backslash A$, derive $xy : A$.
- **Right introduction (abstraction):** If, assuming $y : B$ on the right, one can derive $xy : A$, then $x : A/B$.
- **Left introduction (abstraction):** If, assuming $x : B$ on the left, one can derive $xy : A$, then $y : B \backslash A$.

These rules are precisely the rules of *implicational logic* with two directed implications. The Lambek calculus is thus a logic -- specifically, a *non-commutative substructural logic* (it lacks the structural rules of exchange, weakening, and contraction that are present in classical and intuitionistic logic). The absence of exchange reflects the fact that word order matters in natural language: "the dog" and "dog the" are not interchangeable.

An important result, established by Pentus (1997), is that the product-free Lambek calculus generates exactly the class of context-free languages. This places the Lambek calculus squarely at the Type 2 level of the Chomsky hierarchy -- a result that the paper's fourfold framework predicts, since the Lambek calculus is the canonical grammar formalism at the level where the correspondence is an isomorphism. However, the full Lambek calculus with product generates a larger class (Pentus, 1993), and extensions with modalities (Moortgat, 1997) or displacement operators (Morrill, Valentin, and Fadda, 2011) can reach the mildly context-sensitive level. The distinction between the product-free and full calculus matters for the fourfold mapping and should be kept in mind throughout.

The significance of this reformulation is profound. A *grammatical derivation* in the Lambek calculus is a *proof* in a logical system. This is not an analogy; it is a formal identity. Every proof in the Lambek calculus corresponds to a grammatical derivation, and every grammatical derivation corresponds to a proof. The formalism simultaneously defines a grammar, a logic, and (via Curry-Howard) a typed calculus.

### 4.2 Categorial Grammar: Ajdukiewicz, Bar-Hillel, Lambek

The tradition of *categorial grammar* (CG) predates Chomsky's work. Kazimierz Ajdukiewicz (1935) proposed that the syntactic structure of a language could be captured entirely by assigning *functional types* to words and combining them by *function application*. In Ajdukiewicz's framework, there are no phrase-structure rules: the grammar consists solely of a *lexicon* (a mapping from words to types) and a *combinatory principle* (function application).

Yehoshua Bar-Hillel (1953) refined Ajdukiewicz's proposal and introduced the notation $A/B$ for a functor that takes a $B$ argument to its right and produces an $A$. This notation, subsequently adopted by Lambek, became the standard notation for categorial types.

In categorial grammar, every word is assigned one or more syntactic types (categories), and sentences are derived by functional application alone. Consider the assignment:

- "John" : $NP$
- "sleeps" : $NP \backslash S$ (takes an $NP$ to its left, returns $S$)
- "the" : $NP / N$ (takes an $N$ to its right, returns $NP$)
- "big" : $N / N$ (takes an $N$ to its right, returns $N$)
- "dog" : $N$

The derivation of "The big dog sleeps" proceeds:

1. "big" : $N/N$ applied to "dog" : $N$ yields "big dog" : $N$.
2. "the" : $NP/N$ applied to "big dog" : $N$ yields "the big dog" : $NP$.
3. "the big dog" : $NP$ applied to "sleeps" : $NP \backslash S$ yields "the big dog sleeps" : $S$.

The sentence is well-formed (type $S$) because the functional types compose correctly. An ill-formed string -- such as "sleeps the big" -- would fail to reduce to type $S$, because the types do not compose: "sleeps" requires an $NP$ to its left, but "the" requires an $N$ to its right, and no valid composition exists.

The critical observation is that the categorial types *are* function types in a typed lambda calculus. The category $NP/N$ is the function type $N \to NP$. The category $NP \backslash S$ is the function type $NP \to S$ (with the argument position reversed to reflect word-order directionality). Sentence formation *is* function application. Parsing *is* type-checking.

### 4.3 Combinatory Categorial Grammar (Steedman)

Mark Steedman's Combinatory Categorial Grammar (CCG; Steedman, 1987, 2000) extends the classical categorial framework by enriching the set of combinatory operations beyond function application. In addition to application (both forward and backward), CCG permits:

- **Composition** ($B$): If $x : A/B$ and $y : B/C$, then $xy : A/C$. This is function composition.
- **Type-raising** ($T$): A category $A$ may be "raised" to $B/(B \backslash A)$ or $(B/A) \backslash B$, transforming an argument into a function over functions.
- **Crossed composition** and **substitution** variants that handle certain word-order phenomena.

These additional combinators correspond precisely to the combinators of *combinatory logic* (Curry and Feys, 1958) -- the system that is equivalent in expressive power to the lambda calculus but uses named combinators ($B$, $C$, $S$, $K$, $I$, etc.) rather than variable-binding. The $B$ combinator of CCG is the composition combinator of combinatory logic; type-raising corresponds to the combinator $C^*$ that permutes argument order.

CCG is significant for three reasons. First, it generates exactly the class of mildly context-sensitive languages (Vijay-Shanker and Weir, 1994), placing it at the conjectured complexity level of natural language. Second, it maintains a transparent interface between syntax and semantics: every syntactic derivation directly determines a semantic interpretation via the lambda calculus, with each combinatory rule corresponding to a specific lambda term. Third, it has proven computationally practical: CCG parsers (Clark and Curran, 2007; Lewis and Steedman, 2014) achieve state-of-the-art performance on broad-coverage semantic parsing tasks.

The connection between CCG and type theory is explicit and constitutive. A CCG derivation *is* a proof in a type-theoretic system, and the semantics assigned to a sentence by CCG *is* a typed lambda term. This makes CCG arguably the most successful realisation of the grammar-type-proof correspondence in computational practice.

### 4.4 Montague Grammar and the Lambda Calculus Connection

Richard Montague's programme of formal semantics (Montague, 1970a, 1970b, 1973) forged the definitive link between natural language grammar and the typed lambda calculus. Montague's central thesis -- stated provocatively in the opening sentence of "Universal Grammar" -- was that "there is in my opinion no important theoretical difference between natural languages and the artificial languages of logicians."

Montague grammar proceeds in three steps:

1. **Syntactic analysis.** Each expression of a natural language is assigned a *syntactic category* from a categorial grammar.
2. **Type assignment.** Each syntactic category is mapped to a *semantic type* in a typed lambda calculus. The basic semantic types are $e$ (entity) and $t$ (truth value); complex types are formed by the function-type constructor $\to$.
3. **Compositional interpretation.** Each syntactic rule is associated with a *semantic rule* that specifies how the meaning of the complex expression is computed from the meanings of its parts.

The principle of compositionality -- that the meaning of a complex expression is a function of the meanings of its parts and their mode of combination -- is not assumed as an axiom but *derived* as a consequence of the typed structure. If syntax is a type system and semantics is a type-preserving interpretation (a *homomorphism*), then compositionality is a theorem.

In category-theoretic terms, Montague grammar defines a *functor* from the syntactic category (whose objects are syntactic types and whose morphisms are grammatical derivations) to the semantic category (whose objects are semantic types and whose morphisms are lambda terms). The functoriality of this mapping -- the fact that it preserves composition -- is the formal content of compositionality.

### 4.5 The Parallel Between Grammar Hierarchy and Type-System Hierarchy

Having established the grammar-type connection through categorial grammar and Montague semantics, we can now state the full parallel between the Chomsky hierarchy and a corresponding hierarchy of type systems, with the correspondence strength explicitly classified at each level (as introduced in Section 1.1).

**Regular grammars correspond to finite types (enumerations, sum types without recursion).** A regular language has no recursive structure; its recognition requires only finite memory. Correspondingly, the types modelling regular phenomena are finite -- they can be fully enumerated. The states of a minimal DFA correspond to the constructors of a finite sum type. No recursive type constructor is needed because the structures being classified have bounded depth. *Strength: structural embedding.*

**Context-free grammars correspond to recursive algebraic types.** CFGs define languages by mutual recursion over nonterminals. Algebraic data types define types by mutual recursion over type constructors. The isomorphism is exact: a BNF grammar *is* a system of recursive type equations, and parsing *is* constructing a value of the corresponding type. The pushdown automaton's stack corresponds to the call stack of a recursive descent parser, which is a structural recursion (catamorphism) over the recursive type. *Strength: isomorphism.*

**Context-sensitive grammars correspond to parametric polymorphism and refinement types.** Context-sensitivity means that well-formedness depends on context. In type systems, this is modelled by polymorphism (the type of an expression depends on the context of instantiation), bounded quantification (type constraints depend on the surrounding type environment), and refinement types (types augmented with context-dependent predicates). System F, the polymorphic lambda calculus, occupies this level. The worked example in Section 2.3 demonstrates that context-sensitive membership can be encoded as a type-checking problem, but not via a structural isomorphism. *Strength: structural embedding (conjectured).*

**Unrestricted grammars correspond to full dependent types.** When types may depend on arbitrary values, type-checking becomes theorem-proving, which is undecidable in general. The Calculus of Constructions and Martin-Lof's Intuitionistic Type Theory are the type-theoretic counterparts of unrestricted grammars. Both operate at the boundary of decidability. The parallel is between two forms of uncomputability rather than a constructive mapping. *Strength: analogy.*

**The MCS gap conjecture.** The mildly context-sensitive level presents the most important open problem in the fourfold correspondence. The grammar-automaton correspondence for MCS languages is established (TAGs correspond to embedded pushdown automata; CCGs correspond to a class of linear indexed grammars), but no canonical type system has been identified for this level.

We propose the following conjecture. The type system corresponding to mildly context-sensitive languages is a *restricted second-order system* -- specifically, a fragment of System F with *bounded polymorphism* and *restricted structural rules*. The conjecture rests on three observations:

1. **CCG corresponds to combinatory logic.** The combinators of CCG ($B$, $T$, $S$) are a restricted subset of the combinators of full combinatory logic. In the type-theoretic reading, this means CCG corresponds to a *restricted* type system -- one that permits certain forms of polymorphic composition but not the full power of System F.

2. **MCS languages require more than a single stack but less than a full tape.** The embedded pushdown automata that recognise MCS languages use a finite nesting of stacks -- more memory than a PDA but less than an LBA. The type-theoretic analogue would be a system with bounded polymorphic nesting: type variables may be quantified, but the depth of quantification is bounded or the forms of quantification are restricted.

3. **Linear type systems provide controlled structural rules.** MCS grammars are characterised by constrained use of structural rules (weakening, contraction). Linear type systems (Girard, 1987) provide exactly the framework for controlling structural rules at the type level. A linear type system with bounded second-order quantification would permit context-dependent typing (polymorphism) while restricting the structural rules to ensure polynomial type-checking -- mirroring the polynomial parsability of MCS languages.

We therefore conjecture that the type system corresponding to MCS languages is a *bounded linear polymorphic calculus*: a fragment of the linear lambda calculus with second-order quantification restricted to bounded polymorphism (System F$_{<:}$ restricted to linear types) or to a finite rank. This conjecture is falsifiable: it predicts that the languages typable in such a system coincide with the MCS class, a claim amenable to formal investigation. Even if the conjecture proves incorrect, it provides a concrete starting point for the search, which is more productive than an identification of the gap alone.

### 4.6 Pregroup Grammars: Lambek's Algebraic Turn

In 1999, Lambek proposed a radical simplification of his own 1958 calculus: *pregroup grammars* (Lambek, 1999, 2008). A pregroup is a partially ordered monoid in which every element has both a left adjoint and a right adjoint. In a pregroup grammar, syntactic types are elements of a pregroup, and grammatical derivation is reduction via the adjunction inequalities:

$$a^l \cdot a \leq 1 \leq a \cdot a^l$$
$$a \cdot a^r \leq 1 \leq a^r \cdot a$$

where $a^l$ and $a^r$ are the left and right adjoints of type $a$, and $1$ is the identity element (corresponding to the sentence type $S$ when the derivation succeeds).

Pregroup grammars depart from the Lambek calculus in a significant way: they are *non-logical*. Whereas the Lambek calculus is a proof system with introduction and elimination rules, pregroup grammars are an *algebraic* formalism with adjunction and multiplication. This eliminates the distinction between introduction and elimination rules (and hence between "hypothetical" and "categorical" reasoning) in favour of a purely computational calculus of type reduction.

The practical advantage of pregroups is parsing efficiency: pregroup parsing is polynomial, and the algebraic structure provides a natural framework for compositional semantics via functors to the category of vector spaces. This last observation connects pregroup grammars directly to the DisCoCat framework (see Section 5.7), where grammatical types are mapped to vector spaces and sentence meaning is computed as a tensor contraction determined by the grammatical structure.

---

## 5. The Curry-Howard-Lambek Triangle and the Fourfold Correspondence

The deepest structural result underlying the fourfold correspondence is the *Curry-Howard-Lambek correspondence*, which identifies three apparently independent mathematical domains -- logic, computation, and category theory -- as three descriptions of the same underlying structure. When combined with the grammatical dimension supplied by Lambek's own syntactic calculus, this three-way correspondence extends to four, producing the full grammar-proof-type-category correspondence that is the thesis of this dissertation.

### 5.1 Proofs = Programs (Curry-Howard)

The Curry-Howard correspondence, discovered independently by Haskell Curry (from the 1930s onward) and William Alwyn Howard (1969, published 1980), establishes an isomorphism between systems of formal logic and typed lambda calculi. The correspondence is stated as a dictionary:

| Logic | Computation |
|-------|-------------|
| Proposition | Type |
| Proof | Program (term) |
| Implication $A \Rightarrow B$ | Function type $A \to B$ |
| Conjunction $A \wedge B$ | Product type $A \times B$ |
| Disjunction $A \vee B$ | Sum type $A + B$ |
| Truth ($\top$) | Unit type $\mathbf{1}$ |
| Falsity ($\bot$) | Empty type $\mathbf{0}$ |
| Universal $\forall x. P(x)$ | Dependent function type $\Pi(x{:}A). P(x)$ |
| Existential $\exists x. P(x)$ | Dependent pair type $\Sigma(x{:}A). P(x)$ |
| Modus ponens | Function application |
| Hypothesis | Variable |
| Proof normalisation | Computation (beta-reduction) |

The correspondence is not metaphorical. It is a bijection between the derivations of a formal logic and the well-typed terms of a corresponding type system. Simply typed lambda calculus corresponds to intuitionistic propositional logic. System F (the polymorphic lambda calculus; Girard, 1972; Reynolds, 1974) corresponds to second-order intuitionistic logic. The Calculus of Constructions (Coquand and Huet, 1988) corresponds to higher-order intuitionistic predicate logic. In each case, a proposition is provable if and only if its corresponding type is inhabited (has a term of that type).

The practical consequence is that proof assistants and dependently typed programming languages are, quite literally, programming environments for writing proofs. A verified Lean or Rocq program is simultaneously a proof of the proposition expressed by its type. This duality between proving and programming is the most productive single idea in the intersection of logic and computer science.

### 5.2 Programs = Morphisms (Lambek)

Joachim Lambek (1972, 1980) extended the Curry-Howard correspondence to include category theory by demonstrating that typed lambda calculi correspond to *Cartesian closed categories* (CCCs). In a Cartesian closed category:

| Computation | Category Theory |
|-------------|-----------------|
| Type | Object |
| Program (term) | Morphism (arrow) |
| Function type $A \to B$ | Exponential object $B^A$ |
| Product type $A \times B$ | Categorical product $A \times B$ |
| Application | Evaluation morphism $\text{eval} : B^A \times A \to B$ |
| Lambda abstraction | Currying (transpose) |
| Beta-reduction | Composition of morphisms |
| A type theory | A category |

The triple correspondence is then:

$$\text{Intuitionistic propositional logic} \cong \text{Simply typed lambda calculus} \cong \text{Cartesian closed categories}$$

More generally:

$$\text{Intuitionistic predicate logic} \cong \text{Dependent type theory} \cong \text{Locally Cartesian closed categories}$$

Lambek's contribution was to recognise that the categorical perspective is not merely a third description of the same thing but provides genuine additional insight. Categories are algebraic structures that capture the essence of *composition*: the way in which morphisms (proofs, programs, derivations) may be sequentially combined. The categorical perspective makes composition -- the most fundamental operation in all three domains -- the primitive concept, from which all other structure is derived.

### 5.3 The Linguistic Extension: Grammatical Derivations = Proofs = Typed Terms = Morphisms

The extension of the Curry-Howard-Lambek correspondence to grammar is implicit in Lambek's own work, since his 1958 syntactic calculus is simultaneously a grammar formalism, a logical system, and a typed calculus. We make the extension explicit by adding the grammatical column to the correspondence table:

| Grammar | Logic | Computation | Category |
|---------|-------|-------------|----------|
| Syntactic category | Proposition | Type | Object |
| Grammatical derivation | Proof | Program (term) | Morphism |
| Functor category $A/B$ | Implication $B \Rightarrow A$ | Function type $B \to A$ | Exponential $A^B$ |
| Function application | Modus ponens | Beta-reduction | Evaluation |
| Lexicon | Axioms | Constants (primitives) | Generators |
| Grammaticality | Provability | Type inhabitedness | Morphism existence |
| Sentence type $S$ | Goal proposition | Target type | Terminal object |

In categorial grammar, *parsing a sentence is constructing a proof is type-checking a term is composing morphisms in a category*. These are not four different activities that happen to be analogous. They are the same activity described in four mathematical languages.

The fourfold correspondence thus takes the following form: a string of words $w_1 \ldots w_n$ is grammatical (reduces to type $S$) if and only if there exists a proof in the Lambek calculus (or the appropriate logic) that the type assignment $w_1{:}A_1, \ldots, w_n{:}A_n$ entails $S$, if and only if there exists a well-typed lambda term of the appropriate type, if and only if there exists a morphism in the corresponding category from the tensor product of the objects $A_1 \otimes \cdots \otimes A_n$ to $S$.

### 5.4 The Consolidated Fourfold Correspondence Table

The following table presents the full four-column, four-row correspondence -- the signature contribution of this dissertation. For each level of the Chomsky hierarchy, all four dimensions (grammar, automaton/machine, type, proof/logic) are displayed, together with the assessed correspondence strength.

| Chomsky Level | Grammar Formalism | Automaton | Type System | Proof Calculus | Strength |
|---------------|-------------------|-----------|-------------|----------------|----------|
| **Type 3** (Regular) | Regular grammar / Regular expressions | Finite automaton (DFA/NFA) | Finite types / Enumerations | Propositional logic (finite, decidable) | Embedding |
| **Type 2** (Context-free) | Context-free grammar / BNF / Lambek calculus (product-free) | Pushdown automaton | Recursive algebraic types / Simply typed lambda calculus | Intuitionistic propositional logic / Natural deduction | **Isomorphism** |
| **MCS** (Mildly context-sensitive) | TAG / CCG / Pregroup grammars | Embedded pushdown automaton / Linear indexed automaton | *Conjecture: bounded linear polymorphic calculus* | Restricted second-order logic / Combinatory logic (restricted) | Partial (open) |
| **Type 1** (Context-sensitive) | Context-sensitive grammar | Linear bounded automaton | System F (parametric polymorphism) / Refinement types | Second-order intuitionistic logic | Embedding |
| **Type 0** (Unrestricted) | Unrestricted grammar | Turing machine | Full dependent types (CoC, MLTT) | Higher-order intuitionistic predicate logic | Analogy |

**Reading the table.** Each row represents a level of the hierarchy. The correspondence is strongest at Type 2, where all four columns are provably isomorphic. At Type 3, the grammar-automaton correspondence is an isomorphism (Kleene), but the grammar-type and grammar-proof correspondences are structural embeddings. At MCS, the grammar-automaton correspondence is an isomorphism (Vijay-Shanker and Weir), but the type and proof columns are conjectural. At Type 1, the grammar-automaton correspondence is an isomorphism (Kuroda), the grammar-type correspondence is a structural embedding (Section 2.3), and the grammar-proof correspondence is an analogy. At Type 0, all non-grammar-automaton correspondences are analogies grounded in the shared boundary of undecidability.

### 5.5 Where the Fourfold Correspondence Holds

The fourfold correspondence holds most precisely and productively in the following settings:

**The Lambek calculus and intuitionistic implicational logic.** The original and cleanest case. Lambek's syntactic calculus with its two directed implications ($/$, $\backslash$) corresponds to a non-commutative intuitionistic logic, which corresponds to a lambda calculus with directional application, which corresponds to a biclosed monoidal category. The correspondence is an isomorphism at every level: derivations biject with proofs biject with terms biject with morphisms.

**Combinatory categorial grammar and combinatory logic.** CCG's combinatory rules ($B$, $T$, $S$) correspond to the combinators of combinatory logic, which correspond to specific natural transformations in a Cartesian closed category. The correspondence is exact and has been exploited computationally in CCG-based semantic parsers.

**Montague grammar and typed lambda calculus.** Montague's syntax-semantics interface is a functor from a syntactic category to a semantic category. The functoriality of this mapping -- the fact that it preserves composition -- is the formal content of compositionality.

**Pregroup grammars and compact closed categories.** Lambek's pregroup grammars correspond to *compact closed categories* -- categories with duals for every object, generalising the duality of a vector space and its dual. This correspondence has been the basis for the DisCoCat framework (see Section 5.7).

### 5.6 Where It Breaks Down: Limitations, Gradient Grammaticality, and Non-Compositionality

The fourfold correspondence is not universal. Several significant breakdowns and limitations must be acknowledged. This section addresses them directly, engaging with the empirical critiques that have been raised against the compositional, generativist framework within which the correspondence is formulated.

**Ambiguity.** Natural language is pervasively ambiguous: lexical ambiguity ("bank" = riverbank or financial institution), structural ambiguity ("I saw the man with the telescope"), and scope ambiguity ("Every student read a book"). Type systems, by design, reject ambiguity: a well-typed term has a unique type (up to equivalence). The fourfold correspondence, in its standard form, associates grammaticality with the *existence* of a derivation/proof/term/morphism but does not account for the *multiplicity* of derivations that corresponds to ambiguity. Extensions involving intersection types (Copestake, 2002) and underspecified representations (Bos, 1996) have been proposed but do not yet fully integrate into the Curry-Howard-Lambek framework.

**Movement and long-distance dependencies.** The Lambek calculus in its original form cannot handle displacement phenomena -- cases where a syntactic constituent appears in a position distant from where it is semantically interpreted (e.g., wh-questions: "What did John eat __?"). Extensions such as the Displacement calculus (Morrill, Valentin, and Fadda, 2011) and multimodal type-logical grammars (Moortgat, 1997) address this limitation, but at the cost of additional structural complexity.

**Pragmatics and context-dependence.** The Curry-Howard correspondence connects syntax (grammar), semantics (types/logic), and proof theory (computation). Natural language has a fourth dimension -- *pragmatics* -- encompassing context-dependent meaning, conversational implicature, presupposition, and speech acts. No fully satisfactory type-theoretic or categorical account of pragmatics currently exists. Dynamic semantics (Groenendijk and Stokhof, 1991) treats meaning as context-change potential, and dependent type theories of dialogue (Ranta, 1994; Cooper, 2005) offer partial treatments, but a comprehensive Curry-Howard-style correspondence for pragmatics remains an open problem.

#### 5.6.1 Gradient Grammaticality

The Chomsky hierarchy assumes binary grammaticality: a string is either in the language or it is not; a term is either well-typed or it is not. Natural language is not like this. Grammaticality is *gradient* -- speakers assign degrees of acceptability to sentences on a continuous scale rather than making categorical in/out judgments (Lau, Clark, and Lappin, 2017; Sprouse, Schutze, and Almeida, 2013).

Consider the following cline of acceptability in English:

1. "The cat sat on the mat." (fully acceptable)
2. "The cat sat on." (degraded but interpretable)
3. "Who did you wonder whether saw Mary?" (island violation -- degraded but parsable)
4. "Cat the on mat sat the." (severely degraded but individual words recognisable)
5. "Furiously sleep ideas green colourless." (anomalous but grammatically parsable in reverse)

A binary grammar assigns each of these to {grammatical, ungrammatical}. Human judgments place them on a continuum. This poses a genuine challenge to the fourfold correspondence, which inherits the binary well-formedness assumption from both formal grammar and type theory.

Several responses to this challenge exist within the type-theoretic tradition:

*Probabilistic/weighted grammars.* Weighted context-free grammars (WCFGs) assign real-valued weights (typically log-probabilities) to productions, and the "grammaticality" of a string is its total weight rather than a binary value. This moves from $L \subseteq \Sigma^*$ (a language as a set) to $p : \Sigma^* \to \mathbb{R}$ (a language as a probability distribution). The type-theoretic analogue would be a *graded* or *probabilistic* type system, in which types carry numerical annotations representing confidence or frequency. Graded monads (Katsumata, 2014) and quantitative type theories (Atkey, 2018; McBride, 2016) provide formal frameworks for types annotated with quantities. Whether these can be connected to probabilistic grammars via a weighted Curry-Howard correspondence is an active research question.

*Fuzzy type theory.* Novak (2005) developed a fuzzy type theory in which propositions carry truth values from $[0, 1]$ rather than $\{0, 1\}$, and typing judgments are graded accordingly. This provides a direct type-theoretic model of gradient grammaticality, though the connection to the Curry-Howard-Lambek correspondence has not been fully worked out.

*Soft constraints in Optimality Theory.* Optimality Theory (Prince and Smolensky, 1993/2004) models grammaticality as the outcome of ranked constraint satisfaction, where the "optimal" candidate is the one that satisfies the highest-ranked constraints. Violations of lower-ranked constraints produce gradient degradation. This can be formalised type-theoretically as a system of *ranked typing constraints* where a term may satisfy some constraints but not others.

The honest assessment is that gradient grammaticality is a genuine limitation of the fourfold correspondence in its current form. The binary framework is exact for formal and computational languages (programs are well-typed or not; strings are in the language or not) and approximate for natural language. The correspondence can be *extended* to the gradient case via probabilistic or graded type systems, but these extensions are in early stages and no analogue of the clean Curry-Howard isomorphism has been established for them.

#### 5.6.2 The Multiword Expression Problem

A substantial proportion of natural language consists of *multiword expressions* (MWEs) -- prefabricated chunks that are stored and retrieved as units rather than generated compositionally. These include:

- **Fixed idioms:** "kick the bucket" (= die), "spill the beans" (= reveal a secret). Semantically non-compositional: the meaning of the whole is not a function of the meanings of the parts.
- **Semi-fixed expressions:** "take X into account," "by and large," "as a matter of fact." Partially productive, partially fixed.
- **Collocations:** "heavy rain" (not *strong rain*), "make a decision" (not *do a decision*). Statistically preferred combinations that are not predictable from compositionality alone.
- **Light verb constructions:** "take a walk," "give a talk," "make a mistake." The verb contributes little semantic content; the construction as a whole is partially compositional.
- **Formulaic sequences:** Greetings ("how do you do"), discourse markers ("you know," "I mean"), conversational routines.

Corpus studies consistently find that MWEs constitute a large proportion of running text. Estimates vary: Erman and Warren (2000) found that approximately 55% of their corpus consisted of "prefabs"; Wray (2002) surveys estimates ranging from 30% to 80% depending on genre and definition. Even the conservative lower bound of 30% represents a massive portion of language use that resists compositional analysis.

The fourfold correspondence rests fundamentally on compositionality -- the principle that the grammar/type/proof/morphism of the whole is determined by the grammars/types/proofs/morphisms of the parts and their mode of combination. If a third or more of natural language is non-compositional, then the fourfold correspondence does not *fail* -- it simply does not *apply* to that portion of language. This is not a minor caveat; it represents a systematic gap between the formal architecture and the empirical reality of language use.

Several approaches attempt to accommodate MWEs within compositional frameworks:

- **Extended lexicon.** Treat MWEs as atomic lexical entries with their own types. "Kick the bucket" receives a single type $NP \backslash S$ meaning "die," rather than being composed from "kick," "the," and "bucket." This preserves compositionality at the cost of a vastly expanded lexicon. Categorial grammar has been extended in this direction (Baldwin and Kim, 2010).

- **Construction Grammar.** Goldberg (1995, 2006) proposes that *all* of linguistic knowledge consists of "constructions" -- form-meaning pairings that range from fully fixed (idioms) to fully productive (argument structure rules). On this view, there is no principled boundary between compositional and non-compositional language: all language is constructional, and the degree of productivity varies continuously. This is a fundamental challenge to the fourfold correspondence, which assumes that composition is the basic mechanism.

- **Distributional composition.** The DisCoCat framework (Section 5.7) can accommodate non-compositional expressions to some extent, because the meaning vectors assigned to words are learned from distributional statistics that already encode collocational information. A word's vector reflects not only its "compositional" meaning but also its typical collocates. However, DisCoCat still computes sentence meaning via structural composition (tensor contraction), so fully frozen idioms require special treatment.

We acknowledge the multiword expression problem as a genuine limitation of the fourfold correspondence when applied to natural language. The correspondence applies cleanly to the *compositional* portion of language and must be supplemented by a theory of stored/retrieved units (a "constructicon" in the terminology of Goldberg, 2006, or a "phrasal lexicon" in the terminology of Becker, 1975) for the non-compositional portion. In computational languages, where MWEs are rare or absent (every expression is compositional by construction), this limitation does not arise.

#### 5.6.3 The Generativist vs. Usage-Based Debate

The fourfold correspondence is framed within the generativist tradition, and it is important to acknowledge that this framing is itself contested. The debate between generativist and usage-based approaches to language centres on a fundamental question: is linguistic knowledge a system of abstract rules (grammars, types, proofs) that generates linguistic expressions, or is it a structured inventory of constructions learned from usage patterns, where "rules" are emergent generalisations over stored exemplars?

The generativist position (Chomsky, 1957, 1965, 1995) holds that linguistic competence is a system of recursive rules, that the poverty of the stimulus implies innate grammatical knowledge, and that the Chomsky hierarchy (or refinements of it) characterises the formal complexity of this system. The fourfold correspondence is a natural extension of this programme.

The usage-based position (Langacker, 1987; Goldberg, 1995, 2006; Bybee, 2006, 2010; Tomasello, 2003) holds that linguistic knowledge is an inventory of constructions at varying levels of abstraction, that children learn language from input via general cognitive mechanisms (analogy, categorisation, statistical learning), and that the sharp competence/performance distinction is empirically unjustified. On this view, the Chomsky hierarchy is at best an approximation to one dimension of linguistic complexity (recursive depth) and at worst a misleading idealisation that ignores the gradient, probabilistic, construction-specific, and frequency-driven nature of real linguistic knowledge.

This dissertation does not attempt to resolve this debate. The fourfold correspondence is compatible with the generativist position and provides formal tools that extend the generativist programme. It is less compatible with the strong usage-based position, which rejects the premise that abstract formal grammars are the right description of linguistic knowledge. However, a *moderate* usage-based position -- which acknowledges that language has compositional structure while insisting that this structure is probabilistic, gradient, and construction-sensitive -- can potentially be accommodated by extending the correspondence to weighted grammars, graded type systems, and probabilistic proof theories (Section 5.6.1). This extension is a direction for future work rather than an accomplished result.

### 5.7 The DisCoCat Framework: Compositional Distributional Semantics via Category Theory

A significant modern development that operationalises the categorical dimension of the fourfold correspondence is the *DisCoCat* framework (Categorical Compositional Distributional Semantics), introduced by Coecke, Sadrzadeh, and Clark (2010). DisCoCat addresses a long-standing tension in computational semantics between two traditions:

- **Distributional semantics**, in which word meanings are represented as vectors in a high-dimensional space (derived from co-occurrence statistics), capturing semantic similarity but lacking compositional structure.
- **Compositional semantics**, in which sentence meanings are built up from word meanings via grammatical structure (the Montague tradition), providing compositionality but lacking the statistical richness of distributional models.

DisCoCat resolves this tension by using category theory as the bridge. The key insight is that both grammatical structure (pregroup grammars) and vector spaces are *compact closed categories*, and meaning assignment is a *functor* from the grammatical category to the category of finite-dimensional vector spaces and linear maps:

$$F : \mathbf{Preg} \to \mathbf{FdVect}$$

Under this functor:

- Each grammatical type $A$ is mapped to a vector space $F(A)$ (e.g., $F(N)$ is the noun space, $F(S)$ is the sentence space).
- Each word of type $A$ is mapped to a vector in $F(A)$ (or a tensor in $F(A)$ for complex types).
- The meaning of a sentence is computed by *contracting* the tensors according to the grammatical structure -- a process determined entirely by the categorical structure of the derivation.

DisCoCat thus realises the fourfold correspondence in a computationally concrete way: grammatical parsing determines a categorical morphism, which determines a linear-algebraic computation (tensor contraction), which produces a vector representing the sentence's meaning. The framework has been implemented and tested empirically (Grefenstette and Sadrzadeh, 2011; Kartsaklis et al., 2012), demonstrating that category-theoretic compositionality can be combined with distributional word vectors to produce meaningful sentence representations.

The connection to quantum computing is suggestive and has been exploited: the compact closed categories used in DisCoCat are the same categories used to model quantum processes (Abramsky and Coecke, 2004), and the tensor contraction operations that compute sentence meaning are formally identical to quantum circuit operations. This connection has led to implementations of DisCoCat on quantum computers (Lorenz et al., 2023; Meichanetzidis et al., 2021), creating a literal realisation of "parsing as quantum computation."

---

## 6. Modern Developments

The fourfold correspondence is not a historical curiosity but an active area of research with ongoing developments across programming language theory, computational linguistics, and theoretical linguistics. This section surveys the most significant modern developments that extend, challenge, or apply the correspondence.

### 6.1 Programming Language Theory: Bidirectional Type-Checking, Algebraic Effects, and HoTT

**Bidirectional type-checking.** Modern type-checkers increasingly employ *bidirectional* strategies that combine two modes: *type synthesis* (bottom-up: infer the type of a term from its structure) and *type checking* (top-down: verify that a term has a given expected type). This bidirectionality mirrors the bidirectionality of parsing: top-down (predictive, LL) and bottom-up (shift-reduce, LR) parsers correspond to type-checking-mode and type-synthesis-mode type-checkers, respectively. The parallel extends to the *interleaving* of modes: just as Earley parsing combines top-down prediction with bottom-up completion, bidirectional type-checking (Dunfield and Krishnaswami, 2021) interleaves synthesis and checking at subterm boundaries.

The grammar-type parallel here is not merely structural but *methodological*: the same algorithmic strategies that were developed for parsing context-free grammars have been independently rediscovered in the context of type-checking. This suggests that the two problems are not merely analogous but are, at a deep level, the same problem in different mathematical clothing.

**Algebraic effects and handlers.** The algebraic effects framework (Plotkin and Power, 2003; Plotkin and Pretnar, 2013) extends the type-theoretic paradigm from classifying *values* to classifying *computations*. If types classify what a term *is*, effect types classify what a term *does* -- what side effects (I/O, state mutation, exceptions, nondeterminism) it may produce. This extends the fourfold correspondence in a linguistically suggestive direction: just as effect types classify computational side effects, linguistic *mood* (declarative, interrogative, imperative) classifies the "pragmatic effect" of an utterance beyond its propositional content. A declarative sentence is a "pure" linguistic computation; a question is a computation with an "input effect" (it demands a response from the environment); an imperative is a computation with an "output effect" (it changes the state of the world). Whether this analogy can be made formally precise remains an open question, but it is consistent with the spirit of the fourfold correspondence.

**Homotopy Type Theory (HoTT).** Homotopy Type Theory (Univalent Foundations Program, 2013) extends the Curry-Howard correspondence into topology by identifying types with *spaces* and proofs with *paths*. The identity type $a =_A b$ is interpreted as the space of paths from $a$ to $b$ in the space $A$, and higher identity types correspond to homotopies between paths, homotopies between homotopies, and so on -- the full structure of homotopy theory.

HoTT adds a new dimension to the fourfold correspondence: the propositions-as-types reading gains a geometric interpretation (propositions as spaces, proofs as paths), and the categories involved become *higher categories* ($\infty$-groupoids). While HoTT has not yet been connected to linguistics in a substantive way, the programme of *Higher-Dimensional Grammar* (Mellies, 2006, building on Burroni, 1993) uses higher-dimensional categories to model grammatical rewriting, suggesting that HoTT may eventually provide a natural framework for grammatical phenomena that involve multiple levels of derivational equivalence.

### 6.2 Natural Language Processing: CCG Parsing, Pregroup Grammars, and Neural Approaches

**CCG parsing at scale.** Combinatory Categorial Grammar has transitioned from a theoretical formalism to a practical NLP technology. The C&C parser (Clark and Curran, 2007) and subsequent neural CCG parsers (Lewis and Steedman, 2014; Clark et al., 2018) achieve high-accuracy broad-coverage parsing of English, producing typed semantic representations that can be directly used for downstream reasoning tasks. The success of CCG parsing demonstrates that the grammar-type-proof correspondence is not merely a theoretical elegance but a viable engineering architecture.

CCG-based semantic parsing systems, such as those used in question answering (Artzi and Zettlemoyer, 2013) and robot instruction understanding (Matuszek et al., 2012), translate English sentences into typed logical forms -- lambda calculus expressions with explicit types -- that can be evaluated against a knowledge base. In these systems, the fourfold correspondence operates in real time: parsing constructs a grammatical derivation, which *is* a proof, which *determines* a typed lambda term, which *is* a query.

**Pregroup grammars and quantum NLP.** The DisCoCat framework, grounded in pregroup grammars (Section 5.7), has generated an active programme of *quantum natural language processing* (QNLP). The company Quantinuum (formerly Cambridge Quantum) has implemented DisCoCat-based NLP models on quantum hardware (Lorenz et al., 2023), demonstrating that sentence meaning can be computed via quantum circuit operations. The lambeq library (Kartsaklis et al., 2021) provides a pipeline from text to quantum circuits via pregroup parsing, making the grammar-category-computation correspondence directly executable on quantum computers.

**Neural approaches and the implicit grammar question.** Transformer-based language models (Vaswani et al., 2017) -- including BERT (Devlin et al., 2019), GPT (Radford et al., 2018, 2019), and their successors -- achieve remarkable performance on language tasks without using any explicit grammar. This raises the question: do these models implicitly learn grammatical structure, and if so, at what level of the Chomsky hierarchy does their implicit grammar reside?

A body of *probing* studies has investigated this question. Hewitt and Manning (2019) demonstrated that BERT's internal representations encode a geometric analogue of dependency parse trees, accessible via a linear transformation of the embedding space. Clark et al. (2019) showed that specific attention heads in BERT encode specific syntactic relations (subject-verb, determiner-noun). Goldberg (2019) demonstrated that BERT tracks subject-verb agreement across long-distance dependencies with high accuracy -- a context-sensitive phenomenon.

These findings are *suggestive* that transformers learn *at least* context-free structure (nested phrase structure) and *some* context-sensitive structure (agreement phenomena). However, an important methodological caveat must be acknowledged: the probing methodology has been challenged on the grounds that probing classifiers may find structure in random representations simply because the probes themselves are powerful enough to learn the task independently of the representations being probed (Hewitt and Liang, 2019; Pimentel et al., 2020). The relevant question is not whether a probe *can* extract syntactic information from a transformer, but whether the transformer *encodes* that information in a way that differs meaningfully from a random baseline. Control experiments using "selectivity" measures (Hewitt and Liang, 2019) partially address this concern but do not fully resolve it.

Whether transformers learn anything corresponding to a *type system* in the categorial grammar sense is a more subtle and more speculative question. If specific attention heads implement something like functional application -- combining an element of type $A/B$ with an element of type $B$ to produce type $A$ -- then the transformer would be implicitly implementing a form of categorial grammar. Early evidence from Jawahar et al. (2019) and others suggests that lower layers encode local (regular/context-free) structure while higher layers encode more global (context-sensitive) structure, consistent with a hierarchical organisation that mirrors the Chomsky hierarchy. However, definitive evidence that transformers learn type-theoretic structure in the precise sense of categorial grammar has not been established. This remains one of the most important open questions at the intersection of formal linguistics and deep learning, and we characterise the current evidence as suggestive rather than conclusive.

### 6.3 Linguistics: The Minimalist Program and Merge

Chomsky's Minimalist Program (Chomsky, 1995, 2000, 2008) represents the most recent major framework in the generativist tradition. It asks: what is the *minimal* computational system needed for natural language? The answer proposed is strikingly austere: a single recursive operation, *Merge*, together with a lexicon and interface conditions.

Merge takes two syntactic objects $\alpha$ and $\beta$ and combines them into a set $\{\alpha, \beta\}$. *External Merge* combines two independent syntactic objects (corresponding to "first merge" or "base generation"). *Internal Merge* takes a syntactic object already contained within a larger structure and re-merges it at a higher position (corresponding to "movement" in earlier transformational frameworks).

The parallel between Merge and function application in the typed lambda calculus has been noted by several authors (Collins, 2002; Stabler, 2011; Lecomte, 2011). The parallel rests on the following observations:

1. Both operations are binary: they take two inputs and produce one output.
2. Both operations are recursive: the output may serve as an input to a further application of the same operation.
3. Both operations are the *sole* structure-building operation of their respective systems (Merge for syntax, application for lambda calculus).
4. External Merge, which combines two independent objects, mirrors ordinary function application ($f(x)$). Internal Merge, which "moves" an element from a position where it is already present, mirrors *variable binding* -- the lambda abstraction that binds a variable already present in the body.

Stabler (1997, 2011) formalised this parallel by defining *Minimalist Grammars* (MGs) as a precise mathematical formalism and demonstrating that MGs generate exactly the class of mildly context-sensitive languages (the same class generated by CCGs and TAGs). Moreover, Stabler showed that MGs can be translated into a form of categorial grammar, making the Merge-as-application connection explicit.

However, the equivalence is not perfect. Merge operates on *sets* (unordered), while function application operates on *terms* (ordered). In Merge, $\{\alpha, \beta\} = \{\beta, \alpha\}$: the operation is symmetric. Function application $f(x)$ is inherently asymmetric: $f$ is the function, $x$ is the argument. This asymmetry is introduced in Minimalist syntax by the labelling algorithm -- the mechanism that determines which of the two merged objects is the "head" (the function) and which is the "complement" (the argument). Whether this difference is superficial (a matter of presentation) or deep (reflecting a genuine structural distinction between linguistic and computational combination) remains debated.

---

## 7. Implications

The fourfold correspondence between grammars, automata, types, and proofs is not merely a theoretical curiosity. It has practical implications for the design of programming languages, the engineering of natural language processing systems, the evaluation of linguistic theories, and the architecture of governance systems.

### 7.1 For Programming Language Design: What Grammar Theory Teaches Type System Designers

The grammar hierarchy provides a principled framework for understanding the trade-offs in type system design. Each level of the hierarchy corresponds to a regime of type-theoretic expressiveness with characteristic decidability properties:

- **Type 3 / Finite types:** Type checking is trivial (constant-time lookup). Languages with only enumeration types and no type constructors (assembly language, early BASIC) occupy this level.
- **Type 2 / Recursive algebraic types:** Type checking is decidable and efficient (typically linear in the size of the term). Languages with pattern matching over algebraic data types (Haskell, OCaml, Rust) occupy this level for their core type systems.
- **Type 1 / Parametric polymorphism:** Type checking remains decidable for System F (though type inference is undecidable in full System F; Wells, 1999). Note that the decidability landscape is more nuanced than "preserved across all four dimensions" suggests: type-*checking* in System F is decidable, but type *inference* is undecidable, a distinction with no direct analogue in the grammar-automaton correspondence. Languages with generics and bounded quantification (Java, C#, Kotlin) operate at this level.
- **Type 0 / Dependent types:** Type checking is decidable only if all functions terminate. Languages with full dependent types (Agda, Lean, Rocq) must enforce termination checking to keep type-checking decidable, or else accept the risk of non-termination (as in some uses of Haskell's type families and TypeScript's conditional types).

The lesson for language designers is that the expressiveness of the type system and the decidability of type-checking are constrained by the same trade-offs that constrain the expressiveness and parsability of grammars. A language designer who adds a feature that pushes the type system from the context-free level (decidable, efficient) to the context-sensitive level (decidable but potentially expensive) or the unrestricted level (potentially undecidable) should do so with the same awareness that a grammar designer brings to the addition of context-sensitive rules.

**The locality difference between parse errors and type errors.** An important practical difference between parsing and type-checking, not captured by the formal correspondence, concerns *error locality*. Parse errors are typically *local*: the parser can point to the character or token where the parse fails ("expected ')' to close '('"). Type errors are often *non-local*: the error manifests in a location far from the code that causes it (a function defined with a wrong return type in a distant module causes a type error at the call site). This locality difference has profound implications for developer experience. The fourfold correspondence predicts that parsing and type-checking are structurally analogous, but it does not predict that their *error modalities* are analogous. A productive research direction, suggested by the grammar-type parallel, is whether parser error-recovery techniques (Burke and Fisher, 1987; Corchuelo et al., 2002) can be adapted to improve the locality and helpfulness of type error messages.

**A decision tree for type-system level selection.** The fourfold correspondence, combined with domain analysis, suggests a practical decision procedure for language designers:

1. *Does your domain require only finite classification (flags, modes, simple states)?* -- Finite types suffice (Type 3). Decidability is trivial; cognitive cost is near-zero.
2. *Does your domain require recursive data structures (trees, nested expressions, hierarchical configurations)?* -- You need recursive algebraic types (Type 2). Decidability is guaranteed; pattern matching provides a strong mental model.
3. *Does your domain require code reuse across types, or type-dependent constraints (generic containers, type-safe APIs, protocol-indexed operations)?* -- You need parametric polymorphism or bounded quantification (Type 1). Decidability is preserved for type-checking but type inference may be undecidable in full generality. Cognitive cost is significant: studies of Java generics adoption (Parnin et al., 2013) show that many developers avoid generics or use them incorrectly.
4. *Does your domain require types that depend on runtime values (length-indexed arrays, statically verified protocols, theorem-proving)?* -- You need dependent types (Type 0). Type-checking is decidable only with termination enforcement. Cognitive cost is high: even experienced functional programmers find dependent types challenging (Brady, 2013).

Each step down this tree increases expressiveness but also increases the computational cost of type-checking and the cognitive cost to the developer. The fourfold correspondence provides the theoretical justification for this trade-off: it is the same trade-off that governs grammars and parsing, manifested in the type-theoretic dimension.

### 7.2 For NLP: What Type Theory Teaches Parser Designers

The type-theoretic perspective suggests that parsing should be understood not merely as *recognition* (is this string in the language?) but as *type inference* (what is the type -- the semantic structure -- of this expression?). This shift in perspective has practical consequences:

- **Typed semantic representations are more useful than untyped parse trees.** A parse tree records the syntactic structure of a sentence but does not directly encode its meaning. A typed lambda term -- produced by a CCG or Montague-style parser -- simultaneously encodes syntactic structure and semantic content. NLP systems that use typed representations (Artzi and Zettlemoyer, 2013; Liang, 2013) can directly interface with knowledge bases and reasoning engines, whereas those that use untyped parse trees require an additional semantic interpretation step.

- **Type-checking provides an additional source of constraints for parsing.** Ambiguous sentences may have multiple syntactic parses but, when semantic types are taken into account, only a subset of the parses may be well-typed. Type-driven parsing (Baldridge and Kruijff, 2003) exploits this observation to reduce parsing ambiguity by filtering out type-inconsistent derivations. This is directly analogous to the way that type-checking in a compiler eliminates programs that are syntactically valid but semantically ill-formed.

- **The Curry-Howard correspondence suggests new parsing algorithms.** If parsing is proof search, then the vast literature on proof-search strategies (tableau methods, resolution, sequent calculus) becomes directly applicable to parsing. Conversely, parsing algorithms (Earley, CYK, chart parsing) may find applications in proof search. This cross-pollination has been productive: type-logical grammars use proof-search strategies as parsing algorithms, and Earley-style algorithms have been applied to proof search in linear logic (Hodas and Miller, 1994).

### 7.3 For Linguistics: Computational Adequacy of Grammatical Theories

The fourfold correspondence provides a principled criterion for evaluating linguistic theories: a grammatical theory is computationally adequate if it generates exactly the class of languages attested in natural language (the mildly context-sensitive class) and provides a transparent interface to semantic interpretation (type-theoretic compositionality). This criterion favours theories in the categorial tradition (Lambek calculus, CCG, pregroup grammars) that are explicitly type-theoretic, over theories in the phrase-structure tradition (GB, Minimalism) that are less directly connected to type theory, though Stabler's formalisations of Minimalist Grammars have substantially narrowed this gap.

The open question of whether Merge is equivalent to function application (Section 6.3) has profound implications. If the equivalence holds, then Chomsky's Minimalist Program and the categorial grammar tradition are not rival theories but alternative descriptions of the same computational system -- the system of typed function application. This would constitute a unification of the two major traditions in generative linguistics, mediated by the Curry-Howard-Lambek correspondence.

### 7.4 For System Design: Governance Rule Grammars and Decidability

An implication of the fourfold correspondence that extends beyond the academic domains of linguistics and type theory concerns the design of *governance systems* -- systems of rules that determine whether an action, configuration, or state transition is permitted. In the ORGANVM system architecture (and in analogous systems such as Kubernetes admission controllers, AWS IAM policies, and regulatory compliance engines), governance rules form a *grammar* over the space of permitted operations.

The Chomsky hierarchy provides a framework for classifying the expressiveness and decidability of governance rule systems:

- **Regular governance rules** (equivalent to finite automata) can verify properties that require no memory of prior states: simple whitelists, blacklists, and pattern-matching rules. Policy enforcement is $O(n)$ and guaranteed to terminate.
- **Context-free governance rules** (equivalent to pushdown automata) can verify properties involving nesting and recursion: hierarchical access control, nested approval workflows, recursive organisational structures. Enforcement is polynomial and decidable.
- **Context-sensitive governance rules** (equivalent to linear bounded automata) can verify properties that depend on context: role-based access control with constraints across organisational boundaries, cross-departmental approval dependencies, budget allocation rules that depend on prior allocations. Enforcement is decidable but potentially expensive (PSPACE-complete in the worst case).
- **Unrestricted governance rules** (equivalent to Turing machines) can express arbitrary conditions, including rules that depend on the outcome of arbitrary computations. Enforcement may not terminate. This is the regime of governance rules that invoke external services, evaluate arbitrary code, or depend on conditions that are themselves undecidable.

The practical lesson is that governance system designers should deliberately choose the *weakest* grammar level that suffices for their requirements, in order to preserve decidability and tractability. A governance system whose rules are context-free is guaranteed to be decidable and polynomially enforceable. Promoting rules to the context-sensitive level should be done with awareness of the computational cost, and permitting unrestricted rules should be done only with explicit non-termination safeguards (timeouts, resource bounds, human-in-the-loop escalation).

### 7.5 Cognitive Complexity as a Practical Dimension

From a human-computer interaction perspective, the most important property of a type system is not its decidability or expressiveness but its *cognitive cost to the user*. The fourfold correspondence gains significant practical value when augmented with a cognitive-complexity dimension that parallels the computational-complexity hierarchy:

| Type Level | Cognitive Demand | Evidence |
|------------|-----------------|----------|
| Type 3 (Finite types) | Trivial: enumerate and select. Cognitive cost near-zero. | Universal adoption; no learning barrier. |
| Type 2 (Recursive algebraic types) | Moderate: requires understanding recursion, a well-documented cognitive barrier (Kahney, 1983). Pattern matching provides a strong compensating mental model. | Widely adopted in FP languages; pattern matching is learnable. |
| Type 1 (Parametric polymorphism) | Significant: requires reasoning about type variables ("for all types T"), adding a layer of abstraction. | Studies of Java generics adoption (Parnin et al., 2013) show avoidance and misuse. |
| Type 0 (Dependent types) | High: requires reasoning about values at the type level, blurring the phase distinction between compile-time and run-time. | Even experienced FP programmers find dependent types challenging (Brady, 2013). |

This cognitive hierarchy is not merely a restatement of the computational hierarchy in human terms. The two hierarchies can diverge: for example, Haskell's type classes (a Type 1 feature) have been shown to be more cognitively accessible than Java's bounded wildcards (also Type 1), despite comparable formal expressiveness, because type classes provide a more intuitive mental model (dictionary passing). The cognitive dimension is thus partially independent of the formal dimension and provides additional design guidance that the formal correspondence alone does not supply.

---

## 8. Discussion

The fourfold correspondence between grammars, automata, types, and proofs, as developed in this dissertation, admits several interpretations of varying philosophical strength.

The **weak interpretation** holds that the four domains exhibit structural analogies: regular grammars *resemble* finite types in that both lack recursion; context-free grammars *resemble* recursive algebraic types in that both are defined by mutual recursion. On this interpretation, the correspondence is a useful heuristic for cross-domain reasoning but does not establish genuine identity.

The **moderate interpretation** holds that the four domains are formally related by precise mathematical maps -- functors, translations, encodings -- that preserve relevant structure. The grammar-automaton correspondence is a theorem; the Curry-Howard correspondence is a theorem; the Lambek extension to categories is a theorem. The grammar-type correspondence, at least at the context-free level, is a constructive isomorphism. On this interpretation, the fourfold correspondence is a mathematical result, albeit one that is fully proved only at certain levels and remains conjectural at others.

The **strong interpretation** holds that the four domains are *four descriptions of a single mathematical structure*. Grammars, automata, type systems, and proof calculi are not four different things that happen to be related; they are four perspectives on one thing -- the structure of compositional computation. This interpretation is supported by the Curry-Howard-Lambek correspondence, which demonstrates that logic, computation, and category theory are literally the same mathematical object viewed from three angles. The addition of grammar as a fourth perspective is Lambek's own contribution, rooted in his observation that his syntactic calculus is simultaneously a grammar, a logic, a calculus, and a category.

This dissertation has presented evidence for the moderate interpretation while arguing that the strong interpretation is a productive and largely correct research programme. The primary gap is at the mildly context-sensitive level: the grammar-automaton correspondence is established (TAG/CCG correspond to embedded pushdown automata / linear indexed grammars), but the grammar-type correspondence is not. Identifying the type system that stands in the same structural relationship to mildly context-sensitive grammars as recursive algebraic types stand to context-free grammars would close this gap and substantially strengthen the case for the strong interpretation. The conjecture proposed in Section 4.5 -- that the MCS type system is a bounded linear polymorphic calculus -- provides a concrete and falsifiable target for this investigation.

A further caveat concerns the scope of the correspondence. The fourfold correspondence, in the form presented here, applies primarily to *competence* -- the abstract formal systems that define languages, types, proofs, and categories. It says less about *performance* -- the actual processes by which humans parse sentences, programmers write programs, or mathematicians construct proofs. The probing studies reviewed in Section 6.2 provide suggestive evidence that neural language models may implicitly learn some type-theoretic structure, but the methodological concerns about probing (Hewitt and Liang, 2019; Pimentel et al., 2020) mean that this evidence should be treated with caution.

The limitations identified in Section 5.6 -- gradient grammaticality, multiword expressions, and the generativist-vs.-usage-based debate -- are not peripheral issues. They characterise the majority of natural language use. The fourfold correspondence is exact for formal and computational languages and approximate for natural language. This is not a failure of the correspondence but a honest assessment of its scope: it captures the *compositional, rule-governed* dimension of language, which is the dimension most amenable to formal analysis, while leaving the *gradient, constructional, usage-driven* dimension to complementary theoretical frameworks.

Finally, the correspondence between grammar levels and type-system levels, while structurally compelling, is not as mathematically precise as the grammar-automaton correspondence at all levels. The latter is a family of *theorems* with precise statements and rigorous proofs. The former is, at present, a family of results ranging from *theorems* (at the context-free level) through *structural embeddings* (at the regular and context-sensitive levels) to *analogies* (at the unrestricted level). Formulating and proving containment and separation theorems for a "Chomsky hierarchy of type systems" -- with the correspondence strength rigorously characterised at each level -- remains the deepest open problem identified by this investigation.

---

## 9. Conclusion

This dissertation has traced the development of a fourfold structural correspondence linking formal grammars, abstract automata, type systems, and proof calculi. The correspondence originates in Chomsky's 1956 hierarchy and the grammar-automaton results of the 1960s, deepens through Lambek's 1958 syntactic calculus and the Curry-Howard correspondence of the 1960s-1980s, and finds modern expression in the DisCoCat framework and quantum natural language processing.

The principal contributions are as follows:

1. **Systematic extension of the grammar-automaton correspondence to a fourfold correspondence, with stratified precision claims.** Each level of the Chomsky hierarchy has been paired with a type-theoretic regime (finite types, recursive algebraic types, parametric polymorphism, dependent types) and a proof-theoretic regime (propositional logic, first-order logic, second-order logic, higher-order logic). The correspondence strength has been explicitly classified at each level: isomorphism at Type 2, structural embedding at Types 3 and 1, analogy at Type 0.

2. **Identification of the mildly context-sensitive gap and a concrete conjecture.** The type-theoretic characterisation of mildly context-sensitive languages -- the conjectured complexity class of natural language -- remains an open problem. We have proposed that the corresponding type system is a bounded linear polymorphic calculus (a restricted fragment of System F with linear types and bounded quantification), and we have argued that this conjecture is both motivated by the formal structure and amenable to verification.

3. **Cross-linguistic grounding.** The linguistic claims have been grounded in typologically diverse evidence: Turkish (agglutinative morphology), Mandarin Chinese (tonal phenomena), American Sign Language (simultaneous multi-channel structure), Warlpiri (non-configurational syntax), and Mohawk (polysynthetic word formation). This evidence demonstrates both the scope and the limitations of the fourfold correspondence across the world's languages.

4. **Explicit treatment of limitations.** The paper has directly addressed gradient grammaticality, the multiword expression problem (30-80% of running text), the contested status of Shieber (1985), and the generativist-vs.-usage-based debate. These are not footnotes but central concerns that delimit the scope of the correspondence.

5. **Analysis of the Merge-application connection.** We have reviewed the evidence for and against the formal equivalence of Chomsky's Merge operation and typed function application, concluding that the parallel is deep and productive but not yet a proved isomorphism. The key obstacle is the symmetry of Merge (which operates on unordered sets) versus the asymmetry of application (which distinguishes function from argument).

6. **Survey of the neural grammar question.** We have reviewed the evidence that transformer-based language models implicitly learn structure corresponding to the Chomsky hierarchy, finding strong evidence for context-free structure, partial evidence for context-sensitive structure, and no definitive evidence for type-theoretic structure in the categorial grammar sense. We have characterised the probing evidence as suggestive, acknowledging the methodological challenges identified by Hewitt and Liang (2019) and Pimentel et al. (2020).

7. **Practical implications.** We have drawn out implications for programming language design (a decision tree for type-system level selection, the locality difference between parse errors and type errors), NLP engineering (type-theoretic parsing produces richer representations than untyped parsing), linguistic theory (computational adequacy as an evaluation criterion), governance system architecture (the Chomsky hierarchy classifies the decidability of governance rules), and cognitive complexity (a human-complexity hierarchy paralleling the computational-complexity hierarchy).

Three directions for future work present themselves with particular urgency. First, the verification or refutation of the MCS gap conjecture (Section 4.5) would either close the most important lacuna in the fourfold correspondence or redirect the search toward the correct type system. Second, the development of *weighted* or *graded* Curry-Howard correspondences that accommodate gradient grammaticality would extend the formal framework to cover the probabilistic, frequency-sensitive dimension of natural language. Third, the extension of the fourfold correspondence to *multi-dimensional* grammars -- capturing the simultaneous structure of sign languages and the multi-channel nature of spoken language (syntax, prosody, gesture) -- would test the limits of the string-based framework and potentially reveal new mathematical structures.

The fourfold correspondence, if it holds in its full generality, tells us something remarkable about the relationship between language and computation: that the structures we use to organise sentences, the machines we build to recognise patterns, the type systems we design to prevent errors, and the proofs we construct to establish truth are not four different things but four aspects of a single mathematical reality. The convergence of Chomsky's grammars, Turing's machines, Church's types, and Lambek's categories is one of the deepest structural results of the twentieth century, and its full articulation remains one of the most compelling open problems of the twenty-first.

---

## References

Abramsky, S. and Coecke, B. (2004). A categorical semantics of quantum protocols. In *Proceedings of the 19th Annual IEEE Symposium on Logic in Computer Science*, pp. 415--425.

Ajdukiewicz, K. (1935). Die syntaktische Konnexitat. *Studia Philosophica*, 1, 1--27.

Artzi, Y. and Zettlemoyer, L. (2013). Weakly supervised learning of semantic parsers for mapping instructions to actions. *Transactions of the Association for Computational Linguistics*, 1, 49--62.

Atkey, R. (2018). Syntax and semantics of quantitative type theory. In *Proceedings of the 33rd Annual ACM/IEEE Symposium on Logic in Computer Science*, pp. 56--65.

Backus, J. (1959). The syntax and semantics of the proposed international algebraic language of the Zurich ACM-GAMM conference. In *Proceedings of the International Conference on Information Processing*, UNESCO, pp. 125--131.

Baker, M. C. (1988). *Incorporation: A Theory of Grammatical Function Changing*. University of Chicago Press.

Baker, M. C. (1996). *The Polysynthesis Parameter*. Oxford University Press.

Baldridge, J. and Kruijff, G.-J. M. (2003). Multi-modal combinatory categorial grammar. In *Proceedings of the 10th Conference of the European Chapter of the Association for Computational Linguistics*, pp. 211--218.

Baldwin, T. and Kim, S. N. (2010). Multiword expressions. In Indurkhya, N. and Damerau, F. J. (eds.), *Handbook of Natural Language Processing*, 2nd edn, pp. 267--292. CRC Press.

Bar-Hillel, Y. (1953). A quasi-arithmetical notation for syntactic description. *Language*, 29(1), 47--58.

Becker, J. D. (1975). The phrasal lexicon. In *Proceedings of the 1975 Workshop on Theoretical Issues in Natural Language Processing*, pp. 60--63.

Becker, T., Rambow, O., and Niv, M. (1992). The derivational generative power of formal systems, or, scrambling is beyond LCFRS. Technical Report IRCS-92-38, University of Pennsylvania.

Belinkov, Y. and Glass, J. (2019). Analysis methods in neural language processing: A survey. *Transactions of the Association for Computational Linguistics*, 7, 49--72.

Bos, J. (1996). Predicate logic unplugged. In *Proceedings of the 10th Amsterdam Colloquium*, pp. 133--142.

Brady, E. (2013). *Type-Driven Development with Idris*. Manning Publications.

Bresnan, J. (2001). *Lexical-Functional Syntax*. Blackwell.

Bresnan, J. (2007). Is syntactic knowledge probabilistic? Experiments with the English dative alternation. In Featherston, S. and Sternefeld, W. (eds.), *Roots: Linguistics in Search of Its Evidential Base*, pp. 75--96. Mouton de Gruyter.

Burroni, A. (1993). Higher-dimensional word problems with applications to equational logic. *Theoretical Computer Science*, 115(1), 43--62.

Bybee, J. (2006). From usage to grammar: The mind's response to repetition. *Language*, 82(4), 711--733.

Bybee, J. (2010). *Language, Usage and Cognition*. Cambridge University Press.

Cardelli, L. and Wegner, P. (1985). On understanding types, data abstraction, and polymorphism. *Computing Surveys*, 17(4), 471--523.

Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory*, 2(3), 113--124.

Chomsky, N. (1957). *Syntactic Structures*. Mouton, The Hague.

Chomsky, N. (1959). On certain formal properties of grammars. *Information and Control*, 2(2), 137--167.

Chomsky, N. (1962). Context-free grammars and pushdown storage. *MIT Research Laboratory of Electronics Quarterly Progress Report*, 65, 187--194.

Chomsky, N. (1965). *Aspects of the Theory of Syntax*. MIT Press, Cambridge, MA.

Chomsky, N. (1995). *The Minimalist Program*. MIT Press, Cambridge, MA.

Chomsky, N. (2000). Minimalist inquiries: The framework. In Martin, R., Michaels, D., and Uriagereka, J. (eds.), *Step by Step: Essays on Minimalist Syntax in Honor of Howard Lasnik*, pp. 89--155. MIT Press.

Chomsky, N. (2008). On phases. In Freidin, R., Otero, C. P., and Zubizarreta, M. L. (eds.), *Foundational Issues in Linguistic Theory*, pp. 133--166. MIT Press.

Clark, K., Khandelwal, U., Levy, O., and Manning, C. D. (2019). What does BERT look at? An analysis of BERT's attention. In *Proceedings of the 2019 ACL Workshop BlackboxNLP*, pp. 276--286.

Clark, S. and Curran, J. R. (2007). Wide-coverage efficient statistical parsing with CCG and log-linear models. *Computational Linguistics*, 33(4), 493--552.

Clark, S., Curran, J. R., and Osborne, M. (2018). Statistical parsing. In Clark, A., Fox, C., and Lappin, S. (eds.), *The Handbook of Computational Linguistics and Natural Language Processing*, 2nd edn. Blackwell.

Coecke, B., Sadrzadeh, M., and Clark, S. (2010). Mathematical foundations for a compositional distributional model of meaning. *Linguistic Analysis*, 36(1--4), 345--384.

Collins, C. (2002). Eliminating labels. In Epstein, S. D. and Seely, T. D. (eds.), *Derivation and Explanation in the Minimalist Program*, pp. 42--64. Blackwell.

Cooper, R. (2005). Records and record types in semantic theory. *Journal of Logic and Computation*, 15(2), 99--112.

Copestake, A. (2002). *Implementing Typed Feature Structure Grammars*. CSLI Publications.

Coquand, T. and Huet, G. (1988). The Calculus of Constructions. *Information and Computation*, 76(2--3), 95--120.

Culy, C. (1985). The complexity of the vocabulary of Bambara. *Linguistics and Philosophy*, 8(3), 345--351.

Curry, H. B. and Feys, R. (1958). *Combinatory Logic*, Vol. I. North-Holland.

Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of NAACL-HLT 2019*, pp. 4171--4186.

Dunfield, J. and Krishnaswami, N. R. (2021). Bidirectional typing. *ACM Computing Surveys*, 54(5), 1--38.

Elhage, N., Nanda, N., Olsson, C., et al. (2021). A mathematical framework for transformer circuits. *Transformer Circuits Thread*.

Erman, B. and Warren, B. (2000). The idiom principle and the open choice principle. *Text*, 20(1), 29--62.

Evey, R. J. (1963). *Application of pushdown store machines*. Proceedings of the Fall Joint Computer Conference, pp. 215--227.

Freeman, T. and Pfenning, F. (1991). Refinement types for ML. In *Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation*, pp. 268--277.

Gazdar, G. (1988). Applicability of indexed grammars to natural languages. In Reyle, U. and Rohrer, C. (eds.), *Natural Language Parsing and Linguistic Theories*, pp. 69--94. Reidel.

Girard, J.-Y. (1972). *Interpretation fonctionnelle et elimination des coupures de l'arithmetique d'ordre superieur*. PhD thesis, Universite Paris VII.

Girard, J.-Y. (1987). Linear logic. *Theoretical Computer Science*, 50(1), 1--101.

Goldberg, A. E. (1995). *Constructions: A Construction Grammar Approach to Argument Structure*. University of Chicago Press.

Goldberg, A. E. (2006). *Constructions at Work: The Nature of Generalization in Language*. Oxford University Press.

Goldberg, Y. (2019). Assessing BERT's syntactic abilities. arXiv preprint arXiv:1901.05287.

Grefenstette, E. and Sadrzadeh, M. (2011). Experimental support for a categorical compositional distributional model of meaning. In *Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing*, pp. 1394--1404.

Groenendijk, J. and Stokhof, M. (1991). Dynamic predicate logic. *Linguistics and Philosophy*, 14(1), 39--100.

Hale, K. (1983). Warlpiri and the grammar of non-configurational languages. *Natural Language and Linguistic Theory*, 1(1), 5--47.

Hewitt, J. and Liang, P. (2019). Designing and interpreting probes with control tasks. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing*, pp. 2733--2743.

Hewitt, J. and Manning, C. D. (2019). A structural probe for finding syntax in word representations. In *Proceedings of NAACL-HLT 2019*, pp. 4129--4138.

Hodas, J. S. and Miller, D. (1994). Logic programming in a fragment of intuitionistic linear logic. *Information and Computation*, 110(2), 327--365.

Hopcroft, J. E. and Ullman, J. D. (1979). *Introduction to Automata Theory, Languages, and Computation*. Addison-Wesley.

Howard, W. A. (1980). The formulae-as-types notion of construction. In Seldin, J. P. and Hindley, J. R. (eds.), *To H. B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism*, pp. 479--490. Academic Press. (Manuscript circulated 1969.)

Jawahar, G., Sagot, B., and Seddah, D. (2019). What does BERT learn about the structure of language? In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pp. 3651--3657.

Joshi, A. K. (1985). Tree adjoining grammars: How much context-sensitivity is required to provide reasonable structural descriptions? In Dowty, D. R., Karttunen, L., and Zwicky, A. M. (eds.), *Natural Language Parsing*, pp. 206--250. Cambridge University Press.

Joshi, A. K., Levy, L. S., and Takahashi, M. (1975). Tree adjunct grammars. *Journal of Computer and System Sciences*, 10(1), 136--163.

Joshi, A. K., Vijay-Shanker, K., and Weir, D. (1991). The convergence of mildly context-sensitive grammar formalisms. In Sells, P., Shieber, S. M., and Wasow, T. (eds.), *Foundational Issues in Natural Language Processing*, pp. 31--81. MIT Press.

Kahney, H. (1983). What do novice programmers know about recursion? In *Proceedings of CHI '83*, pp. 235--239. ACM.

Kaplan, R. and Kay, M. (1994). Regular models of phonological rule systems. *Computational Linguistics*, 20(3), 331--378.

Kartsaklis, D., Fan, I., Yeung, R., Pearson, A., Lorenz, R., Toumi, A., de Felice, G., Meichanetzidis, K., Clark, S., and Coecke, B. (2021). lambeq: An efficient high-level Python library for quantum NLP. arXiv preprint arXiv:2110.04236.

Kartsaklis, D., Sadrzadeh, M., and Pulman, S. (2012). A unified sentence space for categorical distributional-compositional semantics: Theory and experiments. In *Proceedings of COLING 2012*, pp. 549--558.

Katsumata, S. (2014). Parametric effect monads and semantics of effect systems. In *Proceedings of the 41st ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, pp. 633--645.

Kleene, S. C. (1956). Representation of events in nerve nets and finite automata. In Shannon, C. E. and McCarthy, J. (eds.), *Automata Studies*, pp. 3--42. Princeton University Press.

Koskenniemi, K. (1983). *Two-Level Morphology: A General Computational Model for Word-Form Recognition and Production*. University of Helsinki.

Kuroda, S.-Y. (1964). Classes of languages and linear-bounded automata. *Information and Control*, 7(2), 207--223.

Lambek, J. (1958). The mathematics of sentence structure. *American Mathematical Monthly*, 65(3), 154--170.

Lambek, J. (1972). Deductive systems and categories III: Cartesian closed categories, intuitionist propositional calculus, and combinatory logic. In Lawvere, F. W. (ed.), *Toposes, Algebraic Geometry and Logic*, Lecture Notes in Mathematics 274, pp. 57--82. Springer.

Lambek, J. (1980). From lambda calculus to Cartesian closed categories. In Seldin, J. P. and Hindley, J. R. (eds.), *To H. B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism*, pp. 375--402. Academic Press.

Lambek, J. (1999). Type grammar revisited. In Lecomte, A., Lamarche, F., and Perrier, G. (eds.), *Logical Aspects of Computational Linguistics*, Lecture Notes in Computer Science 1582, pp. 1--27. Springer.

Lambek, J. (2008). *From Word to Sentence: A Computational Algebraic Approach to Grammar*. Polimetrica.

Langacker, R. W. (1987). *Foundations of Cognitive Grammar*, Vol. I: *Theoretical Prerequisites*. Stanford University Press.

Langacker, R. W. (2008). *Cognitive Grammar: A Basic Introduction*. Oxford University Press.

Lau, J. H., Clark, A., and Lappin, S. (2017). Grammaticality, acceptability, and probability: A probabilistic view of linguistic knowledge. *Cognitive Science*, 41(5), 1202--1241.

Lecomte, A. (2011). *Meaning, Logic and Ludics*. Imperial College Press.

Lewis, M. and Steedman, M. (2014). A* CCG parsing with a supertag-factored model. In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing*, pp. 990--1000.

Liang, P. (2013). Lambda dependency-based compositional semantics. arXiv preprint arXiv:1309.4408.

Lillo-Martin, D. and Sandler, W. (2006). Sign language and linguistic universals. Cambridge University Press.

Lorenz, R., Pearson, A., Meichanetzidis, K., Kartsaklis, D., and Coecke, B. (2023). QNLP in practice: Running compositional models of meaning on a quantum computer. *Journal of Artificial Intelligence Research*, 76, 1305--1342.

Manning, C. D., Clark, K., Hewitt, J., Khandelwal, U., and Levy, O. (2020). Emergent linguistic structure in artificial neural networks trained by self-supervision. *Proceedings of the National Academy of Sciences*, 117(48), 30046--30054.

Martin-Lof, P. (1975). An intuitionistic theory of types: Predicative part. In Rose, H. E. and Shepherdson, J. C. (eds.), *Logic Colloquium '73*, pp. 73--118. North-Holland.

Martin-Lof, P. (1984). *Intuitionistic Type Theory*. Bibliopolis, Naples.

Matuszek, C., Herbst, E., Zettlemoyer, L., and Fox, D. (2012). Learning to parse natural language commands to a robot control system. In *Proceedings of the 13th International Symposium on Experimental Robotics*, pp. 403--415.

McBride, C. (2016). I got plenty o' nuttin'. In Lindley, S., McBride, C., Trinder, P., and Sannella, D. (eds.), *A List of Successes That Can Change the World*, Lecture Notes in Computer Science 9600, pp. 207--233. Springer.

Meichanetzidis, K., Toumi, A., de Felice, G., and Coecke, B. (2021). Grammar-aware question-answering on quantum computers. arXiv preprint arXiv:2012.03756.

Mellies, P.-A. (2006). Functorial boxes in string diagrams. In *Computer Science Logic*, Lecture Notes in Computer Science 4207, pp. 1--30. Springer.

Michaelis, J. and Kracht, M. (1997). Semilinearity as a syntactic invariant. In Retoré, C. (ed.), *Logical Aspects of Computational Linguistics*, Lecture Notes in Computer Science 1328, pp. 329--345. Springer.

Montague, R. (1970a). Universal grammar. *Theoria*, 36(3), 373--398.

Montague, R. (1970b). English as a formal language. In Visentini, B. (ed.), *Linguaggi nella Societa e nella Tecnica*, pp. 189--224. Edizioni di Comunita.

Montague, R. (1973). The proper treatment of quantification in ordinary English. In Hintikka, K. J. J., Moravcsik, J. M. E., and Suppes, P. (eds.), *Approaches to Natural Language*, pp. 221--242. Reidel.

Moortgat, M. (1997). Categorial type logics. In van Benthem, J. and ter Meulen, A. (eds.), *Handbook of Logic and Language*, pp. 93--177. Elsevier/MIT Press.

Moortgat, M. (2011). Typelogical grammar. In *The Stanford Encyclopedia of Philosophy*. Metaphysics Research Lab, Stanford University.

Morrill, G., Valentin, O., and Fadda, M. (2011). The Displacement calculus. *Journal of Logic, Language and Information*, 20(1), 1--48.

Myhill, J. (1957). Finite automata and the representation of events. *WADD Technical Report*, 57--624.

Nanda, N., Chan, L., Lieberum, T., Smith, J., and Steinhardt, J. (2023). Progress measures for grokking via mechanistic interpretability. In *Proceedings of the International Conference on Learning Representations*.

Naur, P. (ed.) (1960). Report on the algorithmic language ALGOL 60. *Communications of the ACM*, 3(5), 299--314.

Novak, V. (2005). On fuzzy type theory. *Fuzzy Sets and Systems*, 149(2), 235--273.

Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., and Carter, S. (2020). Zoom in: An introduction to circuits. *Distill*, 5(3), e00024.001.

Parnin, C., Bird, C., and Murphy-Hill, E. (2013). Adoption and use of Java generics. *Empirical Software Engineering*, 18(6), 1047--1089.

Pentus, M. (1993). Lambek grammars are context-free. In *Proceedings of the 8th Annual IEEE Symposium on Logic in Computer Science*, pp. 429--433.

Pentus, M. (1997). Product-free Lambek calculus and context-free grammars. *Journal of Symbolic Logic*, 62(2), 648--660.

Pimentel, T., Valvoda, J., Hall Maudslay, R., Zmigrod, R., Williams, A., and Cotterell, R. (2020). Information-theoretic probing for linguistic structure. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, pp. 4609--4622.

Plotkin, G. D. and Power, J. (2003). Algebraic operations and generic effects. *Applied Categorical Structures*, 11(1--2), 69--94.

Plotkin, G. D. and Pretnar, M. (2013). Handling algebraic effects. *Logical Methods in Computer Science*, 9(4:23), 1--36.

Pollard, C. (1984). *Generalized Phrase Structure Grammars, Head Grammars, and Natural Language*. PhD thesis, Stanford University.

Prince, A. and Smolensky, P. (1993/2004). *Optimality Theory: Constraint Interaction in Generative Grammar*. Blackwell. (Original manuscript 1993; published 2004.)

Pullum, G. K. and Gazdar, G. (1982). Natural languages and context-free languages. *Linguistics and Philosophy*, 4(4), 471--504.

Rabin, M. O. and Scott, D. (1959). Finite automata and their decision problems. *IBM Journal of Research and Development*, 3(2), 114--125.

Radford, A., Narasimhan, K., Salimans, T., and Sutskever, I. (2018). Improving language understanding by generative pre-training. OpenAI Technical Report.

Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I. (2019). Language models are unsupervised multitask learners. OpenAI Technical Report.

Ranta, A. (1994). *Type-Theoretical Grammar*. Oxford University Press.

Reynolds, J. C. (1974). Towards a theory of type structure. In *Colloque sur la Programmation*, Lecture Notes in Computer Science 19, pp. 408--425. Springer.

Sandler, W. and Lillo-Martin, D. (2006). *Sign Language and Linguistic Universals*. Cambridge University Press.

Shieber, S. M. (1985). Evidence against the context-freeness of natural language. *Linguistics and Philosophy*, 8(3), 333--343.

Sprouse, J., Schutze, C. T., and Almeida, D. (2013). A comparison of informal and formal acceptability judgments using a random sample from *Linguistic Inquiry* 2001--2010. *Lingua*, 134, 219--248.

Stabler, E. (1997). Derivational minimalism. In Retoré, C. (ed.), *Logical Aspects of Computational Linguistics*, Lecture Notes in Computer Science 1328, pp. 68--95. Springer.

Stabler, E. (2011). Computational perspectives on minimalism. In Boeckx, C. (ed.), *The Oxford Handbook of Linguistic Minimalism*, pp. 617--641. Oxford University Press.

Stabler, E. (2013). Two models of minimalist, incremental syntactic analysis. *Topics in Cognitive Science*, 5(3), 611--633.

Steedman, M. (1987). Combinatory grammars and parasitic gaps. *Natural Language and Linguistic Theory*, 5(3), 403--439.

Steedman, M. (2000). *The Syntactic Process*. MIT Press, Cambridge, MA.

Tenney, I., Das, D., and Pavlick, E. (2019). BERT rediscovers the classical NLP pipeline. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, pp. 4593--4601.

Tomasello, M. (2003). *Constructing a Language: A Usage-Based Theory of Language Acquisition*. Harvard University Press.

Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society*, 2(42), 230--265.

Univalent Foundations Program. (2013). *Homotopy Type Theory: Univalent Foundations of Mathematics*. Institute for Advanced Study.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems 30*, pp. 5998--6008.

Veldhuizen, T. L. (2003). C++ templates are Turing complete. Unpublished manuscript.

Vijay-Shanker, K. (1987). *A Study of Tree Adjoining Grammars*. PhD thesis, University of Pennsylvania.

Vijay-Shanker, K. and Weir, D. (1994). The equivalence of four extensions of context-free grammars. *Mathematical Systems Theory*, 27(6), 511--546.

Wells, J. B. (1999). Typability and type checking in System F are equivalent and undecidable. *Annals of Pure and Applied Logic*, 98(1--3), 111--156.

Wray, A. (2002). *Formulaic Language and the Lexicon*. Cambridge University Press.

Carpenter, B. (1997). *Type-Logical Semantics*. MIT Press, Cambridge, MA.

Moortgat, M. (2011). Typelogical grammar. In *The Stanford Encyclopedia of Philosophy*. Metaphysics Research Lab, Stanford University.
