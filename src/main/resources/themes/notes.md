-It only seems to be possible to publish a source-code theme by exporting it manually as a jar, and then publishing it-

https://blog.jetbrains.com/platform/2017/12/export-intellij-editor-themes-as-plugins/



To create a Sourcecode highlighting we can either publish it manually as a
separate jar, or we must create a full theme. The advantage of the theme is
that in order to make the sourcecode look good the theme must also fit, and we
can simply extend the default dark theme and just add the source code
highlighting stuff.

Creating a theme reference:
https://www.youtube.com/watch?v=9J0j-90dC60&t=582s


### Developing tools

#### UI Inspector

is a built-in plugin that lets you view the tree of the Editors UI elements.
This is motly usefull for buildilng an actual theme. Needs to be enabled first
(use editor search). (see video above)

#### Laf Defaults

Plugin (?) to view the categories and properties of the Theme elements in the
editor. (see video above)


