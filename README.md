# Shalev

A framework for systematic book writing using LLMs.

--- 

Shalev is a framework for writing books with the help of LLM based agents. Agents help create content, and synchronize content among various parts of the book. 

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


