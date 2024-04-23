# Shalev

(UNDER DEVELOPMENT)

A framework for systematic book writing using LLMs .

--- 

Shalev is a framework for writing books, large research papers, theses, or book like websites with the help of LLM based agents. The general idea is that structure, ideas, and style are laid out by the **authors**, while agents help refine content and synchronize style and content among various parts of the book. It is particularly geared towards books of a _scientific_, _mathematical_, or _programming_ nature, but it is not limited to these types of books.

The name is motivated by the late author, [Meir Shalev](https://en.wikipedia.org/wiki/Meir_Shalev) as well as the similar Hebrew word "shiluv" (שילוב) which means "combination". Indeed as attested by Meir Shalev, he used to write his books based on various sub-components which he would later combine into a cohesive story. Similarly, in Shalev, the basic entity is a **component** which is combined into the final product. Importantly, in Shalev, the components are manipulated and refined with the help of LLM along the way. 

At the moment Shalev is a set of software tools combined with procedures for writing a book. It may be set as a visual studio code (or other IDE) plug-in, but it is still not. At the moment, Shalev is being developed to aid the creation of the following books: 

* _Linear Algebra with Julia and JAX: Fundamentals for Data Science, Machine Learning
and Artificial Intelligence_.
* _Statistics with Julia: Fundamentals for Data Science, Machine Learning and Artificial Intelligence._ 
* _Statistics with Python: Fundamentals for Data Science, Machine Learning and Artificial Intelligence._
* _The Tales of Curious Epsilon_
* _Structured Markov Chains and Linear Control Theory_

The need and opportunity for a tool like Shalev became apparent during work on [_The Mathematical Engineering of Deep Learning_](https://deeplearningmath.org/) especially since Chat-GPT became available during the final year of work on that book. Yet for that book, using Chat-GPT for anything beyond table and formula formatting was not really possible as the style and messaging of the book needed to be kept and any Chat-GPT text generated was not really useful. Still, working on a deep learning book during the Chat-GPT era made it clear that many editing tasks can be automated in ways where the authors have (almost) full control of the final product, and where LLMs save an immense amount of time. Note that many of these tasks are not directly related to English language or creative writing, but are rather related to tasks of enforcing style and consistency along the book among others.

Shalev is also related to the world of automatic software creation (e.g. GitHub co-pilot). A general paradigm that it attempts to employ is [flow engineering](https://arxiv.org/abs/2401.08500).

We note that Shalev can help with creation of freeform text, mathematical formulas, bibliography, computer programming code (appearing in book), [TikZ](https://texample.net/tikz/examples/) illustrations and other elements appearing the book.

Shalev is closely tied to GitHub, Pandoc, and LaTeX.

## Main idea

Here we outline the main entities in a Shalev **project**. 

The atoms of such a project are called **components** where you can think of a component as a part of the book. Each component has a **component type** where component types can be _chapter_, _section_, _subsection_, _code-snippet_, etc. Shalev comes with basic component types motivated by the example projects it was developed for. New component types can be defined as well. Depending on the component type, some components can have children (e.g. a _chapter_ can have _sections_ as children). These component types are **non-leaf** components. Other  component types are **leafs** (e.g. a _code-snippet_). There is also the **root** component which is the whole project and it includes all other components.

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


