+++ System Overview
[[<image System%20Diagram.jpg size="medium"]]

The **Newsdora** system processes information in the form of "streams" from data sources (**J**).  These streams are processed in several parallel, pipelined stages (**A** through **D**) and ultimately delivered to the user in the form of an audio program (**E**).  Feedback from the user in the form of actions (**H**) and spoken commands (**G**) is accepted by the system and used to both tune the program delivery as well as overall system control.  

+++ Processing Stages and Sub-problems
**(A)** In the first processing stage, streams of information are converted into streams of "stories".  A [[[story]]] is a collection of //facts// and //monologue// regarding a //theme// or //subject//.  Stories may be interrelated by theme or subject, but are self-contained.  For instance, AP news feeds come in general themes of //General News//, //Sports//, //Global Regions//, //Business/Financial//, //Elections//, //Entertainment & Lifestyles//, //Other//.  In addition, you can imagine other subject categories such as //Weather//, //Local News//, //Traffic//, etc.  The individual stories are like //songs//, the categories are //genres//.  

**(B)** In addition to stories & genres (categories), there are a myriad of attributes that can be mined from the story text itself: subject/theme, location, time, key players, word frequencies, nouns, verbs, ...  all the way up to symantic networks & meaning/interpretations.  These characteristics are processed in the second stage.  Emitted from the second stage is a stream of stories annotated with [[[metadata]]].

**(C)** These annotated stories are assembled into [[[stations]]] or //channels// in the [[[selection]]]///mixing// stage.  Stories may be related by category, theme, subject, key players, or other metadata in a multi-dimensional space.  Stations are arrangements of related (and perhaps unrelated) stories along a temporal flow.

**(D)** These stations are then encoded for delivery to the client for vocalization and presentation **(E)**

**(F)** Finally, user preference modeling is updated in response to user feedback via voice interface **(G)** or actions **(H)**