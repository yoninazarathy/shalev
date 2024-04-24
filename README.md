# Shalev (UNDER DEVELOPMENT)

**A framework for systematic book writing with the help of LLM Agents.**

![A mechanical arm](img/shalev_illustration.png)

Shalev is a framework for integrating LLMs in the process of writing books, extensive research papers, theses, or book-like websites. The general idea is that structure, ideas, and style are laid out by the (human) **authors**, while LLM-agents help refine content and synchronize style and content among various parts of the book. Shalev is particularly geared towards books of a _scientific_, _mathematical_, or _programming_ nature, but it is not limited to these types of creations.

The name is motivated by the late author, [Meir Shalev](https://en.wikipedia.org/wiki/Meir_Shalev) as well as the similar Hebrew word "shiluv" (שילוב) which means "combination". Indeed as attested by Meir Shalev, he used to write his novels based on various sub-components which he would later combine into a cohesive story. Similarly, in Shalev, the basic entity is a **component** (typically a piece of text) which is combined into the final product. Importantly, in Shalev, the components are manipulated and refined with the help of LLM along the way. LLM-Agents are used to improve text, implement comments, uniformize style, and test for consistency, among other tasks.

At the moment Shalev, under development, is a CLI tool and a conceptual framework for book editing. In the future Shalev may be a visual studio code (or other IDE) plug-in, but there are no plans for this yet. In any case, the Shalev framework heavily relies on git workflows, as any changes to a component are committed, together with metadata. Also in any Shalev project, it is typical that the authors program, or "prompt engineer", from time to time, as part of their book writing process. These  auxillary programs, or LLM prompts, are also stored as part of the project and are used to help create and improve the project.

Shalev has two main components, **Shalev Agent Framework** (SAF) and **Shalev Composer Framework** (SCF). The SAF is the part associated with carrying out LLM/AI agent based tasks on components. The SCF is simply the tool that aggregates the components into a document that is compiled via LaTeX, pandoc, or other means. A Shalev **project** (book) has metadata associated both with the SAF and SCF, and this metadata, also edited during the book writing processes, specifies for the SAF and the SCF how to carry out various **actions**. Some metadata has to do with the whole project, either for the SAF or SCF, while other metadata is component specific.

Both the SAF and SCF have associated **actions** and the main use of the Shalev CLI is to execute these actions. SAF actions carry out LLM-Agent computations to transform components. This can include rewriting a component, uniformizing the style of several components, and other custom LLM-Agent based actions applied to the body of the project. SCF actions are more straightforward and include compilation of the components into the **latest draft** and similar formatting actions using LaTeX, pandoc, etc. 

Note also that an important part of Shalev has to do with **review feedback** and its implementation in the project. In such cases, metadata of components includes annotated (human) review feedback from proofreading and revising. Then SAF actions can implement this feedback either locally or across many or all components.  

Also note that some SAF actions do not change the actual body of a component but rather check for consistency, comparison of example code (in case the book has computer programming code) output, and similar checks.

## Motivation

At the moment, Shalev is being developed to aid the creation of the following books: 

* _Linear Algebra with Julia and JAX: Fundamentals for Data Science, Machine Learning and Artificial Intelligence_: This book will be based on short Julia and JAX (Python) code examples. Linear algebra concepts will be augmented with both Julia and JAX examples. Among other tasks, Shalev will be used to ensure consistency among examples and across the two languages (Julia and JAX/Python).
* _Statistics with Julia: Fundamentals for Data Science, Machine Learning and Artificial Intelligence, Second Edition._ The [first edition](https://statisticswithjulia.org/) will be revised with agent framework actions.
* _Statistics with Python: Fundamentals for Data Science, Machine Learning and Artificial Intelligence._ This is a port of Statistics with Julia, adapted to Python. Shalev will be used for the port. 
* _The Tales of Curious Epsilon_. This book is an exploratory mathematics book based on old existing blog posts. The writing style is very different to the other books. 
* _Structured Markov Chains and Linear Control Theory_. An early [rough version](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/bookSS16_WHOLE_BOOK_v2.pdf) of this book exists and Shalev will be used to as an aid to complete it.
* _The Mathematical Engineering of Deep Learning, Second edition_. The [first edition](https://deeplearningmath.org/) exists but deep learning is moving very fast and there is room to update to a second edition, also with the help of Shalev.

The need and opportunity for a tool like Shalev became apparent during work on [_The Mathematical Engineering of Deep Learning_](https://deeplearningmath.org/) especially since Chat-GPT became available during the final year of work on that book. Yet for that book, using Chat-GPT for anything beyond table and formula formatting was not really possible as the style and messaging of the book needed to be kept and any Chat-GPT text generated was not really useful. Still, working on a deep learning book during the Chat-GPT era made it clear that many editing tasks can be automated in ways where the authors have (almost) full control of the final product, and where LLMs save an immense amount of time. Note that many of these tasks are not directly related to English language or creative writing, but are rather related to tasks of enforcing style and consistency along the book among others.

Shalev is also related to the world of automatic software creation (e.g. GitHub co-pilot). A general paradigm that it attempts to employ is [flow engineering](https://arxiv.org/abs/2401.08500).

We note that Shalev can help with creation and editing of freeform text, mathematical formulas, bibliography, computer programming code (appearing in book), [TikZ](https://texample.net/tikz/examples/) illustrations and other elements appearing the book.

## Components

The atoms of a Shalev project are called **components** where you can think of a component as a part of the book. Each component has a **component type** where component types can be _chapter_, _section_, _subsection_, _code-snippet_, etc. Shalev comes with basic component types motivated by the example projects it was developed for. New component types can be defined as well. Depending on the component type, some components can have children (e.g. a _chapter_ can have _sections_ as children). These component types are **non-leaf** components. Other  component types are **leafs** (e.g. a _code-snippet_). There is also the **root** component which is the whole project and it includes all other components.

In Git, components reside in the `components` folder, where each subfolder of `components` is a uniquely named component. E.g. `diffusion_example_a`. Now the component directory, `diffusion_example_a` has one textual (LaTeX, Markdown, TikZ, etc, plain text...) file that is called `body.txt` and another file called `metadata.json`. A full specification of the metadata is in the sequel. As for the body, it is pure text, or code (in case the project includes computer code), but for non-leaf components it can also have lines such as 

```
!!!>include(foo)
```

where `foo` is a different component name. Note also that one component is called `root`. 

All components are included via a tree structure from `root`, and (typically) every component is included only once.  

This structure then allows the main action of the SCF, **compileproject** to execute. The basics of this action is to construct all of the components into one source file, e.g. a valid complete LaTeX file, and then produce output via LaTeX compilation. 

QQQQQQ

In greatest simplicity a component type is made of a text file (also perhaps LaTeX or Markdown), where if it is **non-leaf** there are also special commands to include components in it. Note that non-leaf components can still include text on their own right just like the fact that a section can have text followed by sub-sections, etc... 

The project is compiled simply merging all 

Each component has a unique name, unique UUID and component type. It also has information which describes the state of the component 

The created **book** evolves in a GitHub repository where the evolving files each represent a **component** of the book (section, example, figure, subsection, etc.... ). Components can be in various levels of **maturity**, where maturity is an positive integer numerical value. For example initially a component can just be a collection of textual notes indicating what it means to represent (maturity = 0). Then as it matures, among commits it becomes a more concrete book component. Each component has a unique text based id and UUID. A component has a **type** which is section, example, figure, subsection, etc.... Components are hiearchical, so sections are parts of chapters, subsections are parts of sections, etc.

The book has a specified (and editable) **schema** which outlines how components are associated with each other and this means the chapter, section, subsection, example sequence etc. With the **scheme** it is clear how to collect all of the components into the whole book. 

In addition to the schema, the components of the book are related via a **constrution DAG** (directed acyclic graph). This graph indicates how components affect each other.

A book can have various **presentation formats** with the basic format being a LaTeX formatted document, but others are also possible. It is integrated with [Pandoc](https://pandoc.org/).

## Actions

The book evolves via a sequence of actions and these are recorded in an action-log. It is the writing team's choice when to carry out these actions. The Git repo maintains history of all of the actions. In fact every commit is associated with an action.

Actions are always (certainly in this version) human instigated. The main thing that the writing team does is work on actions.

### User Editing Actions

These actions are actions of editing components (writing), revising the schema, revising the presentation formats, or revising the construction DAG. 

### Admin Actions

The basic admin actions are to create the book via a presentation format. There are also other admin actions that summarize the progress etc...

### Proofread Actions

These are actions where the book is annotated, proofread, and collets input.

### Agent Actions (AI)

This is where AI/LLMs/Agents are used to help improve the book. Agent actions invoke LLMs to imrpove text, implement proofread inputs, enforce consitnency along the construction DAG, and generally improve the maturity of components. 


