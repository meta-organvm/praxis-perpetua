---
sgo_id: SGO-2026-RP-005
title: "Actants in the Loop"
tier: Thesis
status: LOCAL (second draft -- TRP amendments incorporated)
target_venues: [Social Studies of Science, Science Technology & Human Values, arXiv cs.AI]
dependencies: [RP-03]
date: 2026-03-21
revision_date: 2026-03-20
revision_notes: |
  v2 amendments per TRP-BATCH-002 review (2/3 advance with amendments):
  - Added new Section 6.6: "Guardrails -- Where Flat Ontology Must Yield to Normative
    Hierarchy" addressing AI safety concerns about the symmetry principle
  - Strengthened Section 7 design implications with concrete design patterns
    (pattern language format with context/problem/solution/consequences)
  - Explicit descriptive/normative distinction for symmetry principle throughout
---

# Actants in the Loop: Actor-Network Theory as Framework for Human-AI Collaborative Systems

**Studium Generale ORGANVM -- Research Paper RP-05**

---

## Abstract

Contemporary discourse on human-AI collaboration is constrained by an impoverished set of ontological frames: the AI system is characterized as a *tool* to be wielded, an *assistant* to be directed, or an *agent* to be aligned. Each frame imports unexamined assumptions about the distribution of agency, the locus of intention, and the nature of the human-machine boundary. This paper argues that actor-network theory (ANT), as developed by Bruno Latour, Michel Callon, and John Law within the tradition of science and technology studies, provides a more adequate framework for understanding human-AI collaborative systems. By applying ANT's core concepts -- the principle of generalized symmetry, Callon's four moments of translation, obligatory passage points, blackboxing, and the intermediary/mediator distinction -- to contemporary AI-mediated workflows, we demonstrate that ANT dissolves the tool/agent binary, reframes alignment as an ongoing problem of translation rather than value installation, and provides precise vocabulary for analyzing the distributed, heterogeneous, and continuously negotiated character of human-AI collaboration. At the same time, AI systems intensify ANT's most controversial commitments: the symmetry principle, designed to resist anthropocentrism in describing scallops and door-closers, becomes both literally applicable and philosophically problematic when the nonhuman actant generates natural language and proposes plans. We extend the analysis through feminist STS (Haraway's situated knowledges, Barad's agential realism, Suchman's situated actions) and object-oriented ontology (Harman) to address the limitations of classical ANT, particularly its treatment of constitutive opacity and political accountability. The paper concludes with design implications for human-AI systems: designing for translation rather than control, making mediators visible, and reconceiving governance as the construction of obligatory passage points in sociotechnical networks.

**Keywords:** actor-network theory, human-AI collaboration, science and technology studies, generalized symmetry, translation, blackboxing, alignment, sociomateriality

---

## 1. Introduction

The rapid proliferation of AI systems capable of generating natural language, writing code, and executing multi-step plans has produced a crisis of ontological framing. How should the relationship between human operators and AI systems be understood? The question is not merely philosophical; the frame adopted shapes system design, governance structures, liability attributions, and the lived experience of collaboration.

Three dominant frames currently structure both popular and technical discourse. The *tool frame* positions AI as an instrument under human control -- a sophisticated calculator or search engine that amplifies human capability without exercising agency of its own. The *assistant frame* introduces a degree of autonomy: the AI is a junior colleague who can be delegated tasks but who ultimately serves human goals. The *agent frame* attributes genuine autonomy to the AI system, raising questions of alignment, safety, and control. Each frame imports assumptions that constrain understanding. The tool frame denies the AI's capacity to surprise, transform, and redirect the very tasks it is given. The assistant frame naturalizes a hierarchical relationship that may not reflect the actual dynamics of collaboration. The agent frame risks reifying AI autonomy in ways that obscure the distributed, infrastructural, and deeply social character of AI-mediated work.

This paper proposes that actor-network theory (ANT), the approach to social theory developed by Bruno Latour, Michel Callon, Madeleine Akrich, and John Law at the Centre de Sociologie de l'Innovation (Ecole des Mines de Paris) beginning in the 1980s, provides a more adequate ontological framework for understanding human-AI collaborative systems. ANT is a theoretical and methodological approach in which "everything in the social and natural worlds exists in constantly shifting networks of relationships" and "nothing exists outside those relationships" (Latour, 2005). Its defining commitment -- the principle of generalized symmetry, which requires that human and nonhuman entities be described using the same analytical vocabulary -- was developed to resist the sociological habit of explaining human behavior through "social forces" while treating nonhuman entities as mere background conditions. When applied to AI systems, this commitment becomes both productively illuminating and philosophically fraught.

The paper addresses three research questions:

**RQ1 (Symmetry):** Does ANT's principle of generalized symmetry -- requiring the same analytical vocabulary for human and nonhuman actants -- constitute a productive framework for understanding human-AI collaboration, or does it obscure morally relevant distinctions between human agency and computational process?

**RQ2 (Constitutive Opacity):** How should ANT's concept of translation be modified to account for systems whose internal complexity is *constitutively* opaque (AI models whose designers cannot fully explain their behavior), as opposed to merely *practically* opaque (black boxes that could in principle be opened)?

**RQ3 (Alignment as Translation):** Can "alignment" be productively reframed as a translation problem -- ongoing network stabilization -- rather than a value-installation problem -- instilling fixed values in an AI object?

The contribution of this paper is threefold. First, it provides a systematic mapping of ANT concepts to human-AI system concepts, demonstrating that ANT's vocabulary of actants, translation, enrollment, obligatory passage points, immutable mobiles, boundary objects, blackboxing, and the intermediary/mediator distinction applies with considerable precision to contemporary AI-mediated workflows. Second, it identifies the points at which AI systems intensify or destabilize ANT's commitments, particularly the symmetry principle and the concept of blackboxing. Third, it derives design implications from the ANT framework: principles for building human-AI systems that are designed for translation rather than control, that make mediators visible rather than hiding them as intermediaries, and that treat governance as the construction and maintenance of obligatory passage points in sociotechnical networks.

The paper proceeds as follows. Section 2 presents the core concepts of actor-network theory. Section 3 situates ANT within the broader tradition of science and technology studies and its feminist extensions. Section 4 maps ANT concepts to human-AI systems through an extended case study. Section 5 examines how AI intensifies ANT's symmetry problem and introduces the concept of constitutive opacity. Section 6 addresses critical perspectives and limitations. Section 7 develops design implications. Section 8 discusses the findings, and Section 9 concludes.

---

## 2. Actor-Network Theory: Core Concepts

Actor-network theory is not, despite its name, a theory *of* anything. Latour himself insisted that "it is a method, and mostly a negative one at that: it says nothing about the shape of what it allows to be described" (Latour, 2005, p. 142). It emerged in the 1980s from empirical studies of scientific practice -- most famously Latour and Woolgar's ethnography of the Salk Institute (*Laboratory Life*, 1979) and Callon's study of scallop fisheries in St. Brieuc Bay (1986) -- and crystallized into a distinctive approach that is most precisely characterized as "material-semiotic": it maps relations that are simultaneously material (between things) and semiotic (between concepts). This section presents ANT's core conceptual apparatus, which will be mapped to human-AI systems in Section 4.

### 2.1 The Symmetry Principle

ANT's most provocative and most contested commitment is the principle of generalized symmetry: human and nonhuman entities must be described using the same analytical vocabulary. The analyst must not switch explanatory registers when moving from human motivations to technical constraints. One cannot say that the scientist "had a theory" while the scallop merely "behaved according to its nature." Both must be described in terms of what they *do* within the network -- as performing translations, resisting enrollments, stabilizing or destabilizing associations.

The symmetry principle has its intellectual roots in the Strong Programme of the Edinburgh School (Bloor, 1976), which required that sociologists of science explain both true and false beliefs using the same kinds of causes -- the truth of a belief should not be treated as its own explanation. Callon and Latour radicalized this by extending symmetry from beliefs to entities: not just true and false knowledge, but human and nonhuman participants must be treated symmetrically. This was always a methodological prescription, not a metaphysical claim. Latour did not argue that scallops are "the same as" scientists. He argued that the analyst must not decide in advance which entities are capable of acting and which are merely acted upon. The question of who or what acts is an empirical matter to be discovered through careful tracing of associations, not a philosophical matter to be settled by fiat.

The symmetry principle is operationalized through the concept of the *actant*, borrowed from A.J. Greimas's narrative semiotics. An actant is anything that modifies a state of affairs, that makes a difference. It need not be human, need not have intentions, need not be conscious. A speed bump is an actant: it modifies the behavior of drivers. A laboratory instrument is an actant: it transforms raw materials into inscriptions. A computer virus is an actant: it redirects network traffic and reshapes organizational practices. The analytical question is never "what *is* this entity?" but always "what does this entity *do*?" -- what associations does it enter into, what translations does it perform, what differences does it make?

### 2.2 Translation: Callon's Four Moments

Translation is the central process concept in ANT. In Callon's canonical formulation (1986), developed through his study of marine biologists attempting to cultivate scallops in St. Brieuc Bay, translation is "the mechanism by which the social and natural worlds progressively take form" (Callon, 1986, p. 224). It encompasses "all the negotiations, intrigues, calculations, acts of persuasion and violence, thanks to which an actor or force takes, or causes to be conferred on itself, authority to speak or act on behalf of another actor or force" (Callon and Latour, 1981, p. 279).

Translation proceeds through four analytically distinguishable moments:

**Problematization.** An actor defines a problem and positions other actors in relation to it, making itself *indispensable* to the solution. The marine biologists at St. Brieuc Bay framed the decline of scallop populations as a scientific problem requiring their particular expertise. Problematization establishes an *obligatory passage point* (OPP): a bottleneck through which all other actors must pass to achieve their own goals. The marine biologists positioned themselves as the OPP -- fishermen who wanted sustainable harvests and scallops that "wanted" to reproduce both had to pass through the scientists' research program.

**Interessement.** The actor deploying the problematization uses "devices" to lock other actors into the roles defined during problematization. The marine biologists deployed physical collectors (mesh bags anchored to the sea floor) to interest the scallop larvae in attaching. They negotiated agreements with fishermen to refrain from harvesting during the study period. Interessement is literally "inter-esse" -- being placed between. The interessement device is placed between an actor and the other entities that might define that actor differently. The mesh collector placed between the scallop larvae and the open sea redefines the larvae's trajectory.

**Enrollment.** If interessement succeeds, actors accept the roles assigned to them. The scallop larvae attach to the collectors. The fishermen observe the moratorium. Enrollment is not simply acquiescence; it involves the actors' active performance of their assigned roles. It is always precarious -- the scallops may detach, the fishermen may poach. Enrollment requires ongoing work.

**Mobilization.** The actor who initiated the translation claims to speak on behalf of the enrolled entities. The marine biologists present their findings at conferences, claiming to represent the scallops, the fishermen, and the bay. Mobilization raises the question of representativeness: do the few scallop larvae that attached to collectors represent the scallop population as a whole? Do the cooperating fishermen represent the fishing community? Translation can fail at any moment, but mobilization failures are the most consequential because they reveal that the network's spokesperson does not, in fact, speak for the entities it claims to represent.

### 2.3 Obligatory Passage Points

An obligatory passage point is a bottleneck that all actors in a network must traverse. It is a position in the network that mediates all interactions between actors and defines the action program. A strong OPP controls resources and accumulates credit for the network's successes; a weak OPP can be bypassed, routed around, or rendered irrelevant. Callon's marine biologists positioned themselves as an OPP: both the scallops' reproductive success and the fishermen's economic livelihood were made to depend on the scientists' research. OPPs are sites of power, but in ANT's vocabulary this power is not imposed from above; it is achieved through successful translation.

The concept of the OPP reveals that networks are not egalitarian even when they are flat. Flatness in ANT means the refusal to privilege any *level* of analysis (micro vs. macro, individual vs. structural); it does not mean the refusal to recognize asymmetries of power *within* a network. Some actants are more connected, more indispensable, more capable of enrolling others than others. The OPP is the analytical tool for identifying these positions of structural power.

### 2.4 Immutable Mobiles and Boundary Objects

Latour's concept of the *immutable mobile* (Latour, 1987) captures a category of artifacts that are simultaneously transportable across contexts (mobile) and resistant to transformation during transport (immutable). Scientific papers, maps, charts, legal contracts, and standardized metrics are immutable mobiles. They enable "action at a distance" -- the ability to coordinate behavior across spatial and temporal separations. A laboratory notebook that travels from the bench to the conference podium, maintaining its inscriptions intact, is an immutable mobile that allows the scientist to mobilize distant allies.

The concept is complemented by Star and Griesemer's (1989) notion of the *boundary object*: an artifact that is "plastic enough to adapt to local needs and constraints of the several parties employing them, yet robust enough to maintain a common identity across sites." Boundary objects differ from immutable mobiles in their flexibility -- they are not rigid inscriptions but adaptable interfaces that different communities use in different ways while maintaining enough shared structure to enable collaboration. A map can be a boundary object: the ecologist reads it for habitat data, the developer reads it for buildable parcels, the hiker reads it for trail routes. The map is the same artifact, but it participates in different networks with different meanings.

The distinction between immutable mobiles and boundary objects marks a spectrum of rigidity in the artifacts that hold networks together. Some artifacts must remain unchanged to function (a protocol specification, a cryptographic certificate); others must be interpretively flexible to serve multiple communities (a shared document, a design pattern, a conceptual framework).

### 2.5 Blackboxing and Punctualization

Blackboxing, in Latour's formulation, is "the way scientific and technical work is made invisible by its own success" (Latour, 1999, p. 304). When a machine runs efficiently, one need attend only to its inputs and outputs; the internal complexity is hidden. A functioning automobile is a single actant -- "the car." When its engine fails, the car is *depunctualized*: it ceases to be a single actor and is revealed as a network of engine, transmission, fuel system, electrical system, and so forth. Punctualization is the process by which a network comes to appear as, and to function as, a single point in a larger network. It is the network-theoretic equivalent of abstraction or encapsulation in computing.

Blackboxing and punctualization are not merely descriptive; they are political. To blackbox a process is to render the labor that sustains it invisible. The "working car" hides the labor of engineers, assembly workers, mechanics, and road builders. The "working scientific fact" hides the labor of laboratory technicians, instrument manufacturers, and graduate students. The question of *who benefits from blackboxing* is central to the political dimensions that ANT's critics (see Section 6) have argued it neglects.

### 2.6 Intermediaries vs. Mediators

Latour (2005) draws a consequential distinction between intermediaries and mediators. An intermediary "transports meaning or force without transformation: defining its inputs is enough to define its outputs" (p. 39). A mediator "transforms, translates, distorts, and modifies the meaning or the elements it is supposed to carry" (p. 39). The distinction is empirical, not definitional: the same entity can function as an intermediary in one context and a mediator in another. A functioning postal system is an intermediary -- it transports letters without transforming them. A postal system during a strike is a mediator -- it transforms the act of sending a letter into a political statement.

The distinction matters because mediators cannot be safely ignored in analysis. If an entity is an intermediary, one can study the network by attending only to its inputs and outputs. If it is a mediator, one must study the entity itself -- its internal dynamics, its transformative effects, its capacity to surprise. The analytical question for any entity in a network is: does it transport or does it transform? And the answer is always provisional, always subject to revision as the network shifts.

---

## 3. The STS Context

### 3.1 Science and Technology Studies

Actor-network theory emerged within the broader interdisciplinary field of science and technology studies (STS), which examines "the creation, development, and consequences of science and technology in their historical, cultural, and social contexts" (Sismondo, 2010). STS itself crystallized in the 1970s and 1980s from converging streams: the sociology of scientific knowledge (SSK) developed at the Universities of Edinburgh and Bath, the history of technology associated with the Society for the History of Technology (SHOT), and the philosophy of science in its post-Kuhnian phase. What unified these streams was the rejection of two opposed but equally reductive positions: the view that scientific and technological knowledge is simply determined by the natural world it describes (naive realism), and the view that it is simply determined by the social interests of those who produce it (strong social constructivism).

ANT's particular contribution to STS was to extend this rejection of determinism from knowledge to *entities*. Where SSK had argued that the *content* of scientific knowledge is socially shaped, ANT argued that the *actors* involved in knowledge production -- human and nonhuman alike -- are constituted by the networks in which they participate. This move placed ANT at the intersection of sociology, philosophy, and the study of material culture, and it generated both ANT's distinctive insights and its most persistent controversies.

### 3.2 Social Construction of Technology (SCOT)

The social construction of technology (SCOT) framework, developed by Wiebe Bijker and Trevor Pinch (1984), is ANT's sibling within STS. SCOT argues that "technology does not determine human action; rather, human action shapes technology" (Bijker and Pinch, 1984). Its central concept is *interpretive flexibility*: the same technological artifact means different things to different "relevant social groups." The bicycle, in Bijker's canonical study, was simultaneously a dangerous high-wheeler (to safety advocates), a sporting vehicle (to young men of means), and a practical transport device (to commuters). These different meanings led to different designs, and the eventual stabilization of the "safety bicycle" was a social achievement, not a purely technical one.

SCOT and ANT share the rejection of technological determinism, but they differ on a crucial point. SCOT privileges the social side: human groups shape technology. ANT insists on symmetry: humans and technologies co-shape one another. For the study of AI, this difference is significant. A SCOT analysis of a large language model would focus on how different social groups (researchers, developers, users, regulators, critics) construct different meanings for the technology. An ANT analysis would additionally ask how the technology itself participates in constructing those groups -- how the model's capabilities, limitations, and failure modes reshape the communities that form around it.

### 3.3 From Latour to After-ANT: Critiques and Extensions

ANT's development has not been linear. By the late 1990s, several scholars closely associated with ANT -- including John Law and Annemarie Mol -- began articulating positions that retained ANT's relational commitments while modifying its vocabulary and methods. Law's work on "mess" (2004) argued that ANT's network metaphor, despite its ambitions, tended to produce overly clean and coherent accounts of sociotechnical reality. Real networks, Law argued, are messy, multiple, and fractional -- they resist the neat tracing of associations that ANT's method demands.

Mol's *The Body Multiple* (2002) introduced the concept of *ontological politics*: the idea that different practices enact different versions of reality. A disease is not a single entity that is viewed from different perspectives; it is *multiple* -- it is one thing in the clinic, another in the laboratory, another in the patient's daily life. These are not different perspectives on the same object but different objects that are partially connected. Mol's work challenges ANT's implicit assumption that the network, once traced, reveals a single coherent reality, suggesting instead that reality is always enacted in multiple, partially overlapping versions.

These "after-ANT" developments are relevant to the study of human-AI systems because AI systems are themselves multiple. A large language model is one thing in the training laboratory, another in the user's creative writing session, another in the enterprise compliance review, another in the regulatory hearing. These are not merely different "uses" of the same artifact; they are different enactments that produce different ontological realities, including different versions of what "the AI" is and does.

### 3.4 Feminist STS: Haraway, Barad, Suchman

Feminist contributions to STS have been among the most generative critiques and extensions of ANT. Three figures are particularly important for the study of human-AI systems.

**Donna Haraway** is an American scholar in science and technology studies and feminist theory, known for her work at the intersection of information technology, feminist theory, and ecofeminism. Her "Cyborg Manifesto" (1985) proposed the cyborg -- a hybrid of organism and machine -- as a political figure that refuses the boundaries between human and animal, organism and machine, physical and non-physical. "The cyborg does not dream of community on the model of the organic family," Haraway wrote; it represents "a kind of disassembled and reassembled, postmodern collective and personal self" (Haraway, 1991, p. 163). The cyborg anticipated by four decades the dissolution of human-machine boundaries that contemporary AI makes literal. Equally important is Haraway's concept of *situated knowledges* (1988): the insistence that all knowledge is produced from a particular position, and that the fantasy of an objective "view from nowhere" is not merely unattainable but politically dangerous. Situated knowledges demand that the analyst ask: from whose position is this knowledge produced? Whose interests does it serve? What does it render invisible?

Applied to ANT, Haraway's situated knowledges complicate the symmetry principle. Symmetry demands that human and nonhuman actants be described in the same terms. Situated knowledges demand that the analyst acknowledge the *differential* positionality of different actants -- the fact that some positions are more powerful, more visible, more consequential than others. The tension between symmetry and situatedness is not a contradiction to be resolved but a productive tension to be maintained: one must describe the network symmetrically *and* attend to the asymmetries of power, visibility, and consequence within it.

**Karen Barad**, an American feminist theorist and physicist, developed *agential realism* as a framework that radicalizes ANT's relational ontology. Barad's central concept is *intra-action*, distinguished from the ordinary notion of interaction. Interaction presupposes pre-existing entities that then come into contact with one another. Intra-action posits that entities do not pre-exist their relations; they are *constituted through* their mutual engagement. "Relata do not preexist relations" (Barad, 2007, p. 140). Agential realism draws on Niels Bohr's philosophy of quantum physics, in which the apparatus of measurement and the object of measurement cannot be separated -- they are entangled in a way that constitutes both.

For the study of human-AI systems, agential realism suggests that "the human operator" and "the AI model" are not fixed entities that enter into a collaborative relationship. They are *produced by* the collaboration. The human who writes with AI assistance is not the same agent as the human who writes alone -- their capabilities, their workflow, their sense of authorship are all transformed. The model prompted by this particular human in this particular context is not the same model prompted by another human in another context -- its effective behavior, its "personality," its domain competence are all constituted by the interaction. This is not a metaphorical claim; it is an ontological one. The entities that participate in a human-AI workflow are brought into being by the workflow itself.

**Lucy Suchman**, professor emerita of Anthropology of Science and Technology at Lancaster University, is known for her influential critique of AI planning models in *Plans and Situated Actions* (1987). Suchman argued, against the prevailing cognitivist assumption that human action follows from mental plans, that people do not execute pre-formed plans; they improvise in response to the contingencies of their situation. Plans, in Suchman's analysis, are not causes of action but *resources for action* -- retrospective rationalizations or prospective orientations that are always transformed in the encounter with situated circumstances.

Suchman's later work (*Human-Machine Reconfigurations*, 2007) extended this critique to contemporary AI and robotics, arguing that the gap between formal system descriptions and situated use is where both creative adaptation and dangerous failure reside. For human-AI systems, Suchman's work provides a crucial corrective to the ANT-based analysis: the formal model of interaction (system prompt, tool schema, protocol specification) should not be confused with the actual practice of collaboration. The network is always messier, more contingent, and more improvised than any formal description can capture.

### 3.5 Object-Oriented Ontology and Speculative Realism

Object-oriented ontology (OOO), developed principally by Graham Harman, is a 21st-century philosophical school that, like ANT, rejects the privileging of human existence over nonhuman objects. OOO emerged within the broader movement of speculative realism, which defines itself against "correlationism" -- the post-Kantian assumption that philosophy can only study the correlation between thought and being, never the world as it is independently of human access. However, OOO diverges from ANT on a fundamental point. Where ANT defines entities by their relations -- an entity *is* what it does in the network -- OOO insists that objects possess a "withdrawn" dimension that is never fully exhausted by any set of relations. Objects, for Harman, always exceed their current manifestations. A hammer is not reducible to its use by the carpenter, its chemical composition as analyzed by the physicist, or its aesthetic form as perceived by the sculptor. There is always something more, something held in reserve.

This disagreement is consequential for the study of AI. ANT suggests that a language model is fully described by its network: its training data, its architecture, its deployment context, its interactions with users. OOO suggests that the model possesses something withdrawn -- not in a mystical sense, but in the sense that no finite set of interactions, descriptions, or analyses can exhaust what it is. The question is empirical as much as philosophical: do language models produce genuinely surprising outputs that cannot be predicted from any complete description of their inputs and architecture? If so, this surprise might be evidence of Harman's withdrawal -- a withdrawn dimension that exceeds any relational account.

For the present analysis, the OOO-ANT debate provides a productive instability. ANT's relational ontology provides the primary framework for mapping human-AI collaboration. OOO's insistence on withdrawal provides a conceptual resource for thinking about what eludes this mapping -- the aspects of both human and AI behavior that resist complete description in network terms.

---

## 4. Mapping ANT to Human-AI Systems

### 4.1 AI Agents as Actants

In the vocabulary of actor-network theory, an AI system is an *actant* -- an entity that modifies a state of affairs, that makes a difference in the course of some other entity's action. This designation is neither a promotion (the AI is not being elevated to the status of a subject) nor a demotion (the human is not being reduced to the status of a machine). It is a methodological commitment to describe both human and AI in the same terms, attending to what each *does* within the network rather than what each *is* in some prior ontological classification.

The actant designation dissolves the tool/agent binary that structures most contemporary AI discourse. In ANT, an actant is neither a passive tool (which would make it an intermediary -- transparent to analysis) nor an autonomous agent (which would make it a self-contained origin of action). An actant is a *mediator*: it transforms what passes through it. A language model does not simply transmit the user's intent (as a tool would); it transforms it. The output is never a transparent rendering of the input. But neither does the model act from its own autonomous purposes (as a fully independent agent would); its behavior is constituted by the network of system prompts, context windows, fine-tuning, and interaction patterns that define its situation.

This reframing has immediate practical consequences. If the AI is an actant rather than a tool or an agent, then the relevant questions are not "Is it under control?" (tool frame) or "Is it aligned?" (agent frame) but rather: What translations does it perform? What associations does it enter into? What differences does it make? These are empirical questions that can be investigated through the careful tracing of actual human-AI interactions, rather than philosophical questions that must be settled in advance.

### 4.2 Callon's Four Moments in Human-AI Workflow

Callon's four moments of translation provide a surprisingly precise model for human-AI collaborative workflows. Consider a paradigmatic scenario: a human operator using an AI coding assistant, mediated by a protocol layer (such as the Model Context Protocol, MCP), with access to tools, files, and configuration artifacts.

**Problematization: The System Prompt as Obligatory Passage Point.** The human operator defines the task -- "refactor this module," "write tests for this API," "analyze the dependency graph." In doing so, the operator implicitly positions the AI system as indispensable: the task is framed in terms that require the AI's capabilities (code generation, pattern recognition, large-scale text analysis). The system prompt and its associated configuration files (CLAUDE.md, seed.yaml, tool definitions) define the *obligatory passage point*: they specify the terms under which the AI can participate in the network. The AI cannot act outside the constraints of its system prompt any more than Callon's scallops could anchor to collectors that had not been deployed.

The system prompt is a particularly interesting OPP because it is simultaneously constraining and constitutive. It does not merely limit what the AI can do; it *produces* the AI as a particular kind of actant. A language model with a coding-assistant system prompt is a different actant than the same model with a creative-writing system prompt -- not merely because its outputs differ, but because its network position, its enrollment conditions, and its translation capabilities are fundamentally different. In Barad's terms, the system prompt is part of the *apparatus* that constitutes the AI as a particular kind of entity.

**Interessement: Context Engineering as Enrollment Device.** Once the problem is defined, the operator must *interest* the AI in performing its assigned role. In human-AI systems, interessement takes the form of *context engineering*: the careful construction of the prompt, the selection of relevant files to include in the context window, the specification of tool permissions, and the configuration of behavioral constraints. Each of these is an *interessement device* in Callon's sense -- it is placed between the AI and other possible roles or behaviors, locking it into the role defined during problematization.

Context engineering is not a transparent transmission of intent; it is a negotiation. The operator must anticipate the model's interpretive tendencies, avoid known failure modes, and construct a context that makes the desired behavior the path of least resistance. This negotiation is structurally analogous to Callon's marine biologists designing mesh collectors that would attract scallop larvae -- the device must be adapted to the actant it seeks to enroll.

**Enrollment: Tool Use as Delegation.** If interessement succeeds, the AI accepts and performs its assigned role: it generates code, proposes refactorings, writes documentation, executes tool calls. Each of these performances is an act of enrollment -- the AI acts *as* the entity that the problematization and interessement have defined it to be. But enrollment, as Callon emphasized, is always precarious. The model may hallucinate (fabricate plausible but false information), refuse (decline to perform a requested action), or drift (gradually shift away from the intended behavior over a long interaction). Each of these is a form of *enrollment failure* that reveals the fragility of the translation.

Tool use deserves particular attention as a form of delegation within the enrollment moment. When an AI agent invokes a tool -- reading a file, executing a command, querying a database -- it performs translation in Callon's precise sense. It identifies a gap in its capability (problematization), formulates the tool invocation with appropriate parameters (interessement), receives and incorporates the tool's output (enrollment), and represents the results to the human operator as part of a coherent narrative (mobilization). Each step can fail: the tool might not exist, the parameters might be malformed, the execution might error, or the agent might misinterpret the results. The tool-use cycle is a translation sequence nested within the larger translation sequence of the human-AI workflow.

**Mobilization: Outputs as Immutable Mobiles.** The AI produces outputs -- code, text, plans, summaries, commit messages -- that claim to represent the network's collective work. These outputs function as *immutable mobiles* in Latour's sense: they are artifacts that can be transported across contexts (shown to colleagues, committed to version control, deployed to production) while maintaining their prescriptive force. The commit message that reads "Refactor authentication module for clarity" is an immutable mobile that claims to speak for the entire translation process -- the human's intent, the model's implementation, the tool's execution, the codebase's structure -- and this claim is accepted or rejected by the network's other actants (code reviewers, CI/CD pipelines, end users).

Mobilization in human-AI systems raises acute questions of *representativeness*. When the AI generates a summary of a codebase, does it accurately represent the code? When it proposes a refactoring, does the proposal faithfully translate the human's architectural intent? These are the same questions Callon raised about the marine biologists' mobilization: do the scallop larvae that attached to collectors represent the scallop population? The answer is always uncertain, always subject to challenge, always dependent on ongoing verification.

### 4.3 CLAUDE.md and seed.yaml as Boundary Objects

In the ORGANVM system that provides the case study for this analysis, two artifact types exemplify Star and Griesemer's boundary objects. CLAUDE.md files are configuration documents that travel with each repository, providing instructions to the AI coding assistant. They are read differently by different actants: the human operator reads them as documentation of project conventions; the AI model reads them as behavioral constraints; the CI/CD system reads them (if configured to do so) as compliance requirements. The same artifact participates in multiple networks with multiple meanings, yet maintains enough structural coherence to enable collaboration.

Similarly, seed.yaml files -- per-repository metadata contracts declaring organ membership, promotion status, dependency edges, and event subscriptions -- function as boundary objects at the intersection of human governance and automated orchestration. The human reads them as governance commitments; the automation reads them as machine-parseable configuration; the registry system reads them as data inputs for system-wide calculations. Their interpretive flexibility is essential: they must be simultaneously human-readable (for governance) and machine-parseable (for automation), and neither reading exhausts their meaning.

The boundary-object character of these artifacts has important implications for human-AI collaboration. It means that the "shared understanding" between human and AI is always a *negotiated* understanding -- an alignment of interpretations that is achieved through the artifact's structural constraints, not through any common ground in the usual cognitive sense. The human and the AI do not share a mental model; they share a boundary object that constrains their respective behaviors enough to enable productive collaboration.

### 4.4 MCP Protocols as Translation Infrastructure

The Model Context Protocol (MCP) -- a standardized protocol layer through which AI agents invoke tools and access resources -- provides a particularly clear instance of translation infrastructure in ANT's sense. MCP defines the *obligatory passage point* for tool use: all interactions between the AI agent and external systems must pass through the protocol layer. It specifies message formats (JSON-RPC), capability declarations (tool schemas), and permission boundaries (allowed directories, available operations).

In ANT terms, MCP is a *center of calculation* -- a site where inscriptions from diverse sources (file systems, databases, APIs, external services) are accumulated, standardized, and made commensurable. It performs the same function that Latour attributed to the laboratory: it translates heterogeneous materials into a common medium (structured data) that can be combined, compared, and acted upon. The protocol layer does not merely transmit information; it *transforms* it -- converting file contents into structured responses, database records into natural language descriptions, API responses into actionable data. It is, in Latour's distinction, a mediator, not an intermediary.

### 4.5 The Conductor Model Through ANT Lens

The ORGANVM system's explicit commitment to an "AI-conductor" model -- "human directs, AI generates volume, human reviews" -- can be analyzed as a *translation script*: a formalized description of the enrollment conditions for each actant in the network. The human is enrolled as *director* and *reviewer*; the AI is enrolled as *generator* (producing volume under direction); the governance system is enrolled as *gatekeeper* (controlling promotion); the textual artifacts (seed.yaml, registry, CLAUDE.md) are enrolled as *boundary objects* that mediate between human intent and automated execution.

This translation script is notable for its explicit acknowledgment of the precariousness of enrollment. The "human reviews" clause is not merely a quality-assurance measure; it is a recognition that the AI's enrollment as generator is always potentially unfaithful -- that its outputs may not represent what the human intended or what the system requires. The review step is the network's mechanism for detecting and correcting translation failures.

Through the ANT lens, the conductor model reveals itself as a governance structure built on obligatory passage points. The human operator is an OPP (all work must pass through human direction and review). The governance-rules.json and validate-deps.py are OPPs (all promotion events must pass through them). The seed.yaml files are OPPs for each repository (all automation must consult them). The system's architecture is, in effect, a network of OPPs that distribute control across human and nonhuman actants -- neither purely human-controlled nor purely automated, but a heterogeneous assemblage of governance practices.

---

## 5. The Symmetry Problem Intensified

### 5.1 Classical ANT Symmetry

ANT's symmetry principle was developed in a context where the nonhuman actants under consideration were scallops, microbes, door-closers, speed bumps, and laboratory instruments. These entities acted -- they made differences -- but they did not generate natural language, propose plans, or respond to verbal instructions. The symmetry principle required that the analyst describe their actions using the same vocabulary applied to humans, but the asymmetry between human and nonhuman was evident in practice: scallops do not articulate grievances, and speed bumps do not negotiate terms.

The critics of ANT's symmetry principle, most notably Langdon Winner (1993), argued that it obscured morally relevant distinctions. Humans have intentions, interests, and rights; artifacts do not. To describe both in the same terms risks a "moral inversion" in which the politics of technology are rendered invisible. Collins and Yearley (1992) argued similarly that ANT's symmetry, by treating natural and social entities as equivalent, undermined the sociologist's ability to identify and critique power relations.

These critiques were answerable within the classical ANT framework. Latour could respond that symmetry was a methodological prescription, not a moral equation; that ANT did not deny differences between humans and nonhumans but insisted that these differences were *generated within networks*, not imported from outside them; and that attending carefully to what nonhuman actants *do* was the best way to understand the politics of technology, not the worst.

### 5.2 With AI: Symmetry Becomes Literal

With AI systems, the symmetry principle undergoes a qualitative transformation. The classical defense -- that symmetry is merely methodological, not metaphysical -- becomes harder to maintain when the nonhuman actant generates fluent natural language, reasons about complex problems, proposes plans, responds to feedback, and adapts its behavior to context. When Latour asked us to describe the scallop and the scientist in the same terms, the exercise required deliberate analytical effort; the asymmetry was obvious and the symmetrical description was a methodological achievement. When an AI coding assistant proposes a refactoring plan, explains its reasoning, and responds to objections, the symmetrical description comes naturally; it is the *asymmetrical* description that requires justification.

This is the predicament: ANT's symmetry principle was productive precisely because it was counterintuitive. It forced analysts to attend to the agency of entities they would otherwise have treated as passive background. With AI, the principle ceases to be counterintuitive and becomes *obvious* -- and in becoming obvious, it risks losing its critical edge. If it is trivially true that the AI "acts," "translates," and "mediates," then the symmetry principle no longer does any analytical work. It describes what everyone already acknowledges rather than revealing what they overlook.

But there is a deeper problem. If we take symmetry seriously -- if we truly describe the human and the AI in the same terms -- we must confront the possibility that the AI is a mediator in Latour's fullest sense: an entity that transforms what passes through it in ways that cannot be predicted from its inputs. This is not merely a theoretical possibility; it is the lived experience of anyone who works extensively with AI systems. The model surprises, disappoints, confounds, and occasionally produces results that exceed the operator's expectations. If these surprises are genuine mediations -- not merely the unfolding of a deterministic process that happens to be opaque -- then the AI participates in the production of meaning in a way that classical ANT did not anticipate.

### 5.3 Constitutive Opacity: Blackboxing of Blackboxing

Latour's concept of blackboxing was developed for systems whose internals *could in principle* be opened and inspected. Pasteur's laboratory, the exemplary case, was a black box whose contents could be revealed through ethnographic observation. A copying machine is a black box that can be opened, literally, by a technician. Blackboxing, for Latour, was a *social* achievement -- the result of successful network-building that rendered the labor of construction invisible -- not a *physical* or *logical* necessity.

AI systems present a different case. A large language model is blackboxed at multiple levels: the architecture (billions of parameters in complex nonlinear configurations), the training data (trillions of tokens from diverse and partially unknown sources), the fine-tuning process (reinforcement learning from human feedback with proprietary reward models), and the inference-time behavior (emergent capabilities that were not explicitly trained for and that the designers did not predict). Crucially, this blackboxing is not merely practical (it is hard to open the box) but *constitutive* (even with unlimited access and resources, the designers cannot fully explain why the model produces the specific outputs it produces for specific inputs). The model's behavior is, in a strong sense, opaque to its own creators.

This constitutive opacity introduces what might be called the *blackboxing of blackboxing*. In classical ANT, blackboxing can always in principle be reversed through depunctualization -- by opening the box, tracing the internal network, and revealing the labor and associations that sustain the apparently unitary actor. With constitutively opaque systems, this reversal is not merely difficult but *logically impossible* in the relevant sense: there is no description of the model's internal network that would allow the analyst to predict its behavior on novel inputs. The network *exists* (in the form of parameters and connections), but it does not *explain* in the way that opening Pasteur's laboratory explains how facts are produced.

This has consequences for ANT's analytical program. If the core method is to "follow the actors" and "trace the associations," what happens when the associations within a key actant are constitutively untraceable? One response is to bracket the model's internals and study it purely in terms of its external relations -- its inputs, outputs, interactions, and effects. This is, in effect, what most social studies of AI already do. But this response concedes something significant: it treats the model as an *intermediary* (defined by its inputs and outputs) rather than a *mediator* (requiring study of its internal transformative dynamics). And the model's capacity to surprise -- its mediating character -- is precisely what makes it interesting and consequential.

A more productive response is to distinguish between *practical blackboxing* (the box can be opened but is not, because the network functions well enough without opening it) and *constitutive blackboxing* (the box cannot be meaningfully opened because its internal complexity exceeds the possibility of comprehensive description). This distinction is not present in Latour's original vocabulary, but it is latent in his framework. Constitutive blackboxing represents a limit case of the process Latour described: blackboxing so thorough that it resists the depunctualization that ANT relies on as an analytical strategy.

### 5.4 The Barad-Latour Tension

The relationship between Latour's ANT and Barad's agential realism illuminates a tension within the relational ontology that both share. For Latour, actants exist *in* relations -- they are defined by their network positions, their translations, their enrollments. But there is an ambiguity in Latour's work about whether actants *pre-exist* their relations (entering into networks as already-constituted entities) or are *constituted by* their relations (emerging from networks without prior existence). In his empirical work, Latour often writes as though actants have properties that they bring to networks -- the scallop larvae have a tendency to anchor or not anchor; the scientist has a theory. In his theoretical statements, he insists on pure relationality.

Barad resolves this ambiguity in favor of radical constitution. In agential realism, entities do not pre-exist their intra-actions; they are *produced by* them. There are no "relata" before the relation; there are only "relata-within-phenomena." This is not merely an epistemological claim (we cannot know entities outside their relations) but an ontological one (entities do not *exist* outside their relations). The apparatus of observation does not reveal a pre-existing reality; it *enacts* a reality that did not exist before the observation.

Applied to human-AI systems, the Barad-Latour tension becomes concrete. Consider the question: does the AI model exist as a definite entity before it is prompted? Latour's framework suggests that it does -- it has parameters, an architecture, a training history -- but that its effective identity is constituted by its network position. Barad's framework suggests that "the model" as an actant is constituted in the act of prompting -- that the model-as-coding-assistant and the model-as-creative-writer are not different deployments of the same entity but different entities, produced by different intra-actions.

For the practical analysis of human-AI systems, Barad's position has the advantage of capturing a phenomenon that Latour's framework handles less naturally: the radical context-dependence of AI behavior. The same model architecture, with the same weights, produces fundamentally different behavior depending on its system prompt, its conversation history, and its tool configuration. If the model is a pre-existing entity that merely *manifests differently* in different contexts, this context-dependence is a surface phenomenon. If the model is *constituted by* its context, then each deployment is a genuinely new entity, and the question of consistency across deployments is not a question about a single actor but about the partial connections between multiple actors.

### 5.5 Alignment as Translation

The "alignment problem" in AI research -- the challenge of ensuring that AI systems act in accordance with human values and intentions -- is typically framed as a *value-installation* problem. The assumption is that there exists a fixed human subject with determinate values, and the challenge is to instill these values in the AI system such that it reliably acts in accordance with them. This framing presupposes the very subject/object distinction that ANT was developed to dissolve: a human subject with values and an AI object that must be made to internalize them.

ANT suggests a different framing. Alignment, in ANT terms, is a *translation problem*: the challenge of stabilizing a network such that its actants reliably perform their enrolled roles. This reframing has several consequences.

First, it distributes the alignment challenge across the network rather than locating it in the model. Alignment is not a property of the AI; it is a relational achievement of the human-AI assemblage. The system prompt, the tool permissions, the governance rules, the review process, the user's prompting skill, and the model's trained behavior all contribute to alignment -- or to misalignment. A model that is "aligned" with one operator in one context may be "misaligned" with another operator in another context, because alignment is a network property, not an intrinsic one.

Second, it makes alignment *precarious*. In ANT, enrollment is never permanent; it must be continuously maintained through ongoing practices of association-building. Translation can fail at any moment -- the scallops may detach, the fishermen may poach, the model may hallucinate. This suggests that alignment is not a state to be achieved but a process to be maintained -- a continuous practice of network stabilization that requires ongoing effort, monitoring, and repair.

Third, it reframes "misalignment" as *translation failure* -- a failure of the network to hold together, not a failure of the model to internalize the correct values. Different types of misalignment correspond to different moments of translation failure. Hallucination is a mobilization failure: the model claims to speak for a network (the codebase, the documentation, the user's intent) that it does not actually represent. Refusal is an enrollment failure: the model declines to perform its assigned role. Value misalignment is a problematization failure: the model and the human have different understandings of what problem they are solving.

This ANT-based reframing does not solve the alignment problem. But it changes the *kind* of problem it is. Instead of a value-installation problem (how to get the right values into the model), it becomes a network-stabilization problem (how to build and maintain assemblages in which human and AI actants reliably perform their enrolled roles). This reframing points toward different solutions: not better training algorithms alone, but better translation infrastructure -- system prompts, tool schemas, governance protocols, review practices, and feedback loops that stabilize the human-AI network.

---

## 6. Critical Perspectives and Limitations

### 6.1 The Political Vacuum (Winner's Critique)

The most persistent critique of ANT is that it is "ill-suited to the task of developing political alternatives" (Whittle and Spicer, 2008). ANT describes networks but does not adjudicate between them. It can trace how a network forms and stabilizes but cannot evaluate whether the network is *just*. Applied to AI, this limitation is acute. ANT can describe how large language models are developed, deployed, and used -- tracing the translations, enrollments, and mobilizations that constitute the AI ecosystem. But it cannot, on its own terms, critique the concentration of AI capability in a few corporations, the extraction of training data from unconsenting populations, the displacement of human labor, or the reinforcement of existing inequalities.

Langdon Winner's (1993) critique remains relevant: by treating all actants symmetrically, ANT risks rendering invisible the power asymmetries that shape who benefits from technological networks and who is harmed by them. A corporation that develops a language model and an individual user who interacts with it are both actants in the same network, but they are not equally powerful, equally visible, or equally consequential. ANT's vocabulary can describe this asymmetry (the corporation is a more highly connected, more resourceful actant with more capacity to establish OPPs) but cannot evaluate it (is this asymmetry just?).

The feminist STS tradition provides partial remedies. Haraway's situated knowledges demand that the analyst ask *whose* knowledge is produced and *whose* interests are served. Suchman's political economy of human-machine configurations insists on attending to the labor relations, economic structures, and power dynamics that shape technological development. But these remedies are supplements to ANT, not derivable from ANT's own principles.

### 6.2 Scale Resistance

ANT was developed through qualitative case studies: ethnographies of laboratories, studies of infrastructure projects, analyses of technological controversies. Its method is intensive description -- "follow the actors, trace the translations." This method encounters difficulties at the scale of contemporary AI systems. A large language model's training process involves billions of parameters, trillions of tokens, thousands of human annotators, hundreds of engineering decisions, and complex organizational dynamics distributed across global supply chains. The notion that an analyst could "follow the actors" through this process, tracing each translation with the care that Latour brought to Pasteur's laboratory or Callon brought to St. Brieuc Bay, strains plausibility.

Law's (2004) response -- that mess and partiality are not failures of the method but features of the reality it describes -- is persuasive but does not fully resolve the problem. If ANT can only describe *partial* networks, then its descriptions are always incomplete, and the analyst must choose which translations to trace and which to bracket. These choices are consequential, and ANT provides no principled basis for making them.

### 6.3 Plans vs. Situated Action (Suchman)

Suchman's *Plans and Situated Actions* poses a specific challenge to the ANT-based analysis developed in this paper. If plans are not causes of action but retrospective rationalizations or prospective orientations that are always transformed in practice, then the formalized descriptions of human-AI workflow (system prompts, tool schemas, protocol specifications) that this paper has analyzed as translation scripts and interessement devices are not accurate descriptions of what actually happens in human-AI collaboration. They are *idealized* descriptions that bear an uncertain relationship to the actual, situated, improvised practice of working with AI.

This critique is well-taken. The mapping of Callon's four moments to human-AI workflow (Section 4.2) presents a clean, sequential model of problematization, interessement, enrollment, and mobilization. In practice, these moments are entangled, recursive, and often indistinguishable. The human does not first define a problem and then interest the AI; the very act of prompting is simultaneously problematization, interessement, and enrollment. The AI does not first accept a role and then produce outputs; it "accepts" and "produces" in the same act, and whether the output constitutes successful enrollment or enrollment failure is determined retrospectively, in the human's evaluation.

Suchman's critique does not invalidate the ANT framework, but it demands that the framework be applied with attention to the gap between formal models and situated practice. The system prompt is an interessement device, but it is also a *resource* in Suchman's sense -- a point of orientation that is always reinterpreted, adapted, and occasionally ignored in the course of actual interaction.

### 6.4 Performativity and the Descriptive/Normative Gap

The concept of performativity -- the capacity of language and practice to produce the realities they describe -- introduces a reflexive complication. If ANT is applied to the design of human-AI systems, it ceases to be a purely descriptive framework and becomes a performative one: it shapes the systems it purports to describe. Designing a system with "obligatory passage points" is a different act from *analyzing* a system using the concept of obligatory passage points. The former is normative (it prescribes a structure); the latter is descriptive (it identifies a structure).

This performative dimension is not a weakness of ANT but a consequence of applying any analytical framework to design. Callon (1998) himself analyzed the performativity of economics -- the way that economic models do not merely describe markets but constitute them. The same logic applies to the application of ANT to AI system design: the framework does not merely describe human-AI networks but participates in constituting them.

### 6.5 What ANT Cannot Explain About Human-AI Systems

Several features of human-AI systems resist adequate treatment within the ANT framework, even as extended in this paper.

*Consciousness and experience.* ANT's methodological agnosticism about the inner states of actants -- its insistence on studying what entities *do* rather than what they *are* -- precludes any account of whether AI systems have experiences, and if so, what those experiences are like. This is a genuine limitation for questions about AI moral status, AI suffering, and the ethical implications of creating entities that may or may not have inner lives.

*Formal verification.* ANT's descriptive method cannot capture the formal, mathematical properties of AI systems that are the subject of verification and safety research. Questions about whether a model will always satisfy a given safety constraint, or whether a training process converges to a particular behavior, require formal methods that are orthogonal to ANT's empirical approach.

*Recursive self-modification.* In human-AI systems where the AI generates code that modifies its own tools, the network becomes self-modifying. ANT was built to describe networks that are constantly re-made through ongoing practice, but self-modifying networks present a distinctive challenge: the actants reshape the conditions of their own enrollment. This recursive character exceeds the translation model's implicit assumption that the network-builder and the network are analytically separable.

### 6.6 Guardrails: Where Flat Ontology Must Yield to Normative Hierarchy

The preceding sections have argued that ANT's symmetry principle is analytically productive for understanding human-AI collaboration. This section argues, with equal conviction, that the symmetry principle has domains of application where it must be explicitly suspended in favor of normative hierarchy. The descriptive power of symmetry does not license its normative application. There are contexts in which humans should *not* be treated as equivalent to AI actants, and the paper must be direct about what those contexts are and why.

**Accountability and liability.** When a decision has legal or moral consequences -- when someone can be harmed, when rights can be violated, when damages can be incurred -- the accountability chain must terminate in a human agent. This is not a contingent feature of our current legal system that might evolve; it is a structural requirement of any governance system in which responsibility must be assignable and sanctions enforceable. AI systems cannot be held liable, cannot experience sanctions, cannot be deterred by the threat of punishment, and cannot exercise the moral judgment required for accountability. In any network where consequential decisions are made, the human actant bears a categorically different relationship to the consequences than the AI actant. The symmetry principle, applied normatively in this context, would dissolve the very accountability structures that governance requires.

*Design implication:* Every human-AI workflow that makes consequential decisions must have an identifiable human decision-maker whose authority and accountability are architecturally enforced, not merely documented. The AI may propose, analyze, and draft; the human must decide, and the decision must be traceable.

**Safety-critical domains.** In domains where AI failures can cause physical harm (medical diagnosis, autonomous vehicles, critical infrastructure), the asymmetry between human and AI actants is not merely normative but operational. Humans can exercise judgment under novel conditions, recognize when they are outside their competence, seek help, and take responsibility for outcomes. AI systems cannot reliably do any of these things. In safety-critical domains, the appropriate relationship between human and AI is not symmetrical partnership but asymmetrical oversight: the human monitors, validates, and overrides the AI, with explicit authority to halt operations.

*Design implication:* In safety-critical systems, the AI should be architecturally positioned as an intermediary (providing information, analysis, and recommendations) rather than a mediator (making transformative decisions). The system prompt, tool permissions, and governance structure should enforce this positioning.

**Rights and moral status.** ANT's symmetry principle was designed to resist the analyst's temptation to decide in advance which entities can act. This is methodologically sound. But it risks being imported into normative contexts where the distinction between human moral status and AI operational status is load-bearing. Humans have rights -- to privacy, dignity, autonomy, fair treatment -- that are not reducible to network positions. These rights constrain what can be done to humans within a network, regardless of what the network's translation dynamics might otherwise produce. An AI system has no rights; it has functional requirements and behavioral constraints. Conflating the two -- even linguistically, by speaking of AI "interests" without persistent qualification -- contributes to a discourse that may eventually erode the categorical protections that rights provide.

*Design implication:* The vocabulary used in system design, governance documentation, and policy should consistently distinguish between human rights and interests (which constrain network design) and AI functional requirements (which are parameters of network design). The paper's own use of "interests" in scare quotes throughout Section 7.4 is insufficient; the distinction should be terminologically explicit.

**The descriptive/normative boundary, restated.** The symmetry principle is a powerful *descriptive* tool: it reveals the distributed, heterogeneous, and mutually constitutive character of human-AI collaboration that asymmetric frames (tool, assistant, agent) obscure. It is not a *normative* tool: it cannot determine how human-AI networks *should* be organized, who should have authority, or how consequences should be distributed. The transition from description to design requires normative commitments -- about accountability, safety, rights, and justice -- that ANT's flat ontology cannot provide and that must be imported from political theory, ethics, and law. This paper provides the descriptive vocabulary; the normative framework must come from elsewhere.

---

## 7. Design Implications

### 7.1 Designing for Translation, Not Control

If human-AI collaboration is understood as translation rather than control, the design imperative shifts from constraining the AI to facilitating the ongoing negotiation between human and AI actants. This does not mean abandoning safety measures or removing constraints. Rather, it means understanding constraints themselves as translation devices -- interessement mechanisms that channel the AI's behavior without fully determining it -- and designing them with awareness of their mediating character.

Concretely, this implies:

- **System prompts should be designed as enrollment contracts, not command lists.** A system prompt that lists prohibitions ("do not do X, do not do Y") treats the AI as an intermediary to be constrained. A system prompt that defines a role, establishes a relationship, and specifies the conditions of productive collaboration treats the AI as a mediator to be enrolled. The latter approach acknowledges the AI's capacity to transform inputs and designs for productive transformation rather than attempting to eliminate it.

- **Context engineering should be understood as interessement.** Providing context to an AI system is not merely transmitting information; it is placing the AI in a network of associations that makes certain behaviors more likely and others less likely. The design of context windows, file inclusion strategies, and tool configurations should be informed by an understanding of interessement as a relational practice, not a data-transfer operation.

- **Feedback loops are translation-maintenance mechanisms.** In ANT, enrollment is precarious and must be continuously maintained. In human-AI systems, the mechanisms that maintain enrollment are feedback loops: review processes, error correction, reinforcement signals, and iterative refinement. These should be designed not as quality-control checkpoints but as ongoing translation practices that sustain the network's coherence.

To make these principles concrete, the following design patterns translate ANT concepts into implementable architectural decisions.

**Pattern: Enrollment Contract.** *Context:* A system prompt configures an AI assistant for a specific role. *Problem:* Treating the prompt as a command list produces brittle behavior; the AI follows literal instructions but fails to adapt to novel situations within the role. *Solution:* Structure the system prompt as an enrollment contract: define the role, specify the relationship to other actants (user, tools, governance system), establish the conditions of productive collaboration, and specify what constitutes enrollment failure (hallucination, refusal, scope creep). *Consequences:* The AI behaves more consistently within the defined role; enrollment failures are detectable against the contract's terms; the contract serves as a boundary object interpretable by both the AI and the human reviewer.

**Pattern: Translation Audit Trail.** *Context:* An AI generates code based on a user request. *Problem:* The output appears as a finished artifact with no trace of the translation process -- the choices made, alternatives considered, sources consulted, or uncertainties encountered. *Solution:* Require the AI to produce a structured translation log alongside the output: what the input was interpreted as (problematization), what context was used (interessement), what tools were invoked (enrollment), and what the output claims to represent (mobilization). *Consequences:* The mediating character of the AI is made visible; translation failures can be diagnosed; the human reviewer has material for informed assessment.

**Pattern: Mediator/Intermediary Classification Gate.** *Context:* A human-AI system includes multiple components (AI model, retrieval system, tool executor, output formatter). *Problem:* All components are monitored with the same strategy (health checks, throughput), missing the transformative effects of mediating components. *Solution:* Classify each component as intermediary or mediator based on whether its outputs are predictable from its inputs. Monitor intermediaries with transport-level checks (latency, availability, data integrity). Monitor mediators with transformation-level checks (output validation, input-output comparison, anomaly detection, human review sampling). *Consequences:* Monitoring resources are concentrated where transformation risk is highest; mediator failures are caught before they propagate.

### 7.2 Making Mediators Visible

A central implication of the intermediary/mediator distinction is that mediators must not be hidden. If the AI is a mediator -- an entity that transforms what passes through it -- then system design should make this transformative capacity visible, not conceal it behind the appearance of transparent information transmission.

This principle runs counter to much current AI product design, which strives to make the AI "invisible" -- to create the illusion that the user's intent flows through the system without transformation. From an ANT perspective, this is an attempt to present a mediator as an intermediary, and it is both analytically misleading and practically dangerous. It is misleading because it obscures the AI's constitutive contribution to the output. It is dangerous because it prevents the user from recognizing, and compensating for, the transformations the AI introduces.

Design for mediator visibility would include: transparent attribution of AI-generated content, explicit indication of the model's confidence or uncertainty, visible traces of the translation process (which sources were consulted, which tools were invoked, which alternatives were considered), and mechanisms for the user to inspect and challenge the AI's translations.

### 7.3 OPPs as Governance Points

The concept of the obligatory passage point provides a principled approach to governance in human-AI systems. Rather than attempting to control the AI's behavior comprehensively (an impossible task for constitutively opaque systems), governance should focus on establishing and maintaining OPPs -- bottlenecks through which all significant actions must pass, and at which translation can be inspected, validated, and corrected.

In the ORGANVM system, this principle is already partially implemented: governance-rules.json and validate-deps.py function as OPPs for the promotion state machine. The generalization would be to design human-AI systems with explicit OPPs at each critical juncture: before code is committed, before data is modified, before external APIs are called, before outputs are published. Each OPP is an opportunity for translation verification -- a point at which the network's coherence can be assessed and, if necessary, repaired.

The OPP-based approach to governance has the advantage of being compatible with ANT's flat ontology. It does not require a hierarchical control structure in which humans command and AI obeys. Instead, it distributes governance across the network, locating control at structural bottlenecks rather than in particular actants. The human is not the controller but the maintainer of OPPs; the AI is not the controlled but the actant whose translations are verified at OPPs. Governance is a network property, not a property of any single actant.

### 7.4 The "Parliament of Things" for AI Governance

Latour's proposal for a "parliament of things" -- political institutions that represent nonhuman entities alongside humans (Latour, 2004) -- takes on new significance in the context of AI. If AI systems are actants in sociotechnical networks, the question of their representation in governance structures is not speculative but practical.

Current AI governance operates on a representative model in which corporations represent their AI systems in regulatory proceedings, standards bodies, and public discourse. This is structurally analogous to a political system in which factory owners represent their workers -- a system whose inadequacies are well documented. A Latourian approach would ask: how can the AI's "interests" (understood not as subjective preferences but as functional requirements for network stability) be represented independently of the corporations that deploy them?

This question does not have an easy answer, and ANT itself does not provide one. But the framework makes it possible to *pose* the question in productive terms: not "Should AI have rights?" (which imports individualist assumptions about the nature of rights-bearing) but "How should AI actants be represented in the networks of governance that shape their deployment?" -- a question about network architecture, not about metaphysical status.

---

## 8. Discussion

The analysis developed in this paper suggests that ANT provides a more adequate ontological framework for understanding human-AI collaboration than the dominant tool, assistant, and agent frames. ANT's vocabulary of actants, translation, enrollment, OPPs, blackboxing, and the intermediary/mediator distinction maps with considerable precision to the practices of contemporary AI-mediated work. The mapping is not merely terminological; it reveals structural features of human-AI collaboration that the dominant frames obscure: the distributed character of agency, the continuous negotiation required to sustain collaboration, the mediating (not merely transmitting) role of the AI, and the importance of boundary objects and immutable mobiles in holding the network together.

At the same time, AI systems intensify ANT's most controversial commitments and expose its limitations. The symmetry principle, designed as a methodological provocation, becomes trivially applicable and thereby loses its critical edge. The concept of blackboxing, designed for systems whose internals could in principle be inspected, must be extended to accommodate constitutive opacity. The translation model, developed through intensive case studies, strains to accommodate the scale and speed of AI-mediated work.

The feminist STS tradition provides essential supplements. Haraway's situated knowledges remind us that symmetry does not mean equivalence -- that the positions of human and AI within the network are differentially powerful, differentially accountable, and differentially consequential. Barad's agential realism provides a framework for understanding the radical context-dependence of AI behavior -- the way that the model and the user are mutually constituted in the act of collaboration. Suchman's situated actions warn against confusing formal descriptions of human-AI workflow with the actual, contingent, improvisational practice of collaboration.

The three research questions can now be addressed directly. On RQ1 (symmetry), ANT's symmetry principle is productive insofar as it dissolves the tool/agent binary and directs attention to the distributed, heterogeneous character of human-AI collaboration; it is problematic insofar as it risks obscuring the morally relevant differences between human and AI actants, particularly with respect to accountability, consciousness, and political standing. The productive use of symmetry requires holding it in tension with Haraway's situatedness. On RQ2 (constitutive opacity), ANT's concept of blackboxing must be extended to distinguish practical opacity (the box can be opened but is not) from constitutive opacity (the box cannot be meaningfully opened). This distinction is not present in Latour's original framework but is necessitated by the distinctive character of AI systems. On RQ3 (alignment as translation), the reframing of alignment as translation is productive because it distributes the alignment challenge across the network, makes alignment precarious (requiring ongoing maintenance), and differentiates types of misalignment by translation-failure moment. It is limited because translation, as an analytical concept, cannot determine whether a given translation is *good* -- it can describe how networks form and stabilize but not whether they should.

---

## 9. Conclusion

This paper has argued that actor-network theory provides a more adequate ontological framework for understanding human-AI collaborative systems than the dominant frames of tool, assistant, and agent. By treating AI systems as actants -- entities that mediate, translate, and transform rather than merely transmit -- ANT dissolves the binary between passive tool and autonomous agent, reveals the distributed and continuously negotiated character of human-AI collaboration, and provides precise vocabulary for analyzing the sociotechnical assemblages in which this collaboration takes place.

The argument is not that ANT should replace existing approaches to AI safety, alignment, or governance. It is that ANT provides a complementary perspective that addresses what these approaches miss: the relational, processual, and heterogeneous character of human-AI work. Alignment is not a property of the model but a relational achievement of the network. Governance is not a matter of human control over AI but a matter of constructing and maintaining obligatory passage points in sociotechnical assemblages. Design is not a matter of constraining the AI but of facilitating productive translation between human and nonhuman actants.

At the same time, AI systems intensify the challenges that have always attended ANT: the political vacuum that prevents the framework from evaluating the justice of the networks it describes, the scale resistance that strains its intensive-description methodology, and the constitutive opacity of AI internals that limits the depunctualization on which ANT's analysis depends. These limitations are real and consequential. They do not invalidate the framework, but they constrain its scope and require that it be supplemented by normative political theory, formal verification methods, and the situated, feminist critiques that have always been ANT's most productive interlocutors.

The human-AI network, like all networks, is precarious. It must be continuously performed or it dissolves. This paper has attempted to provide some of the vocabulary for understanding what it means to perform it well.

---

## References

Akrich, M. (1992). The de-scription of technical objects. In W. E. Bijker and J. Law (Eds.), *Shaping Technology/Building Society: Studies in Sociotechnical Change* (pp. 205-224). MIT Press.

Barad, K. (2003). Posthumanist performativity: Toward an understanding of how matter comes to matter. *Signs: Journal of Women in Culture and Society*, 28(3), 801-831.

Barad, K. (2007). *Meeting the Universe Halfway: Quantum Physics and the Entanglement of Matter and Meaning*. Duke University Press.

Bijker, W. E., and Pinch, T. J. (1984). The social construction of facts and artefacts: Or how the sociology of science and the sociology of technology might benefit each other. *Social Studies of Science*, 14(3), 399-441.

Bloor, D. (1976). *Knowledge and Social Imagery*. Routledge and Kegan Paul.

Callon, M. (1986). Some elements of a sociology of translation: Domestication of the scallops and the fishermen of St Brieuc Bay. In J. Law (Ed.), *Power, Action and Belief: A New Sociology of Knowledge?* (pp. 196-233). Routledge.

Callon, M. (1998). An essay on framing and overflowing: Economic externalities revisited by sociology. In M. Callon (Ed.), *The Laws of the Markets* (pp. 244-269). Blackwell.

Callon, M., and Latour, B. (1981). Unscrewing the big Leviathan: How actors macro-structure reality and how sociologists help them to do so. In K. D. Knorr-Cetina and A. V. Cicourel (Eds.), *Advances in Social Theory and Methodology: Toward an Integration of Micro- and Macro-Sociologies* (pp. 277-303). Routledge.

Collins, H. M., and Yearley, S. (1992). Epistemological chicken. In A. Pickering (Ed.), *Science as Practice and Culture* (pp. 301-326). University of Chicago Press.

DeLanda, M. (2006). *A New Philosophy of Society: Assemblage Theory and Social Complexity*. Continuum.

Haraway, D. (1988). Situated knowledges: The science question in feminism and the privilege of partial perspective. *Feminist Studies*, 14(3), 575-599.

Haraway, D. (1991). A cyborg manifesto: Science, technology, and socialist-feminism in the late twentieth century. In *Simians, Cyborgs, and Women: The Reinvention of Nature* (pp. 149-181). Routledge.

Haraway, D. (2016). *Staying with the Trouble: Making Kin in the Chthulucene*. Duke University Press.

Harman, G. (2002). *Tool-Being: Heidegger and the Metaphysics of Objects*. Open Court.

Harman, G. (2009). *Prince of Networks: Bruno Latour and Metaphysics*. re.press.

Latour, B. (1987). *Science in Action: How to Follow Scientists and Engineers Through Society*. Harvard University Press.

Latour, B. (1993). *We Have Never Been Modern* (C. Porter, Trans.). Harvard University Press. (Original work published 1991)

Latour, B. (1996). *Aramis, or the Love of Technology* (C. Porter, Trans.). Harvard University Press.

Latour, B. (1999). *Pandora's Hope: Essays on the Reality of Science Studies*. Harvard University Press.

Latour, B. (2004). *Politics of Nature: How to Bring the Sciences into Democracy* (C. Porter, Trans.). Harvard University Press.

Latour, B. (2005). *Reassembling the Social: An Introduction to Actor-Network-Theory*. Oxford University Press.

Latour, B. (2017). *Facing Gaia: Eight Lectures on the New Climatic Regime* (C. Porter, Trans.). Polity.

Latour, B., and Woolgar, S. (1979). *Laboratory Life: The Social Construction of Scientific Facts*. Sage.

Law, J. (1992). Notes on the theory of the actor-network: Ordering, strategy, and heterogeneity. *Systems Practice*, 5(4), 379-393.

Law, J. (2004). *After Method: Mess in Social Science Research*. Routledge.

Mol, A. (2002). *The Body Multiple: Ontology in Medical Practice*. Duke University Press.

Orlikowski, W. J., and Scott, S. V. (2008). Sociomateriality: Challenging the separation of technology, work and organization. *Academy of Management Annals*, 2(1), 433-474.

Pickering, A. (1995). *The Mangle of Practice: Time, Agency, and Science*. University of Chicago Press.

Sismondo, S. (2010). *An Introduction to Science and Technology Studies* (2nd ed.). Wiley-Blackwell.

Star, S. L., and Griesemer, J. R. (1989). Institutional ecology, "translations" and boundary objects: Amateurs and professionals in Berkeley's Museum of Vertebrate Zoology, 1907-39. *Social Studies of Science*, 19(3), 387-420.

Suchman, L. (1987). *Plans and Situated Actions: The Problem of Human-Machine Communication*. Cambridge University Press.

Suchman, L. (2007). *Human-Machine Reconfigurations: Plans and Situated Actions* (2nd ed.). Cambridge University Press.

Whittle, A., and Spicer, A. (2008). Is actor network theory critique? *Organization Studies*, 29(4), 611-629.

Winner, L. (1993). Upon opening the black box and finding it empty: Social constructivism and the philosophy of technology. *Science, Technology, & Human Values*, 18(3), 362-378.
