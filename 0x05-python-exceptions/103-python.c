#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i)
    {
        element = ((PyListObject *)p)->ob_item[i];
        printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element))
            print_python_bytes(element);
        else if (PyList_Check(element))
            print_python_list(element);
        else if (PyFloat_Check(element))
            print_python_float(element);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %zd bytes: ", size < 10 ? size + 1 : 10);

    for (i = 0; i < size && i < 10; ++i)
    {
        printf("%02x", (unsigned char)str[i]);
        if (i < size - 1 && i < 9)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
