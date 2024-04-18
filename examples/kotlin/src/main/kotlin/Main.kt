// comments are a neutral gray as usual
/**
 * Kdoc is (almost) same as  comments. It's important, but doesn't need to pop out at you. Only references like [String]
 * will pop out.
 *
 * @param arguments Parameters etc. are highlighted the same as the actual arguments
 */
fun main(arguments: Array<String>) {
    // syntax elements like 'fun', 'val' and 'class' are basically unimportant when reading or writing code (any errors
    // will scream at you in red), so no need to put correct ones in bright colors.

    // variables
    // ------------------------------------------------------------
    val regularVariable = "value" // green for local variables. Strings are also green but don't pop at you as much
    val unused = "value" // unused ones are gray
    var mutableVariable = "value" // added underline for mutable ones
    mutableVariable = "newValue"

    // classes and its functions
    // ------------------------------------------------------------
    val classInstance = AClass("some string") // classes are bold blue
    classInstance.classFunction(regularVariable) // so are class functions
    classInstance.classField // fields are pink
    classInstance.mutableClassField = mutableVariable // mutable fields underlined like the variables

    // static and extensions
    // ------------------------------------------------------------
    // functions without a class are like regular functions but cursive. It is generally not important to know the
    // sub-type when reading/writing code. So they are all blue, but in cursive so there is a slight distinction.
    nonClassFunction()
    inlineFunction()
    println(arguments)
    classInstance.extensionFunction()
}

// The names of function definitions are simply white. Popped out a little to differentiate from the plain syntax stuff
public fun nonClassFunction() {
    /**/
}

public inline fun inlineFunction() {
    /**/
}

fun AClass.extensionFunction() {
    println(this)
}

// A class is basically like a (constructor) function in kotlin, so it's highlighted the same
class AClass(regularVariable: String) {
    val classField = regularVariable + "value"
    lateinit var mutableClassField: String
    fun classFunction(functionArgument: String) {
        println(functionArgument)
    }

    // annotations are basically syntax elements. Highlight them the same
    @Deprecated(message = "some", replaceWith = ReplaceWith("classFunction()"))
    fun deprecatedFunction(functionArgument: String) {
        println(functionArgument)
    }
}
