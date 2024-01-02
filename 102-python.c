#include <Python.h>

/**
 * print_python_string - Prints information about Python string objects
 * @p: PyObject string to analyze
 */
void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");
    printf("  type: compact unicode object\n");
    printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}
