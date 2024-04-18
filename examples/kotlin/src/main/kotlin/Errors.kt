class Errors {
    // Errors used to be easy to overlook in large sourcecode files. Not anymore!
    syntaxerror

    // You are trying to some something that doesn't exist (anymore), this happens often when renaming stuff and is hard
    // to spot in large files.
    val someVariable = thisIsNotAThing
}