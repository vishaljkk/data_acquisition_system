//myModule.c//

#include <Python.h>
#include <stdio.h>
#include<time.h>
#define PI 3.14159265358979323846
float guassian(int mean,int std,int x){
  float a=(1/(pow((2*PI),0.5)*std))*(exp(-pow((x-mean),2)/(2*pow(std,2))));
  return a;
}
int creategdp(int m, int s, int x1, int x2) {
  //int m=atoi(argv[1]);
  //int s=atoi(argv[2]);
  //int x1=atoi(argv[3]);
  //int x2=atoi(argv[4]);
  FILE *fptr;
  if ((fptr = fopen("guassian.txt","w")) == NULL){
    printf("Error! opening file");
    exit(1);
  }
  for(int i=x1;i<=x2;i++){
    fprintf(fptr,"%d",i);
    fprintf(fptr,"\n");
    float k=guassian(m,s,i);
    fprintf(fptr,"%f",k);
    fprintf(fptr,"\n");
  }
  fclose(fptr);

  return 0;
}




int nsleep(long miliseconds)
{
   struct timespec req, rem;
   //printf("This is the passed milliseconds %ld",miliseconds);
   if(miliseconds > 999)
   {   
        req.tv_sec = (int)(miliseconds / 1000);                            /* Must be Non-Negative */
        req.tv_nsec = (miliseconds - ((long)req.tv_sec * 1000)) * 1000000; /* Must be in range of 0 to 999999999 */
   }   
   else
   {   
        req.tv_sec = 0;                         /* Must be Non-Negative */
        req.tv_nsec = miliseconds * 1000000;    /* Must be in range of 0 to 999999999 */
   }   

   return nanosleep(&req , &rem);
}


int gdp(int m,int s,int x1,int x2)
{
   int ret = creategdp(m,s,x1,x2);
   return ret;
}
 
int Cfib(int n)
{
   int ret = nsleep(n);
   printf("sleep result %d\n",ret);
   return ret;
}


static PyObject* dp(PyObject* self, PyObject* args)
{
    int m, s, x1, x2;
 
    if (!PyArg_ParseTuple(args, "iiii", &m, &s, &x1, &x2))
        return NULL;
 
    return Py_BuildValue("i", gdp(m,s,x1,x2));
}

 
static PyObject* fib(PyObject* self, PyObject* args)
{
    int n;
 
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
 
    return Py_BuildValue("i", Cfib(n));
}

static PyObject* version(PyObject* self)
{
    return Py_BuildValue("s", "Version 1.0");
}
 
static PyMethodDef myMethods[] = {
    {"dp", dp , METH_VARARGS, "Calculate the guassian dp"},
    {"fib", fib, METH_VARARGS, "Run the nanosleep function"},
    {"version", (PyCFunction)version, METH_NOARGS, "Returns the version."},
    {NULL, NULL, 0, NULL}
};
 
static struct PyModuleDef myModule = {
	PyModuleDef_HEAD_INIT,
	"myModule",
	"Fibonacci Module",
	-1,
	myMethods
};

PyMODINIT_FUNC PyInit_myModule(void)
{
    return PyModule_Create(&myModule);
}


