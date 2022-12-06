#include <Python.h>
void print_python_list_info(PyObject *p)
{
 PyListObject *ll;
 ll = (PyListObject *)p;
 int i = 0;

 printf("[*] Size of the Python List = %ld", ll->ob_base.ob_size);
 printf("[*] Allocated = %ld", ll->allocated);
 for( ; i < ll->ob_base.ob_size; i++)
 {
  printf("Element %i: %s", i, ll->ob_item[i]->ob_type->tp_name);
 } 
}
