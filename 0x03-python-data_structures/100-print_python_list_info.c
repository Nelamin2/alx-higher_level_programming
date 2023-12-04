#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints some basic
 *							info about Python lists
 * @p: Python list
 */
void print_python_list_info(PyObject *p)
{
    int elem;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (elem = 0; elem < size; elem++)
    {
        PyObject *item = PyList_GetItem(p, elem);
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %d: %s\n", elem, type_name);
    }
}
