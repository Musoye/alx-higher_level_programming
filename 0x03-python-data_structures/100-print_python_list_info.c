#include <Python.h>

/*
 * print_python_list_info - print and modifypy list in c
 * @p: PyObject which here is python list
 * Return: NULL
 */
void print_python_list_info(PyObject *p)
{
 int size, alloc;
 PyObject *obj;
 size = Py_SIZE(p);
 alloc = ((PyListObject *)p)->allocated;
 int i = 0;

 printf("[*] Size of the Python List = %d\n", size);
 printf("[*] Allocated = %d", alloc);
 for( ; i < size; i++)
 {
  printf("Element %d: ", i);

  obj = PyList_GetItem(p, i);
  printf("%s\n", Py_TYPE(obj)->tp_name);
 } 
}
